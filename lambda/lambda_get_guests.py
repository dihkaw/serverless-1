import json
import boto3

def lambda_handler(event, context):
    # Membuat klien DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('BukuTamuTable')
    
    try:
        # Scan untuk mengambil semua item dari tabel
        response = table.scan()
        
        # Jika tidak ada item yang ditemukan, buat 5 baris data awal
        if not response['Items']:
            initial_data = [
                {'id': '1', 'nama': 'Tamu 1', 'pesan': 'Halo, ini pesan dari Tamu 1'},
                {'id': '2', 'nama': 'Tamu 2', 'pesan': 'Halo, ini pesan dari Tamu 2'},
                {'id': '3', 'nama': 'Tamu 3', 'pesan': 'Halo, ini pesan dari Tamu 3'},
                {'id': '4', 'nama': 'Tamu 4', 'pesan': 'Halo, ini pesan dari Tamu 4'},
                {'id': '5', 'nama': 'Tamu 5', 'pesan': 'Halo, ini pesan dari Tamu 5'}
            ]
            
            # Masukkan data awal ke dalam tabel
            for item in initial_data:
                table.put_item(Item=item)
            
            # Scan lagi untuk mengambil data yang baru saja dimasukkan
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
