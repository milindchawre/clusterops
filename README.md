# clusterops

CLI to start/stop ec2's and rds instances.

Preparing for Development
-------------------------
1. Ensure pip and pipenv are installed
2. Clone repository: `https://github.com/milindchawre/clusterops`
3. `cd clusterops`
4. Fetch development dependencies `make install`
5. Activate virtualenv: `pipenv shell`

Usage
-----
Start/Stop ec2 machines based on tags or instance-ids.
```
$ cluster-ops [start/stop] ec2 --tag NAME=VALUE NAME2=VALUE2 --instance-ids id1 id2
```

Start/Stop rds.
```
$ cluster-ops [start/stop] rds db-name-1 db-name-2
```

### Running Tests
-----------------
Run tests locally using make if virtualenv is active:
```
$ make
```
If virtualenv isn’t active then use:
```
$ pipenv run make
```
