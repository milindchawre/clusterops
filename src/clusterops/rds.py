def check_db_status(client, db, action):
    """
    Check current status of RDS before starting/stopping it
    """
    response = client.describe_db_instances(DBInstanceIdentifier=db)
    if action == "start":
        if response["DBInstances"][0]["DBInstanceStatus"] == "available":
            print(f"The DB {db} is already running.")
            return True
        elif response["DBInstances"][0]["DBInstanceStatus"] != "stopped":
            print("To start the DB, it should be in stopped state.", end=" ")
            print(f"DB {db} is in {response['DBInstances'][0]['DBInstanceStatus']} state.")
            return True
    elif action == "stop":
        if response["DBInstances"][0]["DBInstanceStatus"] == "stopped":
            print(f"The DB {db} is already in stopped state.")
            return True
        elif response["DBInstances"][0]["DBInstanceStatus"] != "available":
            print("To stop the DB, it should be in available state.", end=" ")
            print(f"DB {db} is in {response['DBInstances'][0]['DBInstanceStatus']} state.")
            return True
    return False


def start_rds(client, dbs):
    """
    Start RDS instances
    """
    print("Starting RDS ...")
    for db in dbs:
        if check_db_status(client, db, "start"):
            continue
        result = client.start_db_instance(DBInstanceIdentifier=db)
        print(result)
        print(f"Started DB {db}")
    print("RDS instances STARTED!")


def stop_rds(client, dbs):
    """
    Stop RDS instances
    """
    print("Stopping RDS ...")
    for db in dbs:
        if check_db_status(client, db, "stop"):
            continue
        result = client.stop_db_instance(DBInstanceIdentifier=db)
        print(result)
        print(f"Stopped DB {db}")
    print("RDS instances STOPPED!")
