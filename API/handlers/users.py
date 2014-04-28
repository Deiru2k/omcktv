import hashlib
from tornado.web import asynchronous
from tornado.gen import coroutine
from API.handlers.base import BaseHandler, authenticated, Op, json


class UserHandler(BaseHandler):

    @asynchronous
    @coroutine
    def get(self, username):

        user = yield Op(self.users.find_one(username))
        if user:
            del user['password']
            self.write(json.dumps(user))
        else:
            self.set_status(404)
        self.finish()

    @authenticated
    @asynchronous
    @coroutine
    def delete(self, username):

        if username != 'Misaka42':
            result = yield Op(self.users.remove, {'_id': username})
            self.write(json.dumps(result))
            self.finish()
        else:
            self.set_status(500)
            self.write('Cannot delete Misaka42, HAHA')
            self.finish()


class UsersHandler(BaseHandler):

    @asynchronous
    @coroutine
    def get(self):

        users_cursor = self.users.find()
        users = yield Op(users_cursor.to_list)
        self.write(json.dumps(users))
        self.finish()

    @authenticated
    @asynchronous
    @coroutine
    def post(self):

        new_user = json.loads(self.request.body.decode('UTF-8'))
        new_user['password'] = hashlib.sha256(new_user['password'].encode('UTF-8')).hexdigest()
        user_id = yield Op(self.users.insert, new_user)
        user = yield Op(self.users.find_one, user_id)
        del user['password']
        self.write(json.dumps(user))
        self.finish()