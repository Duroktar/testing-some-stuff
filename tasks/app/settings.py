import os

__homedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Set mode here dummy!
MODE = "Development"

# Development settings go here
DEV_HOST = 'localhost'
DEV_PORT = os.environ.get('TASKSERVICE_SERVICE_PORT')
# DEV_PORT = os.environ.get('TASKS_SERVICE_PORT')
DEV_DB_PATH = os.path.join(__homedir, 'data', 'tasks-test.db')

# DANGER - Production Settings go here.
HOST = 'www.someurl.com/'
PORT = os.environ.get('TASKSERVICE_SERVICE_PORT')
DB_PATH = os.path.join(__homedir, 'data', 'tasks.db')

# Use these to get settings.
def getDatabase():
    ENV_LOOKUP = dict(
        Production=DB_PATH,
        Development=DEV_DB_PATH
    )
    return ENV_LOOKUP[MODE]


def getHost():
    ENV_LOOKUP = dict(
        Production=HOST,
        Development=DEV_HOST
    )
    return ENV_LOOKUP[MODE]


def getPort():
    ENV_LOOKUP = dict(
        Production=PORT,
        Development=DEV_PORT
    )
    return int(ENV_LOOKUP[MODE])
