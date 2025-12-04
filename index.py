import datetime
import json
import os
import uuid

import boto3


def lambda_handler(event, context):
    sqs = boto3.resource("sqs")
    queue_name = os.environ.get("SCHEDULED_QUEUE", "scheduled")
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    id = str(uuid.uuid4())

    message_body = {
        "job_class": event,
        "job_id": id,
        "provider_job_id": None,
        "queue_name": queue_name,
        "priority": None,
        "arguments": [],
        "executions": 0,
        "exception_executions": {},
        "locale": "en",
        "timezone": "UTC",
        "enqueued_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    message_attributes = {
        "shoryuken_class": {
            "DataType": "String",
            "StringValue": "ActiveJob::QueueAdapters::ShoryukenAdapter::JobWrapper",
        }
    }

    queue.send_message(
        MessageBody=json.dumps(message_body), MessageAttributes=message_attributes
    )
