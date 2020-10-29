from clusterops import ec2
from clusterops import rds


def start_resource(aws):
    """
    Start AWS Resource
    """
    client = initialize_aws_client(aws.resource)
    if aws.resource == "ec2":
        ec2.start_ec2(client, aws.tags, aws.instance_ids)
    elif aws.resource == "rds":
        rds.start_rds(client, aws.db)


def stop_resource(aws):
    """
    Stop AWS Resource
    """
    client = initialize_aws_client(aws.resource)
    if aws.resource == "ec2":
        ec2.stop_ec2(client, aws.tags, aws.instance_ids)
    elif aws.resource == "rds":
        rds.stop_rds(client, aws.db)


def initialize_aws_client(resource):
    """
    Initialize AWS client
    """
    import boto3

    print("Initializing AWS client ...")
    client = boto3.client(resource, region_name="eu-west-1")
    return client
