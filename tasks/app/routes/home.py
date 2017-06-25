from __future__ import print_function
import falcon


class HomeResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        message = {
            'message': 'Welcome to the tasks homepage. Navigate to /tasks from here for your next task.',
            'author': 'Duroktar'
        }
        resp.body = json.dumps(message)
  