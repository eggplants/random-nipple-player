from NippleOptionDict import NippleOptionDict as NippleOptionDict
from typing import Any

class RandomPlayer:
    vals: Any
    ear: Any
    actor: Any
    serif: Any
    finish: Any
    dir: Any
    thread: Any
    play_obj: Any
    def __init__(self, vals: NippleOptionDict) -> None: ...
    def play(self) -> None: ...
    def play_track(self, track_path: str) -> None: ...
    def play_final(self) -> None: ...
    def stop(self) -> None: ...
