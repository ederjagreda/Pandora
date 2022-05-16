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

import sys, os, time, traceback
from functools import wraps

for i in ["PandoraSubmitter_ui", "PandoraSubmitter_ui_ps2"]:
    try:
        del sys.modules[i]
    except:
        pass

sys.path.append(os.path.join(os.path.dirname(__file__), "UserInterfacesPandora"))

if psVersion == 1:
    import PandoraPythonSubmitter_ui
else:
    import PandoraPythonSubmitter_ui_ps2 as PandoraPythonSubmitter_ui


class PandoraPythonSubmitter(QDialog, PandoraPythonSubmitter_ui.Ui_dlg_pandoraSubmitter):
    def __init__(self, core):
        QDialog.__init__(self)
        self.setupUi(self)

        self.core = core
        self.core.parentWindow(self)

        self.setTooltips()
        self.core.callback(name="onSubmitterOpen", types=["curApp", "custom"], args=[self])
        self.connectEvents()
        self.loadSettings()

    def err_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                erStr = "%s ERROR - PandoraSubmitter %s:\n%s\n\n%s" % (
                    time.strftime("%d/%m/%y %X"),
                    args[0].core.version,
                    "".join(traceback.format_stack()),
                    traceback.format_exc(),
                )
                args[0].core.writeErrorLog(erStr)

        return func_wrapper

    @err_decorator
    def closeEvent(self, event):
        self.saveSettings()

    @err_decorator
    def setTooltips(self):
        self.l_projectName.setToolTip(
            "Use the same project name for all renderjobs of the project you are working on"
        )
        self.l_jobName.setToolTip(
            'Use an individial job name for each submission e.g. "Shot-020_anm_v0007"'
        )
        self.l_prio.setToolTip(
            """Sets the priority of the renderjob. Jobs with higher priority will be rendered before jobs with lower priority.
Please contact the renderfarm administrator before increasing the priority."""
        )
        self.l_framesPerTask.setToolTip(
            """Each renderjob is divided into multiple tasks. Each task contains the same number of frames to be be rendered and each task can be rendered by a different renderslave.
If you have a lot of frames, which render fast you may want to increase this value. For jobs with long rendertimes you want to decrease it."""
        )
        self.l_submitSuspended.setToolTip(
            "If checked, the renderjob will be submitted as suspended (deactivated). It can be activated manually later in the RenderHandler."
        )
        self.l_submitDependent.setToolTip(
            "If checked, all external files (e.g. Textures, References) will be submitted with this renderjob"
        )
        self.l_uploadOutput.setToolTip(
            """If checked the rendered images will be uploaded to the renderfarm server.
If set to False, the renderings can be found locally on the renderslave, which rendered the job."""
        )

    @err_decorator
    def connectEvents(self):
        self.b_browseFilename.clicked.connect(self.browseFileName)
        self.b_submit.clicked.connect(self.startSubmission)

    @err_decorator
    def browseFileName(self):
        selectedPath = QFileDialog.getOpenFileName(
            self, "Select python file", self.e_filename.text(), "All files (*.*)"
        )[0]

        if selectedPath != "":
            self.e_filename.setText(self.core.fixPath(selectedPath))

    @err_decorator
    def loadSettings(self):
        cData = {}
        cData["projectName"] = ["lastUsedSettings", "projectName"]
        cData["priority"] = ["lastUsedSettings", "priority"]
        cData["framesPerTask"] = ["lastUsedSettings", "framesPerTask"]
        cData["taskTimeout"] = ["lastUsedSettings", "taskTimeout"]
        cData["concurrentTasks"] = ["lastUsedSettings", "concurrentTasks"]
        cData["suspended"] = ["lastUsedSettings", "suspended"]
        cData["dependentFiles"] = ["lastUsedSettings", "dependentFiles"]
        cData["localMode"] = ["globals", "localMode"]
        cData["uploadOutput"] = ["lastUsedSettings", "uploadOutput"]

        cData = self.core.getConfig(data=cData)

        if cData["projectName"] is not None:
            self.e_projectName.setText(cData["projectName"])

        if cData["priority"] is not None:
            try:
                self.sp_priority.setValue(cData["priority"])
            except:
                pass

        if cData["framesPerTask"] is not None:
            try:
                self.sp_framesPerTask.setValue(cData["framesPerTask"])
            except:
                pass

        if cData["taskTimeout"] is not None:
            try:
                self.sp_rjTimeout.setValue(cData["taskTimeout"])
            except:
                pass

        if cData["concurrentTasks"] is not None:
            try:
                self.sp_concurrent.setValue(cData["concurrentTasks"])
            except:
                pass

        if cData["suspended"] is not None:
            try:
                self.chb_suspended.setChecked(cData["suspended"])
            except:
                pass

        if cData["dependentFiles"] is not None:
            try:
                self.chb_dependencies.setChecked(cData["dependentFiles"])
            except:
                pass

        if cData["localMode"] is not None and cData["localMode"]:
            self.chb_uploadOutput.setChecked(False)
            self.f_osUpload.setVisible(False)
        else:
            if cData["uploadOutput"] is not None:
                try:
                    self.chb_uploadOutput.setChecked(cData["uploadOutput"])
                except:
                    pass

    @err_decorator
    def saveSettings(self):
        cData = []
        cData.append(["lastUsedSettings", "projectName", self.e_projectName.text()])
        cData.append(["lastUsedSettings", "priority", self.sp_priority.value()])
        cData.append(["lastUsedSettings", "framesPerTask", self.e_projectName.text()])
        cData.append(["lastUsedSettings", "taskTimeout", self.sp_rjTimeout.value()])
        cData.append(["lastUsedSettings", "concurrentTasks", self.sp_concurrent.value()])
        cData.append(["lastUsedSettings", "suspended", self.chb_suspended.isChecked()])
        cData.append(
            ["lastUsedSettings", "dependentFiles", self.chb_dependencies.isChecked()]
        )
        cData.append(
            ["lastUsedSettings", "uploadOutput", self.chb_uploadOutput.isChecked()]
        )

        self.core.setConfig(data=cData)

    @err_decorator
    def startSubmission(self):
        if (
            not os.path.isabs(self.e_filename.text())
            or os.path.splitext(self.e_filename.text())[1] == ""
        ):
            QMessageBox.warning(
                self.core.messageParent,
                "Submission canceled",
                "Submission Canceled:\n\nOutputpath is invalid.\nPlease enter a complete filename.",
            )
            return

        # self.core.appPlugin.preSubmit(self, rSettings)

        jobData = {}
        jobData["projectName"] = self.e_projectName.text()
        jobData["jobName"] = self.e_jobName.text()
        jobData["priority"] = self.sp_priority.value()
        jobData["framesPerTask"] = self.sp_framesPerTask.value()
        jobData["suspended"] = self.chb_suspended.isChecked()
        jobData["submitDependendFiles"] = self.chb_dependencies.isChecked()
        jobData["uploadOutput"] = self.chb_uploadOutput.isChecked()
        jobData["timeout"] = self.sp_rjTimeout.value()
        jobData["concurrentTasks"] = self.sp_concurrent.value()
        jobData["filename"] = self.e_filename.text()
        jobData["startFrame"] = 0
        jobData["endFrame"] = 0

        self.saveSettings()

        import PandoraCore
        Pandora = PandoraCore.PandoraCore(app="Python")
        result = Pandora.submitJob(jobData)
        # self.core.appPlugin.undoRenderSettings(self, rSettings)

        if isinstance(result, list) and result[0] == "Success":
            msg = QMessageBox(
                QMessageBox.Information,
                "Submit Pandora renderjob",
                'Successfully submited job "%s"' % jobData["jobName"],
                QMessageBox.Ok,
            )
            msg.addButton("Open in explorer", QMessageBox.YesRole)
            self.core.parentWindow(msg)
            action = msg.exec_()

            if action == 0:
                self.core.openFolder(os.path.dirname(result[2]))
            self.close()
        elif result.startswith("Submission canceled"):
            QMessageBox.warning(self.core.messageParent, "Submission canceled", result)

    @err_decorator
    def enterEvent(self, event):
        QApplication.restoreOverrideCursor()
