import boto3
from django.conf import settings


class Bucket:
    def __init__(self):
        session = boto3.Session()
        self.conn = session.client(
            service_name=settings.AWS_SERVICES_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL
        )

    """
    CRUD:
    """

    def get_object(self):
        response = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if response['KeyCount']:
            return response['Contents']
        else:
            return None

    def delete_obbject(self):
        client = boto3.client('s3')
        response = client.delete_object(
            Bucket='settings.AWS_STORAGE_BUCKET_NAME',
            Key='face-massge.jpg'
        )
        print(response)

    def download_object(self, key):
        pass

    def update_object(self, file):
        pass


bucket = Bucket()
