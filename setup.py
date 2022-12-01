import io
from os.path import abspath, dirname, join
import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
    name='micropython-linenotify',
    py_modules=['linenotify'],
    version='0.0.4',
    description='Line Notify with MicroPython on ESP32/ESP8266 ',
    long_description=DESCRIPTION,
    keywords= ['linenotify', 'esp32', 'esp8266' ,'micropython'],
    url='https://github.com/PerfecXX/micropython-linenotify',
    author='Teeraphat Kullanankanjana',
    author_email='ku.teeraphat@hotmail.com',
    maintainer='Teeraphat Kullanankanjana',
    maintainer_email='ku.teeraphat@hotmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 3 - Alpha', 
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)
