import boto3

def lambda_handler(event, context):
    ec2 = boto3.client("ec2")
    instance_id = "i-0dbbf785ffa3d2d06"

    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"the ec2 has been started: {instance_id}")

    except Exception as e:
        print(f"the error is {e}")

        
