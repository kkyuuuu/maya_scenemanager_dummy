# -*- coding: utf-8 -*-

import sys
import maya.OpenMayaUI
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from stylesheets import *
from font import *
from shiboken2 import wrapInstance

def maya_widget():
	maya_main_window_ptr = maya.OpenMayaUI.MQtUtil.mainWindow()
	if sys.version_info[0] > 2:
		return wrapInstance(int(maya_main_window_ptr), QWidget)
	else:
		return wrapInstance(long(maya_main_window_ptr), QWidget)

def clear_layout(layout):
	while layout.count():
		item = layout.takeAt(0)
		widget = item.widget()
		if widget is not None:
			widget.deleteLater()
		else:
			clear_layout(item.layout())

class TabWidget(QTabWidget):

	def __init__(self, labels, triangular=False, document=False, parent=None):
		super(TabWidget, self).__init__(parent)
		self.setFont(font_tab())
		self.setStyleSheet(tabwidget)
		self._labels = labels
		self._triangular = triangular
		self._document = document
		self._layouts = []
		self.init()

	@property
	def layouts(self):
		return self._layouts

	def init(self):
		if self._triangular:
			self.setTabShape(QTabWidget.Triangular)

		if self._document:
			self.setDocumentMode(True)

		for label in self._labels:
			widget = QWidget()
			layout = QVBoxLayout()
			layout.setContentsMargins(3, 3, 3, 3)
			layout.setSpacing(0)
			widget.setLayout(layout)
			self._layouts.append(layout)
			self.addTab(widget, label)

class Label(QLabel):

	def __init__(self, label='', icon=None, parent=None):
		super(Label, self).__init__(parent)
		self.setFont(font_text())
		self._label = label
		self._icon = icon
		self.init()

	def init(self):
		self.setText(self._label)
		if self._icon:
			self.setPixmap(self._icon)

class CheckBox(QCheckBox):

	def __init__(self, label='', parent=None):
		super(CheckBox, self).__init__(parent)
		self.setFont(font_text())
		self._label = label
		self.init()
		self.connections()

	def init(self):
		self.setText(self._label)

	def connections(self):
		self.stateChanged.connect(self.on_checked)

	def on_checked(self):
		if self.isChecked():
			self.setStyleSheet(checkbox_on)
		else:
			self.setStyleSheet(checkbox_off)

class PushButton(QPushButton):

	def __init__(self, label='', icon=None, parent=None):
		super(PushButton, self).__init__(parent)
		self.setFont(font_text())
		self._label = label
		self._icon = icon
		self.init()

	def init(self):
		self.setStyleSheet(pushbutton)
		self.setText(self._label)
		if self._icon:
			self.setIcon(QIcon(self._icon))

class ComboBox(QComboBox):

	def __init__(self, parent=None, color=True):
		super(ComboBox, self).__init__(parent)
		self.setFont(font_text())
		self.setIconSize(QSize(23, 23))
		self._color = color
		self.connections()

	def connections(self):
		self.setStyleSheet(combobox_default)
		self.currentIndexChanged.connect(self.on_change_index)

	def on_change_index(self, index):
		if self._color:
			if index > 0:
				self.setStyleSheet(combobox_selection)
			elif index == 0:
				self.setStyleSheet(combobox_default)

	def allItem(self):
		return [self.itemText(i) for i in range(self.count())]

class TreeWidget(QTreeWidget):

	def __init__(self, parent):
		super(TreeWidget, self).__init__(parent)
		self.setFont(font_text())
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		# self.setSortingEnabled(True)
		self.setAnimated(True)
		self.setFocusPolicy(Qt.NoFocus)
		self.setAlternatingRowColors(True)
		self.setExpandsOnDoubleClick(True)
		self.setIconSize(QSize(23, 23))

