#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import app_globals as G

from PyQt4 import QtGui

from window import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.setup_app()
    sys.exit(app.exec_())
