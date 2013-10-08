#!/usr/bin/env python
"""
おっさんはビールで起動する
"""

import random
import muraibot


def main():
    import sys

    if len(sys.argv) < 4:
        print("Usage: beer.py <server[:port]> <channel> <nickname> [password]")
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print("Error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]
    password = sys.argv[4] if len(sys.argv) == 5 else None

    random.seed(None)
    murai = muraibot.MuraiBot(channel, nickname, server, port, password)
    murai.start()


if __name__ == "__main__":
    main()
