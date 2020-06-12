# Login Template
The template uses the following:
- Flask
- SQLite
- WTForms
- Bootstrap CSS

Template contains the following:
- Register
- Login
- Logout
- Password Reset (Token & SMTP)

## Setup

### SQLite - Create Database
    from flaskApi import db
    from flaskApi.models import *
    db.create_all()

### SQLite - Query Database
    from flaskApi import db
    from flaskApi.models import *
    User.query.all()

### Run The Application
    python3 flaskApi.py