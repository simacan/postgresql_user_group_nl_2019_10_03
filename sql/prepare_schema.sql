drop table if exists bloated;

create table if not exists bloated (
    id bigserial not null,
    value double precision not null
);

create index if not exists
    idx_bloated_id_value
on
    bloated
using
    btree (id, value)
with
    (fillfactor=%(fillfactor)s)
;

truncate bloated;
