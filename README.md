# IGS Attendance

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)


## Getting Started

### Prerequisites

List of dependencies that you will need to install before you can run this web application.

- Python (version 3.10 or latest) using DOCKER Image
- Other dependencies (requirements.txt) using DOCKER Image

    alembic==1.12.0
    blinker==1.6.3
    click==8.1.7
    Flask==2.3.3
    Flask-Login==0.6.2
    Flask-Mail==0.9.1
    Flask-Migrate==4.0.5
    flask-redis==0.4.0
    Flask-SQLAlchemy==3.1.1
    Flask-WTF==1.2.1
    greenlet==3.0.0
    itsdangerous==2.1.2
    Jinja2==3.1.2
    Mako==1.2.4
    MarkupSafe==2.1.3
    python-decouple==3.8
    python-dotenv==1.0.0
    redis==5.0.1
    SQLAlchemy==2.0.22
    typing_extensions==4.8.0
    Werkzeug==2.3.7
    WTForms==3.1.0

- DEV   : SQLite & DB-Browser
- PROD  : PostgreSQL (version 12 or latest) using DOCKER Image
- Redis Memory Cache using DOCKER Image

### Development Installation

1. Clone the repository and Create Python Environment:

   ```bash
   git clone https://github.com/azharnian/igsattendance.git
   cd igsattendance
   python -m venv env

2. Activate environment (Windows using Git Bash)

    ```bash
    source env/Scripts/activate
 
3. Linux / Mac using Terminal

   ```bash
    source env/bin/activate

4. Install python library and dependencies

    ```bash
    pip install -r requirments.txt

5. Set .env, create env variables from file application/config.py or copy from copy_of_env

    ```bash
    touch .env

6. Initialize Flask-Migrate for Database

    ```bash
    flask db init
    flask db migrate
    flask db upgrade

6. Run the application

    ```bash
    python app.py

