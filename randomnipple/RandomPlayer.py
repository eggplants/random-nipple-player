from glob import glob
from multiprocessing import Process
from os import path
from random import randint
from typing import Optional

import simpleaudio as sa

from randomnipple.NippleOptionDict import NippleOptionDict


class RandomPlayer:
    def __init__(self, vals: NippleOptionDict) -> None:
        self.vals = vals
        self.ear = [i for i in ('left', 'right',) if vals[i]][0]
        self.actor = [i for i in ('loli', 'boyish', 'low',) if vals[i]][0]
        self.serif = [i for i in (
            'serif_enable', 'serif_disable',) if vals[i]][0]
        self.finish = [i for i in ('wet', 'dry',) if vals[i]][0]
        self.dir = self.__set_dir()
        self.thread = Process(target=self.__play)
        self.play_obj: Optional[sa.shiny.PlayObject] = None

    def __set_dir(self) -> str:
        base = self.vals['dir']
        d = ((base if self.ear == 'left'
              else path.join(base, '【左耳】2021.0612')))
        t = ('ロリ' if self.actor == 'loli'
             else 'ボーイッシュ' if self.actor == 'boyish'
             else '低音お姉さん')
        return path.join(d, t)

    def play(self) -> None:
        self.thread.start()

    def __play(self) -> None:
        first_track = path.join(
            self.dir, 'ループ音声', '01.この音声からランダム再生を初めてください.wav')
        self.play_track(first_track)

        loop_tracks = (sorted(glob(path.join(self.dir, 'ループ音声', '*.wav')))[1:]
                       if self.serif == 'serif_enable'
                       else glob(path.join(self.dir, 'ループ音声', '*.wav')))
        loop_tracks_len = len(loop_tracks)
        while True:
            rand_int = randint(0, loop_tracks_len-1)
            self.play_track(loop_tracks[rand_int])

    def play_track(self, track_path: str) -> None:
        if path.isfile(track_path):
            wav_obj = sa.WaveObject.from_wave_file(track_path)
            self.play_obj = wav_obj.play()
            if self.play_obj is not None:
                self.play_obj.wait_done()

    def play_final(self) -> None:
        self.thread = Process(target=self.__play_final)
        self.thread.start()

    def __play_final(self) -> None:
        final_track = path.join(
            self.dir, '絶頂音声',
            ('14.射精用トラック.wav' if self.finish == 'wet'
             else '15.乳首ドライ絶頂用トラック.wav'))
        self.play_track(final_track)

    def stop(self) -> None:
        if self.play_obj is not None and self.play_obj.is_playing():
            self.play_obj.stop()
        if self.thread.is_alive():
            self.thread.terminate()
