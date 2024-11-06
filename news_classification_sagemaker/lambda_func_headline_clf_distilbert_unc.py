import json
import boto3

def lambda_handler(event, context):
    sm_runtime = boto3.client('sagemaker-runtime')

    body = event
    headline = body.get('query', {}).get('headline')
    if not headline:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Headline is missing in the query'})
        }

    payload = json.dumps({'inputs': headline})

    endpoint_name = 'multiclass-headline-clf-v2'  # Ensure this is correct
    try:
        resp = sm_runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='application/json',
            Body=payload
        )
        result = json.loads(resp['Body'].read().decode())
        return {
            'statusCode': 200,
            'body': json.dumps({'text': headline, 'result': result})
        }
    except sm_runtime.exceptions.ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
