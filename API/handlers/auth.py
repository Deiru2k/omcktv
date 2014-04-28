__author__ = 'ilya'

from API.handlers.base import BaseHandler, authenticated, login, logout
from tornado.web import asynchronous
from tornado.gen import coroutine, Task
from bson import json_util as json


class LoginHandler(BaseHandler):

    @asynchronous
    @coroutine
    def post(self):
        creds = json.loads(self.request.body.decode('ASCII'))
        username, password = creds['username'], creds['password']
        user = yield Task(login, self, username, password)
        if user:
            self.write(json.dumps(user))
        else:
            self.set_status(400)
        self.finish()


class LogoutHandler(BaseHandler):

    @authenticated
    @asynchronous
    @coroutine
    def get(self):
        user = yield Task(self.get_current_user)
        logout(self, user['_id'])
        print(self.clear_cookie('user_token'))
        self.finish()


class CurrentUser(BaseHandler):

    @authenticated
    @asynchronous
    @coroutine
    def get(self):
        user = yield Task(self.get_current_user)
        del user['password']
        self.write(json.dumps(user))
        self.finish()