## Start Localstack
```
alias awslocal=' aws --endpoint-url=http://localhost:4566 '

docker-compose up -d
```
## Upload Lambda code
```
awslocal s3 mb s3://dummy-bucket
awslocal s3 cp lambda/function.zip s3://dummy-bucket/function.zip
```

## Deploy cloudformation stack
```
awslocal cloudformation deploy \
  --stack-name localstack-stack \
  --template-file template.yaml \
  --capabilities CAPABILITY_IAM
```
## Invoke Lambda function

### via api-gateway
```
API_ID=$(awslocal apigateway get-rest-apis --query "items[?name=='my-api'].id" --output text)

curl http://localhost:4566/restapis/$API_ID/dev/_user_request_/lambda
```

### send SQS message
```
QUEUE_URL=$(awslocal sqs get-queue-url --queue-name my-queue --query QueueUrl --output text)

awslocal sqs send-message --queue-url $QUEUE_URL --message-body "Test message"
```
### check lambda logs
```
awslocal logs describe-log-groups

# Find the log group name for your Lambda function
awslocal logs get-log-events --log-group-name /aws/lambda/my-function --log-stream-name <log-stream-name>
```

## LocalStack UI Access
```
# LocalStack Web UI is available at:
http://localhost:4571
```

## Restart LocalStack
```
# Stop the current container
docker-compose down

# Start it again
docker-compose up -d

# Check logs (optional)
docker-compose logs -f localstack
```

## Cleanup
```
awslocal cloudformation delete-stack --stack-name localstack-stack

docker-compose down
