__author__ = 'ilya'

from motor import Op
from tornado.gen import coroutine
from tornado.web import asynchronous
from API.handlers.base import BaseHandler, authenticated
from bson import json_util as json
from bson.objectid import ObjectId


class NewsFlashHandler(BaseHandler):

    @asynchronous
    @coroutine
    def get(self, id):

        newsflash = yield Op(self.news.find_one, ObjectId(id))

        self.write(json.dumps(newsflash))
        self.finish()

    @asynchronous
    @authenticated
    @coroutine
    def post(self, id):

        post = json.loads(self.request.body)
        post["_id"] = ObjectId(post["_id"])
        result_id = yield Op(self.news.save, post)
        result = yield Op(self.news.find_one, result_id)

        self.write(json.dumps(result))
        self.finish()


class NewsHandler(BaseHandler):

    @asynchronous
    @coroutine
    def get(self):

        news_cursor = self.news.find().sort('$natural', -1).limit(10)
        news = yield Op(news_cursor.to_list)

        self.write(json.dumps(news))
        self.finish()


    @asynchronous
    @authenticated
    @coroutine
    def post(self):

        newsflash = json.loads(self.request.body)
        result_id = yield Op(self.news.insert, newsflash)
        result = yield Op(self.news.find_one(result_id))

        self.write(json.dumps(result))
        self.finish()