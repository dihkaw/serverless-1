import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BukuTamuTable')

def lambda_handler(event, context):
    try:
        guest_id = event['pathParameters']['id']
        body = json.loads(event['body'])

        response = table.update_item(
            Key={'id': guest_id},
            UpdateExpression="SET #n = :name, message = :message",
            ExpressionAttributeNames={"#n": "name"},
            ExpressionAttributeValues={
                ":name": body["name"],
                ":message": body["message"]
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Data tamu berhasil diperbarui", "updated": response["Attributes"]})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
