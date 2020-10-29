import pytest
from clusterops import cli


@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_values(parser):
    """
    Test whether values in parser are set properly
    """
    args = parser.parse_args(["start", "ec2", "--tags", "name=value", "--instance-ids", "i-0282b825usu2n2i3n382"])
    assert args.action == "start"
    assert args.resource == "ec2"
    assert args.instance_ids == ["i-0282b825usu2n2i3n382"]
    assert args.tags == ["name=value"]
    args = parser.parse_args(["stop", "rds", "db1", "db2"])
    assert args.action == "stop"
    assert args.resource == "rds"
    assert args.db == ["db1", "db2"]


def test_parser_invalid_values(parser):
    """
    Test invalid cases for cli parser
    """
    with pytest.raises(SystemExit):
        parser.parse_args(["start", "ec2", "--tags"])
    with pytest.raises(SystemExit):
        parser.parse_args(["start", "ec2", "--instance-ids"])
    with pytest.raises(SystemExit):
        parser.parse_args(["start", "rds"])


def test_check_args(parser):
    """
    Test validate parser arguments
    """
    args = parser.parse_args(["start", "ec2"])
    with pytest.raises(SystemExit):
        cli.check_args(args, parser)
