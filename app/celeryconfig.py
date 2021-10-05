import os

from dotenv import load_dotenv
from kombu.utils.url import safequote


load_dotenv()

task_serializer = 'pickle'
result_serializer = 'pickle'
accept_content = ['json', 'pickle']
broker_url = os.getenv('BROKER_URL')
result_backend = os.getenv('RESULT_BACKEND')
task_routes = {
    'ps.similar': {'queue': 'ps_similar'},
}
enable_utc = True

# CELERY_BROKER_TRANSPORT_OPTIONS = {
#     'region': os.getenv('AWS_REGION'),
#     'predefined_queues': {
#         'default': {
#             'url': os.getenv('SQS_URL'),
#         }
#     }
# }
# aws_access_key = safequote(os.getenv('AWS_ACCESS_KEY_ID'))
# aws_secret_key = safequote(os.getenv('AWS_SECRET_ACCESS_KEY'))
# broker_url = "sqs://{aws_access_key}:{aws_secret_key}@".format(
#     aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
# )
#result_backend = 'rpc://'

# 1 приавм такски
# зависимости.