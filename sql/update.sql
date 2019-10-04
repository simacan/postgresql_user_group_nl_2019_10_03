update
	bloated
set
	value = random()
where
	id >= %(block_start)s and
	id < %(block_end)s;
