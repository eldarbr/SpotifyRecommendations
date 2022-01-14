# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from Configurator import Configurator
from OAuth_Master import SpotifyOAuth
from Spotify_Api import SpotifyApi
from typing import Union
import re
import json


class Ui_MainWindow(object):
    def __init__(self):
        self.configurator = Configurator()
        self.api = SpotifyApi()
        self.user_id = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.preferencesTab = QtWidgets.QWidget()
        self.preferencesTab.setObjectName("preferencesTab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.preferencesTab)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.authorizationBox = QtWidgets.QGroupBox(self.preferencesTab)
        self.authorizationBox.setMinimumSize(QtCore.QSize(0, 150))
        self.authorizationBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.authorizationBox.setObjectName("authorizationBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.authorizationBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.authorizeButtonWidget = QtWidgets.QWidget(self.authorizationBox)
        self.authorizeButtonWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.authorizeButtonWidget.setObjectName("authorizeButtonWidget")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.authorizeButtonWidget)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.authorizationStateWidget = QtWidgets.QWidget(self.authorizeButtonWidget)
        self.authorizationStateWidget.setMaximumSize(QtCore.QSize(16777215, 55))
        self.authorizationStateWidget.setObjectName("authorizationStateWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.authorizationStateWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.authorizationStateInfoLabel = QtWidgets.QLabel(self.authorizationStateWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.authorizationStateInfoLabel.setFont(font)
        self.authorizationStateInfoLabel.setObjectName("authorizationStateInfoLabel")
        self.verticalLayout_4.addWidget(self.authorizationStateInfoLabel)
        self.authorizationStateLabel = QtWidgets.QLabel(self.authorizationStateWidget)
        self.authorizationStateLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.authorizationStateLabel.setObjectName("authorizationStateLabel")
        self.verticalLayout_4.addWidget(self.authorizationStateLabel)
        self.horizontalLayout_17.addWidget(self.authorizationStateWidget)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.authorizeButton = QtWidgets.QPushButton(self.authorizeButtonWidget)
        self.authorizeButton.setMinimumSize(QtCore.QSize(130, 40))
        self.authorizeButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.authorizeButton.setFont(font)
        self.authorizeButton.setObjectName("authorizeButton")
        self.horizontalLayout_17.addWidget(self.authorizeButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.authorizeButtonWidget)
        self.verticalLayout_8.addWidget(self.authorizationBox)
        self.playlistBox = QtWidgets.QGroupBox(self.preferencesTab)
        self.playlistBox.setObjectName("playlistBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.playlistBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.playlistsHandlingWidget = QtWidgets.QWidget(self.playlistBox)
        self.playlistsHandlingWidget.setObjectName("playlistsHandlingWidget")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.playlistsHandlingWidget)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.updatePlaylistsButton = QtWidgets.QPushButton(self.playlistsHandlingWidget)
        self.updatePlaylistsButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.updatePlaylistsButton.setFont(font)
        self.updatePlaylistsButton.setObjectName("updatePlaylistsButton")
        self.horizontalLayout_19.addWidget(self.updatePlaylistsButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem2)
        self.createPlaylistButton = QtWidgets.QPushButton(self.playlistsHandlingWidget)
        self.createPlaylistButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.createPlaylistButton.setFont(font)
        self.createPlaylistButton.setObjectName("createPlaylistButton")
        self.horizontalLayout_19.addWidget(self.createPlaylistButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.playlistsHandlingWidget)
        self.playlistsListWidget = QtWidgets.QListWidget(self.playlistBox)
        self.playlistsListWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.playlistsListWidget.setFont(font)
        self.playlistsListWidget.setObjectName("playlistsListWidget")
        self.verticalLayout_3.addWidget(self.playlistsListWidget)
        self.playlistHandlingWidget = QtWidgets.QWidget(self.playlistBox)
        self.playlistHandlingWidget.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.playlistHandlingWidget.setFont(font)
        self.playlistHandlingWidget.setObjectName("playlistHandlingWidget")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.playlistHandlingWidget)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.overwriteRadioButton = QtWidgets.QRadioButton(self.playlistHandlingWidget)
        self.overwriteRadioButton.setObjectName("overwriteRadioButton")
        self.horizontalLayout_18.addWidget(self.overwriteRadioButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
        self.appendRadioButton = QtWidgets.QRadioButton(self.playlistHandlingWidget)
        self.appendRadioButton.setObjectName("appendRadioButton")
        self.horizontalLayout_18.addWidget(self.appendRadioButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.playlistHandlingWidget)
        self.recommendationsLimitWidget = QtWidgets.QWidget(self.playlistBox)
        self.recommendationsLimitWidget.setObjectName("recommendationsLimitWidget")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.recommendationsLimitWidget)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.recommendationsLimitLabel = QtWidgets.QLabel(self.recommendationsLimitWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.recommendationsLimitLabel.setFont(font)
        self.recommendationsLimitLabel.setObjectName("recommendationsLimitLabel")
        self.horizontalLayout_20.addWidget(self.recommendationsLimitLabel)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem6)
        self.recommendationsLimitSpinBox = QtWidgets.QSpinBox(self.recommendationsLimitWidget)
        self.recommendationsLimitSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.recommendationsLimitSpinBox.setFont(font)
        self.recommendationsLimitSpinBox.setMinimum(1)
        self.recommendationsLimitSpinBox.setMaximum(100)
        self.recommendationsLimitSpinBox.setProperty("value", 100)
        self.recommendationsLimitSpinBox.setObjectName("recommendationsLimitSpinBox")
        self.horizontalLayout_20.addWidget(self.recommendationsLimitSpinBox)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem7)
        self.verticalLayout_3.addWidget(self.recommendationsLimitWidget)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout_8.addWidget(self.playlistBox)
        self.tabWidget.addTab(self.preferencesTab, "")
        self.recommendationsTab = QtWidgets.QWidget()
        self.recommendationsTab.setObjectName("recommendationsTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.recommendationsTab)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.seedsPoolBox = QtWidgets.QGroupBox(self.recommendationsTab)
        self.seedsPoolBox.setMinimumSize(QtCore.QSize(0, 115))
        self.seedsPoolBox.setMaximumSize(QtCore.QSize(16777215, 115))
        self.seedsPoolBox.setObjectName("seedsPoolBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.seedsPoolBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.seedsPool = QtWidgets.QPlainTextEdit(self.seedsPoolBox)
        self.seedsPool.setObjectName("seedsPool")
        self.gridLayout_3.addWidget(self.seedsPool, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.seedsPoolBox)
        self.recommendationsScrollArea = QtWidgets.QScrollArea(self.recommendationsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recommendationsScrollArea.sizePolicy().hasHeightForWidth())
        self.recommendationsScrollArea.setSizePolicy(sizePolicy)
        self.recommendationsScrollArea.setMinimumSize(QtCore.QSize(550, 0))
        self.recommendationsScrollArea.setWidgetResizable(True)
        self.recommendationsScrollArea.setObjectName("recommendationsScrollArea")
        self.recommendationsScrollAreaWidget = QtWidgets.QWidget()
        self.recommendationsScrollAreaWidget.setEnabled(True)
        self.recommendationsScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 535, 700))
        self.recommendationsScrollAreaWidget.setObjectName("recommendationsScrollAreaWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.recommendationsScrollAreaWidget)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recommendationsForm = QtWidgets.QFormLayout()
        self.recommendationsForm.setContentsMargins(10, -1, -1, -1)
        self.recommendationsForm.setSpacing(10)
        self.recommendationsForm.setObjectName("recommendationsForm")
        self.acousticnessLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.acousticnessLabel.setObjectName("acousticnessLabel")
        self.recommendationsForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.acousticnessLabel)
        self.acousticnessWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.acousticnessWidget.setObjectName("acousticnessWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.acousticnessWidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acousticnessMinLabel = QtWidgets.QLabel(self.acousticnessWidget)
        self.acousticnessMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.acousticnessMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                               QtCore.Qt.AlignmentFlag.AlignTrailing |
                                               QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.acousticnessMinLabel.setObjectName("acousticnessMinLabel")
        self.horizontalLayout.addWidget(self.acousticnessMinLabel)
        self.acousticnessMin = QtWidgets.QSlider(self.acousticnessWidget)
        self.acousticnessMin.setMaximum(100)
        self.acousticnessMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.acousticnessMin.setObjectName("acousticnessMin")
        self.horizontalLayout.addWidget(self.acousticnessMin)
        self.acousticnessEnabled = QtWidgets.QCheckBox(self.acousticnessWidget)
        self.acousticnessEnabled.setText("")
        self.acousticnessEnabled.setObjectName("acousticnessEnabled")
        self.horizontalLayout.addWidget(self.acousticnessEnabled)
        self.acousticnessTargetLabel = QtWidgets.QLabel(self.acousticnessWidget)
        self.acousticnessTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.acousticnessTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                  QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                  QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.acousticnessTargetLabel.setObjectName("acousticnessTargetLabel")
        self.horizontalLayout.addWidget(self.acousticnessTargetLabel)
        self.acousticnessTarget = QtWidgets.QSlider(self.acousticnessWidget)
        self.acousticnessTarget.setMaximum(100)
        self.acousticnessTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.acousticnessTarget.setObjectName("acousticnessTarget")
        self.horizontalLayout.addWidget(self.acousticnessTarget)
        self.acousticnessMaxLabel = QtWidgets.QLabel(self.acousticnessWidget)
        self.acousticnessMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.acousticnessMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                               QtCore.Qt.AlignmentFlag.AlignTrailing |
                                               QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.acousticnessMaxLabel.setObjectName("acousticnessMaxLabel")
        self.horizontalLayout.addWidget(self.acousticnessMaxLabel)
        self.acousticnessMax = QtWidgets.QSlider(self.acousticnessWidget)
        self.acousticnessMax.setMaximum(100)
        self.acousticnessMax.setSliderPosition(100)
        self.acousticnessMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.acousticnessMax.setObjectName("acousticnessMax")
        self.horizontalLayout.addWidget(self.acousticnessMax)
        self.recommendationsForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.acousticnessWidget)
        self.danceabilityLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.danceabilityLabel.setObjectName("danceabilityLabel")
        self.recommendationsForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.danceabilityLabel)
        self.danceabilityWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.danceabilityWidget.setObjectName("danceabilityWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.danceabilityWidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.danceabilityMinLabel = QtWidgets.QLabel(self.danceabilityWidget)
        self.danceabilityMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.danceabilityMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                               QtCore.Qt.AlignmentFlag.AlignTrailing |
                                               QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.danceabilityMinLabel.setObjectName("danceabilityMinLabel")
        self.horizontalLayout_2.addWidget(self.danceabilityMinLabel)
        self.danceabilityMin = QtWidgets.QSlider(self.danceabilityWidget)
        self.danceabilityMin.setMaximum(100)
        self.danceabilityMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.danceabilityMin.setObjectName("danceabilityMin")
        self.horizontalLayout_2.addWidget(self.danceabilityMin)
        self.danceabilityEnabled = QtWidgets.QCheckBox(self.danceabilityWidget)
        self.danceabilityEnabled.setText("")
        self.danceabilityEnabled.setObjectName("danceabilityEnabled")
        self.horizontalLayout_2.addWidget(self.danceabilityEnabled)
        self.danceabilityTargetLabel = QtWidgets.QLabel(self.danceabilityWidget)
        self.danceabilityTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.danceabilityTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                  QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                  QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.danceabilityTargetLabel.setObjectName("danceabilityTargetLabel")
        self.horizontalLayout_2.addWidget(self.danceabilityTargetLabel)
        self.danceabilityTarget = QtWidgets.QSlider(self.danceabilityWidget)
        self.danceabilityTarget.setMaximum(100)
        self.danceabilityTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.danceabilityTarget.setObjectName("danceabilityTarget")
        self.horizontalLayout_2.addWidget(self.danceabilityTarget)
        self.danceabilityMaxLabel = QtWidgets.QLabel(self.danceabilityWidget)
        self.danceabilityMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.danceabilityMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                               QtCore.Qt.AlignmentFlag.AlignTrailing |
                                               QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.danceabilityMaxLabel.setObjectName("danceabilityMaxLabel")
        self.horizontalLayout_2.addWidget(self.danceabilityMaxLabel)
        self.danceabilityMax = QtWidgets.QSlider(self.danceabilityWidget)
        self.danceabilityMax.setMaximum(100)
        self.danceabilityMax.setSliderPosition(100)
        self.danceabilityMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.danceabilityMax.setObjectName("danceabilityMax")
        self.horizontalLayout_2.addWidget(self.danceabilityMax)
        self.recommendationsForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.danceabilityWidget)
        self.durationLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.durationLabel.setObjectName("durationLabel")
        self.recommendationsForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.durationLabel)
        self.durationWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.durationWidget.setObjectName("durationWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.durationWidget)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.durationMinLabel = QtWidgets.QLabel(self.durationWidget)
        self.durationMinLabel.setMaximumSize(QtCore.QSize(30, 16777215))
        self.durationMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.durationMinLabel.setObjectName("durationMinLabel")
        self.horizontalLayout_3.addWidget(self.durationMinLabel)
        self.durationMin = QtWidgets.QTimeEdit(self.durationWidget)
        self.durationMin.setMaximumSize(QtCore.QSize(55, 16777215))
        self.durationMin.setWrapping(False)
        self.durationMin.setFrame(True)
        self.durationMin.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.durationMin.setAccelerated(True)
        self.durationMin.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.durationMin.setObjectName("durationMin")
        self.horizontalLayout_3.addWidget(self.durationMin)
        self.durationEnabled = QtWidgets.QCheckBox(self.durationWidget)
        self.durationEnabled.setMaximumSize(QtCore.QSize(15, 16777215))
        self.durationEnabled.setText("")
        self.durationEnabled.setObjectName("durationEnabled")
        self.horizontalLayout_3.addWidget(self.durationEnabled)
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.durationTargetLabel = QtWidgets.QLabel(self.durationWidget)
        self.durationTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                              QtCore.Qt.AlignmentFlag.AlignTrailing |
                                              QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.durationTargetLabel.setObjectName("durationTargetLabel")
        self.horizontalLayout_3.addWidget(self.durationTargetLabel)
        self.durationTarget = QtWidgets.QTimeEdit(self.durationWidget)
        self.durationTarget.setMaximumSize(QtCore.QSize(55, 16777215))
        self.durationTarget.setMaximumTime(QtCore.QTime(0, 59, 59))
        self.durationTarget.setObjectName("durationTarget")
        self.horizontalLayout_3.addWidget(self.durationTarget)
        spacerItem7 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.durationMaxLabel = QtWidgets.QLabel(self.durationWidget)
        self.durationMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.durationMaxLabel.setObjectName("durationMaxLabel")
        self.horizontalLayout_3.addWidget(self.durationMaxLabel)
        self.durationMax = QtWidgets.QTimeEdit(self.durationWidget)
        self.durationMax.setMaximumSize(QtCore.QSize(55, 16777215))
        self.durationMax.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 59, 59)))
        self.durationMax.setMaximumTime(QtCore.QTime(0, 59, 59))
        self.durationMax.setObjectName("durationMax")
        self.horizontalLayout_3.addWidget(self.durationMax)
        self.recommendationsForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.durationWidget)
        self.energyLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.energyLabel.setObjectName("energyLabel")
        self.recommendationsForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.energyLabel)
        self.energyWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.energyWidget.setObjectName("energyWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.energyWidget)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.energyMinLabel = QtWidgets.QLabel(self.energyWidget)
        self.energyMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.energyMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                         QtCore.Qt.AlignmentFlag.AlignTrailing |
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.energyMinLabel.setObjectName("energyMinLabel")
        self.horizontalLayout_4.addWidget(self.energyMinLabel)
        self.energyMin = QtWidgets.QSlider(self.energyWidget)
        self.energyMin.setMaximum(100)
        self.energyMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.energyMin.setObjectName("energyMin")
        self.horizontalLayout_4.addWidget(self.energyMin)
        self.energyEnabled = QtWidgets.QCheckBox(self.energyWidget)
        self.energyEnabled.setText("")
        self.energyEnabled.setObjectName("energyEnabled")
        self.horizontalLayout_4.addWidget(self.energyEnabled)
        self.energyTargetLabel = QtWidgets.QLabel(self.energyWidget)
        self.energyTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.energyTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                            QtCore.Qt.AlignmentFlag.AlignTrailing |
                                            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.energyTargetLabel.setObjectName("energyTargetLabel")
        self.horizontalLayout_4.addWidget(self.energyTargetLabel)
        self.energyTarget = QtWidgets.QSlider(self.energyWidget)
        self.energyTarget.setMaximum(100)
        self.energyTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.energyTarget.setObjectName("energyTarget")
        self.horizontalLayout_4.addWidget(self.energyTarget)
        self.energyMaxLabel = QtWidgets.QLabel(self.energyWidget)
        self.energyMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.energyMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                         QtCore.Qt.AlignmentFlag.AlignTrailing |
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.energyMaxLabel.setObjectName("energyMaxLabel")
        self.horizontalLayout_4.addWidget(self.energyMaxLabel)
        self.energyMax = QtWidgets.QSlider(self.energyWidget)
        self.energyMax.setMaximum(100)
        self.energyMax.setProperty("value", 100)
        self.energyMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.energyMax.setObjectName("energyMax")
        self.horizontalLayout_4.addWidget(self.energyMax)
        self.recommendationsForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.energyWidget)
        self.instrumentalnessLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.instrumentalnessLabel.setObjectName("instrumentalnessLabel")
        self.recommendationsForm.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.instrumentalnessLabel)
        self.instrumentalnessWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.instrumentalnessWidget.setObjectName("instrumentalnessWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.instrumentalnessWidget)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.instrumentalnessMinLabel = QtWidgets.QLabel(self.instrumentalnessWidget)
        self.instrumentalnessMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.instrumentalnessMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                   QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                   QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.instrumentalnessMinLabel.setObjectName("instrumentalnessMinLabel")
        self.horizontalLayout_5.addWidget(self.instrumentalnessMinLabel)
        self.instrumentalnessMin = QtWidgets.QSlider(self.instrumentalnessWidget)
        self.instrumentalnessMin.setMaximum(100)
        self.instrumentalnessMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.instrumentalnessMin.setObjectName("instrumentalnessMin")
        self.horizontalLayout_5.addWidget(self.instrumentalnessMin)
        self.instrumentalnessEnabled = QtWidgets.QCheckBox(self.instrumentalnessWidget)
        self.instrumentalnessEnabled.setText("")
        self.instrumentalnessEnabled.setObjectName("instrumentalnessEnabled")
        self.horizontalLayout_5.addWidget(self.instrumentalnessEnabled)
        self.instrumentalnessTargetLabel = QtWidgets.QLabel(self.instrumentalnessWidget)
        self.instrumentalnessTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.instrumentalnessTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                      QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                      QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.instrumentalnessTargetLabel.setObjectName("instrumentalnessTargetLabel")
        self.horizontalLayout_5.addWidget(self.instrumentalnessTargetLabel)
        self.instrumentalnessTarget = QtWidgets.QSlider(self.instrumentalnessWidget)
        self.instrumentalnessTarget.setMaximum(100)
        self.instrumentalnessTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.instrumentalnessTarget.setObjectName("instrumentalnessTarget")
        self.horizontalLayout_5.addWidget(self.instrumentalnessTarget)
        self.instrumentalnessMaxLabel = QtWidgets.QLabel(self.instrumentalnessWidget)
        self.instrumentalnessMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.instrumentalnessMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                   QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                   QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.instrumentalnessMaxLabel.setObjectName("instrumentalnessMaxLabel")
        self.horizontalLayout_5.addWidget(self.instrumentalnessMaxLabel)
        self.instrumentalnessMax = QtWidgets.QSlider(self.instrumentalnessWidget)
        self.instrumentalnessMax.setMaximum(100)
        self.instrumentalnessMax.setSliderPosition(100)
        self.instrumentalnessMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.instrumentalnessMax.setObjectName("instrumentalnessMax")
        self.horizontalLayout_5.addWidget(self.instrumentalnessMax)
        self.recommendationsForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.instrumentalnessWidget)
        self.keyLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.keyLabel.setObjectName("keyLabel")
        self.recommendationsForm.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.keyLabel)
        self.keyWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.keyWidget.setObjectName("keyWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.keyWidget)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.keyMinLabel = QtWidgets.QLabel(self.keyWidget)
        self.keyMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.keyMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                      QtCore.Qt.AlignmentFlag.AlignTrailing |
                                      QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.keyMinLabel.setObjectName("keyMinLabel")
        self.horizontalLayout_6.addWidget(self.keyMinLabel)
        self.keyMin = QtWidgets.QSlider(self.keyWidget)
        self.keyMin.setMinimum(-1)
        self.keyMin.setMaximum(11)
        self.keyMin.setProperty("value", -1)
        self.keyMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.keyMin.setObjectName("keyMin")
        self.horizontalLayout_6.addWidget(self.keyMin)
        self.keyEnabled = QtWidgets.QCheckBox(self.keyWidget)
        self.keyEnabled.setText("")
        self.keyEnabled.setObjectName("keyEnabled")
        self.horizontalLayout_6.addWidget(self.keyEnabled)
        self.keyTargetLabel = QtWidgets.QLabel(self.keyWidget)
        self.keyTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.keyTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                         QtCore.Qt.AlignmentFlag.AlignTrailing |
                                         QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.keyTargetLabel.setObjectName("keyTargetLabel")
        self.horizontalLayout_6.addWidget(self.keyTargetLabel)
        self.keyTarget = QtWidgets.QSlider(self.keyWidget)
        self.keyTarget.setMinimum(-1)
        self.keyTarget.setMaximum(11)
        self.keyTarget.setProperty("value", -1)
        self.keyTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.keyTarget.setObjectName("keyTarget")
        self.horizontalLayout_6.addWidget(self.keyTarget)
        self.keyMaxLabel = QtWidgets.QLabel(self.keyWidget)
        self.keyMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.keyMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                      QtCore.Qt.AlignmentFlag.AlignTrailing |
                                      QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.keyMaxLabel.setObjectName("keyMaxLabel")
        self.horizontalLayout_6.addWidget(self.keyMaxLabel)
        self.keyMax = QtWidgets.QSlider(self.keyWidget)
        self.keyMax.setMinimum(-1)
        self.keyMax.setMaximum(11)
        self.keyMax.setSliderPosition(11)
        self.keyMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.keyMax.setObjectName("keyMax")
        self.horizontalLayout_6.addWidget(self.keyMax)
        self.recommendationsForm.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.keyWidget)
        self.livenessLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.livenessLabel.setObjectName("livenessLabel")
        self.recommendationsForm.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.livenessLabel)
        self.livenessWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.livenessWidget.setObjectName("livenessWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.livenessWidget)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.livenessMinLabel = QtWidgets.QLabel(self.livenessWidget)
        self.livenessMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.livenessMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.livenessMinLabel.setObjectName("livenessMinLabel")
        self.horizontalLayout_8.addWidget(self.livenessMinLabel)
        self.livenessMin = QtWidgets.QSlider(self.livenessWidget)
        self.livenessMin.setMaximum(100)
        self.livenessMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.livenessMin.setObjectName("livenessMin")
        self.horizontalLayout_8.addWidget(self.livenessMin)
        self.livenessEnabled = QtWidgets.QCheckBox(self.livenessWidget)
        self.livenessEnabled.setText("")
        self.livenessEnabled.setObjectName("livenessEnabled")
        self.horizontalLayout_8.addWidget(self.livenessEnabled)
        self.livenessTargetLabel = QtWidgets.QLabel(self.livenessWidget)
        self.livenessTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.livenessTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                              QtCore.Qt.AlignmentFlag.AlignTrailing |
                                              QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.livenessTargetLabel.setObjectName("livenessTargetLabel")
        self.horizontalLayout_8.addWidget(self.livenessTargetLabel)
        self.livenessTarget = QtWidgets.QSlider(self.livenessWidget)
        self.livenessTarget.setMaximum(100)
        self.livenessTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.livenessTarget.setObjectName("livenessTarget")
        self.horizontalLayout_8.addWidget(self.livenessTarget)
        self.livenessMaxLabel = QtWidgets.QLabel(self.livenessWidget)
        self.livenessMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.livenessMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.livenessMaxLabel.setObjectName("livenessMaxLabel")
        self.horizontalLayout_8.addWidget(self.livenessMaxLabel)
        self.livenessMax = QtWidgets.QSlider(self.livenessWidget)
        self.livenessMax.setMaximum(100)
        self.livenessMax.setProperty("value", 100)
        self.livenessMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.livenessMax.setObjectName("livenessMax")
        self.horizontalLayout_8.addWidget(self.livenessMax)
        self.recommendationsForm.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.livenessWidget)
        self.loudnessLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.loudnessLabel.setObjectName("loudnessLabel")
        self.recommendationsForm.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.loudnessLabel)
        self.loudnessWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.loudnessWidget.setObjectName("loudnessWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.loudnessWidget)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.loudnessMinLabel = QtWidgets.QLabel(self.loudnessWidget)
        self.loudnessMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.loudnessMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.loudnessMinLabel.setObjectName("loudnessMinLabel")
        self.horizontalLayout_9.addWidget(self.loudnessMinLabel)
        self.loudnessMin = QtWidgets.QSlider(self.loudnessWidget)
        self.loudnessMin.setMinimum(-60)
        self.loudnessMin.setMaximum(0)
        self.loudnessMin.setProperty("value", -60)
        self.loudnessMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.loudnessMin.setObjectName("loudnessMin")
        self.horizontalLayout_9.addWidget(self.loudnessMin)
        self.loudnessEnabled = QtWidgets.QCheckBox(self.loudnessWidget)
        self.loudnessEnabled.setText("")
        self.loudnessEnabled.setObjectName("loudnessEnabled")
        self.horizontalLayout_9.addWidget(self.loudnessEnabled)
        self.loudnessTargetLabel = QtWidgets.QLabel(self.loudnessWidget)
        self.loudnessTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.loudnessTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                              QtCore.Qt.AlignmentFlag.AlignTrailing |
                                              QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.loudnessTargetLabel.setObjectName("loudnessTargetLabel")
        self.horizontalLayout_9.addWidget(self.loudnessTargetLabel)
        self.loudnessTarget = QtWidgets.QSlider(self.loudnessWidget)
        self.loudnessTarget.setMinimum(-60)
        self.loudnessTarget.setMaximum(0)
        self.loudnessTarget.setProperty("value", -60)
        self.loudnessTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.loudnessTarget.setObjectName("loudnessTarget")
        self.horizontalLayout_9.addWidget(self.loudnessTarget)
        self.loudnessMaxLabel = QtWidgets.QLabel(self.loudnessWidget)
        self.loudnessMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.loudnessMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.loudnessMaxLabel.setObjectName("loudnessMaxLabel")
        self.horizontalLayout_9.addWidget(self.loudnessMaxLabel)
        self.loudnessMax = QtWidgets.QSlider(self.loudnessWidget)
        self.loudnessMax.setMinimum(-60)
        self.loudnessMax.setMaximum(0)
        self.loudnessMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.loudnessMax.setObjectName("loudnessMax")
        self.horizontalLayout_9.addWidget(self.loudnessMax)
        self.recommendationsForm.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.loudnessWidget)
        self.modeLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.modeLabel.setObjectName("modeLabel")
        self.recommendationsForm.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.modeLabel)
        self.modeWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.modeWidget.setObjectName("modeWidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.modeWidget)
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.modeMinLabel = QtWidgets.QLabel(self.modeWidget)
        self.modeMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.modeMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                       QtCore.Qt.AlignmentFlag.AlignTrailing |
                                       QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modeMinLabel.setObjectName("modeMinLabel")
        self.horizontalLayout_10.addWidget(self.modeMinLabel)
        self.modeMin = QtWidgets.QSlider(self.modeWidget)
        self.modeMin.setMaximum(1)
        self.modeMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.modeMin.setObjectName("modeMin")
        self.horizontalLayout_10.addWidget(self.modeMin)
        self.modeEnabled = QtWidgets.QCheckBox(self.modeWidget)
        self.modeEnabled.setText("")
        self.modeEnabled.setObjectName("modeEnabled")
        self.horizontalLayout_10.addWidget(self.modeEnabled)
        self.modeTargetLabel = QtWidgets.QLabel(self.modeWidget)
        self.modeTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.modeTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignTrailing |
                                          QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modeTargetLabel.setObjectName("modeTargetLabel")
        self.horizontalLayout_10.addWidget(self.modeTargetLabel)
        self.modeTarget = QtWidgets.QSlider(self.modeWidget)
        self.modeTarget.setMaximum(1)
        self.modeTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.modeTarget.setObjectName("modeTarget")
        self.horizontalLayout_10.addWidget(self.modeTarget)
        self.modeMaxLabel = QtWidgets.QLabel(self.modeWidget)
        self.modeMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.modeMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                       QtCore.Qt.AlignmentFlag.AlignTrailing |
                                       QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.modeMaxLabel.setObjectName("modeMaxLabel")
        self.horizontalLayout_10.addWidget(self.modeMaxLabel)
        self.modeMax = QtWidgets.QSlider(self.modeWidget)
        self.modeMax.setMaximum(1)
        self.modeMax.setProperty("value", 1)
        self.modeMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.modeMax.setObjectName("modeMax")
        self.horizontalLayout_10.addWidget(self.modeMax)
        self.recommendationsForm.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.modeWidget)
        self.popularityLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.popularityLabel.setObjectName("popularityLabel")
        self.recommendationsForm.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.popularityLabel)
        self.popularityWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.popularityWidget.setObjectName("popularityWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.popularityWidget)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.popularityMinLabel = QtWidgets.QLabel(self.popularityWidget)
        self.popularityMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.popularityMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                             QtCore.Qt.AlignmentFlag.AlignTrailing |
                                             QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.popularityMinLabel.setObjectName("popularityMinLabel")
        self.horizontalLayout_11.addWidget(self.popularityMinLabel)
        self.popularityMin = QtWidgets.QSlider(self.popularityWidget)
        self.popularityMin.setMaximum(100)
        self.popularityMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.popularityMin.setObjectName("popularityMin")
        self.horizontalLayout_11.addWidget(self.popularityMin)
        self.popularityEnabled = QtWidgets.QCheckBox(self.popularityWidget)
        self.popularityEnabled.setText("")
        self.popularityEnabled.setObjectName("popularityEnabled")
        self.horizontalLayout_11.addWidget(self.popularityEnabled)
        self.popularityTargetLabel = QtWidgets.QLabel(self.popularityWidget)
        self.popularityTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.popularityTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.popularityTargetLabel.setObjectName("popularityTargetLabel")
        self.horizontalLayout_11.addWidget(self.popularityTargetLabel)
        self.popularityTarget = QtWidgets.QSlider(self.popularityWidget)
        self.popularityTarget.setMaximum(100)
        self.popularityTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.popularityTarget.setObjectName("popularityTarget")
        self.horizontalLayout_11.addWidget(self.popularityTarget)
        self.popularityMaxLabel = QtWidgets.QLabel(self.popularityWidget)
        self.popularityMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.popularityMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                             QtCore.Qt.AlignmentFlag.AlignTrailing |
                                             QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.popularityMaxLabel.setObjectName("popularityMaxLabel")
        self.horizontalLayout_11.addWidget(self.popularityMaxLabel)
        self.popularityMax = QtWidgets.QSlider(self.popularityWidget)
        self.popularityMax.setMaximum(100)
        self.popularityMax.setSliderPosition(100)
        self.popularityMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.popularityMax.setObjectName("popularityMax")
        self.horizontalLayout_11.addWidget(self.popularityMax)
        self.recommendationsForm.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.popularityWidget)
        self.speechinessLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.speechinessLabel.setObjectName("speechinessLabel")
        self.recommendationsForm.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.speechinessLabel)
        self.speechinessWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.speechinessWidget.setObjectName("speechinessWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.speechinessWidget)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.speechinessMinLabel = QtWidgets.QLabel(self.speechinessWidget)
        self.speechinessMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.speechinessMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                              QtCore.Qt.AlignmentFlag.AlignTrailing |
                                              QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.speechinessMinLabel.setObjectName("speechinessMinLabel")
        self.horizontalLayout_13.addWidget(self.speechinessMinLabel)
        self.speechinessMin = QtWidgets.QSlider(self.speechinessWidget)
        self.speechinessMin.setMaximum(100)
        self.speechinessMin.setSliderPosition(0)
        self.speechinessMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.speechinessMin.setObjectName("speechinessMin")
        self.horizontalLayout_13.addWidget(self.speechinessMin)
        self.speechinessEnabled = QtWidgets.QCheckBox(self.speechinessWidget)
        self.speechinessEnabled.setText("")
        self.speechinessEnabled.setObjectName("speechinessEnabled")
        self.horizontalLayout_13.addWidget(self.speechinessEnabled)
        self.speechinessTargetLabel = QtWidgets.QLabel(self.speechinessWidget)
        self.speechinessTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.speechinessTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                 QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                 QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.speechinessTargetLabel.setObjectName("speechinessTargetLabel")
        self.horizontalLayout_13.addWidget(self.speechinessTargetLabel)
        self.speechinessTarget = QtWidgets.QSlider(self.speechinessWidget)
        self.speechinessTarget.setMaximum(100)
        self.speechinessTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.speechinessTarget.setObjectName("speechinessTarget")
        self.horizontalLayout_13.addWidget(self.speechinessTarget)
        self.speechinessMaxLabel = QtWidgets.QLabel(self.speechinessWidget)
        self.speechinessMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.speechinessMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                              QtCore.Qt.AlignmentFlag.AlignTrailing |
                                              QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.speechinessMaxLabel.setObjectName("speechinessMaxLabel")
        self.horizontalLayout_13.addWidget(self.speechinessMaxLabel)
        self.speechinessMax = QtWidgets.QSlider(self.speechinessWidget)
        self.speechinessMax.setMaximum(100)
        self.speechinessMax.setSliderPosition(100)
        self.speechinessMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.speechinessMax.setObjectName("speechinessMax")
        self.horizontalLayout_13.addWidget(self.speechinessMax)
        self.recommendationsForm.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.speechinessWidget)
        self.tempoLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.tempoLabel.setObjectName("tempoLabel")
        self.recommendationsForm.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.tempoLabel)
        self.tempoWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.tempoWidget.setObjectName("tempoWidget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tempoWidget)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.tempoMinLabel = QtWidgets.QLabel(self.tempoWidget)
        self.tempoMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.tempoMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                        QtCore.Qt.AlignmentFlag.AlignTrailing |
                                        QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tempoMinLabel.setObjectName("tempoMinLabel")
        self.horizontalLayout_14.addWidget(self.tempoMinLabel)
        self.tempoMin = QtWidgets.QSlider(self.tempoWidget)
        self.tempoMin.setMaximum(300)
        self.tempoMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.tempoMin.setObjectName("tempoMin")
        self.horizontalLayout_14.addWidget(self.tempoMin)
        self.tempoEnabled = QtWidgets.QCheckBox(self.tempoWidget)
        self.tempoEnabled.setText("")
        self.tempoEnabled.setObjectName("tempoEnabled")
        self.horizontalLayout_14.addWidget(self.tempoEnabled)
        self.tempoTargetLabel = QtWidgets.QLabel(self.tempoWidget)
        self.tempoTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.tempoTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                           QtCore.Qt.AlignmentFlag.AlignTrailing |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tempoTargetLabel.setObjectName("tempoTargetLabel")
        self.horizontalLayout_14.addWidget(self.tempoTargetLabel)
        self.tempoTarget = QtWidgets.QSlider(self.tempoWidget)
        self.tempoTarget.setMaximum(300)
        self.tempoTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.tempoTarget.setObjectName("tempoTarget")
        self.horizontalLayout_14.addWidget(self.tempoTarget)
        self.tempoMaxLabel = QtWidgets.QLabel(self.tempoWidget)
        self.tempoMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.tempoMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                        QtCore.Qt.AlignmentFlag.AlignTrailing |
                                        QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tempoMaxLabel.setObjectName("tempoMaxLabel")
        self.horizontalLayout_14.addWidget(self.tempoMaxLabel)
        self.tempoMax = QtWidgets.QSlider(self.tempoWidget)
        self.tempoMax.setMaximum(300)
        self.tempoMax.setProperty("value", 300)
        self.tempoMax.setSliderPosition(300)
        self.tempoMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.tempoMax.setObjectName("tempoMax")
        self.horizontalLayout_14.addWidget(self.tempoMax)
        self.recommendationsForm.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.tempoWidget)
        self.timeSignatureLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.timeSignatureLabel.setObjectName("timeSignatureLabel")
        self.recommendationsForm.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.timeSignatureLabel)
        self.valenceLabel = QtWidgets.QLabel(self.recommendationsScrollAreaWidget)
        self.valenceLabel.setObjectName("valenceLabel")
        self.recommendationsForm.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.valenceLabel)
        self.valenceWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.valenceWidget.setObjectName("valenceWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.valenceWidget)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.valenceMinLabel = QtWidgets.QLabel(self.valenceWidget)
        self.valenceMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.valenceMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignTrailing |
                                          QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.valenceMinLabel.setObjectName("valenceMinLabel")
        self.horizontalLayout_7.addWidget(self.valenceMinLabel)
        self.valenceMin = QtWidgets.QSlider(self.valenceWidget)
        self.valenceMin.setMaximum(100)
        self.valenceMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.valenceMin.setObjectName("valenceMin")
        self.horizontalLayout_7.addWidget(self.valenceMin)
        self.valenceEnabled = QtWidgets.QCheckBox(self.valenceWidget)
        self.valenceEnabled.setText("")
        self.valenceEnabled.setObjectName("valenceEnabled")
        self.horizontalLayout_7.addWidget(self.valenceEnabled)
        self.valenceTargetLabel = QtWidgets.QLabel(self.valenceWidget)
        self.valenceTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.valenceTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                             QtCore.Qt.AlignmentFlag.AlignTrailing |
                                             QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.valenceTargetLabel.setObjectName("valenceTargetLabel")
        self.horizontalLayout_7.addWidget(self.valenceTargetLabel)
        self.valenceTarget = QtWidgets.QSlider(self.valenceWidget)
        self.valenceTarget.setMaximum(100)
        self.valenceTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.valenceTarget.setObjectName("valenceTarget")
        self.horizontalLayout_7.addWidget(self.valenceTarget)
        self.valenceMaxLabel = QtWidgets.QLabel(self.valenceWidget)
        self.valenceMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.valenceMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignTrailing |
                                          QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.valenceMaxLabel.setObjectName("valenceMaxLabel")
        self.horizontalLayout_7.addWidget(self.valenceMaxLabel)
        self.valenceMax = QtWidgets.QSlider(self.valenceWidget)
        self.valenceMax.setMaximum(100)
        self.valenceMax.setSliderPosition(100)
        self.valenceMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.valenceMax.setObjectName("valenceMax")
        self.horizontalLayout_7.addWidget(self.valenceMax)
        self.recommendationsForm.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.valenceWidget)
        self.timeSignatureWidget = QtWidgets.QWidget(self.recommendationsScrollAreaWidget)
        self.timeSignatureWidget.setObjectName("timeSignatureWidget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.timeSignatureWidget)
        self.horizontalLayout_12.setSpacing(15)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.timeSignatureMinLabel = QtWidgets.QLabel(self.timeSignatureWidget)
        self.timeSignatureMinLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.timeSignatureMinLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.timeSignatureMinLabel.setObjectName("timeSignatureMinLabel")
        self.horizontalLayout_12.addWidget(self.timeSignatureMinLabel)
        self.timeSignatureMin = QtWidgets.QSlider(self.timeSignatureWidget)
        self.timeSignatureMin.setMinimum(3)
        self.timeSignatureMin.setMaximum(7)
        self.timeSignatureMin.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.timeSignatureMin.setObjectName("timeSignatureMin")
        self.horizontalLayout_12.addWidget(self.timeSignatureMin)
        self.timeSignatureEnabled = QtWidgets.QCheckBox(self.timeSignatureWidget)
        self.timeSignatureEnabled.setText("")
        self.timeSignatureEnabled.setObjectName("timeSignatureEnabled")
        self.horizontalLayout_12.addWidget(self.timeSignatureEnabled)
        self.timeSignatureTargetLabel = QtWidgets.QLabel(self.timeSignatureWidget)
        self.timeSignatureTargetLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.timeSignatureTargetLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                   QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                   QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.timeSignatureTargetLabel.setObjectName("timeSignatureTargetLabel")
        self.horizontalLayout_12.addWidget(self.timeSignatureTargetLabel)
        self.timeSignatureTarget = QtWidgets.QSlider(self.timeSignatureWidget)
        self.timeSignatureTarget.setMinimum(3)
        self.timeSignatureTarget.setMaximum(7)
        self.timeSignatureTarget.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.timeSignatureTarget.setObjectName("timeSignatureTarget")
        self.horizontalLayout_12.addWidget(self.timeSignatureTarget)
        self.timeSignatureMaxLabel = QtWidgets.QLabel(self.timeSignatureWidget)
        self.timeSignatureMaxLabel.setMinimumSize(QtCore.QSize(45, 0))
        self.timeSignatureMaxLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                                QtCore.Qt.AlignmentFlag.AlignTrailing |
                                                QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.timeSignatureMaxLabel.setObjectName("timeSignatureMaxLabel")
        self.horizontalLayout_12.addWidget(self.timeSignatureMaxLabel)
        self.timeSignatureMax = QtWidgets.QSlider(self.timeSignatureWidget)
        self.timeSignatureMax.setMinimum(3)
        self.timeSignatureMax.setMaximum(7)
        self.timeSignatureMax.setSliderPosition(7)
        self.timeSignatureMax.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.timeSignatureMax.setObjectName("timeSignatureMax")
        self.horizontalLayout_12.addWidget(self.timeSignatureMax)
        self.recommendationsForm.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.timeSignatureWidget)
        self.verticalLayout_2.addLayout(self.recommendationsForm)
        self.recommendationsScrollArea.setWidget(self.recommendationsScrollAreaWidget)
        self.verticalLayout.addWidget(self.recommendationsScrollArea)
        self.generateRecommendationsWidget = QtWidgets.QWidget(self.recommendationsTab)
        self.generateRecommendationsWidget.setObjectName("generateRecommendationsWidget")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.generateRecommendationsWidget)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.generateButton = QtWidgets.QPushButton(self.generateRecommendationsWidget)
        self.generateButton.setMinimumSize(QtCore.QSize(200, 40))
        self.generateButton.setMaximumSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout_16.addWidget(self.generateButton)
        self.verticalLayout.addWidget(self.generateRecommendationsWidget)
        self.tabWidget.addTab(self.recommendationsTab, "")
        self.analysisTab = QtWidgets.QWidget()
        self.analysisTab.setObjectName("analysisTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.analysisTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.analysisUrlEdit = QtWidgets.QLineEdit(self.analysisTab)
        self.analysisUrlEdit.setObjectName("analysisUrlEdit")
        self.verticalLayout_5.addWidget(self.analysisUrlEdit)
        self.analysisButtonWidget = QtWidgets.QWidget(self.analysisTab)
        self.analysisButtonWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.analysisButtonWidget.setObjectName("analysisButtonWidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.analysisButtonWidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.analysisButton = QtWidgets.QPushButton(self.analysisButtonWidget)
        self.analysisButton.setMinimumSize(QtCore.QSize(0, 35))
        self.analysisButton.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.analysisButton.setFont(font)
        self.analysisButton.setObjectName("analysisButton")
        self.horizontalLayout_15.addWidget(self.analysisButton)
        self.verticalLayout_5.addWidget(self.analysisButtonWidget)
        self.analysisResultTextBrowser = QtWidgets.QTextBrowser(self.analysisTab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.analysisResultTextBrowser.setFont(font)
        self.analysisResultTextBrowser.setObjectName("analysisResultTextBrowser")
        self.verticalLayout_5.addWidget(self.analysisResultTextBrowser)
        self.tabWidget.addTab(self.analysisTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.functionality()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.authorizationBox.setTitle(_translate("MainWindow", "Authorization"))
        self.authorizationStateInfoLabel.setText(_translate("MainWindow", "Current Spotify authorization state:"))
        self.authorizationStateLabel.setText(_translate("MainWindow", "Unauthorized"))
        self.authorizeButton.setText(_translate("MainWindow", "Authorize"))
        self.playlistBox.setTitle(_translate("MainWindow", "Playlist"))
        self.updatePlaylistsButton.setText(_translate("MainWindow", "Reload"))
        self.createPlaylistButton.setText(_translate("MainWindow", "Create new playlist"))
        self.overwriteRadioButton.setText(_translate("MainWindow", "Overwrite"))
        self.appendRadioButton.setText(_translate("MainWindow", "Append"))
        self.recommendationsLimitLabel.setText(_translate("MainWindow", "Recommendations limit:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preferencesTab), _translate("MainWindow", "Preferences"))
        self.seedsPoolBox.setTitle(_translate("MainWindow", "Seeds pool"))
        self.acousticnessLabel.setText(_translate("MainWindow", "Acousticness"))
        self.acousticnessMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.acousticnessTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.acousticnessMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.danceabilityLabel.setText(_translate("MainWindow", "Danceability"))
        self.danceabilityMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.danceabilityTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.danceabilityMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.durationLabel.setText(_translate("MainWindow", "Duration"))
        self.durationMinLabel.setText(_translate("MainWindow", "min"))
        self.durationMin.setDisplayFormat(_translate("MainWindow", "mm:ss"))
        self.durationTargetLabel.setText(_translate("MainWindow", "target"))
        self.durationTarget.setDisplayFormat(_translate("MainWindow", "mm:ss"))
        self.durationMaxLabel.setText(_translate("MainWindow", "max"))
        self.durationMax.setDisplayFormat(_translate("MainWindow", "mm:ss"))
        self.energyLabel.setText(_translate("MainWindow", "Energy"))
        self.energyMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.energyTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.energyMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.instrumentalnessLabel.setText(_translate("MainWindow", "Instrumentalness"))
        self.instrumentalnessMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.instrumentalnessTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.instrumentalnessMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.keyLabel.setText(_translate("MainWindow", "Key"))
        self.keyMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.keyTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.keyMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.livenessLabel.setText(_translate("MainWindow", "Liveness"))
        self.livenessMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.livenessTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.livenessMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.loudnessLabel.setText(_translate("MainWindow", "Loudness"))
        self.loudnessMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.loudnessTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.loudnessMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.modeLabel.setText(_translate("MainWindow", "Mode"))
        self.modeMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.modeTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.modeMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.popularityLabel.setText(_translate("MainWindow", "Popularity"))
        self.popularityMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.popularityTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.popularityMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.speechinessLabel.setText(_translate("MainWindow", "Speechiness"))
        self.speechinessMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.speechinessTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.speechinessMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.tempoLabel.setText(_translate("MainWindow", "Tempo"))
        self.tempoMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.tempoTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.tempoMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.timeSignatureLabel.setText(_translate("MainWindow", "Time signature"))
        self.valenceLabel.setText(_translate("MainWindow", "Valence"))
        self.valenceMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.valenceTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.valenceMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.timeSignatureMinLabel.setText(_translate("MainWindow", "min: 0"))
        self.timeSignatureTargetLabel.setText(_translate("MainWindow", "target: 0"))
        self.timeSignatureMaxLabel.setText(_translate("MainWindow", "max: 0"))
        self.generateButton.setText(_translate("MainWindow", "Generate recommendations"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.recommendationsTab), _translate("MainWindow", "Recommendations"))
        self.analysisButton.setText(_translate("MainWindow", "Get analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))

    def functionality(self):
        self.authorizeButton.clicked.connect(self.authorize)
        self.updatePlaylistsButton.clicked.connect(self.reload_playlists_list)
        self.generateButton.clicked.connect(self.get_recommendations)
        self.analysisButton.clicked.connect(self.track_analysis)

    def after_init(self):
        self.sliderss_init()
        self.show_authorization_status()
        self.appendRadioButton.setChecked(True)

    def sliderss_triggers(self):
        self.acousticnessMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.acousticnessMax.value(), self.acousticnessMaxLabel,
                                                 [self.acousticnessTarget, self.acousticnessMin]))
        self.acousticnessTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.acousticnessTarget.value(), self.acousticnessTargetLabel,
                                                    self.acousticnessMin, self.acousticnessMax))
        self.acousticnessMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.acousticnessMin.value(), self.acousticnessMinLabel,
                                                 [self.acousticnessTarget, self.acousticnessMax]))
        self.danceabilityMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.danceabilityMax.value(), self.danceabilityMaxLabel,
                                                 [self.danceabilityTarget, self.danceabilityMin]))
        self.danceabilityTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.danceabilityTarget.value(), self.danceabilityTargetLabel,
                                                    self.danceabilityMin, self.danceabilityMax))
        self.danceabilityMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.danceabilityMin.value(), self.danceabilityMinLabel,
                                                 [self.danceabilityTarget, self.danceabilityMax]))
        self.energyMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.energyMax.value(), self.energyMaxLabel,
                                                 [self.energyTarget, self.energyMin]))
        self.energyTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.energyTarget.value(), self.energyTargetLabel,
                                                    self.energyMin, self.energyMax))
        self.energyMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.energyMin.value(), self.energyMinLabel,
                                                 [self.energyTarget, self.energyMax]))
        self.instrumentalnessMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.instrumentalnessMax.value(), self.instrumentalnessMaxLabel,
                                                 [self.instrumentalnessTarget, self.instrumentalnessMin]))
        self.instrumentalnessTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.instrumentalnessTarget.value(),
                                                    self.instrumentalnessTargetLabel,
                                                    self.instrumentalnessMin, self.instrumentalnessMax))
        self.instrumentalnessMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.instrumentalnessMin.value(), self.instrumentalnessMinLabel,
                                                 [self.instrumentalnessTarget, self.instrumentalnessMax]))
        self.keyMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.keyMax.value(), self.keyMaxLabel,
                                                 [self.keyTarget, self.keyMin]))
        self.keyTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.keyTarget.value(), self.keyTargetLabel,
                                                    self.keyMin, self.keyMax))
        self.keyMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.keyMin.value(), self.keyMinLabel,
                                                 [self.keyTarget, self.keyMax]))
        self.livenessMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.livenessMax.value(), self.livenessMaxLabel,
                                                 [self.livenessTarget, self.livenessMin]))
        self.livenessTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.livenessTarget.value(), self.livenessTargetLabel,
                                                    self.livenessMin, self.livenessMax))
        self.livenessMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.livenessMin.value(), self.livenessMinLabel,
                                                 [self.livenessTarget, self.livenessMax]))
        self.loudnessMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.loudnessMax.value(), self.loudnessMaxLabel,
                                                 [self.loudnessTarget, self.loudnessMin]))
        self.loudnessTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.loudnessTarget.value(), self.loudnessTargetLabel,
                                                    self.loudnessMin, self.loudnessMax))
        self.loudnessMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.loudnessMin.value(), self.loudnessMinLabel,
                                                 [self.loudnessTarget, self.loudnessMax]))
        self.modeMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.modeMax.value(), self.modeMaxLabel,
                                                 [self.modeTarget, self.modeMin]))
        self.modeTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.modeTarget.value(), self.modeTargetLabel,
                                                    self.modeMin, self.modeMax))
        self.modeMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.modeMin.value(), self.modeMinLabel,
                                                 [self.modeTarget, self.modeMax]))
        self.popularityMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.popularityMax.value(), self.popularityMaxLabel,
                                                 [self.popularityTarget, self.popularityMin]))
        self.popularityTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.popularityTarget.value(), self.popularityTargetLabel,
                                                    self.popularityMin, self.popularityMax))
        self.popularityMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.popularityMin.value(), self.popularityMinLabel,
                                                 [self.popularityTarget, self.popularityMax]))
        self.speechinessMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.speechinessMax.value(), self.speechinessMaxLabel,
                                                 [self.speechinessTarget, self.speechinessMin]))
        self.speechinessTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.speechinessTarget.value(), self.speechinessTargetLabel,
                                                    self.speechinessMin, self.speechinessMax))
        self.speechinessMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.speechinessMin.value(), self.speechinessMinLabel,
                                                 [self.speechinessTarget, self.speechinessMax]))
        self.tempoMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.tempoMax.value(), self.tempoMaxLabel,
                                                 [self.tempoTarget, self.tempoMin]))
        self.tempoTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.tempoTarget.value(), self.tempoTargetLabel,
                                                    self.tempoMin, self.tempoMax))
        self.tempoMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.tempoMin.value(), self.tempoMinLabel,
                                                 [self.tempoTarget, self.tempoMax]))
        self.timeSignatureMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.timeSignatureMax.value(), self.timeSignatureMaxLabel,
                                                 [self.timeSignatureTarget, self.timeSignatureMin]))
        self.timeSignatureTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.timeSignatureTarget.value(), self.timeSignatureTargetLabel,
                                                    self.timeSignatureMin, self.timeSignatureMax))
        self.timeSignatureMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.timeSignatureMin.value(), self.timeSignatureMinLabel,
                                                 [self.timeSignatureTarget, self.timeSignatureMax]))
        self.valenceMax.valueChanged.connect(
            lambda: self.changed_max_param_value(self.valenceMax.value(), self.valenceMaxLabel,
                                                 [self.valenceTarget, self.valenceMin]))
        self.valenceTarget.valueChanged.connect(
            lambda: self.changed_target_param_value(self.valenceTarget.value(), self.valenceTargetLabel,
                                                    self.valenceMin, self.valenceMax))
        self.valenceMin.valueChanged.connect(
            lambda: self.changed_min_param_value(self.valenceMin.value(), self.valenceMinLabel,
                                                 [self.valenceTarget, self.valenceMax]))

    def sliderss_init(self):
        self.changed_max_param_value(self.acousticnessMax.maximum(), self.acousticnessMaxLabel, None)
        self.changed_target_param_value(self.acousticnessTarget.value(), self.acousticnessTargetLabel,
                                        self.acousticnessMin, self.acousticnessMax)
        self.changed_min_param_value(self.acousticnessMin.minimum(), self.acousticnessMinLabel, None)
        self.changed_max_param_value(self.danceabilityMax.maximum(), self.danceabilityMaxLabel, None)
        self.changed_target_param_value(self.danceabilityTarget.value(), self.danceabilityTargetLabel,
                                        self.danceabilityMin, self.danceabilityMax)
        self.changed_min_param_value(self.danceabilityMin.minimum(), self.danceabilityMinLabel, None)
        self.changed_max_param_value(self.energyMax.maximum(), self.energyMaxLabel, None)
        self.changed_target_param_value(self.energyTarget.value(), self.energyTargetLabel,
                                        self.energyMin, self.energyMax)
        self.changed_min_param_value(self.energyMin.minimum(), self.energyMinLabel, None)
        self.changed_max_param_value(self.instrumentalnessMax.maximum(), self.instrumentalnessMaxLabel, None)
        self.changed_target_param_value(self.instrumentalnessTarget.value(), self.instrumentalnessTargetLabel,
                                        self.instrumentalnessMin, self.instrumentalnessMax)
        self.changed_min_param_value(self.instrumentalnessMin.minimum(), self.instrumentalnessMinLabel, None)
        self.changed_max_param_value(self.keyMax.maximum(), self.keyMaxLabel, None)
        self.changed_target_param_value(self.keyTarget.value(), self.keyTargetLabel,
                                        self.keyMin, self.keyMax)
        self.changed_min_param_value(self.keyMin.minimum(), self.keyMinLabel, None)
        self.changed_max_param_value(self.livenessMax.maximum(), self.livenessMaxLabel, None)
        self.changed_target_param_value(self.livenessTarget.value(), self.livenessTargetLabel,
                                        self.livenessMin, self.livenessMax)
        self.changed_min_param_value(self.livenessMin.minimum(), self.livenessMinLabel, None)
        self.changed_max_param_value(self.loudnessMax.maximum(), self.loudnessMaxLabel, None)
        self.changed_target_param_value(self.loudnessTarget.value(), self.loudnessTargetLabel,
                                        self.loudnessMin, self.loudnessMax)
        self.changed_min_param_value(self.loudnessMin.minimum(), self.loudnessMinLabel, None)
        self.changed_max_param_value(self.modeMax.maximum(), self.modeMaxLabel, None)
        self.changed_target_param_value(self.modeTarget.value(), self.modeTargetLabel,
                                        self.modeMin, self.modeMax)
        self.changed_min_param_value(self.modeMin.minimum(), self.modeMinLabel, None)
        self.changed_max_param_value(self.popularityMax.maximum(), self.popularityMaxLabel, None)
        self.changed_target_param_value(self.popularityTarget.value(), self.popularityTargetLabel,
                                        self.popularityMin, self.popularityMax)
        self.changed_min_param_value(self.popularityMin.minimum(), self.popularityMinLabel, None)
        self.changed_max_param_value(self.speechinessMax.maximum(), self.speechinessMaxLabel, None)
        self.changed_target_param_value(self.speechinessTarget.value(), self.speechinessTargetLabel,
                                        self.speechinessMin, self.speechinessMax)
        self.changed_min_param_value(self.speechinessMin.minimum(), self.speechinessMinLabel, None)
        self.changed_max_param_value(self.tempoMax.maximum(), self.tempoMaxLabel, None)
        self.changed_target_param_value(self.tempoTarget.value(), self.tempoTargetLabel,
                                        self.tempoMin, self.tempoMax)
        self.changed_min_param_value(self.tempoMin.minimum(), self.tempoMinLabel, None)
        self.changed_max_param_value(self.timeSignatureMax.maximum(), self.timeSignatureMaxLabel, None)
        self.changed_target_param_value(self.timeSignatureTarget.value(), self.timeSignatureTargetLabel,
                                        self.timeSignatureMin, self.timeSignatureMax)
        self.changed_min_param_value(self.timeSignatureMin.minimum(), self.timeSignatureMinLabel, None)
        self.changed_max_param_value(self.valenceMax.maximum(), self.valenceMaxLabel, None)
        self.changed_target_param_value(self.valenceTarget.value(), self.valenceTargetLabel,
                                        self.valenceMin, self.valenceMax)
        self.changed_min_param_value(self.valenceMin.minimum(), self.valenceMinLabel, None)

        self.sliderss_triggers()

    def changed_min_param_value(self, newValue, valueTargetLabel, restrictionTargets: Union[object, list]):
        valueTargetLabel.setText(f"min: {newValue}")
        if type(restrictionTargets) != list:
            restrictionTargets = [restrictionTargets]
        for target in restrictionTargets:
            if target is not None:
                target.setMinimum(newValue)

    def changed_max_param_value(self, newValue, valueTargetLabel, restrictionTargets: Union[object, list]):
        valueTargetLabel.setText(f"max: {newValue}")
        if type(restrictionTargets) != list:
            restrictionTargets = [restrictionTargets]
        for target in restrictionTargets:
            if target is not None:
                target.setMaximum(newValue)


    def changed_target_param_value(self, newValue, valueTargetLabel, minRestictionTarget, maxRestrictionTarget):
        valueTargetLabel.setText(f"target: {newValue}")
        if minRestictionTarget is not None:
            minRestictionTarget.setMaximum(newValue)
        if maxRestrictionTarget is not None:
            maxRestrictionTarget.setMinimum(newValue)

    def show_authorization_status(self):
        self.api.prepare_token()
        if self.api.valid_token:
            self.authorizationStateLabel.setText("Authorized")
            self.authorizeButton.setEnabled(False)

    def authorize(self):
        oauth_master = SpotifyOAuth(self.show_authorization_status)
        oauth_master.init_authorization()

    def reload_playlists_list(self):
        playlists = self.api.get_playlists_list()
        self.get_user_id()
        self.own_playlists = []
        if playlists is None:
            print("[Ui_MainWindow reload_playlists_list] Error getting playlists list")
        else:
            self.playlistsListWidget.clear()
            for playlist in playlists:
                if playlist["owner"]["id"] == self.user_id:
                    self.own_playlists += [playlist]
                    self.playlistsListWidget.addItem(playlist["name"])

    def get_user_id(self):
        if self.user_id is None or len(self.user_id) == 0:
            self.configurator.read_config()
            self.user_id = self.configurator.config["user_info"]["user_id"]
            if len(self.user_id) == 0:
                self.api.get_user_info()
                self.get_user_id()

    def get_recommendations(self):
        playlists_index = self.playlistsListWidget.currentRow()
        seeds = self.seedsPool.toPlainText().split("\n")
        if playlists_index == -1 or len(seeds[0]) == 0 or len(seeds) > 5:
            return
        target_playlist_id = self.own_playlists[playlists_index]["id"]

        acousticness = self.prepare_param_value(self.acousticnessMin, self.acousticnessTarget,
                                                self.acousticnessMax, self.acousticnessEnabled, multiplier=0.01)
        danceability = self.prepare_param_value(self.danceabilityMin, self.danceabilityTarget,
                                                self.danceabilityMax, self.danceabilityEnabled, multiplier=0.01)

        duration_ms_min_min = -self.durationMin.minimumTime().msecsTo(QtCore.QTime(0, 0, 0))
        duration_ms_min = -self.durationMin.time().msecsTo(QtCore.QTime(0, 0, 0))
        duration_ms_max_max = -self.durationMax.maximumTime().msecsTo(QtCore.QTime(0, 0, 0))
        duration_ms_max = -self.durationMax.time().msecsTo(QtCore.QTime(0, 0, 0))

        duration_ms = ([duration_ms_min, None][int(duration_ms_min == duration_ms_min_min)],
                       [-self.durationTarget.time().msecsTo(QtCore.QTime(0, 0, 0)), None][int(not self.durationEnabled.isChecked())],
                       [duration_ms_max, None][int(duration_ms_max == duration_ms_max_max)]
        )
        duration_ms = [duration_ms, None][int(duration_ms == (None, None, None))]

        energy = self.prepare_param_value(self.energyMin, self.energyTarget,
                                          self.energyMax, self.energyEnabled, multiplier=0.01)
        instrumentalness = self.prepare_param_value(self.instrumentalnessMin, self.instrumentalnessTarget,
                                                    self.instrumentalnessMax, self.instrumentalnessEnabled,
                                                    multiplier=0.01)
        key = self.prepare_param_value(self.keyMin, self.keyTarget, self.keyMax, self.keyEnabled)
        liveness = self.prepare_param_value(self.livenessMin, self.livenessTarget,
                                            self.livenessMax, self.livenessEnabled, multiplier=0.01)
        loudness = self.prepare_param_value(self.loudnessMin, self.loudnessTarget,
                                            self.loudnessMax, self.loudnessEnabled)
        mode = self.prepare_param_value(self.modeMin, self.modeTarget, self.modeMax, self.modeEnabled)
        popularity = self.prepare_param_value(self.popularityMin, self.popularityTarget,
                                              self.popularityMax, self.popularityEnabled)
        speechiness = self.prepare_param_value(self.speechinessMin, self.speechinessTarget,
                                               self.speechinessMax, self.speechinessEnabled, multiplier=0.01)
        tempo = self.prepare_param_value(self.tempoMin, self.tempoTarget, self.tempoMax, self.tempoEnabled)
        time_signature = self.prepare_param_value(self.timeSignatureMin, self.timeSignatureTarget,
                                                  self.timeSignatureMax, self.timeSignatureEnabled)
        valence = self.prepare_param_value(self.valenceMin, self.valenceTarget,
                                           self.valenceMax, self.valenceEnabled, multiplier=0.01)

        recommendations = self.api.get_recommendations(seeds, limit=self.recommendationsLimitSpinBox.value(),
                                                       acousticness=acousticness, danceability=danceability,
                                                       duration_ms=duration_ms, energy=energy,
                                                       instrumentalness=instrumentalness, key=key, liveness=liveness,
                                                       loudness=loudness, mode=mode, popularity=popularity,
                                                       speechiness=speechiness, tempo=tempo,
                                                       time_signature=time_signature, valence=valence)
        recommended_track_uris = list()
        for track in recommendations["tracks"]:
            recommended_track_uris += [track["uri"]]

        if self.appendRadioButton.isChecked():
            self.api.append_tracks_to_playlist(target_playlist_id, recommended_track_uris)
        else:
            self.api.overwrite_tracks_in_playlist(target_playlist_id, recommended_track_uris)

    def prepare_param_value(self, paramMin, paramTarget, paramMax, paramEnabled, multiplier=1.0):
        if multiplier == int(multiplier):
            multiplier = int(multiplier)
        param = (
            [paramMin.value()*multiplier, None][int(paramMin.value() == paramMin.minimum())],
            [paramTarget.value()*multiplier, None][int(not paramEnabled.isChecked())],
            [paramMax.value()*multiplier, None][int(paramMax.value() == paramMax.maximum())]
        )
        param = [param, None][int(param == (None, None, None))]
        return param

    def track_analysis(self):
        url = self.analysisUrlEdit.text()
        q = re.search(r"http[s]*://open.spotify.com/track/([\dA-Za-z]+)", url)
        if q is None:
            return
        track_id = q[1]
        audio_features = self.api.get_track_audio_features(track_id)
        s = json.dumps(audio_features, indent='       ')
        self.analysisResultTextBrowser.setText(s)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.after_init()
    sys.exit(app.exec_())
