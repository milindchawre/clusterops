def convert_tags_to_aws_filters(tags):
    """
    Convert tags from [NAME=VALUE] format to AWS filter format
    """
    filters = []
    for tag in tags:
        tag_dict = {}
        name, value = tag.split("=")
        tag_dict["Name"] = "tag:" + name
        tag_dict["Values"] = [value]
        filters.append(tag_dict)
    return filters


def get_instance_ids_from_tags(client, tags):
    """
    This function return instance-ids from ec2 tags
    """
    tags_filters = convert_tags_to_aws_filters(tags)
    result = client.describe_instances(Filters=tags_filters)
    instance_ids = []
    instances = result["Reservations"]
    for i in instances:
        instance_ids.append(i["Instances"][0]["InstanceId"])
    return instance_ids


def start_ec2(client, tags, ids):
    """
    Start EC2 instances
    """
    print("Starting EC2's ...")
    instances = []
    if tags is not None:
        instances = get_instance_ids_from_tags(client, tags)
    if ids is not None:
        instances.extend(ids)
    result = client.start_instances(InstanceIds=instances)
    print(result)
    print(f"EC2 instances STARTED!\nInstance IDs: {instances}")


def stop_ec2(client, tags, ids):
    """
    Stop EC2 instances
    """
    print("Stopping EC2's ...")
    instances = []
    if tags is not None:
        instances = get_instance_ids_from_tags(client, tags)
    if ids is not None:
        instances.extend(ids)
    result = client.stop_instances(InstanceIds=instances)
    print(result)
    print(f"EC2 instances STOPPED!\nInstance IDs: {instances}")
