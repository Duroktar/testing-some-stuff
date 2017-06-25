from __future__ import print_function
import dateparser
from .db import BaseStorage, SqlError
import parsedatetime
from datetime import datetime

cal = parsedatetime.Calendar()


class TaskService(BaseStorage):
    def setup(self):
        self.executescript("""
            CREATE TABLE IF NOT EXISTS Tasks(
                Id              INTEGER PRIMARY KEY,
                description     TEXT,
                time            TEXT);
            """)

    def getAllTasks(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Tasks ORDER BY time")
        return cursor.fetchall()

    def getNextTask(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Tasks ORDER BY time")
        now = dateparser.parse("now")
        nextUp = cursor.fetchone()
        while now > dateparser.parse(nextUp[2]):
            nextUp = cursor.fetchone()
        return nextUp

    def createTask(self, description, when):
        time_struct, parse_status = cal.parse(when)
        whenDate = datetime(*time_struct[:6])
        if whenDate is None:
            whenDate = dateparser.parse(when)
        if whenDate is not None:
            self.execute('''INSERT INTO Tasks(description, time)
                            VALUES(?, ?)''', (description, whenDate))
        else:
            return "Error parsing time: %s" % when
        return None


# if __name__ == '__main__':
#     import sys
#     db = "tasks-test.db"

#     testdb = TaskService(db)
#     testdb.createTask('Walk the dog', 'tomorrow at 3pm')
#     testdb.createTask('Mow the lawn', 'tomorrow at 5pm')
#     testdb.createTask('Go to bed', 'tomorrow at 10pm')
#     print(testdb.getAllTasks())
#     print(testdb.getNextTask())
