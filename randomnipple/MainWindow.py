from typing import Any, List

import PySimpleGUI as sg  # type: ignore[import]

from randomnipple import __version__
from randomnipple.NippleOptionDict import NippleOptionDict
from randomnipple.RandomPlayer import RandomPlayer
from randomnipple.VoiceDirectoryChecker import VoiceDirectoryChecker

sg.theme("DarkAmber")


class MainWindow:
    def __init__(self) -> None:
        self.layout = self.__layout()

        self.window = sg.Window(
            "Random Nipple Player v" + __version__, self.layout, keep_on_top=True
        )

    def __layout(self) -> List[List[Any]]:
        select_folder = [
            [
                sg.InputText(key="dir", size=(50, 1)),
                sg.FolderBrowse(target="dir", key="browse"),
            ]
        ]

        ear = [
            [
                sg.Radio("右耳　　", key="left", group_id="ear", default=True),
                sg.Radio("左耳　", key="right", group_id="ear"),
            ]
        ]

        actor = [
            [
                sg.Radio("ロリ", key="loli", group_id="actor", default=True),
                sg.Radio("ボーイッシュ", key="boyish", group_id="actor"),
                sg.Radio("低音お姉さん", key="low", group_id="actor"),
            ]
        ]

        first = [
            [
                sg.Radio("有り　　", key="first_enable", group_id="first", default=True),
                sg.Radio("無し　", key="first_disable", group_id="first"),
            ]
        ]

        serif = [
            [
                sg.Radio("有り", key="serif_enable", group_id="serif", default=True),
                sg.Radio("無し(オノマトペモード)　　　　 ", key="serif_disable", group_id="serif"),
            ]
        ]

        finish = [
            [
                sg.Radio("ウェット", key="wet", group_id="finish", default=True),
                sg.Radio("ドライ", key="dry", group_id="finish"),
            ]
        ]

        spin = [
            [
                sg.Spin(
                    [_ for _ in range(1, 100)],
                    initial_value=1,
                    key="repeat",
                    size=(5, 1),
                ),
                sg.Text("回　　　　　　　　　　　　　　　　"),
            ]
        ]

        return [
            [sg.Frame("フォルダ選択", [[sg.Column(select_folder, size=(460, 40))]])],
            [sg.Frame("方向", ear), sg.Frame("ボイス", actor)],
            [sg.Frame("挨拶", first), sg.Frame("ランダムセリフ", serif)],
            [sg.Frame("フィニッシュ", finish), sg.Frame("同一トラックリピート回数(オノマトペモード時)", spin)],
            [
                sg.Button("Play!", key="play", button_color="green"),
                sg.Button("Close", key="close", button_color="red"),
            ],
        ]

    def launch(self) -> None:
        signal = True
        while signal:
            signal = self.__do()
            self.__toggle_button(False)
        else:
            self.window.close()

    def __toggle_button(self, flag: bool) -> None:
        for i in ("browse", "play", "close"):
            self.window[i].update(disabled=flag)

    def __do(self) -> bool:
        vals: NippleOptionDict
        evt, vals = self.window.read()
        # print(vals)  # debug
        if evt == "play":
            self.__toggle_button(True)
            if not VoiceDirectoryChecker.check(vals["dir"]):
                sg.PopupError(
                    "指定したフォルダは有効ではありません。\n" "指定したフォルダ: " + vals["dir"], keep_on_top=True
                )
                return True
            r = RandomPlayer(vals)
            r.play()
            rtn = sg.popup(
                "再生中: 焦らしパート",
                title="再生中...",
                custom_text=("Finish!", "Cancel"),
                keep_on_top=True,
            )
            if rtn == "Finish!":
                r.stop()
                r.play_final()
                rtn = sg.popup(
                    "再生中: フィニッシュパート",
                    title="再生中...",
                    custom_text="Cancel",
                    keep_on_top=True,
                )
            r.stop()
            return True
        else:
            return False
