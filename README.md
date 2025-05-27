# Analytics Tool

This project sets up a development environment for analytics using Docker Compose. It integrates PostgreSQL, Apache Superset, Trino, and pgAdmin.

## Overview

- **Postgres:** A PostgreSQL database (analytics_db) is created and initialized with a Retail Banking DDL (see `init_retail_banking.sql`).
- **Trino:** A custom Trino image (built from `Dockerfile.trino`) is used to copy custom config files (from `trino/etc`) into `/etc/trino` at build time (to avoid macOS Docker bind mount issues).
- **Apache Superset:** A web-based analytics dashboard (available at http://localhost: 8088) is configured to query data from PostgreSQL (via Trino).
- **pgAdmin:** A web UI for PostgreSQL (available at http://localhost: 5050) is integrated. Use the JDBC URL (jdbc:postgresql://postgres: 5432/analytics_db) to connect in pgAdmin.

## Prerequisites

- Docker and Docker Compose (latest version recommended).
- (Optional) A Linux VM or a non-synced folder (if you encounter macOS Docker issues).

## Getting Started

1. Clone this repository.
2. (Optional) Review and adjust the Retail Banking DDL (`init_retail_banking.sql`) if needed.
3. Run the stack:
   ```sh
   docker-compose down -v && docker-compose up -d
   ```
4. **Postgres:** The database (analytics_db) is created and initialized (via `init_retail_banking.sql`).
5. **Trino:** A custom Trino image is built (using `Dockerfile.trino`) so that custom configs (from `trino/etc`) are copied into `/etc/trino` at build time.
6. **Apache Superset:** Access the dashboard at http://localhost: 8088 (default admin/admin).
7. **pgAdmin:** Access the PostgreSQL web UI at http://localhost: 5050 (default admin@example.com/admin). Use the JDBC URL (jdbc:postgresql://postgres: 5432/analytics_db) to connect.

## Troubleshooting

- **Trino Java Error:** If you see "could not exec java to determine jvm version: exit status 1" (even with a custom image), it is likely a Docker Desktop for Mac issue. Try running on a Linux VM or a non-synced folder.
- **pgAdmin:** Ensure that the Postgres service is healthy (pgAdmin depends on it) and that you use the correct JDBC URL (jdbc:postgresql://postgres: 5432/analytics_db) in pgAdmin's "Connection" tab.

## Additional Notes

- The Retail Banking DDL (`init_retail_banking.sql`) is mounted into Postgres's `/docker-entrypoint-initdb.d/` so that it runs on first startup (and is idempotent).
- A custom Trino image (using `Dockerfile.trino`) is used to avoid macOS Docker bind mount issues.

## Components

- **PostgreSQL**: Main database running on port 5432
- **Apache Superset**: Web UI accessible at http://localhost:8088
- **Trino**: Query engine running on port 8084

## Accessing the Services

- **Superset**: http://localhost:8088
  - Username: admin
  - Password: admin

- **PostgreSQL**:
  - Host: localhost
  - Port: 5432
  - Database: analytics_db
  - Username: analytics
  - Password: analytics123

- **Trino**:
  - Host: localhost
  - Port: 8084

## Setting up Superset with Trino

1. Log in to Superset (http://localhost:8088)
2. Go to Data → Databases
3. Click "+ Database"
4. Select "Trino" as the database type
5. Use the following connection string:
   ```
   trino://trino:8084/postgresql/analytics_db
   ```
6. Test the connection and save

## Creating Your First Dashboard

1. In Superset, go to Data → Datasets
2. Click "+ Dataset"
3. Select the Trino database
4. Choose a table from your PostgreSQL database
5. Create visualizations and add them to a dashboard

## Stopping the Services

```bash
docker-compose down
```

To remove all data (including volumes):
```bash
docker-compose down -v
```

## Notes

- The PostgreSQL data is persisted in a Docker volume
- Superset configuration is stored in a Docker volume
- Default credentials are set for development purposes only
- For production use, please change all default passwords and secrets 