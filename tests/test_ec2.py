from clusterops import ec2


def test_convert_tags_to_aws_filters():
    """
    Test whether aws filters are generated from tags
    """
    tags = ["Name=Machine-1", "ENV=Testing"]
    assert ec2.convert_tags_to_aws_filters(tags) == [
        {"Name": "tag:Name", "Values": ["Machine-1"]},
        {"Name": "tag:ENV", "Values": ["Testing"]},
    ]
