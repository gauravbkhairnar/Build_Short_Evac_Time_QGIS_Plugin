# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'gaurav.b.khairnar@gmail.com'
__date__ = '2025-12-27'
__copyright__ = 'Copyright 2025, Gaurav Khairnar'

import unittest

from qgis.PyQt.QtGui import QDialogButtonBox, QDialog

from Build_Short_Evac_Time_dialog import BuildShortEvacTimeDialog

from utilities import get_qgis_app
QGIS_APP = get_qgis_app()


class BuildShortEvacTimeDialogTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        self.dialog = BuildShortEvacTimeDialog(None)

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_dialog_ok(self):
        """Test we can click OK."""

        button = self.dialog.button_box.button(QDialogButtonBox.Ok)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Accepted)

    def test_dialog_cancel(self):
        """Test we can click cancel."""
        button = self.dialog.button_box.button(QDialogButtonBox.Cancel)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Rejected)

if __name__ == "__main__":
    suite = unittest.makeSuite(BuildShortEvacTimeDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

