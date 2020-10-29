from argparse import ArgumentParser
from clusterops import resource


def create_parser():
    """
    Initialize the parser
    """
    parser = ArgumentParser(prog="cluster-ops", description="CLI to start/stop AWS resources")
    parser.add_argument("action", choices=["start", "stop"], help="Select start/stop action")
    subparsers = parser.add_subparsers(help="select AWS resource", required=True, dest="resource")
    parser_ec2 = subparsers.add_parser("ec2", help="start/stop ec2")
    # parser_ec2.set_defaults(ec2=True, rds=False)
    parser_ec2.add_argument("--tags", nargs="+", help="select ec2 based on tags")
    parser_ec2.add_argument("--instance-ids", nargs="+", help="select ec2 based on instance ids")
    parser_rds = subparsers.add_parser("rds", help="start/stop RDS")
    # parser_rds.set_defaults(ec2=False, rds=True)
    parser_rds.add_argument("db", nargs="+", help="Name of the db's")
    return parser


def check_args(args, parser):
    """
    Vaildate parser arguments
    """
    if args.resource == "ec2":
        if not (args.tags or args.instance_ids):
            parser.error("Please provide --tags or --instance-ids option.")


def main():
    p = create_parser()
    args = p.parse_args()
    check_args(args, p)
    if args.action == "start":
        resource.start_resource(args)
    elif args.action == "stop":
        resource.stop_resource(args)
