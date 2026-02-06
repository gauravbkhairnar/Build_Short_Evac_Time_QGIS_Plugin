# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:44:52 2026

@author: Gaurav Khairnar
"""


import os
from qgis.PyQt import uic, QtWidgets

FORM_CLASS, _ = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), 'Build_Short_Evac_Time_help.ui')
)

class BuildShortEvacTimeHelpDialog(QtWidgets.QDialog, FORM_CLASS):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

 
        self.setWindowTitle("Build Shortest Evacuation Time – Help")
