variable "region" {
  type = string
  default = "eu-west-1"
  description = "aws region"
}

variable "sns_topic_name" {
  type = string
  default = "files_to_scan"
  description = "sns topic name"
}

variable "sns_subscription_email_address_list" {
  type = string
  default = "avivka8@gmail.com"
  description = "List of email addresses as string(space separated)"
}
