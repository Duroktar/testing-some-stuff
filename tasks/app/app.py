from __future__ import print_function
import falcon
import sys
from gevent.wsgi import WSGIServer

from routes.home import HomeResource
from routes.tasks import TasksResource
from services.tasks import TaskService

import settings

MODE = settings.MODE
HOST = settings.getHost()
PORT = settings.getPort()
DB = settings.getDatabase()

app = falcon.API()

# Resources are represented by long-lived class instances
home = HomeResource()
tasks = TasksResource(TaskService(DB))

# tasks will handle all requests to the '/tasks' URL path
app.add_route('/', home)
app.add_route('/tasks', tasks)

print("*Setting up http server")
http_server = WSGIServer((HOST, PORT), app)

print("*%s server running on http://%s:%s/" % (MODE, HOST, PORT))
try:
    http_server.serve_forever()
except KeyboardInterrupt:
    print("Shutting down server")
    tasks.service.close()

print("Goodbye")
