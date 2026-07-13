data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default_vpc" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

data "aws_ecr_repository" "financial_platform" {
  name = "financial-platform"
}

data "aws_ecs_cluster" "financial_platform" {
  cluster_name = "financial-platform-cluster"
}