from argparse import ArgumentParser
import boto3


# This function is used to delete the bucket on s3

def delete_func(bucket):
    try:
        s3 = boto3.resource("s3")
        delete_obj = s3.Bucket(bucket)
        delete_obj.delete()
        print("bucket has been deleted successfully")
    except Exception:
        print("Bucket Failed to delete")


# This function is used to empty the bucket on s3
def empty_func(bucket):
    try:
        s3 = boto3.resource("s3")
        empty_object = s3.Bucket(bucket)
        empty_object.objects.all().delete()
        print("bucket has been emptied")
    except Exception:
        print("bucket failed to empied")


# This function is used to upload the file on s3 bucket
def upload_func(bucket, path):
    try:
        s3 = boto3.resource("s3")
        s3.meta.client.upload_file(path, bucket, path.split('/')[-1])
        print("File uploaded to S3 bucket")
    except Exception:
        print("File failed to upload on S3 bucket")


obj = ArgumentParser()
obj.add_argument("--bucket", required=True)
obj.add_argument("--empty", action='store_true')
obj.add_argument("--delete", required=False, action='store_true')
obj.add_argument("--upload", required=False)
a = obj.parse_args()
if a.delete == True:
    delete_func(a.bucket)
elif a.empty == True:
    empty_func(a.bucket)
elif a.upload:
    upload_func(a.bucket, a.upload)
else:
    print("incorrect options")

print(a)
