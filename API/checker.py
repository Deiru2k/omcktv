from API.services import services
from pymongo.connection import Connection

c = Connection()
db = c['omcktv']

def check_channels():

    channels = db['channels'].find()

    for chan in channels:
        print(chan)
        status = services[chan['type']](chan['channel'])
        db['channels'].update({'_id': chan['_id']}, {'$set': status})

if __name__ == "__main__":
    check_channels()