resource "aws_cloudwatch_log_group" "terraform_learning" {
  name              = "/financial-platform/terraform-learning"
  retention_in_days = 7

  tags = {
    Project     = "financial-platform"
    Environment = "learning"
    ManagedBy   = "Terraform"
  }
}