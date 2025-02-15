import json
import boto3

def lambda_handler(event, context):
    # Mengambil ID tamu dan data baru dari request
    guest_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    name = body.get('name')
    message = body.get('message')

    if not name or not message:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Nama dan pesan harus diisi!'})
        }

    # Membuat klien DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BukuTamuTable')
    
    try:
        # Memperbarui item di DynamoDB
        table.update_item(
            Key={'id': guest_id},
            UpdateExpression="set name = :n, message = :m",
            ExpressionAttributeValues={
                ':n': name,
                ':m': message
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data tamu berhasil diperbarui!'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
