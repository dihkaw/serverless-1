import json
import boto3

def lambda_handler(event, context):
    # Mengambil ID tamu dari parameter path
    guest_id = event['pathParameters']['id']
    
    # Membuat klien DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BukuTamuTable')
    
    try:
        # Menghapus item dari DynamoDB
        table.delete_item(Key={'id': guest_id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data tamu berhasil dihapus!'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
