#!/usr/bin/env python

from randomnipple.MainWindow import MainWindow


def main() -> None:
    m = MainWindow()
    m.launch()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
