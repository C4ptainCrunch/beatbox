
import asyncio
from os import environ
import datetime
import glob
import base64
import json

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class Component(ApplicationSession):
    async def onJoin(self, details):
        player_lock = asyncio.Lock()

        def get_samples():
            self.log.info("Samples list requested")
            samples = [b[8:-4] for b in glob.glob("samples/*.mp3")]
            return sorted(samples)

        await self.register(get_samples, u'nefliers.beatbox.samples.list')

        async def play_samples(name):
            with await player_lock:
                ############################################
                # THIS IS VULNERABLE TO SHELL INJECTIONS ! #
                ############################################
                await asyncio.create_subprocess_shell('mplayer -really-quiet −af volume=40:0 "samples/%s.mp3" 2&1> /dev/null' % name)
                self.log.info("Playing '{song}'", song=name)

        await self.register(play_samples, u'nefliers.beatbox.samples.play')


if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://127.0.0.1:8080/ws"),
        u"realm1",
    )
runner.run(Component)
