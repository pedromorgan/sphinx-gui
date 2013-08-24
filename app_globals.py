
"""
This file is not yey implemented.. 
But the idea would be to autodetect.. whether 
pyside or PyQt
python 2.. 3 etc
and import the libs on a Global basis within the application.. 
paticular is "import" requiored, eg import pyside, PyQt5 etc
eg

import app_globals as G

# G.PYQT below is whatever is on your system
def MyWidget(G.PYQT): 


"""

PYQT = None
QT_VER = None

""" A hack and pointer to the lib to use, whether pyside or pyqt .. wip"""


## need a sequence to
## Maybe works  is it python 3, is pyside, is pyqt4 or pyqt 5 ?
## QT_VER
try:
	import pyside as PYQT
	
	
except ImportError:
	print 
	
################################################################################

class OPSYS:
	osx = "osx"
	windows = "windows"
	linux = "linux"
	
OS = None
# stuff here to set OS
OS = OPSYS.linux


