# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PandoraPythonSubmitter.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlg_pandoraSubmitter(object):
    def setupUi(self, dlg_pandoraSubmitter):
        if not dlg_pandoraSubmitter.objectName():
            dlg_pandoraSubmitter.setObjectName(u"dlg_pandoraSubmitter")
        dlg_pandoraSubmitter.resize(431, 561)
        self.verticalLayout = QVBoxLayout(dlg_pandoraSubmitter)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(dlg_pandoraSubmitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 411, 541))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gb_filename = QWidget(self.groupBox_2)
        self.gb_filename.setObjectName(u"gb_filename")
        self.horizontalLayout_13 = QHBoxLayout(self.gb_filename)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 0, 9, 0)
        self.l_filename = QLabel(self.gb_filename)
        self.l_filename.setObjectName(u"l_filename")

        self.horizontalLayout_13.addWidget(self.l_filename)

        self.e_filename = QLineEdit(self.gb_filename)
        self.e_filename.setObjectName(u"e_filename")

        self.horizontalLayout_13.addWidget(self.e_filename)

        self.b_browseFilename = QPushButton(self.gb_filename)
        self.b_browseFilename.setObjectName(u"b_browseFilename")
        self.b_browseFilename.setMinimumSize(QSize(50, 0))
        self.b_browseFilename.setMaximumSize(QSize(50, 16777215))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.b_browseFilename.setFont(font)
        self.b_browseFilename.setFocusPolicy(Qt.NoFocus)
        self.b_browseFilename.setContextMenuPolicy(Qt.CustomContextMenu)

        self.horizontalLayout_13.addWidget(self.b_browseFilename)


        self.verticalLayout_4.addWidget(self.gb_filename)

        self.gb_args = QWidget(self.groupBox_2)
        self.gb_args.setObjectName(u"gb_args")
        self.horizontalLayout_5 = QHBoxLayout(self.gb_args)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.l_args = QLabel(self.gb_args)
        self.l_args.setObjectName(u"l_args")
        self.l_args.setMinimumSize(QSize(40, 0))
        self.l_args.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.l_args)

        self.horizontalSpacer = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.gb_args)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_4.addWidget(self.gb_args)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f_taskname = QWidget(self.groupBox)
        self.f_taskname.setObjectName(u"f_taskname")
        self.horizontalLayout_11 = QHBoxLayout(self.f_taskname)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 0, 9, 0)
        self.l_projectName = QLabel(self.f_taskname)
        self.l_projectName.setObjectName(u"l_projectName")

        self.horizontalLayout_11.addWidget(self.l_projectName)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.e_projectName = QLineEdit(self.f_taskname)
        self.e_projectName.setObjectName(u"e_projectName")
        self.e_projectName.setMinimumSize(QSize(200, 0))
        self.e_projectName.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_11.addWidget(self.e_projectName)


        self.verticalLayout_2.addWidget(self.f_taskname)

        self.w_jobname = QWidget(self.groupBox)
        self.w_jobname.setObjectName(u"w_jobname")
        self.horizontalLayout_10 = QHBoxLayout(self.w_jobname)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.l_jobName = QLabel(self.w_jobname)
        self.l_jobName.setObjectName(u"l_jobName")

        self.horizontalLayout_10.addWidget(self.l_jobName)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.e_jobName = QLineEdit(self.w_jobname)
        self.e_jobName.setObjectName(u"e_jobName")
        self.e_jobName.setMinimumSize(QSize(200, 0))
        self.e_jobName.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_10.addWidget(self.e_jobName)


        self.verticalLayout_2.addWidget(self.w_jobname)

        self.f_rjPrio_2 = QWidget(self.groupBox)
        self.f_rjPrio_2.setObjectName(u"f_rjPrio_2")
        self.horizontalLayout_25 = QHBoxLayout(self.f_rjPrio_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(9, 0, 9, 0)
        self.l_prio = QLabel(self.f_rjPrio_2)
        self.l_prio.setObjectName(u"l_prio")

        self.horizontalLayout_25.addWidget(self.l_prio)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_19)

        self.sp_priority = QSpinBox(self.f_rjPrio_2)
        self.sp_priority.setObjectName(u"sp_priority")
        self.sp_priority.setMaximum(100)
        self.sp_priority.setValue(50)

        self.horizontalLayout_25.addWidget(self.sp_priority)


        self.verticalLayout_2.addWidget(self.f_rjPrio_2)

        self.f_rjWidgetsPerTask_2 = QWidget(self.groupBox)
        self.f_rjWidgetsPerTask_2.setObjectName(u"f_rjWidgetsPerTask_2")
        self.horizontalLayout_30 = QHBoxLayout(self.f_rjWidgetsPerTask_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(9, 0, 9, 0)
        self.l_framesPerTask = QLabel(self.f_rjWidgetsPerTask_2)
        self.l_framesPerTask.setObjectName(u"l_framesPerTask")

        self.horizontalLayout_30.addWidget(self.l_framesPerTask)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_25)

        self.sp_framesPerTask = QSpinBox(self.f_rjWidgetsPerTask_2)
        self.sp_framesPerTask.setObjectName(u"sp_framesPerTask")
        self.sp_framesPerTask.setMaximum(9999)
        self.sp_framesPerTask.setValue(5)

        self.horizontalLayout_30.addWidget(self.sp_framesPerTask)


        self.verticalLayout_2.addWidget(self.f_rjWidgetsPerTask_2)

        self.f_rjTimeout = QWidget(self.groupBox)
        self.f_rjTimeout.setObjectName(u"f_rjTimeout")
        self.horizontalLayout_31 = QHBoxLayout(self.f_rjTimeout)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(9, 0, 9, 0)
        self.l_rjTimeout = QLabel(self.f_rjTimeout)
        self.l_rjTimeout.setObjectName(u"l_rjTimeout")

        self.horizontalLayout_31.addWidget(self.l_rjTimeout)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_22)

        self.sp_rjTimeout = QSpinBox(self.f_rjTimeout)
        self.sp_rjTimeout.setObjectName(u"sp_rjTimeout")
        self.sp_rjTimeout.setMinimum(1)
        self.sp_rjTimeout.setMaximum(9999)
        self.sp_rjTimeout.setValue(180)

        self.horizontalLayout_31.addWidget(self.sp_rjTimeout)


        self.verticalLayout_2.addWidget(self.f_rjTimeout)

        self.w_concurrent = QWidget(self.groupBox)
        self.w_concurrent.setObjectName(u"w_concurrent")
        self.horizontalLayout_32 = QHBoxLayout(self.w_concurrent)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(9, 0, 9, 0)
        self.l_concurrent = QLabel(self.w_concurrent)
        self.l_concurrent.setObjectName(u"l_concurrent")

        self.horizontalLayout_32.addWidget(self.l_concurrent)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_26)

        self.sp_concurrent = QSpinBox(self.w_concurrent)
        self.sp_concurrent.setObjectName(u"sp_concurrent")
        self.sp_concurrent.setMinimum(1)
        self.sp_concurrent.setMaximum(9999)
        self.sp_concurrent.setValue(1)

        self.horizontalLayout_32.addWidget(self.sp_concurrent)


        self.verticalLayout_2.addWidget(self.w_concurrent)

        self.f_suspended = QWidget(self.groupBox)
        self.f_suspended.setObjectName(u"f_suspended")
        self.horizontalLayout_29 = QHBoxLayout(self.f_suspended)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(9, 0, 9, 0)
        self.l_submitSuspended = QLabel(self.f_suspended)
        self.l_submitSuspended.setObjectName(u"l_submitSuspended")

        self.horizontalLayout_29.addWidget(self.l_submitSuspended)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_24)

        self.chb_suspended = QCheckBox(self.f_suspended)
        self.chb_suspended.setObjectName(u"chb_suspended")
        self.chb_suspended.setChecked(False)

        self.horizontalLayout_29.addWidget(self.chb_suspended)


        self.verticalLayout_2.addWidget(self.f_suspended)

        self.f_osDependencies = QWidget(self.groupBox)
        self.f_osDependencies.setObjectName(u"f_osDependencies")
        self.horizontalLayout_28 = QHBoxLayout(self.f_osDependencies)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(9, 0, 9, 0)
        self.l_submitDependent = QLabel(self.f_osDependencies)
        self.l_submitDependent.setObjectName(u"l_submitDependent")

        self.horizontalLayout_28.addWidget(self.l_submitDependent)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_23)

        self.chb_dependencies = QCheckBox(self.f_osDependencies)
        self.chb_dependencies.setObjectName(u"chb_dependencies")
        self.chb_dependencies.setChecked(False)

        self.horizontalLayout_28.addWidget(self.chb_dependencies)


        self.verticalLayout_2.addWidget(self.f_osDependencies)

        self.f_osUpload = QWidget(self.groupBox)
        self.f_osUpload.setObjectName(u"f_osUpload")
        self.horizontalLayout_23 = QHBoxLayout(self.f_osUpload)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 0, 9, 0)
        self.l_uploadOutput = QLabel(self.f_osUpload)
        self.l_uploadOutput.setObjectName(u"l_uploadOutput")

        self.horizontalLayout_23.addWidget(self.l_uploadOutput)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_18)

        self.chb_uploadOutput = QCheckBox(self.f_osUpload)
        self.chb_uploadOutput.setObjectName(u"chb_uploadOutput")
        self.chb_uploadOutput.setChecked(False)

        self.horizontalLayout_23.addWidget(self.chb_uploadOutput)


        self.verticalLayout_2.addWidget(self.f_osUpload)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(10, 30, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.b_submit = QPushButton(self.scrollAreaWidgetContents)
        self.b_submit.setObjectName(u"b_submit")

        self.verticalLayout_3.addWidget(self.b_submit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(dlg_pandoraSubmitter)

        QMetaObject.connectSlotsByName(dlg_pandoraSubmitter)
    # setupUi

    def retranslateUi(self, dlg_pandoraSubmitter):
        dlg_pandoraSubmitter.setWindowTitle(QCoreApplication.translate("dlg_pandoraSubmitter", u"Submit Pandora renderjob", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("dlg_pandoraSubmitter", u"Scene settings", None))
        self.l_filename.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Filename:", None))
        self.b_browseFilename.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"...", None))
        self.l_args.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Args:", None))
        self.groupBox.setTitle(QCoreApplication.translate("dlg_pandoraSubmitter", u"Job settings", None))
        self.l_projectName.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Projectname:", None))
        self.l_jobName.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Jobname:", None))
        self.l_prio.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Priority:", None))
        self.l_framesPerTask.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Frames per Task:", None))
        self.l_rjTimeout.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Task Timeout (min):", None))
        self.l_concurrent.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Concurrent tasks:", None))
        self.l_submitSuspended.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Submit suspended:", None))
        self.chb_suspended.setText("")
        self.l_submitDependent.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Submit dependent files:", None))
        self.chb_dependencies.setText("")
        self.l_uploadOutput.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Upload output:", None))
        self.chb_uploadOutput.setText("")
        self.b_submit.setText(QCoreApplication.translate("dlg_pandoraSubmitter", u"Submit", None))
    # retranslateUi