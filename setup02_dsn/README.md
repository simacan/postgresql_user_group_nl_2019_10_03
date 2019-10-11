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
```


```
~/projects/postgresql_user_group_nl_2019_10_03 $ python postgres_bloat_demo.py prepare --rows 1000 'port=5432 dbname=pgbench user=bench1 password=changeme'
Index fill factor [90]: 90
```


```
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
```