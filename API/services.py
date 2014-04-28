__author__ = 'ilya'

from tornado.httpclient import HTTPClient
from xml.dom.minidom import parseString
import json

client = HTTPClient()


def twitch(channel):

    try:
        url = "https://api.twitch.tv/kraken/streams/%s" % channel
        status = json.loads(client.fetch(url).body.decode('UTF-8'))['stream']
        live = bool(status)
        if live:
            response = {
                'live': True,
                'viewers': status['viewers']
            }
        else:
            response = {
                'live': False,
                'viewers': 0
            }
        return response
    except:
        raise Exception('HTTP Error')


def livestream(channel):

    try:
        channel_safe = channel.replace('_', '-')
        url = 'http://x%sx.api.channel.livestream.com/2.0/livestatus.json' % channel_safe
        status = json.loads(client.fetch(url).body.decode('UTF-8'))['channel']
        response = {
            'live': status['isLive'],
            'viewers': status['currentViewerCount']
        }
        return response
    except:
        raise Exception("HTTP Error")


def omckhd(url):

    try:
        body = client.fetch(url).body.decode('UTF-8')
        xml = parseString(body)
        live = xml.getElementsByTagName('publishing')
        viewers = xml.getElementsByTagName('nclients')[0].childNodes[0].nodeValue
        return {
            'live': bool(live),
            'viewers': int(viewers)
        }
    except:
        raise Exception("HTTP Error")

services = {
    "twitch": twitch,
    "livestream": livestream,
    "omckhd": omckhd
}


if __name__ == '__main__':
    print(livestream('kekekee'))
    print(twitch('joindotared'))