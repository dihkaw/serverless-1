import json
import boto3

def lambda_handler(event, context):
    # Membuat klien DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BukuTamuTable')
    
    try:
        # Scan untuk mengambil semua item dari tabel
        response = table.scan()
        
        # Mengembalikan data tamu
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
