TRINO_URI = "trino://trino@analytics_trino:8080/postgresql/analytics_db"
TRINO_NAME = "Trino (Postgres Catalog)"

from superset import db
from superset.models.core import Database

if not db.session.query(Database).filter_by(database_name=TRINO_NAME).first():
    database = Database(
        database_name=TRINO_NAME,
        sqlalchemy_uri=TRINO_URI,
        expose_in_sqllab=True,
        allow_run_async=True,
    )
    db.session.add(database)
    db.session.commit()
    print(f"Successfully registered Trino database: {TRINO_NAME}")
else:
    print(f"Trino database '{TRINO_NAME}' already exists.") 