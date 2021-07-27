from setuptools import find_packages, setup  # type: ignore

from randomnipple import __version__

setup(
    name='random-nipple-player',
    version=__version__,
    description='音声作品「乳首オナ指示でカリカリタイム」(RJ323807)用のプレイヤー',
    description_content_type='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/eggplants/random-nipple-player',
    author='eggplants',
    packages=find_packages(),
    python_requires='>=3.8',
    include_package_data=True,
    license='MIT',
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'rnp=randomnipple.main:main'
        ]
    }
)
