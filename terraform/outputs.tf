output "aws_account_id" {
  description = "AWS account Terraform is authenticated against"
  value       = data.aws_caller_identity.current.account_id
}

output "aws_caller_arn" {
  description = "IAM identity currently used by Terraform"
  value       = data.aws_caller_identity.current.arn
}

output "aws_region" {
  description = "AWS region used by the provider"
  value       = data.aws_region.current.region
}