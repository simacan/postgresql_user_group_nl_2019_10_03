# Demonstration script used at the PostgreSQL User Group of 2019-10-03

## Libraries
You have to have these Python libraries installed:
- psycopg2
- tabulate
- click

## Usage
Please configure an environment variable DSN first, which psycopg2 understands.

Invoke `postgres_bloat_demo.py --help` to see the available options. Typical chain of commands:
1. prepare
2. create_bloat
3. check

You could experiment with the parameters. Defaults were used at the demonstration.

Tested with Python 3.6.8 on Ubuntu 18.04.



