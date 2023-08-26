import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# Specify the instance ID
instance_id = 'i-077ccae625fca587e'

# Describe the EC2 instance
response = ec2_client.describe_instances(InstanceIds=[instance_id])

# Print the instance details
instance = response['Reservations'][0]['Instances'][0]
print("Instance ID:", instance['InstanceId'])
print("Instance State:", instance['State']['Name'])
print("Instance Type:", instance['InstanceType'])
