__author__ = 'ilya'

from tornado.web import Application
from tornado.ioloop import IOLoop
from API.handlers import base, auth, users, streams, news

handlers = [
    (r'/api/login', auth.LoginHandler),
    (r'/api/logout', auth.LogoutHandler),
    (r'/api/current_user', auth.CurrentUser),
    (r'/api/users', users.UsersHandler),
    (r'/api/users/(.*)', users.UserHandler),
    (r'/api/news', news.NewsHandler),
    (r'/api/news/(.*)', news.NewsFlashHandler),
    (r'/api/channels', streams.ChannelsHandler),
    (r'/api/channels/(.*)', streams.ChannelHandler)
]

app = Application(handlers, cookie_secret='adsfhakljdshf189f7d8s9a6ga70gds6ag8f07190-aq7d8fsd87gg')
app.listen(8886)

IOLoop.instance().start()