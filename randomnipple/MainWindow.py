import PySimpleGUI as sg

from randomnipple.NippleOptionDict import NippleOptionDict
from randomnipple.RandomPlayer import RandomPlayer
from randomnipple.VoiceDirectoryChecker import VoiceDirectoryChecker

sg.theme('DarkAmber')


class MainWindow:
    def __init__(self) -> None:
        self.layout = self.__layout()

        self.window = sg.Window('Random Nipple Player', self.layout)

    def __layout(self):
        select_folder = [
            [sg.InputText(key='dir'), sg.FolderBrowse(target='dir')]]

        ear = [[sg.Radio('右耳', key='left', group_id='ear', default=True),
                sg.Radio('左耳', key='right', group_id='ear')]]

        actor = [[sg.Radio('ロリ', key='loli', group_id='actor', default=True),
                  sg.Radio('ボーイッシュ', key='boyish', group_id='actor'),
                  sg.Radio('低音お姉さん', key='low', group_id='actor')]]

        serif = [[sg.Radio('有り', key='serif_enable', group_id='serif', default=True),
                  sg.Radio('無し', key='serif_disable', group_id='serif')]]

        finish = [[sg.Radio('ウェット', key='wet', group_id='finish', default=True),
                   sg.Radio('ドライ', key='dry', group_id='finish')]]

        return [[sg.Frame('フォルダ選択', select_folder)],
                [sg.Frame('方向', ear)],
                [sg.Frame('ボイス', actor)],
                [sg.Frame('ランダムセリフ', serif)],
                [sg.Frame('フィニッシュ', finish)],
                [sg.Button('Play!', key='play'), sg.Button('Close', key='close')]]

    def launch(self) -> None:
        signal = True
        while signal:
            signal = self.__do()
            self.window['play'].update(disabled=False)
            self.window['close'].update(disabled=False)
        else:
            self.window.close()

    def __do(self) -> bool:
        vals: NippleOptionDict
        evt, vals = self.window.read()
        if evt == 'play':
            self.window['play'].update(disabled=True)
            self.window['close'].update(disabled=True)
            if not VoiceDirectoryChecker.check(vals['dir']):
                sg.PopupError('指定したフォルダは有効ではありません。\n'
                              '指定したフォルダ: ' + vals['dir'])
                return True
            r = RandomPlayer(vals)
            r.play()
            rtn = sg.popup(custom_text=('Finish!', 'Cancel'))
            if rtn == 'Finish!':
                r.stop()
                r.play_final()
                rtn = sg.popup(custom_text='Cancel')
            r.stop()
            return True
        else:
            return False
