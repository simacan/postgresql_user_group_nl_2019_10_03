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

