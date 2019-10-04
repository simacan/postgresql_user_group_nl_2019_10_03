#!/usr/bin/env python3

import click
import psycopg2
import psycopg2.extras
import os.path
from tabulate import tabulate


def run_query(dsn, name, parameters={}, print_output=False):
    path = os.path.join('sql', name)
    with open(path, 'r') as file:
        content = file.read()

    conn = psycopg2.connect(dsn)
    conn.autocommit = True
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
            curs.execute(content, parameters)

            description = curs.description

            if description:
                result = curs.fetchall()

                if print_output:
                    colnames = list(map(lambda col: col.name, curs.description))
                    click.echo(tabulate(result, headers=colnames))

                return result
    finally:
        conn.close()


@click.group()
def cli():
    pass


@cli.command()
@click.argument('dsn', envvar='DSN')
@click.option('--rows', prompt='Number of rows', default=100000)
@click.option('--fillfactor', prompt='Index fill factor', default=90)
def prepare(dsn, rows, fillfactor):
    run_query(dsn, 'prepare_schema.sql', {'fillfactor': fillfactor})
    run_query(dsn, 'insert.sql', {'num': rows})
    run_query(dsn, 'vacuum_analyze.sql')


@cli.command()
@click.argument('dsn', envvar='DSN')
@click.option('--updates', prompt='Number of updates', default=10)
@click.option('--block', prompt='Block size', default=1000)
def create_bloat(dsn, updates, block):

    for i in range(0, 10000):
        block_range = {'block_start': i*block, 'block_end': (i+1)*block}

        for u in range(0, updates):
            run_query(dsn, 'update.sql', block_range)

        deleted = run_query(dsn, 'delete.sql', {**block_range, 'fraction': 0.8})[0]['deleted']

        run_query(dsn, 'vacuum_analyze.sql')
        run_query(dsn, 'insert.sql', {'num': deleted})

        click.echo("Creating index bloat... Iteration %d is done" % i)

        if deleted == 0:
            break

    click.echo("Done.")


@cli.command()
@click.argument('dsn', envvar='DSN')
def check(dsn):
    click.echo('Table bloat:')
    click.echo('')
    run_query(dsn, "table_bloat_check.sql", print_output=True)
    click.echo('')
    click.echo('')
    click.echo('Index bloat:')
    click.echo('')
    run_query(dsn, "index_bloat_check.sql", print_output=True)


@cli.command()
@click.argument('dsn', envvar='DSN')
def vacuum(dsn):
    run_query(dsn, "vacuum_analyze.sql")


@cli.command()
@click.argument('dsn', envvar='DSN')
def vacuum_full(dsn):
    run_query(dsn, "vacuum_full.sql")


@cli.command()
@click.argument('dsn', envvar='DSN')
def re_index(dsn):
    run_query(dsn, "re_index.sql")


if __name__ == '__main__':
    cli()