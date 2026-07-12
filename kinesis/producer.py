import json
import boto3
import websocket

from config import AWS_REGION, KINESIS_STREAM_NAME, FINNHUB_API_KEY, FINNHUB_WS_URL

kinesis_client = boto3.client("kinesis", region_name=AWS_REGION)


SYMBOLS = ["AAPL", "MSFT", "NVDA"]


def send_to_kinesis(record: dict):
    symbol = record.get("symbol", "UNKNOWN")

    response = kinesis_client.put_record(
        StreamName=KINESIS_STREAM_NAME, Data=json.dumps(record), PartitionKey=symbol
    )

    print(f"Sent record to Kinesis: {symbol}")
    return response


def on_message(ws, message):
    payload = json.loads(message)

    if payload.get("type") == "trade":
        for trade in payload.get("data", []):
            record = {
                "symbol": trade.get("s"),
                "price": trade.get("p"),
                "volume": trade.get("v"),
                "event_timestamp": trade.get("t"),
                "conditions": trade.get("c"),
            }

            print("Trade received:", record)
            send_to_kinesis(record)
    else:
        print("Message received:", payload)


def on_error(ws, error):
    print("WebSocket error:", error)


def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed:", close_status_code, close_msg)


def on_open(ws):
    print("WebSocket connected.")

    for symbol in SYMBOLS:
        subscribe_message = {"type": "subscribe", "symbol": symbol}

        ws.send(json.dumps(subscribe_message))
        print(f"Subscribed to {symbol}")


if __name__ == "__main__":
    websocket_url = f"{FINNHUB_WS_URL}?token={FINNHUB_API_KEY}"

    ws = websocket.WebSocketApp(
        websocket_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )

    print("Starting Finnhub WebSocket producer...")
    ws.run_forever()
