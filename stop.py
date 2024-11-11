import boto3

def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    instance_id = "<your-instance-id>"

    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"this instance has been stopped {instance_id}")

    except Exception as e:
        print(f"the error is {e}")