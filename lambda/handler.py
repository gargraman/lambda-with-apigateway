def handler(event, context):
    print("Lambda function has been invoked.")
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
