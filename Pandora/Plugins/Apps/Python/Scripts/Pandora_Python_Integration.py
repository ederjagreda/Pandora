# -*- coding: utf-8 -*-
#
####################################################
#
# Pandora - Renderfarm Manager
#
# https://prism-pipeline.com/pandora/
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2020 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Pandora.
#
# Pandora is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pandora is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pandora.  If not, see <https://www.gnu.org/licenses/>.


try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *

    psVersion = 2
except:
    from PySide.QtCore import *
    from PySide.QtGui import *

    psVersion = 1

import os, sys
import traceback, time, platform, shutil
from functools import wraps

if platform.system() == "Windows":
    if sys.version[0] == "3":
        import winreg as _winreg
    else:
        import _winreg


class Pandora_Python_Integration(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

        if platform.system() == "Windows":
            self.examplePath = os.environ["localAppData"] + "\\Programs\\Python\\Python37"

    def err_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            exc_info = sys.exc_info()
            try:
                return func(*args, **kwargs)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                erStr = "%s ERROR - Pandora_Plugin_Python_Integration %s:\n%s\n\n%s" % (
                    time.strftime("%d/%m/%y %X"),
                    args[0].plugin.version,
                    "".join(traceback.format_stack()),
                    traceback.format_exc(),
                )
                if hasattr(args[0].core, "writeErrorLog"):
                    args[0].core.writeErrorLog(erStr)
                else:
                    QMessageBox.warning(
                        args[0].core.messageParent, "Pandora Integration", erStr
                    )

        return func_wrapper

    @err_decorator
    def getExecutable(self):
        execPath = ""
        if platform.system() == "Windows":
            defaultpath = os.path.join(self.getInstallPath(), "python.exe")
            if os.path.exists(defaultpath):
                execPath = defaultpath

        return execPath

    @err_decorator
    def getPythonRegedit(self, pythonPath):
        try:
            key = _winreg.OpenKey(
                _winreg.HKEY_CURRENT_USER,
                pythonPath,
                0,
                _winreg.KEY_READ | _winreg.KEY_WOW64_64KEY,
            )
            return (key, _winreg.HKEY_CURRENT_USER)
        except FileNotFoundError:
            try:
                key = _winreg.OpenKey(
                    _winreg.HKEY_LOCAL_MACHINE,
                    pythonPath,
                    0,
                    _winreg.KEY_READ | _winreg.KEY_WOW64_64KEY,
                )
                return (key, _winreg.HKEY_LOCAL_MACHINE)
            except FileNotFoundError:
                pass

    @err_decorator
    def getInstallPath(self, version=None):
        pythonPath = "SOFTWARE\\Python\\PythonCore"
        results = self.getPythonRegedit(pythonPath)
        if results:
            key, winreg = results
            pythonVersions = []
            try:
                i = 0
                while True:
                    pythonVers = _winreg.EnumKey(key, i)
                    if sys.version[0] == "2":
                        umv = unicode(pythonVers)
                    else:
                        umv = pythonVers
                    i += 1
            except WindowsError:
                pass

            if version is None:
                validVersion = pythonVersions[-1]
            elif version in pythonVersions:
                validVersion = version
            else:
                for i in pythonVersions:
                    if float(i) > float(version):
                        validVersion = i
                        break
                else:
                    self.writeLog("No valid Python found in registry", 0)
                    return None

            key = _winreg.OpenKey(
                winreg,
                "%s\\%s\\InstallPath" % (pythonPath, validVersion),
                0,
                _winreg.KEY_READ | _winreg.KEY_WOW64_64KEY,
            )

            installDir = (_winreg.QueryValueEx(key, ""))[0]

            if installDir is None:
                return ""
            else:
                return installDir
        else:
            return ""

    @err_decorator
    def integrationAdd(self, origin):
        return

    @err_decorator
    def integrationRemove(self, origin, installPath):
        return

    def writePythonFiles(self, mayaPath):
        return

    def removeIntegration(self, installPath):
        return

    def updateInstallerUI(self, userFolders, pItem):
        return

    def installerExecute(self, mayaItem, result):
        return