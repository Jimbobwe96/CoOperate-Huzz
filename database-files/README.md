# `database-files` Folder

This folder contains all the files and configurations related to the database used in this project. It typically includes database schemas, initial seed data, and other relevant scripts to manage or interact with the database.

---

## 🗂 Purpose of the Folder

The `database-files` folder plays a critical role in the following:

- **Managing Database Schema:** Contains `.sql` or migration files defining the structure of the database tables, relationships, and indexes.
- **Seeding Initial Data:** Includes scripts or files to populate the database with starter or mock data for development purposes.
- **Database Configuration:** Holds configuration files (e.g., `config.yml`, `.env`) required for database setup.
- **Backup and Restore:** (Optional) May include scripts for creating backups or restoring the database.

---

## ⚙️ How the Database Works

1. **Bootstrap:**  
   Initial setup of the database is handled via `docker-compose`. This ensures the database container is created and properly configured.

2. **Persisted Data:**  
   Data is persisted in a volume specified in the `docker-compose.yml` file. This means data won't be lost even when the container is stopped or restarted.

3. **Database Management:**  
   Changes to the database structure (e.g., new tables, columns, or indexes) should be made through migrations or updated scripts stored in this folder.

---

## 🚀 How to Re-Bootstrap the Database

Re-bootstrapping the database involves resetting the database container and starting with a fresh database instance. Follow these steps:

### Prerequisites
Ensure Docker is installed and running on your system.

### Steps

1. **Open Docker Desktop**  
   Launch Docker Desktop to view and manage running containers.

2. **Delete the Database Container**  
   Locate the database container related to this project. Stop and delete it to ensure a clean start.  
   Alternatively, use the terminal:
   ```bash
   docker stop <container_name>
   docker rm <container_name>
