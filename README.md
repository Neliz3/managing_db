# Managing db | web-site for the wholesale database

#### Web-site in Python using Flask, PostgreSQL and gspread library

## Table of contents

* [Setup](#Setup)
    * [Technologies Used](#Technologies-Used)
    * [Installation](#Installation)
    * [Requirements](#Requirements)
    * [Room for improvement](#Room-for-improvement)
        * [Future features](#Future-features)
        * [Future changing](#Future-changing)

## Setup

* All packages are located in requirements.txt
* Environmental variables are located in .env

### Technologies Used

* Python 3.8
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* JavaScript
* Bootstrap

### Installation

```bash
python3 -m venv env
```

```bash
. env/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
sudo service postgresql start
```

```bash
python run.py
```

### Requirements

```bash
pip install load-dotenv
```

```bash
pip install Flask
```

```bash
pip install Flask-SQLAlchemy
```

```bash
pip install psycopg2-binary
```

```bash
pip install gspread
```

### Database managing

```bash
sudo -i -u postgres
```

```bash
psql managing_db
```


### Room for improvement

#### Future features

* Adding new languages
* Adding feature for an admin to do more actions

#### Future changing

* Rebuild a database structure for more opportunities (adding some tables)
