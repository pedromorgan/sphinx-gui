#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import app_globals as G

from PyQt4 import QtGui

from sphinxgui import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    """ @todo - splash me"""
    
    window = MainWindow.MainWindow()
  
    
    sys.exit(app.exec_())
