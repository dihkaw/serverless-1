import json
import boto3

def lambda_handler(event, context):
    # Membuat klien DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BukuTamuTable')
    
    try:
        # Parse data dari body request
        body = json.loads(event['body'])
        nama = body['nama']
        pesan = body['pesan']
        
        # Generate ID unik (contoh menggunakan timestamp)
        import time
        id = str(int(time.time()))
        
        # Masukkan data ke dalam tabel
        table.put_item(Item={
            'id': id,
            'nama': nama,
            'pesan': pesan
        })
        
        # Mengembalikan respons sukses
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Izinkan akses dari semua domain
            },
            'body': json.dumps({'message': 'Tamu berhasil ditambahkan!', 'id': id})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': str(e)})
        }
