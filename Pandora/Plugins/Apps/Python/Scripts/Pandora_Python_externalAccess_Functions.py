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
import traceback, time, platform, shutil
from functools import wraps


class Pandora_Python_externalAccess_Functions(object):
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
                erStr = "%s ERROR - Pandora_Plugin_Maya_ext %s:\n%s\n\n%s" % (
                    time.strftime("%d/%m/%y %X"),
                    args[0].plugin.version,
                    "".join(traceback.format_stack()),
                    traceback.format_exc(),
                )
                args[0].core.writeErrorLog(erStr)

        return func_wrapper

    @err_decorator
    def pandoraSettings_loadUI(self, origin, tab):
        pass

    @err_decorator
    def pandoraSettings_saveSettings(self, origin):
        pass

    @err_decorator
    def pandoraSettings_loadSettings(self, origin):
        pass

    @err_decorator
    def copySceneFile(self, origin, origFile, targetPath):
        xgenfiles = [
            x
            for x in os.listdir(os.path.dirname(origFile))
            if x.startswith(os.path.splitext(os.path.basename(origFile))[0])
            and os.path.splitext(x)[1] in [".xgen", "abc"]
        ]
        for i in xgenfiles:
            curFilePath = os.path.join(os.path.dirname(origFile), i).replace("\\", "/")
            tFilePath = os.path.join(os.path.dirname(targetPath), i).replace("\\", "/")
            if curFilePath != tFilePath:
                shutil.copy2(curFilePath, tFilePath)

    # start a Python render job
    @err_decorator
    def startJob(self, origin, jobData={}):
        origin.writeLog("starting Python job. " + jobData["jobname"], 0)

        pythonOverride = self.core.getConfig("dccoverrides", "Python_override")
        pythonOverridePath = self.core.getConfig("dccoverrides", "Python_path")

        if (
            pythonOverride == True
            and pythonOverridePath is not None
            and os.path.exists(pythonOverridePath)
        ):
            pythonPath = pythonOverridePath
        else:
            if "programVersion" in jobData:
                pythonPath = self.getInstallPath(jobData["programVersion"])
            else:
                pythonPath = self.getInstallPath()

            pythonPath = os.path.join(pythonPath,"python.exe")

            if not os.path.exists(pythonPath):
                origin.writeLog("no Python installation found", 3)
                origin.renderingFailed(jobData)
                return "skipped"

        if "outputPath" in jobData:
            curOutput = jobData["outputPath"]
            if origin.localMode:
                newOutputDir = os.path.dirname(curOutput)
            else:
                newOutputDir = os.path.join(
                    origin.localSlavePath,
                    "RenderOutput",
                    jobData["jobcode"],
                    os.path.basename(os.path.dirname(curOutput)),
                )
            newOutputFile = os.path.splitext(os.path.basename(curOutput))[0]
            try:
                os.makedirs(newOutputDir)
            except:
                pass
        else:
            origin.writeLog("no outputpath specified", 2)
            origin.renderingFailed(jobData)
            return False

        if not os.path.exists(jobData["scenefile"]):
            origin.writeLog("scenefile does not exist", 2)
            origin.renderingFailed(jobData)
            return False

        popenArgs = [
            pythonPath
        ]

        popenArgs.append(jobData["scenefile"])

        thread = origin.startRenderThread(pOpenArgs=popenArgs, jData=jobData, prog="python")
        return thread
