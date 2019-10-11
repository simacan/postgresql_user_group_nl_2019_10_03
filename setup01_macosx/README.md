## Setup notes - 001 - MacOSX 

### install psycopg2
```
~/projects/postgresql_user_group_nl_2019_10_03 $ python postgres_bloat_demo.py --help
Traceback (most recent call last):
  File "postgres_bloat_demo.py", line 4, in <module>
    import psycopg2
ModuleNotFoundError: No module named 'psycopg2'
```
https://stackoverflow.com/questions/12906351/importerror-no-module-named-psycopg2

pip install psycopg2-binary



```
~/projects/postgresql_user_group_nl_2019_10_03 $ which pip
/usr/local/opt/python/libexec/bin/pip
~/projects/postgresql_user_group_nl_2019_10_03 $ pip install psycopg2-binary
Collecting psycopg2-binary
  Downloading https://files.pythonhosted.org/packages/ee/ed/2772267467ba5c21a73d37149da0b49a4343c6646d501dbb1450b492d40a/psycopg2_binary-2.8.3-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (1.5MB)
    100% |████████████████████████████████| 1.6MB 3.5MB/s
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.8.3
```
https://stackoverflow.com/questions/33866695/install-psycopg2-on-mac-osx-10-9-5


### install tabulate

```
~/projects/postgresql_user_group_nl_2019_10_03 $ python postgres_bloat_demo.py --help
Traceback (most recent call last):
  File "postgres_bloat_demo.py", line 7, in <module>
    from tabulate import tabulate
ModuleNotFoundError: No module named 'tabulate'
~/projects/postgresql_user_group_nl_2019_10_03 $ pip install tabulate
Collecting tabulate
  Downloading https://files.pythonhosted.org/packages/66/d4/977fdd5186b7cdbb7c43a7aac7c5e4e0337a84cb802e154616f3cfc84563/tabulate-0.8.5.tar.gz (45kB)
    100% |████████████████████████████████| 51kB 2.1MB/s
Building wheels for collected packages: tabulate
  Building wheel for tabulate (setup.py) ... done
  Stored in directory: /Users/dpitts/Library/Caches/pip/wheels/e1/41/5e/e201f95d90fc84f93aa629b6638adacda680fe63aac47174ab
Successfully built tabulate
Installing collected packages: tabulate
Successfully installed tabulate-0.8.5
```




## Setup notes - 002 - setup DSN 


```
~/projects/postgresql_user_group_nl_2019_10_03 $ python postgres_bloat_demo.py prepare
Usage: postgres_bloat_demo.py prepare [OPTIONS] DSN
Try "postgres_bloat_demo.py prepare --help" for help.

Error: Missing argument "DSN".
~/projects/postgresql_user_group_nl_2019_10_03 $ python postgres_bloat_demo.py prepare --help
Usage: postgres_bloat_demo.py prepare [OPTIONS] DSN

Options:
  --rows INTEGER
  --fillfactor INTEGER
  --help                Show this message and exit.
~/projects/postgresql_user_group_nl_2019_10_03 $ python postgres_bloat_demo.py prepare --rows 1000
Usage: postgres_bloat_demo.py prepare [OPTIONS] DSN
Try "postgres_bloat_demo.py prepare --help" for help.

Error: Missing argument "DSN".
```




pgbench=# create user bench1 with password 'changeme';
CREATE ROLE
pgbench=# GRANT ALL PRIVILEGES ON DATABASE "pgbench" to bench1;
GRANT

~ $ psql -d pgbench -U bench1 --password
Password:
psql (11.5)
Type "help" for help.

pgbench=> \q



~/projects/postgresql_user_group_nl_2019_10_03 $ python postgres_bloat_demo.py prepare --rows 1000 'port=5432 dbname=pgbench user=bench1 password=changeme'
Index fill factor [90]: 90




~/projects/postgresql_user_group_nl_2019_10_03 $ psql -d pgbench
psql (11.5)
Type "help" for help.

pgbench=# \d
               List of relations
 Schema |       Name       |   Type   | Owner
--------+------------------+----------+--------
 public | bloated          | table    | bench1
 public | bloated_id_seq   | sequence | bench1
 public | pgbench_accounts | table    | dpitts
 public | pgbench_branches | table    | dpitts
 public | pgbench_history  | table    | dpitts
 public | pgbench_tellers  | table    | dpitts
(6 rows)

pgbench=# \d bloated
                                 Table "public.bloated"
 Column |       Type       | Collation | Nullable |               Default
--------+------------------+-----------+----------+-------------------------------------
 id     | bigint           |           | not null | nextval('bloated_id_seq'::regclass)
 value  | double precision |           | not null |
Indexes:
    "idx_bloated_id_value" btree (id, value) WITH (fillfactor='90')

pgbench=# \d bloated_id_seq
                       Sequence "public.bloated_id_seq"
  Type  | Start | Minimum |       Maximum       | Increment | Cycles? | Cache
--------+-------+---------+---------------------+-----------+---------+-------
 bigint |     1 |       1 | 9223372036854775807 |         1 | no      |     1
Owned by: public.bloated.id





