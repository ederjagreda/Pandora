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


import os, sys
import traceback, time, shutil
from functools import wraps

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *

    psVersion = 2
except:
    from PySide.QtCore import *
    from PySide.QtGui import *

    psVersion = 1


class Pandora_Python_Functions(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

    def err_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            exc_info = sys.exc_info()
            try:
                return func(*args, **kwargs)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                erStr = "%s ERROR - Pandora_Plugin_Python %s:\n%s\n\n%s" % (
                    time.strftime("%d/%m/%y %X"),
                    args[0].plugin.version,
                    "".join(traceback.format_stack()),
                    traceback.format_exc(),
                )
                args[0].core.writeErrorLog(erStr)

        return func_wrapper

    @err_decorator
    def startup(self, origin):
        if os.path.basename(sys.executable) != "python.exe":
            if QApplication.instance() is None:
                return False

            if not hasattr(QApplication, "topLevelWidgets"):
                return False

            for obj in QApplication.topLevelWidgets():
                if obj.objectName() == "MayaWindow":
                    mayaQtParent = obj
                    break
            else:
                return False

            try:
                topLevelShelf = mel.eval("string $m = $gShelfTopLevel")
            except:
                return False

            if cmds.shelfTabLayout(topLevelShelf, query=True, tabLabelIndex=True) == None:
                return False

            origin.timer.stop()
            origin.messageParent = mayaQtParent

        else:
            origin.timer.stop()
            origin.messageParent = QWidget()

    @err_decorator
    def getCurrentFileName(self, origin, path=True):
        print "origin", origin
        print dir(origin)
        if path:
            return path

    @err_decorator
    def saveScene(self, origin, filepath):
        return True

    @err_decorator
    def getFrameRange(self, origin):
        return 0

    @err_decorator
    def setRCStyle(self, origin, rcmenu):
        pass

    @err_decorator
    def onPandoraSettingsOpen(self, origin):
        pass

    @err_decorator
    def getCurrentSceneFiles(self, origin):
        return origin

    @err_decorator
    def onSubmitterOpen(self, origin):
        origin.w_status.setVisible(False)
        origin.w_connect.setVisible(False)

    @err_decorator
    def getSceneCameras(self, origin):
        return []

    @err_decorator
    def getCameraName(self, origin, handle):
        return ""

    @err_decorator
    def getExternalFiles(self, origin, isSubmitting=False):
        return []

    @err_decorator
    def preSubmit(self, origin, rSettings):
        return

    @err_decorator
    def undoRenderSettings(self, origin, rSettings):
        return

    @err_decorator
    def preSubmitChecks(self, origin, jobData):
        pass

    @err_decorator
    def getJobConfigParams(self, origin, cData):
        for i in cData:
            if i[1] == "programVersion":
                break
        else:
            cData.append(["information", "programVersion", "2.7"])
