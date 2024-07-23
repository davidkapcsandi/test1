import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket {bucket_name} created successfully")
    except ClientError as e:
        print(f"Error creating bucket: {e}")
import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    if region:
        s3 = boto3.client('s3', region_name=region)
        try:
            s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
            print(f"S3 bucket {bucket_name} created successfully in {region}")
        except ClientError as e:
            print(f"Error creating bucket: {e}")
    else:
        s3 = boto3.client('s3')
        try:
            s3.create_bucket(Bucket=bucket_name)
            print(f"S3 bucket {bucket_name} created successfully")
        except ClientError as e:
            print(f"Error creating bucket: {e}")

def create_ec2_instance():
    ec2 = boto3.resource('ec2')
    try:
        instance = ec2.create_instances(
            ImageId='ami-05842291b9a0bd79f',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='test'
        )
        print(f"EC2 instance created with ID: {instance[0].id}")
    except ClientError as e:
        print(f"Error creating EC2 instance: {e}")

if __name__ == "__main__":
    bucket_name = 'testing-automation-bucket'
    region = 'eu-west-1'
    create_s3_bucket(bucket_name, region)
    create_ec2_instance()
