# MGEAR is under the terms of the MIT License

# Copyright (c) 2016 Jeremie Passerin, Miquel Campos

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author:     Jeremie Passerin      geerem@hotmail.com  www.jeremiepasserin.com
# Author:     Miquel Campos         hello@miquel-campos.com  www.miquel-campos.com
# Date:       2016 / 10 / 10

import mgear.maya.pyqt as gqt
QtGui, QtCore, QtWidgets, wrapInstance = gqt.qt_import()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(269, 559)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.softness_label = QtWidgets.QLabel(self.groupBox)
        self.softness_label.setObjectName("softness_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.softness_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.softness_slider = QtWidgets.QSlider(self.groupBox)
        self.softness_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.softness_slider.setMaximum(100)
        self.softness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.softness_slider.setObjectName("softness_slider")
        self.horizontalLayout_3.addWidget(self.softness_slider)
        self.softness_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.softness_spinBox.setMaximum(100)
        self.softness_spinBox.setObjectName("softness_spinBox")
        self.horizontalLayout_3.addWidget(self.softness_spinBox)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.maxStretch_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_label.sizePolicy().hasHeightForWidth())
        self.maxStretch_label.setSizePolicy(sizePolicy)
        self.maxStretch_label.setObjectName("maxStretch_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.maxStretch_label)
        self.maxStretch_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_spinBox.sizePolicy().hasHeightForWidth())
        self.maxStretch_spinBox.setSizePolicy(sizePolicy)
        self.maxStretch_spinBox.setMinimum(1.0)
        self.maxStretch_spinBox.setSingleStep(0.1)
        self.maxStretch_spinBox.setProperty("value", 1.5)
        self.maxStretch_spinBox.setObjectName("maxStretch_spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.maxStretch_spinBox)
        self.maxSquash_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxSquash_label.sizePolicy().hasHeightForWidth())
        self.maxSquash_label.setSizePolicy(sizePolicy)
        self.maxSquash_label.setObjectName("maxSquash_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maxSquash_label)
        self.maxSquash_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxSquash_spinBox.sizePolicy().hasHeightForWidth())
        self.maxSquash_spinBox.setSizePolicy(sizePolicy)
        self.maxSquash_spinBox.setMinimum(0.1)
        self.maxSquash_spinBox.setMaximum(1.0)
        self.maxSquash_spinBox.setSingleStep(0.1)
        self.maxSquash_spinBox.setProperty("value", 0.5)
        self.maxSquash_spinBox.setObjectName("maxSquash_spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxSquash_spinBox)
        self.divisions_label = QtWidgets.QLabel(self.groupBox)
        self.divisions_label.setObjectName("divisions_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.divisions_label)
        self.division_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.division_spinBox.setMinimum(1)
        self.division_spinBox.setProperty("value", 2)
        self.division_spinBox.setObjectName("division_spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.division_spinBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.squashStretchProfile_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.squashStretchProfile_pushButton.setObjectName("squashStretchProfile_pushButton")
        self.verticalLayout.addWidget(self.squashStretchProfile_pushButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.ikRefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.ikRefArray_groupBox.setObjectName("ikRefArray_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ikRefArray_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ikRefArray_horizontalLayout = QtWidgets.QHBoxLayout()
        self.ikRefArray_horizontalLayout.setObjectName("ikRefArray_horizontalLayout")
        self.ikRefArray_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.ikRefArray_verticalLayout_1.setObjectName("ikRefArray_verticalLayout_1")
        self.ikRefArray_listWidget = QtWidgets.QListWidget(self.ikRefArray_groupBox)
        self.ikRefArray_listWidget.setDragDropOverwriteMode(True)
        self.ikRefArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ikRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.ikRefArray_listWidget.setAlternatingRowColors(True)
        self.ikRefArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ikRefArray_listWidget.setSelectionRectVisible(False)
        self.ikRefArray_listWidget.setObjectName("ikRefArray_listWidget")
        self.ikRefArray_verticalLayout_1.addWidget(self.ikRefArray_listWidget)
        self.ikRefArray_copyRef_pushButton = QtWidgets.QPushButton(self.ikRefArray_groupBox)
        self.ikRefArray_copyRef_pushButton.setObjectName("ikRefArray_copyRef_pushButton")
        self.ikRefArray_verticalLayout_1.addWidget(self.ikRefArray_copyRef_pushButton)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_1)
        self.ikRefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.ikRefArray_verticalLayout_2.setObjectName("ikRefArray_verticalLayout_2")
        self.ikRefArrayAdd_pushButton = QtWidgets.QPushButton(self.ikRefArray_groupBox)
        self.ikRefArrayAdd_pushButton.setObjectName("ikRefArrayAdd_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayAdd_pushButton)
        self.ikRefArrayRemove_pushButton = QtWidgets.QPushButton(self.ikRefArray_groupBox)
        self.ikRefArrayRemove_pushButton.setObjectName("ikRefArrayRemove_pushButton")
        self.ikRefArray_verticalLayout_2.addWidget(self.ikRefArrayRemove_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ikRefArray_verticalLayout_2.addItem(spacerItem)
        self.ikRefArray_horizontalLayout.addLayout(self.ikRefArray_verticalLayout_2)
        self.gridLayout_3.addLayout(self.ikRefArray_horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.ikRefArray_groupBox, 1, 0, 1, 1)
        self.upvRefArray_groupBox = QtWidgets.QGroupBox(Form)
        self.upvRefArray_groupBox.setObjectName("upvRefArray_groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.upvRefArray_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.upvRefArray_horizontalLayout = QtWidgets.QHBoxLayout()
        self.upvRefArray_horizontalLayout.setObjectName("upvRefArray_horizontalLayout")
        self.upvRefArray_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.upvRefArray_verticalLayout_1.setObjectName("upvRefArray_verticalLayout_1")
        self.headRefArray_listWidget = QtWidgets.QListWidget(self.upvRefArray_groupBox)
        self.headRefArray_listWidget.setDragDropOverwriteMode(True)
        self.headRefArray_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.headRefArray_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.headRefArray_listWidget.setAlternatingRowColors(True)
        self.headRefArray_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.headRefArray_listWidget.setSelectionRectVisible(False)
        self.headRefArray_listWidget.setObjectName("headRefArray_listWidget")
        self.upvRefArray_verticalLayout_1.addWidget(self.headRefArray_listWidget)
        self.headRefArray_copyRef_pushButton = QtWidgets.QPushButton(self.upvRefArray_groupBox)
        self.headRefArray_copyRef_pushButton.setObjectName("headRefArray_copyRef_pushButton")
        self.upvRefArray_verticalLayout_1.addWidget(self.headRefArray_copyRef_pushButton)
        self.upvRefArray_horizontalLayout.addLayout(self.upvRefArray_verticalLayout_1)
        self.upvRefArray_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.upvRefArray_verticalLayout_2.setObjectName("upvRefArray_verticalLayout_2")
        self.headRefArrayAdd_pushButton = QtWidgets.QPushButton(self.upvRefArray_groupBox)
        self.headRefArrayAdd_pushButton.setObjectName("headRefArrayAdd_pushButton")
        self.upvRefArray_verticalLayout_2.addWidget(self.headRefArrayAdd_pushButton)
        self.headRefArrayRemove_pushButton = QtWidgets.QPushButton(self.upvRefArray_groupBox)
        self.headRefArrayRemove_pushButton.setObjectName("headRefArrayRemove_pushButton")
        self.upvRefArray_verticalLayout_2.addWidget(self.headRefArrayRemove_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.upvRefArray_verticalLayout_2.addItem(spacerItem1)
        self.upvRefArray_horizontalLayout.addLayout(self.upvRefArray_verticalLayout_2)
        self.gridLayout_4.addLayout(self.upvRefArray_horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.upvRefArray_groupBox, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.softness_slider, QtCore.SIGNAL("sliderMoved(int)"), self.softness_spinBox.setValue)
        QtCore.QObject.connect(self.softness_spinBox, QtCore.SIGNAL("valueChanged(int)"), self.softness_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.softness_label.setText(gqt.fakeTranslate("Form", "Softness", None, -1))
        self.maxStretch_label.setText(gqt.fakeTranslate("Form", "Max Stretch", None, -1))
        self.maxSquash_label.setText(gqt.fakeTranslate("Form", "Max Squash", None, -1))
        self.divisions_label.setText(gqt.fakeTranslate("Form", "Divisions", None, -1))
        self.squashStretchProfile_pushButton.setText(gqt.fakeTranslate("Form", "Squash and Stretch Profile", None, -1))
        self.ikRefArray_groupBox.setTitle(gqt.fakeTranslate("Form", "IK Reference Array", None, -1))
        self.ikRefArray_copyRef_pushButton.setText(gqt.fakeTranslate("Form", "Copy from Head Ref", None, -1))
        self.ikRefArrayAdd_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.ikRefArrayRemove_pushButton.setText(gqt.fakeTranslate("Form", ">>", None, -1))
        self.upvRefArray_groupBox.setTitle(gqt.fakeTranslate("Form", "Head Reference Array", None, -1))
        self.headRefArray_copyRef_pushButton.setText(gqt.fakeTranslate("Form", "Copy from IK Ref", None, -1))
        self.headRefArrayAdd_pushButton.setText(gqt.fakeTranslate("Form", "<<", None, -1))
        self.headRefArrayRemove_pushButton.setText(gqt.fakeTranslate("Form", ">>", None, -1))

