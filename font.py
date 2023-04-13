# -*- coding: utf-8 -*-

from PySide2.QtGui import QFont

_family = r"Arial"

def font_title():
	font = QFont()
	font.setFamily(_family)
	font.setPointSize(15)
	font.setWeight(50)
	return font

def font_main():
	font = QFont()
	font.setFamily(_family)
	font.setPointSize(10)
	return font

def font_tab():
	font = QFont()
	font.setFamily(_family)
	font.setPointSize(12)
	return font

def font_menu():
	font = QFont()
	font.setFamily(_family)
	font.setPointSize(10)
	return font

def font_text():
	font = QFont()
	font.setFamily(_family)
	font.setPointSize(10)
	return font
