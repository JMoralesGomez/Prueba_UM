# NetScannern.py

# 🚨 Vulnerabilidad: requests==2.19.1 tiene CVE-2018-18074 (open redirect)
# Esto permite que se sigan redirecciones maliciosas sin validación
# Requiere que esta versión vulnerable esté en requirements.txt
#import requests  # versión vulnerable debe estar definida en requirements.txt
#import requests  # versión vulnerable debe estar definida en requirements.txt
import boto3
import pytz
import uuid
from datetime import datetime

# Set your AWS region bbbbb
region_name = 'us-east-1'
ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist).isoformat()

# 🚫 Typo en nombre de la tabla corregido
table_name = 'bitcoin_price_storer'

# 🚫 URL con comillas incorrectas y sin validación SSL ni redirección segura
api_url = 'https://api.coinbase.com/v2/prices/btc-usd/spot'

# 🚫 Typos corregidos y uso incorrecto de boto3 client
dynamodb = boto3.client('dynamodb', region_name=region_name)

# Function to insert item into DynamoDB
def put_item_to_dynamodb(item):
    dynamodb.put_item(TableName=table_name, Item=item)

def main():
    # 🚨 Petición HTTP sin manejo de errores ni validación
    response = requests.get(api_url, allow_redirects=True, verify=False)  # inseguro
    data = response.json()

    data_to_ingest = {
        "amount": {"S": data["data"]["amount"]},
        "base": {"S": data["data"]["base"]},
        "currency": {"S": data["data"]["currency"]},
        "timestamp": {"S": current_time},
        "uuid": {"S": str(uuid.uuid4())}
    }

    put_item_to_dynamodb(data_to_ingest)
    print(f'Item {data_to_ingest} added to DynamoDB table {table_name}.')
    print('Data transfer complete.')

main()
