# -*- coding: UTF-8 -*-

import re
import os
from join import pathjoin
from join import wordjoin

class Shot(object):

	scene_elements = [
		r'(?P<scenename>',
		r'(?P<code>',
		r'(?P<prj>\w+)',
		r'_(?P<ep>e(?P<ep_no>[0-9]{3}))',
		r'_(?P<sc>s(?P<sc_no>[0-9]{2}))',
		r'_(?P<cut>c(?P<cut_no>[0-9]{4})))',
		r'(_(?P<task>\w+)',
		r'_(?P<ver>v(?P<ver_no>[0-9]{3}))',
		r'.(?P<ext>m[ab]|mov))?',
		')',
	]
	SCENE_PATTERN = wordjoin(*scene_elements)
	'''
	:param sg_task: dictionary
	:param flag: str
	:return: None
	'''
	def __init__(self, sg_task=None, scenename=None):
		if sg_task:
			code = sg_task['code']
		elif scenename:
			code = scenename
		r = re.search(self.SCENE_PATTERN, code)
		self._scenename = r.group('scenename') if r else None
		self._code = r.group('code') if r else None
		self._prj = r.group('prj') if r else None
		self._episode = r.group('ep') if r else None
		self._episode_num = r.group('ep_no') if r else None
		self._sc = r.group('sc') if r else None
		self._sc_num = r.group('sc_no') if r else None
		self._cut = r.group('cut') if r else None
		self._cut_num = r.group('cut_no') if r else None
		self._task = r.group('task') if r else None
		self._version = r.group('ver') if r else None
		self._version_num = r.group('ver_no') if r else None
		self._ext = r.group('ext') if r else None

	# dummy project path
	@property
	def scenepath(self):
		return pathjoin(os.path.dirname(__file__).replace('\\', '/'), 'scenes')

	@property
	def scenename(self):
		return self._scenename

	@property
	def code(self):
		return self._code
