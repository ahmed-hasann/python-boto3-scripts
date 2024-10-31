import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Step 1: Describe volumes
    volumes = ec2_client.describe_volumes()['Volumes']

    # Step 2: Filter for unattached volumes
    unattached_volumes = [
        volume for volume in volumes
        if not volume['Attachments']
    ]

    # Step 3: Delete the unattached volumes
    for volume in unattached_volumes:
        volume_id = volume['VolumeId']
        print(f"Deleting unattached volume: {volume_id}")
        ec2_client.delete_volume(VolumeId=volume_id)

    return {
        'statusCode': 200,
        'body': f"Deleted {len(unattached_volumes)} unattached volumes that are no longer in uage."
    }
