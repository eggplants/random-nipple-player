from glob import glob
from multiprocessing import Process
from os import path
from random import randint, sample, shuffle
from typing import List, Optional

import simpleaudio as sa  # type: ignore[import]

from randomnipple.NippleOptionDict import NippleOptionDict


class RandomPlayer:
    def __init__(self, vals: NippleOptionDict) -> None:
        def get_one(options: List[str]) -> str:
            return [i for i in options if i in self.vals][0]

        self.vals = vals
        self.ear = get_one(["left", "right"])
        self.actor = get_one(["loli", "boyish", "low"])
        self.serif = get_one(["serif_enable", "serif_disable"])
        self.finish = get_one(["wet", "dry"])
        self.first = get_one(["first_enable", "first_disable"])
        self.repeat = vals["repeat"]
        self.dir = self.__set_dir()
        self.thread = Process(target=self.__play_loop)
        self.play_obj: Optional[sa.shiny.PlayObject] = None

    def __set_dir(self) -> str:
        base = self.vals["dir"]
        d = base if self.ear == "left" else path.join(base, "【左耳】2021.0612")
        t = (
            "ロリ"
            if self.actor == "loli"
            else "ボーイッシュ"
            if self.actor == "boyish"
            else "低音お姉さん"
        )
        return path.join(d, t)

    def play(self) -> None:
        self.thread.start()

    def __play_loop(self) -> None:
        while True:
            self.__play()

    def __play(self) -> None:
        self.__play_first()
        if self.serif == "serif_enable":
            loop_tracks = sorted(glob(path.join(self.dir, "ループ音声", "*.wav")))[1:-4]
            serif_tracks = sorted(glob(path.join(self.dir, "ループ音声", "*.wav")))[-4:]
            shuffle(serif_tracks)
            for s_track in serif_tracks:
                for track in sample(loop_tracks, randint(1, 8)):
                    self.play_track(track)
                else:
                    self.play_track(s_track)

        else:
            loop_tracks = glob(path.join(self.dir, "オノマトペオンリー", "*.wav"))
            shuffle(loop_tracks)
            for track in loop_tracks:
                self.__play_times(track)

    def play_track(self, track_path: str) -> None:
        if path.isfile(track_path):
            wav_obj = sa.WaveObject.from_wave_file(track_path)
            self.play_obj = wav_obj.play()
            if self.play_obj is not None:
                self.play_obj.wait_done()

    def play_final(self) -> None:
        self.thread = Process(target=self.__play_final)
        self.thread.start()

    def __play_times(self, track: str) -> None:
        for _ in range(self.repeat):
            self.play_track(track)

    def __play_first(self) -> None:
        if self.first == "first_enable":
            first_track = path.join(self.dir, "ループ音声", "01.この音声からランダム再生を初めてください.wav")
            self.play_track(first_track)

    def __play_final(self) -> None:
        final_track = path.join(
            self.dir,
            "絶頂音声",
            ("14.射精用トラック.wav" if self.finish == "wet" else "15.乳首ドライ絶頂用トラック.wav"),
        )
        self.play_track(final_track)

    def stop(self) -> None:
        if self.play_obj is not None and self.play_obj.is_playing():
            self.play_obj.stop()
        if self.thread.is_alive():
            self.thread.terminate()
