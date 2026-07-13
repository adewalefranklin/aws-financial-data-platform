resource "aws_sns_topic" "financial_platform_alerts" {
  name = "financial-platform-terraform-alerts"

  tags = {
    Project     = "financial-platform"
    Environment = "learning"
    ManagedBy   = "Terraform"
  }
}