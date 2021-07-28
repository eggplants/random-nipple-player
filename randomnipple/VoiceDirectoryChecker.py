from glob import glob
from os import path


class VoiceDirectoryChecker:
    def __init__(self) -> None:
        pass

    @staticmethod
    def check(dir_: str) -> bool:
        if not path.isdir(dir_):
            return False
        else:
            f = [len(glob(path.join(dir_, '**/*.wav'), recursive=True)) == 138]
            for i in (dir_, dir_ + '/【左耳】2021.0612',):
                f1 = path.isdir(i)
                f2 = path.isdir(i+'/ボーイッシュ')
                f3 = path.isdir(i+'/ロリ')
                f4 = path.isdir(i+'/低音お姉さん')
                f.extend((f1, f2, f3, f4,))
            return all(f)
