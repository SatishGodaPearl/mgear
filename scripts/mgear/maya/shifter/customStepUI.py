import mgear.maya.pyqt as gqt
from mgear.vendor.Qt import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 593)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.preCustomStep_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.preCustomStep_checkBox.setObjectName("preCustomStep_checkBox")
        self.verticalLayout.addWidget(self.preCustomStep_checkBox)
        self.preCustomStep_horizontalLayout = QtWidgets.QHBoxLayout()
        self.preCustomStep_horizontalLayout.setObjectName(
            "preCustomStep_horizontalLayout")
        self.preCustomStep_verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.preCustomStep_verticalLayout_1.setObjectName(
            "preCustomStep_verticalLayout_1")
        self.preCustomStep_listWidget = QtWidgets.QListWidget(self.groupBox)
        self.preCustomStep_listWidget.setDragDropOverwriteMode(True)
        self.preCustomStep_listWidget.setDragDropMode(
            QtWidgets.QAbstractItemView.InternalMove)
        self.preCustomStep_listWidget.setDefaultDropAction(
            QtCore.Qt.MoveAction)
        self.preCustomStep_listWidget.setAlternatingRowColors(True)
        self.preCustomStep_listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.preCustomStep_listWidget.setProperty("isWrapping", False)
        self.preCustomStep_listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.preCustomStep_listWidget.setObjectName("preCustomStep_listWidget")
        self.preCustomStep_verticalLayout_1.addWidget(
            self.preCustomStep_listWidget)
        self.preCustomStep_horizontalLayout.addLayout(
            self.preCustomStep_verticalLayout_1)
        self.preCustomStep_verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.preCustomStep_verticalLayout_2.setObjectName(
            "preCustomStep_verticalLayout_2")
        self.preCustomStepAdd_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.preCustomStepAdd_pushButton.setObjectName(
            "preCustomStepAdd_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepAdd_pushButton)
        self.preCustomStepNew_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.preCustomStepNew_pushButton.setObjectName(
            "preCustomStepNew_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepNew_pushButton)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)
        self.preCustomStep_verticalLayout_2.addItem(spacerItem)
        self.preCustomStepDuplicate_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.preCustomStepDuplicate_pushButton.setObjectName(
            "preCustomStepDuplicate_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepDuplicate_pushButton)
        self.preCustomStepRemove_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.preCustomStepRemove_pushButton.setObjectName(
            "preCustomStepRemove_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepRemove_pushButton)
        self.preCustomStepRun_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.preCustomStepRun_pushButton.setObjectName(
            "preCustomStepRun_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepRun_pushButton)
        self.preCustomStepEdit_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.preCustomStepEdit_pushButton.setObjectName(
            "preCustomStepEdit_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepEdit_pushButton)
        self.preCustomStepExport_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.preCustomStepExport_pushButton.setObjectName(
            "preCustomStepExport_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepExport_pushButton)
        self.preCustomStepImport_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.preCustomStepImport_pushButton.setObjectName(
            "preCustomStepImport_pushButton")
        self.preCustomStep_verticalLayout_2.addWidget(
            self.preCustomStepImport_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)
        self.preCustomStep_verticalLayout_2.addItem(spacerItem1)
        self.preCustomStep_horizontalLayout.addLayout(
            self.preCustomStep_verticalLayout_2)
        self.verticalLayout.addLayout(self.preCustomStep_horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.postCustomStep_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.postCustomStep_checkBox.setObjectName("postCustomStep_checkBox")
        self.verticalLayout_2.addWidget(self.postCustomStep_checkBox)
        self.preCustomStep_horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.preCustomStep_horizontalLayout_2.setObjectName(
            "preCustomStep_horizontalLayout_2")
        self.preCustomStep_verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.preCustomStep_verticalLayout_3.setObjectName(
            "preCustomStep_verticalLayout_3")
        self.postCustomStep_listWidget = QtWidgets.QListWidget(self.groupBox)
        self.postCustomStep_listWidget.setDragDropOverwriteMode(True)
        self.postCustomStep_listWidget.setDragDropMode(
            QtWidgets.QAbstractItemView.InternalMove)
        self.postCustomStep_listWidget.setDefaultDropAction(
            QtCore.Qt.MoveAction)
        self.postCustomStep_listWidget.setAlternatingRowColors(True)
        self.postCustomStep_listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection)
        self.postCustomStep_listWidget.setViewMode(
            QtWidgets.QListView.ListMode)
        self.postCustomStep_listWidget.setWordWrap(False)
        self.postCustomStep_listWidget.setSelectionRectVisible(False)
        self.postCustomStep_listWidget.setObjectName(
            "postCustomStep_listWidget")
        self.preCustomStep_verticalLayout_3.addWidget(
            self.postCustomStep_listWidget)
        self.preCustomStep_horizontalLayout_2.addLayout(
            self.preCustomStep_verticalLayout_3)
        self.preCustomStep_verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.preCustomStep_verticalLayout_4.setObjectName(
            "preCustomStep_verticalLayout_4")
        self.postCustomStepAdd_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepAdd_pushButton.setObjectName(
            "postCustomStepAdd_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepAdd_pushButton)
        self.postCustomStepNew_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepNew_pushButton.setObjectName(
            "postCustomStepNew_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepNew_pushButton)
        self.postCustomStepDuplicate_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepDuplicate_pushButton.setObjectName(
            "postCustomStepDuplicate_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepDuplicate_pushButton)
        self.postCustomStepRemove_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepRemove_pushButton.setObjectName(
            "postCustomStepRemove_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepRemove_pushButton)
        self.postCustomStepRun_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepRun_pushButton.setObjectName(
            "postCustomStepRun_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepRun_pushButton)
        self.postCustomStepEdit_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepEdit_pushButton.setObjectName(
            "postCustomStepEdit_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepEdit_pushButton)
        self.postCustomStepExport_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepExport_pushButton.setObjectName(
            "postCustomStepExport_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepExport_pushButton)
        self.postCustomStepImport_pushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.postCustomStepImport_pushButton.setObjectName(
            "postCustomStepImport_pushButton")
        self.preCustomStep_verticalLayout_4.addWidget(
            self.postCustomStepImport_pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding)
        self.preCustomStep_verticalLayout_4.addItem(spacerItem2)
        self.preCustomStep_horizontalLayout_2.addLayout(
            self.preCustomStep_verticalLayout_4)
        self.verticalLayout_2.addLayout(self.preCustomStep_horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.groupBox.setTitle(gqt.fakeTranslate(
            "Form", "Custom Steps", None, -1))
        self.preCustomStep_checkBox.setText(
            gqt.fakeTranslate("Form", "Pre Custom Step", None, -1))
        self.preCustomStepAdd_pushButton.setText(
            gqt.fakeTranslate("Form", "Add", None, -1))
        self.preCustomStepNew_pushButton.setText(
            gqt.fakeTranslate("Form", "New", None, -1))
        self.preCustomStepDuplicate_pushButton.setText(
            gqt.fakeTranslate("Form", "Duplicate", None, -1))
        self.preCustomStepRemove_pushButton.setText(
            gqt.fakeTranslate("Form", "Remove", None, -1))
        self.preCustomStepRun_pushButton.setText(
            gqt.fakeTranslate("Form", "Run Sel.", None, -1))
        self.preCustomStepEdit_pushButton.setText(
            gqt.fakeTranslate("Form", "Edit", None, -1))
        self.preCustomStepExport_pushButton.setText(
            gqt.fakeTranslate("Form", "Export", None, -1))
        self.preCustomStepImport_pushButton.setText(
            gqt.fakeTranslate("Form", "Import", None, -1))
        self.postCustomStep_checkBox.setText(
            gqt.fakeTranslate("Form", "Post  Custom Step", None, -1))
        self.postCustomStepAdd_pushButton.setText(
            gqt.fakeTranslate("Form", "Add", None, -1))
        self.postCustomStepNew_pushButton.setText(
            gqt.fakeTranslate("Form", "New", None, -1))
        self.postCustomStepDuplicate_pushButton.setText(
            gqt.fakeTranslate("Form", "Duplicate", None, -1))
        self.postCustomStepRemove_pushButton.setText(
            gqt.fakeTranslate("Form", "Remove", None, -1))
        self.postCustomStepRun_pushButton.setText(
            gqt.fakeTranslate("Form", "Run Sel.", None, -1))
        self.postCustomStepEdit_pushButton.setText(
            gqt.fakeTranslate("Form", "Edit", None, -1))
        self.postCustomStepExport_pushButton.setText(
            gqt.fakeTranslate("Form", "Export", None, -1))
        self.postCustomStepImport_pushButton.setText(
            gqt.fakeTranslate("Form", "Import", None, -1))
