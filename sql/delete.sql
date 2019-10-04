with
deleted as(
    delete
    from
        bloated
    where
        value < %(fraction)s and
        id >= %(block_start)s and
        id < %(block_end)s
    returning
        id
)
select
    count(*) as deleted
from
    deleted

