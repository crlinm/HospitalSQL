## HospitalDB: Patient and Doctor Scheduling Simple System
### Basics of SQL: Queries and Data Management with Python and PostgreSQL
### Project Description

This project provides code for interacting with a database, including the registration of patients, doctors, scheduling appointments, and other data management functions. The project demonstrates the creation and management of a database using Python and PostgreSQL.

### Key Features:
* Database creation at startup.
* Access to the database through Python for retrieving and modifying data.
* Registration of patients and doctors.
* Scheduling patients with doctors.
* Managing appointment schedules.

### Libraries Used:
* psycopg2-binary
* python-dotenv

### Installation

1. Create a virtual environment:
```
python -m venv venv
```
2. Activate the virtual environment:
For Windows:
```
venv\Scripts\activate
```
For Unix/MacOS:
```
source venv/bin/activate
```
3. Install dependencies from the requirements.txt file:
```
pip install -r requirements.txt
```
4. Configure the environment variables:
Create a file named .env in the root directory of the project and fill it with your database configuration details.

`env.template`<br>
This template file includes the necessary environment variables for configuring your database connection. Copy this template to a .env file and fill in the appropriate values
```
DB_HOST=your_database_host
DB_PORT=your_database_port
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```


### Project Structure

**controllers**: Methods for interacting with the database.<br>
**workspace**: Methods for the user interface (superusers, doctors, patients).

