import json
import time
from datetime import datetime, timezone

import boto3

from config import AWS_REGION, KINESIS_STREAM_NAME, S3_BUCKET_NAME, S3_STREAMING_PREFIX

kinesis_client = boto3.client("kinesis", region_name=AWS_REGION)
s3_client = boto3.client("s3", region_name=AWS_REGION)


def get_shard_iterator():
    stream_description = kinesis_client.describe_stream(StreamName=KINESIS_STREAM_NAME)
    shard_id = stream_description["StreamDescription"]["Shards"][0]["ShardId"]

    response = kinesis_client.get_shard_iterator(
        StreamName=KINESIS_STREAM_NAME, ShardId=shard_id, ShardIteratorType="LATEST"
    )

    return response["ShardIterator"]


def write_records_to_s3(records):
    if not records:
        return

    now = datetime.now(timezone.utc)

    s3_key = (
        f"{S3_STREAMING_PREFIX}/"
        f"year={now.year}/"
        f"month={now.month:02d}/"
        f"day={now.day:02d}/"
        f"hour={now.hour:02d}/"
        f"kinesis_records_{int(time.time())}.json"
    )

    body = "\n".join(json.dumps(record) for record in records)

    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=s3_key, Body=body.encode("utf-8"))

    print(f"Wrote {len(records)} records to s3://{S3_BUCKET_NAME}/{s3_key}")


def consume_records():
    shard_iterator = get_shard_iterator()

    print("Reading records from Kinesis and writing to S3...")

    while True:
        response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=10)

        decoded_records = []

        for record in response["Records"]:
            data = json.loads(record["Data"])
            print("Record received:", data)
            decoded_records.append(data)

        write_records_to_s3(decoded_records)

        shard_iterator = response["NextShardIterator"]
        time.sleep(2)


if __name__ == "__main__":
    consume_records()
