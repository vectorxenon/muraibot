"""
おっさんは考える
"""
import random
import re
import time


class MuraiBrain():
    def __init__(self, connection, channel):
        """
        :type connection: irc.client.ServerConnection
        :type channel: str
        """
        self.connection = connection
        self.channel = channel

    def ossan_speek(self, message, percent=100):
        """
        :type message: str
        :type percent: int
        :param message:
        :param percent:
        """
        time.sleep(random.randrange(start=1, stop=3))
        if random.random() * 100 < percent:
            self.connection.privmsg(self.channel, message)

    def think(self, event):
        """
        :type event: irc.client.Event
        :param event:
        """
        random.seed(None)
        if re.search(r'おっさん|へんたい|変態|ossan', event.arguments[0], re.I):
            self.response_called(event.arguments[0])

    def response_called(self, message):
        if re.search(r'の(？|\?)$', message):
            responses = ['ちゃうわw',
                         'やかましいわw',
                         'あーそうだよ？',
                         'はいはい、そーですよっ',
                         'んー？なんだい？'
            ]
        else:
            responses = ['はい、現場のおっさんです',
                         'やめろよw',
                         'うるさいよw',
                         'きたきたきたー',
                         'それじゃ、お邪魔様でした',
                         'おいおい、酷い言い草じゃないか'
            ]
        self.ossan_speek(random.choice(responses), 90)
