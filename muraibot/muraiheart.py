"""
おっさんのこころ
"""
import random
import irc.bot
import irc.strings
import muraibot


class MuraiBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667, password=None):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, password)], nickname, nickname)
        self.channel = channel
        self.brain = muraibot.MuraiBrain(self.connection, channel)

    def on_nicknameinuse(self, conn, event):
        conn.nick(conn.get_nickname() + "_")

    def on_welcome(self, conn, event):
        conn.join(self.channel)

    def on_pubmsg(self, conn, event):
        """
        :type conn: irc.client.ServerConnection
        :type event: irc.client.Event
        """
        self.brain.think(event)

