import asyncio
from datetime import datetime


def print_date(msg):
    print(str(datetime.now()).split(" ")[1].split(".")[0], msg)


def setup_alarm_every_n_seconds(n, msg):
    [loop.call_later(x, print_date, msg) for x in range(n, 200, n)]

loop = asyncio.get_event_loop()

setup_alarm_every_n_seconds(10, "ten seconds are gone!")
setup_alarm_every_n_seconds(30, "half a minute is gone!")
setup_alarm_every_n_seconds(60, "a minute passed!")

print_date("start!")

loop.run_forever()
loop.close()

"""
14:12:21 start!
14:12:31 ten seconds are gone!
14:12:41 ten seconds are gone!
14:12:51 ten seconds are gone!
14:12:51 half a minute is gone!
14:13:01 ten seconds are gone!
14:13:11 ten seconds are gone!
14:13:21 ten seconds are gone!
14:13:21 half a minute is gone!
14:13:21 a minute passed!
14:13:31 ten seconds are gone!
14:13:41 ten seconds are gone!
14:13:51 ten seconds are gone!
14:13:51 half a minute is gone!
14:14:01 ten seconds are gone!
14:14:11 ten seconds are gone!
14:14:21 ten seconds are gone!
14:14:21 half a minute is gone!
14:14:21 a minute passed!
14:14:31 ten seconds are gone!
14:14:41 ten seconds are gone!
14:14:51 ten seconds are gone!
14:14:51 half a minute is gone!
"""

