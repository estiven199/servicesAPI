import sqlalchemy as _sql
from  sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://root:root@127.0.0.1/root"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
