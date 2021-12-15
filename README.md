# ship-and-notify-file-delivery

This app contains a simple implementation of a lambda function that is wrapped in a docker container. That fuction triggered by S3 event, identifies files that are being uploaded to that bucket and notifies that in email using AWS SES.

## Init and Execute

The infra initialization is done using terraform.

The app CI\CD process is implemented using GitHub actions.

There will be a single pipeline that will build the image and spin up the terraform env that would execute the lambda function.

# References

Building docker images for AWS Lambda function:
https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-from-base

Terraform GitHub actions steps:
https://github.com/hashicorp/terraform-github-actions/blob/master/examples/credentials-file.md



