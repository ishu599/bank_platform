from sqlalchemy import Column

from sqlalchemy import Integer

from sqlalchemy import String

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TransactionTable(

    Base

):

    __tablename__ = "transactions"

    id = Column(

        Integer,

        primary_key=True,

        index=True

    )

    username = Column(

        String

    )

    amount = Column(

        Integer

    )