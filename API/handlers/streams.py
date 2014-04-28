from motor import Op
from tornado.gen import coroutine
from tornado.web import asynchronous
from API.handlers.base import BaseHandler, authenticated
from bson import json_util as json

__author__ = 'ilya'


class ChannelsHandler(BaseHandler):

    @asynchronous
    @coroutine
    def get(self):

        live = self.get_argument('live', False)
        main_channels = self.channels.find({'main': True}).sort('order')
        if live:
            other_channels = self.channels.find({'main': False, 'live': True})
        else:
            other_channels = self.channels.find({'main': False})
        main_channels = yield Op(main_channels.to_list)
        other_channels = yield Op(other_channels.to_list)
        main_live_count = yield Op(self.channels.find({'main': True, 'live': True}).count)
        other_live_count = yield Op(self.channels.find({'main': False, 'live': True}).count)

        chanlist = {
            'main': main_channels,
            'other': other_channels,
            '_meta': {
                'main_live': main_live_count,
                'other_live': other_live_count
            }
        }

        self.write(json.dumps(chanlist))
        self.finish()

    @authenticated
    @asynchronous
    @coroutine
    def post(self):

        channel = json.loads(self.request.body.decode('UTF-8'))
        channel_id = yield Op(self.channels.insert, channel)
        channel = yield Op(self.channels.find_one, channel_id)
        self.write(json.dumps(channel))
        self.finish()


class ChannelHandler(BaseHandler):

    @asynchronous
    @coroutine
    def get(self, channel):

        channel = yield Op(self.channels.find_one, channel)

        self.write(json.dumps(channel))
        self.finish()

    @authenticated
    @asynchronous
    @coroutine
    def post(self, channel):

        update = json.loads(self.request.body.decode('UTF-8'))
        channel_id = yield Op(self.channels.save, update)
        channel = yield Op(self.channels.find_one, channel_id)
        self.write(json.dumps(channel))
        self.finish()

    @authenticated
    @asynchronous
    @coroutine
    def delete(self, channel):
        result = yield Op(self.channels.remove, {'_id': channel})
        self.finish()