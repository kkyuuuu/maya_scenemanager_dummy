# -*- coding: utf-8 -*-

from widget import ComboBox
from widget import QColor, QIcon, QPixmap
from config import get_icon, TAG_SCENE, TAG_EPISODE
from collections import OrderedDict

class Default(ComboBox):

	def __init__(self, parent=None):
		super(Default, self).__init__(parent)

	@property
	def fields(self):
		return ['code']

	@property
	def order(self):
		return [{
				'fields_name': 'code',
				'direction': 'asc'
			}]

class Episode(Default):

	_DEFAULT_FILTER = '- Episode -'

	def __init__(self, parent=None):
		super(Episode, self).__init__(parent)

	"""
	Get information from ShotGrid
	"""
	# def refresh(self, sg):
	# 	self.clear()
	# 	self.addItem(self._DEFAULT_FILTER)
	# 	_filters = [
	# 		['project', 'is', SG_PROJECT]
	# 	]
	# 	for sg_episode in sg.find('Episode', _filters, self.fields, self.order):
	# 		code = sg_episode['code']
	# 		self.addItem(code)

	"""
	Dummy infomation 
	"""
	def refresh(self):
		self.clear()
		self.addItem(self._DEFAULT_FILTER)
		for text in range(1, 20):
			self.addItem(TAG_EPISODE + str(text).zfill(3))

class Scene(Default):

	_DEFAULT_FILTER = '- Scene -'

	def __init__(self, parent=None):
		super(Scene, self).__init__(parent)

	def refresh(self):
		self.clear()
		self.addItem(self._DEFAULT_FILTER)
		for text in range(1, 20):
			self.addItem(TAG_SCENE + str(text).zfill(2))

class Status(Default):

	_DEFAULT_FILTER = '- Status -'
	_DATA = OrderedDict()
	_DATA['wat'] = {
		'name': 'Waiting',
		'icon': get_icon('waiting.png'),
		'fore-color': QColor(0, 0, 0),
		'back-color': QColor(200, 200, 200),
	}
	_DATA['wip'] = {
		'name': 'WIP',
		'icon': get_icon('wip.png'),
		'fore-color': QColor(0, 0, 0),
		'back-color': QColor(240, 140, 0),
	}
	_DATA['don'] = {
		'name': 'Done',
		'icon': get_icon('done.png'),
		'fore-color': QColor(0, 0, 0),
		'back-color': QColor(240, 140, 0),
	}
	_DATA['ret'] = {
		'name': 'Retake',
		'icon': get_icon('retake.png'),
		'fore-color': QColor(0, 0, 0),
		'back-color': QColor(210, 10, 0),
	}
	_DATA['cmp'] = {
		'name': 'Complete',
		'icon': get_icon('complete.png'),
		'fore-color': QColor(0, 0, 0),
		'back-color': QColor(0, 160, 220),
	}

	def __init__(self, parent=None):
		super(Status, self).__init__(parent)

	def get(self, key='', flag=''):
		'''
		:param key: str
		:param flag: str
		:return: str
		'''
		if key in list(self._DATA.keys()):
			return self._DATA[key][flag]

	def refresh(self):
		self.clear()
		self.addItem(self._DEFAULT_FILTER)
		for status in self._DATA.keys():
			name = self.get(status, 'name')
			icon = QIcon(QPixmap(self.get(status, 'icon')))
			self.addItem(icon, name)
