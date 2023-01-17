import boto3
import json
import uuid
import datetime
import os


def lambda_handler(event, context):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(
        QueueName=scheduled_queue)

    id = str(uuid.uuid4())

    message_body = {
        "job_class": event,
        "job_id": id,
        "provider_job_id": None,
        "queue_name": os.environ.get('SCHEDULED_QUEUE', default='scheduled'),
        "priority": None,
        "arguments": [],
        "executions": 0,
        "exception_executions": {},
        "locale": "en",
        "timezone": "UTC",
        "enqueued_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }

    message_attributes = {
        "shoryuken_class": {
            "DataType": "String",
            "StringValue": "ActiveJob::QueueAdapters::ShoryukenAdapter::JobWrapper"
        }
    }

    queue.send_message(
        MessageBody=json.dumps(message_body),
        MessageAttributes=message_attributes
    )

# if __name__ == "__main__":
#   event = {
#     "task_name": "test"
#   }
#   lambda_handler(event, None)
