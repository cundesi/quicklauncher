# This file is part of quicklauncher.
# Copyright (C) 2014  Cesar Saez

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation version 3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from PyQt4 import uic, QtGui
from wishlib.qt.QtGui import QMainWindow
from wishlib.si import OverrideWin32Controls

from .. import manager


class Prefs(QMainWindow):

    def __init__(self, parent=None):
        super(Prefs, self).__init__(parent)
        # load from ui file
        uifile = os.path.join(os.path.dirname(__file__), "ui", "prefs.ui")
        self.ui = uic.loadUi(os.path.normpath(uifile), self)
        icon = os.path.join(os.path.dirname(__file__), "ui", "images",
                            "folder_open_icon&16.png")
        self.ui.scripts_button.setIcon(QtGui.QIcon(icon))
        # get manager and set values
        self.manager = manager.Manager()
        self.ui.limit_spinBox.setValue(self.manager.limit)
        self.ui.scripts_lineEdit.setText(self.manager.script_dir)

    def limit_changed(self, value):
        self.manager.limit = value

    @OverrideWin32Controls
    def scripts_clicked(self):
        script_dir = str(QtGui.QFileDialog.getExistingDirectory(
            self, "Scripts directory", self.manager.script_dir))
        if len(script_dir):
            self.manager.script_dir = script_dir
            self.ui.scripts_lineEdit.setText(script_dir)
