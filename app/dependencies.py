from sqlalchemy.orm import Session
from dependency_injector import containers, providers

from app.database import Database


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    database = providers.Singleton(Database)

    session = providers.Singleton(Session, bind=database.provider.get_connection)

container = Container()