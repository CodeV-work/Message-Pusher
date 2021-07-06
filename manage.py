import logging

import click
import uvicorn

from apps import Base, engine
from apps.a_common.db import get_session_local
from apps.logconfig import set_all_log_info
from config import DEBUG, HOST, PORT


@click.group()
def cli():
    set_all_log_info(logging.WARNING)


@cli.command()
def run():
    uvicorn.run(app="apps:app", host=HOST, port=PORT, reload=DEBUG, debug=DEBUG)


@cli.group()
def db():
    pass


@db.command()
def create():
    Base.metadata.create_all(bind=engine)


@db.command()
def clean():
    with get_session_local() as session:
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()


@db.command()
def reset():
    with get_session_local() as session:
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    cli()
