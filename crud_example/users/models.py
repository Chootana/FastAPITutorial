import sqlalchemy
from db import metadata
from db import engine


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column('user_name', sqlalchemy.String, index=True),
    sqlalchemy.Column('email', sqlalchemy.String, index=True),
    sqlalchemy.Column('hashed_password', sqlalchemy.String),
    sqlalchemy.Column('is_active', sqlalchemy.Boolean(), default=True),
    sqlalchemy.Column('is_super_user', sqlalchemy.Boolean(), default=True)
)

metadata.create_all(bind=engine)
