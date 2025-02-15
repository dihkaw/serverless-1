import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Mengambil data dari request body
    body = json.loads(event['body'])
    name = body.get('name')
    message = body.get('message')
    
    if not name or not message:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Nama dan pesan harus diisi!'})
        }
    
    # Membuat ID unik untuk setiap entri tamu
    guest_id = str(datetime.utcnow().timestamp())

    # Membuat klien DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BukuTamuTable')
    
    try:
        # Menambahkan item ke DynamoDB
        table.put_item(
            Item={
                'id': guest_id,
                'name': name,
                'message': message,
                'timestamp': str(datetime.utcnow())
            }
        )
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Data tamu berhasil ditambahkan!'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
