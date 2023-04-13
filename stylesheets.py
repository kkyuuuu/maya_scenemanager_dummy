# -*- coding: utf-8 -*-
from config import get_icon

tabwidget = """
	QTabBar::tab {                  
		background-color: rgb(93, 93, 93);                          
		border-width: 1px;                             
		border-style: solid;                           
		border-color: rgb(40, 40, 40);                           
		border-top-left-radius: 16px;                   
		border-top-right-radius: 16px;                  
		padding: 2px 11px;                                  
	}                                                  
	QTabBar::tab:top:selected {
		color: black;
	    background-color: rgb(200, 200, 200); 
	}
"""

pushbutton = """
	QPushButton {
		border: 1px solid rgb(40, 40, 40);
		border-radius: 8px;
		background-color: rgb(80, 80, 80);
	}
	QPushButton:hover {
		background-color: rgb(100, 100, 100);
		border: 2px solid rgb(82, 133, 166);
	}
	QPushButton:pressed {	
		background-color: rgb(40, 40, 40);
		border: 2px solid rgb(82, 133, 166);
	}
"""

frame = """
	QFrame{
		background-color: rgb(40, 40, 40);
	}
"""

checkbox_on = """
	QCheckBox{color: rgb(0, 255, 0);}
"""

checkbox_off = """
	QCheckBox{color: rgb(200, 200, 200)};
"""

lineedit_default = """
	QLineEdit{
		background-color: rgb(40, 40, 40);
		border: 2px solid rgb(40, 40, 40);
		border-radius: 13px;
	}
"""

lineedit_edit = """
	QLineEdit{
		background-color: rgb(40, 40, 40);
		border: 2px solid rgb(0, 255, 0);
		border-radius: 13px;
	}
"""

lineedit_error = """
	QLineEdit{
		background-color: rgb(40, 40, 40);
		border: 2px solid rgb(255, 0, 0);
		border-radius: 13px;
	}
"""

combobox_default = """
	QComboBox{
		background-color: rgb(93, 93, 93);
		border-radius: 13px;
		border: 1px solid rgb(40, 40, 40);
	}
	QComboBox:item::hover{
		background-color: rgb(39, 44, 54);
	}
	QComboBox::drop-down {
		subcontrol-origin: padding;
		subcontrol-position: top right;
		width: 25px; 
		border-left-width: 3px;
		border-left-color: rgba(40, 40, 40, 150);
		border-left-style: solid;
		border-top-right-radius: 3px;
		border-bottom-right-radius: 3px;	
		background-image: url(%s);
		background-position: center;
		background-repeat: no-reperat;
	}
	QComboBox QAbstractItemView {
		background-color: rgb(40, 40, 40);
		padding: 10px;
		selection-background-color: rgb(82, 133, 166);
	}
"""%(get_icon('cil-arrow-bottom.png'))

combobox_selection = """
	QComboBox{
		background-color: rgb(93, 93, 93);
		border-radius: 13px;
		border: 2px solid rgb(0, 255, 0);
	}
	QComboBox:item::hover{
		background-color: rgb(39, 44, 54);
	}
	QComboBox::drop-down {
		subcontrol-origin: padding;
		subcontrol-position: top right;
		width: 25px; 
		border-left-width: 3px;
		border-left-color: rgba(40, 40, 40, 150);
		border-left-style: solid;
		border-top-right-radius: 3px;
		border-bottom-right-radius: 3px;	
		background-image: url(%s);
		background-position: center;
		background-repeat: no-reperat;
	}
	QComboBox QAbstractItemView {
		background-color: rgb(40, 40, 40);
		padding: 10px;
		selection-background-color: rgb(82, 133, 166);
	}
"""%(get_icon('cil-arrow-bottom.png'))
