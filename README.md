# ship-and-notify-file-delivery

This app contains a simple implementation of a lambda function that is wrapped in a docker container. That fuction triggered by S3 event, identifies files that are being uploaded to that bucket and notifies that in email using AWS SES.

## Init

The infra initialization is done using terraform.

The app CI\CD process is implemented using GitHub actions.

## Execute

TBD