import click

from src import create_app
from src.commons.scripts import clean_db, create_factories, init_db, load_db


@click.group(name="cli")
def cli():
    pass


@cli.command(name="load_db", help="load db")
def load_db_cli():
    app = create_app()
    with app.app_context():
        load_db()


@cli.command(name="create_factories", help="create data")
def create_factories_cli():
    app = create_app()
    with app.app_context():
        create_factories()


@cli.command(name="clean_db")
def clean_db_cli():
    app = create_app()
    with app.app_context():
        clean_db()


@cli.command(name="init_db")
def db_cli():
    app = create_app()
    with app.app_context():
        init_db()


if __name__ == "__main__":
    cli()
