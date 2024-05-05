# Setting up python environment

Run the following to create a virtual environment for the project. (Assuming you have python installed on local machine)

```bash
python -m virtualenv env

```

If you're running the deployed instance, make sure to change the database connection string in `.env` file on the backend.

### Setting up `.env` file

To setup `.env` file on the backend, change the file named `.env` in `/app`.
Add the following in the `.env` file.

```txt
JWT_SECRET_KEY=<RAMDOM_STRING>
JWT_REFRESH_SECRET_KEY=<RANDOM_SECTURE_LONG_STRING>
MONGO_CONNECTION_STRING=<MONGO_DB_CONNECTION_STRING>
# mongodb://localhost:27017/ <-- for local running instances
```

# Activating virtual environment

```bash
# Windows
env/Scripts/activate

```

# Installing dependencies

Assuming you are in the base directory.

```bash
pip install -r requirements.txt
```

# Running the backend

Assuming you are in the backend directory.

```bash
uvicorn app.app:app --reload
```
