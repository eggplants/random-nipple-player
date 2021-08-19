from glob import glob
from os import path


class VoiceDirectoryChecker:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check(dir_: str) -> bool:
        def count_wavs(dir_: str) -> int:
            return len(glob(path.join(dir_, '**/*.wav'), recursive=True))
        if not path.isdir(dir_):
            return False
        else:
            f = [
                path.isdir(i) and \
                path.isdir(i+'/ボーイッシュ') and \
                path.isdir(i+'/ロリ') and \
                path.isdir(i+'/低音お姉さん')
                for i in (dir_, dir_ + '/【左耳】2021.0612',)]
            return all(f) and count_wavs(dir_) == 138
    
