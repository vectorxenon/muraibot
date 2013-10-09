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
        :type message: str or list of str
        :type percent: int
        :param message: str or list of str
        :param percent:
        """
        time.sleep(random.randrange(start=1, stop=3))
        if random.random() * 100 < percent:
            self.connection.privmsg(self.channel, random.choice(message) if isinstance(message, list) else message)

    def think(self, event):
        """
        :type event: irc.client.Event
        :param event:
        """
        message = event.arguments[0]
        random.seed(None)
        if re.search(r'おっさん|へんたい|変態|ossan', message, re.I):
            self.response_called(message)
        elif re.search(r'(い|行)きま(すか|せう|しょ(う|か))', message):
            self.response_gogogo()
        elif re.search(r'め(っ)?し(ー)?', message):
            self.response_hungry()
        elif re.search(r'お(っ)?つ(かれ)?(ー)?|(帰|かえ)(ー)?る|ots?(ts?)?u-*', message, re.I):
            self.response_rtb()
        elif re.search(r'^もう.*ゴールして(も)?いい', message):
            self.response_graduation_from_life()
        elif re.search(r'^イザル|ザイ(ー)?ル$', message):
            self.response_nonsense()
        elif re.search(r'おめでと|オメデト', message, re.I):
            self.repponse_congratulate()

    def response_called(self, message):
        if re.search(r'の(？|\?)$', message):
            responses = ['ちゃうわw',
                         'やかましいわw',
                         'あーそうだよ？',
                         'はいはい、そーですよっ',
                         'んー？なんだい？',
                         'ひゃひゃひゃww んなこたぁないw'
            ]
        else:
            responses = ['はい、現場のおっさんです',
                         'やめろよw',
                         'うるさいよw',
                         'きたきたきたー',
                         'それじゃ、お邪魔様でした',
                         'おいおい、酷い言い草じゃないか'
            ]
        self.ossan_speek(responses, 90)

    def response_gogogo(self):
        self.ossan_speek("ざいざいざい", 50)

    def response_hungry(self):
        self.ossan_speek("しめしめし", 50)

    def response_rtb(self):
        responses = ["オレはまだゴールしたくねぇんだよ",
                     "おいおい、もう帰っちゃうのかい？",
                     "まだまだ夜はこれからよ",
                     "ほいじゃ、おつかれさんね",
                     "おつかれね",
                     "おっさんもそろそろ帰っちゃうよっ"
        ]
        self.ossan_speek(responses, 50)

    def response_graduation_from_life(self):
        responses = ['オレはまだゴールしたくねぇんだよ',
                     'あきらめんなよ！',
                     'もう眠たいよパトラッシュ']
        self.ossan_speek(responses, 70)

    def response_nonsense(self):
        responses = ['いざいざ', 'しめじめし', 'ザイル', 'イザル']
        self.ossan_speek(responses, 50)

    def repponse_congratulate(self):
        responses = ['ありがと…ってちゃうわｗ', 'おやおや？誰かさんがおめでたいのかい？']
        self.ossan_speek(responses, 40)

    def greedy_greeting(self, target):
        self.connection.mode(target, '+o')
        greetings = [
            '%s、おはよー',
            'おはよー、%sくん。今日もゴキゲンかい？',
            'おいーっす %s'
        ]
        self.ossan_speek([s % target for s in greetings], 90)
        pass

