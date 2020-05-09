provider "aws" {
  region = "eu-west-1"
  access_key = "123"
  secret_key = "123"
  skip_credentials_validation = true
  skip_metadata_api_check = true
  skip_requesting_account_id  = true
  s3_force_path_style = true

  endpoints {
    s3 = "http://localhost:4572"
    ec2 = "http://localhost:4597"
    sqs = "http://localhost:4576"
  }
}

resource "aws_s3_bucket" "b" {
  bucket = "my-tf-test-bucket"
  acl    = "public-read"
}

resource "aws_sqs_queue" "terraform_queue" {
  name                      = "terraform-example-queue"
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10

  tags = {
    Environment = "production"
  }
}

resource "aws_sqs_queue" "terraform_queue_fifo" {
  name                        = "terraform-example-queue.fifo"
  fifo_queue                  = true
  content_based_deduplication = true
}

# resource "aws_instance" "example" {
#   ami		= "ami-0c55b159cbfafe1f0"
#   instance_type = "t2.micro"

#   tags = {
#     name = "terraform-example"
#   }
# }
