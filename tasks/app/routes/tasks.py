from __future__ import print_function
import json
import falcon


class TasksResource:
    def __init__(self, service):
        self.service = service

    def on_get(self, req, resp):
        """Returns the next upcoming task

             - usage example -
            http:/HOST:PORT/tasks
         """
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps(self._getNextTaskJSON())

    def on_post(self, req, resp):
        """Creates a new task

             - usage example -
            http:/HOST:PORT/tasks?description="Mow the lawn"&when="tomorrow at 6pm"
         """
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps(self._createNewTask(req.params))

    def _getNextTaskJSON(self):
        nextTask = self.service.getNextTask()
        if nextTask is None:
            return {"success": False, "err": "No tasks"}
        return {"description": nextTask[1], "when": nextTask[2]}

    def _createNewTask(self, params):
        try:
            description = params['description']
            when = params['when']
            resp = self.service.createTask(description, when)
        except Exception as err:
            return {"success": False, "err": str(err)}
        else:
            if resp is not None:
                return {"success": False, "err": resp}
            return {"success": True, "err": None}
