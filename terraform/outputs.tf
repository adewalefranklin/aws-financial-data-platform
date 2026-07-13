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

output "default_vpc_id" {
  description = "Default VPC used by the ECS Fargate task"
  value       = data.aws_vpc.default.id
}

output "default_subnet_ids" {
  description = "Subnets available in the default VPC"
  value       = data.aws_subnets.default_vpc.ids
}

output "financial_platform_ecr_url" {
  description = "URL of the existing financial platform ECR repository"
  value       = data.aws_ecr_repository.financial_platform.repository_url
}

output "financial_platform_ecs_cluster_arn" {
  description = "ARN of the existing ECS cluster"
  value       = data.aws_ecs_cluster.financial_platform.arn
}

output "terraform_learning_log_group_name" {
  description = "Name of the CloudWatch log group created by Terraform"
  value       = aws_cloudwatch_log_group.terraform_learning.name
}

output "financial_platform_alert_topic_arn" {
  description = "ARN of the SNS topic created by Terraform"
  value       = aws_sns_topic.financial_platform_alerts.arn
}
