__author__ = 'ilya'

from motor import Op
from tornado.gen import coroutine
from tornado.web import asynchronous
from API.handlers.base import BaseHandler, authenticated
from bson import json_util as json

class MaraphonesHandler(BaseHandler):

    @asynchronous
    @coroutine
    def get(self):

        page = int(self.get_argument('page', 0))
        maraphones_cursor = self.maraphones.find().skip(page*10).limit(10)
        maraphones = yield Op(maraphones_cursor.to_list)
        maraphones_count = yield Op(self.maraphones.count)

        response = {
            'maraphones': maraphones,
            '_meta': {
                'count': maraphones_count,
                'offset': 10
            }
        }

        self.write(json.dumps(maraphones))
        self.finish()

    @authenticated
    @coroutine
    @asynchronous
    def post(self):

        new_maraphone = json.loads(self.request.body.decode('UTF-8'))
        maraphone_id = yield Op(self.maraphones.insert(new_maraphone))
        maraphone = yield Op(self.maraphones.find_one(maraphone_id))

        self.write(json.dumps(maraphone_id))
