import logging
import json

from src.talks.controller import create_talk


logger = logging.getLogger(__name__)


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def register_talk(event, context):
    logger.info('event: %s', event)
    talk_data = json.loads(event.get('body'))
    status_code = 200
    try:
        create_talk(talk_data)
    except Exception as e:
        logger.exception('create talk error')
        status_code = 400
        response = {'message': str(e)}
    else:
        response = {'message': 'talk created successfully'}
    return {
        'statusCode': status_code,
        'body': json.dumps(response)
    }

