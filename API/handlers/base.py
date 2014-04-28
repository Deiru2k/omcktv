import functools
import hashlib
import urllib
from tornado.web import RequestHandler, asynchronous
from tornado.gen import coroutine, Task
from motor import Op, MotorClient
from bson import json_util as json, ObjectId


connection = MotorClient().open_sync()
db = connection['omcktv']


def authenticated(f):
    @functools.wraps(f)
    @coroutine
    def wrapper(self, *args, **kwargs):
        self._auto_finish = False
        self.current_user = yield Task(self.get_current_user)
        if not self.current_user:
            self.set_status(400)
            self.finish()
        else:
            f(self, *args, **kwargs)

    return wrapper


@coroutine
def login(self, username, password):
    user = yield Op(self.users.find_one, username)
    if user:
        if hashlib.sha256(password.encode('ASCII')).hexdigest() == user['password']:
            session = yield Op(self.sessions.insert, {'user': username})
            self.set_secure_cookie('user_token', str(session))
            del user['password']
            return user
        else:
            return False
    else:
        return False

@coroutine
def logout(self, username):
    session_key = self.get_secure_cookie('user_token')
    result = yield Op(self.sessions.remove, {'_id': session_key})
    return True


class BaseHandler(RequestHandler):
    current_user = None
    db = connection['omcktv']
    channels = db['channels']
    users = db['users']
    sessions = db['sessions']
    news = db['news']
    maraphones = db['maraphones']

    @coroutine
    def get_current_user(self):

        token = self.get_secure_cookie('user_token')
        if token:
            session = yield Op(self.sessions.find_one, ObjectId(token.decode('UTF-8')))
            if session:
                user = yield Op(self.users.find_one, session['user'])
                if user:
                    return user
                else:
                    return False
            else:
                return False