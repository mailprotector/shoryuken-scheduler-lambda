# shoryuken-scheduler-lambda

A lambda that drops a queue item into a defines schedule queue for shoruken to process and create batch jobs.

### Environment Variables
| variable name   | description       |  type  |  default  | required |
| --------------- | ----------------- | :----: | :-------: | :------: |
| SCHEDULED_QUEUE | name of the queue | string | scheduled |    no    |