import boto3

def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    instance_id = "<your-instance-id>"

    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"the ec2 has been started: {instance_id}")

    except Exception as e:
        print(f"the error is {e}")

        
