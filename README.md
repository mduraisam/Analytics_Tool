# Analytics Tool with Trino and Apache Superset

This project sets up an analytics environment using Trino (formerly PrestoSQL) for querying data and Apache Superset for visualization and analytics.

## Components

- **Trino**: Distributed SQL query engine
- **Apache Superset**: Modern data exploration and visualization platform
- **PostgreSQL**: Used as metadata database for Superset
- **Redis**: Used for caching and async tasks in Superset
- **pgAdmin**: Web-based PostgreSQL administration tool

## Prerequisites

- Docker
- Docker Compose
- Git

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd analytics-tool
```

2. Start the services:
```bash
docker-compose up -d
```

3. Initialize Superset:
```bash
docker-compose exec superset superset db upgrade
docker-compose exec superset superset init
```

4. Create an admin user for Superset:
```bash
docker-compose exec superset superset fab create-admin \
    --username admin \
    --firstname Superset \
    --lastname Admin \
    --email admin@example.com \
    --password admin
```

## Accessing the Services

- **Superset**: http://localhost:8088
  - Default credentials: admin/admin
- **Trino**: http://localhost:8080
- **pgAdmin**: http://localhost:5050
  - Default credentials: admin@admin.com/admin

## Configuration Details

### Superset Configuration
The Superset container has been customized with the following dependencies:
- Trino SQLAlchemy dialect for Trino database connectivity
- psycopg2-binary for PostgreSQL connectivity
- Additional system dependencies for building Python packages

Key features of the Superset setup:
- Custom Dockerfile (Dockerfile.superset) with necessary dependencies
- Persistent volume for Superset configuration
- Integration with Trino for data querying
- PostgreSQL backend for metadata storage
- Redis for caching and async operations

### Trino Configuration
- Custom catalog configuration for data sources
- Persistent volume for Trino configuration
- Exposed on port 8080

### Database Setup
- PostgreSQL instance for Superset metadata
- Persistent volume for database storage
- pgAdmin for database management

## Recent Updates

### Dockerfile.superset Updates
The Superset Dockerfile has been enhanced with:
1. System Dependencies:
   - Added build-essential for compiling Python packages
   - Added libpq-dev for PostgreSQL development
   - Updated Python package management

2. Python Package Installation:
   - Added trino[sqlalchemy] for Trino connectivity
   - Added psycopg2-binary for PostgreSQL connectivity
   - Installation verification steps for both packages

3. Environment Setup:
   - Proper user context switching (root/superset)
   - Package installation in both root and superset user environments
   - Verification steps to ensure proper installation

## Troubleshooting

### Common Issues

1. **Database Connection Issues**
   - Ensure PostgreSQL is running: `docker-compose ps`
   - Check logs: `docker-compose logs postgres`

2. **Trino Connection Issues**
   - Verify Trino is running: `docker-compose ps`
   - Check Trino logs: `docker-compose logs trino`
   - Ensure proper catalog configuration

3. **Superset Issues**
   - Check Superset logs: `docker-compose logs superset`
   - Verify all dependencies are installed
   - Ensure proper database initialization

### Logs and Debugging
To view logs for any service:
```bash
docker-compose logs <service-name>
```

To rebuild a specific service:
```bash
docker-compose build --no-cache <service-name>
docker-compose up -d <service-name>
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your License Here] 