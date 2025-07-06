import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactForm')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    name = body.get('name')
    email = body.get('email')
    message = body.get('message')

    response = table.put_item(
        Item={
            'email': email,
            'name': name,
            'message': message
        }
    )

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'message': 'Form submitted successfully'})
    }

