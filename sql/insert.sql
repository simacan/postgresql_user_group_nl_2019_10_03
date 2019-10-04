insert into
    bloated (value)
select
    random()
from
    generate_series(1, %(num)s)
