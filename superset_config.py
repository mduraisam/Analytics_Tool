import os
from datetime import timedelta

# Database configuration
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER', 'analytics')}:{os.getenv('POSTGRES_PASSWORD', 'analytics123')}@postgres:5432/{os.getenv('POSTGRES_DB', 'analytics_db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY', 'your-secret-key')

# Feature flags
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
}

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 300
}

# Celery configuration
CELERY_CONFIG = {
    'broker_url': 'redis://redis:6379/0',
    'result_backend': 'redis://redis:6379/0',
    'task_serializer': 'json',
    'accept_content': ['json'],
    'result_serializer': 'json',
    'timezone': 'UTC',
    'enable_utc': True,
}

# SQL Lab settings
SQLLAB_TIMEOUT = 300
SQLLAB_VALIDATION_TIMEOUT = 10
SQLLAB_DEFAULT_DBID = None

# Security settings
WTF_CSRF_ENABLED = True
WTF_CSRF_EXEMPT_LIST = []
MAPBOX_API_KEY = ''

# Additional database connections
SQLALCHEMY_EXAMPLES_URI = SQLALCHEMY_DATABASE_URI

# Trino database connection
TRINO_DATABASE_CONNECTION = {
    'sqlalchemy_uri': 'trino://trino:8084/postgresql/analytics_db',
    'cache_timeout': 300,
    'expose_in_sqllab': True,
    'allow_run_async': True,
    'allow_csv_upload': True,
    'allow_ctas': True,
    'allow_cvas': True,
    'allow_dml': True,
    'allow_multi_schema_metadata_fetch': True,
}

# Add Trino to the list of available databases
ADDITIONAL_DATABASE_CONNECTIONS = {
    'trino': TRINO_DATABASE_CONNECTION
}

# Session configuration
PERMANENT_SESSION_LIFETIME = timedelta(days=1)
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
} 