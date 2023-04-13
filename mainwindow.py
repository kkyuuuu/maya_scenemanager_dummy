# -*- coding: utf-8 -*-

import logging

from file import *
from widget import *
from config import *
import shot
import entity

if sys.version_info[0] > 2:
	from imp import reload
reload(shot)
reload(entity)

logger = logging.getLogger(__name__)

class MainWindow(QMainWindow):

	_HORIZONTAL_HEADERS = {
		'shotgrid': {
			'header': ['Shot / Scene', 'Status', 'Task', 'Assigned To', 'Start', 'End', 'Size', 'Date'],
			'size': [400, 150, 50, 100, 60, 60, 100, 100],
		},
	}
	_TITLE = ' DUMMY PROJECT'

	def __init__(self, parent=maya_widget()):
		super(MainWindow, self).__init__(parent)
		# settings
		self.ini_path = dirs(pathjoin(os.environ['localappdata'], 'mvinfo', self._TITLE.replace(' ', '')))
		self.ini_file = pathjoin(self.ini_path, 'settings.ini')
		self.settings = QSettings(self.ini_file, QSettings.IniFormat)

		# init ui
		self.ui()

		# connections
		self.connections()

		# init
		self.init()

	def connections(self):
		self.Episode.currentIndexChanged.connect(self.on_episode_change)
		self.pushbutton_search.clicked.connect(self.search_task)

	def init(self):
		# init filters
		self.Episode.refresh()
		self.Scene.refresh()
		self.Status.refresh()

	def on_episode_change(self):
		self.Scene.refresh()

	def search_task(self):
		"""
		I made the return value of shotgrid as an example
		"""
		sg_tasks = [
			{'code': 'dummy_e001_s07_c0340', 'content': 'layout', 'sg_cut_in': 101, 'sg_cut_out': 147,
			 'task_assignees': [{'name': 'kyu'}], 'sg_status_list': 'wat'},
			{'code': 'dummy_e020_s04_c0100', 'content': 'block', 'sg_cut_in': 101, 'sg_cut_out': 160,
			 'task_assignees': [{'name': 'kyu'}], 'sg_status_list': 'wip'},
			{'code': 'dummy_e015_s11_c0280', 'content': 'anim', 'sg_cut_in': 101, 'sg_cut_out': 200,
			 'task_assignees': [{'name': 'kyu'}], 'sg_status_list': 'don'},
			{'code': 'dummy_e008_s03_c0150', 'content': 'block', 'sg_cut_in': 101, 'sg_cut_out': 140,
			 'task_assignees': [{'name': 'kyu'}], 'sg_status_list': 'ret'},
			{'code': 'dummy_e003_s05_c0050', 'content': 'layout', 'sg_cut_in': 101, 'sg_cut_out': 150,
			 'task_assignees': [{'name': 'kyu'}], 'sg_status_list': 'cmp'},
			{'code': 'dummy_e036_s12_c0190', 'content': 'anim', 'sg_cut_in': 101, 'sg_cut_out': 145,
			 'task_assignees': [{'name': 'kyu'}], 'sg_status_list': 'wip'},
			{'code': 'dummy_e030_s02_c0240', 'content': 'anim', 'sg_cut_in': 101, 'sg_cut_out': 137,
			 'task_assignees': [{'name': 'kyu'}], 'sg_status_list': 'cmp'},
		]
		# add item
		for sg_task in sg_tasks:
			logger.info(sg_task)
			self.treewidget.set_item(sg_task)

	def ui(self):
		self.resize(1600, 1000)
		self.setWindowTitle(self._TITLE)
		self.centralwidget = QWidget(self)

		self.main_layout = QVBoxLayout(self.centralwidget)
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)

		self.header_frame = QFrame(self.centralwidget)
		self.header_frame.setStyleSheet(frame)
		self.header_frame.setMinimumSize(QSize(0, 45))
		self.header_frame.setMaximumSize(QSize(16777215, 45))
		self.header_frame.setFrameShape(QFrame.NoFrame)
		self.header_frame.setFrameShadow(QFrame.Raised)

		self.header_layout = QHBoxLayout(self.header_frame)
		self.header_layout.setSpacing(6)
		self.header_layout.setContentsMargins(3, 3, 3, 3)

		self.header_icon = Label(icon=get_icon('project.png'))
		self.header_icon.setMinimumSize(QSize(40, 40))
		self.header_icon.setMaximumSize(QSize(40, 40))
		self.header_icon.setScaledContents(True)
		self.header_layout.addWidget(self.header_icon)

		self.title_label = QLabel(self._TITLE)
		self.title_label.setFont(font_title())
		self.title_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
		self.header_layout.addWidget(self.title_label)
		self.main_layout.addWidget(self.header_frame)

		self.main_frame = QFrame(self.centralwidget)
		self.main_frame.setFrameShape(QFrame.StyledPanel)
		self.main_frame.setFrameShadow(QFrame.Raised)
		self.main_frame_layout = QVBoxLayout(self.main_frame)
		self.main_frame_layout.setContentsMargins(6, 6, 6, 6)
		self.main_frame_layout.setSpacing(6)
		self.filter_layout = QHBoxLayout()
		self.filter_layout.setContentsMargins(0, 0, 0, 0)
		self.filter_layout.setSpacing(6)

		# reset pushbutton
		self.reset_button = PushButton(icon=get_icon('reload.png'))
		self.reset_button.setFixedSize(QSize(30, 30))
		self.reset_button.setIconSize(QSize(28, 28))
		self.filter_layout.addWidget(self.reset_button)

		# episode combobox
		self.Episode = entity.Episode()
		self.Episode.setMinimumSize(QSize(120, 30))
		self.Episode.setMaximumSize(QSize(120, 30))
		self.filter_layout.addWidget(self.Episode)

		# scene combobox
		self.Scene = entity.Scene()
		self.Scene.setMinimumSize(QSize(120, 30))
		self.Scene.setMaximumSize(QSize(120, 30))
		self.filter_layout.addWidget(self.Scene)

		# status combobox
		self.Status = entity.Status()
		self.Status.setMinimumSize(QSize(120, 30))
		self.Status.setMaximumSize(QSize(120, 30))
		self.filter_layout.addWidget(self.Status)

		# task checkbox
		for content in ANI_CONTENTS:
			checkbox = CheckBox(content)
			checkbox.setObjectName('checkbox_{}'.format(content))
			self.filter_layout.addWidget(checkbox)

		# search pushbutton
		self.pushbutton_search = PushButton('Search')
		self.pushbutton_search.setMinimumHeight(30)
		self.pushbutton_search.setMinimumWidth(130)
		self.filter_layout.addWidget(self.pushbutton_search)

		# horizontal spacer
		self.filter_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.filter_layout.addItem(self.filter_spacer)

		# add filter layout
		self.main_frame_layout.addLayout(self.filter_layout)

		# TabWidget
		self.tab = TabWidget([' Tree Dummy '], triangular=False, document=True)
		self.main_frame_layout.addWidget(self.tab)

		# TreeWidget
		self.treewidget = _TreeWidget(self)

		# insert Header
		self.treewidget.setHeaderLabels(self._HORIZONTAL_HEADERS['shotgrid']['header'])
		for idx, width in enumerate(self._HORIZONTAL_HEADERS['shotgrid']['size']):
			self.treewidget.setColumnWidth(idx, width)

		# insert tableWidget
		tab_layouts = self.tab.layouts
		tab_layouts[0].addWidget(self.treewidget)

		# add main frame
		self.main_layout.addWidget(self.main_frame)

		# set layout
		self.setCentralWidget(self.centralwidget)

class _TreeWidget(TreeWidget):

	def __init__(self, parent):
		super(_TreeWidget, self).__init__(parent)
		self.parent = parent
		self.Status = self.parent.Status

	def set_item(self, sg_task):
		top_item = TreeItem(self, sg_task)
		top_item.set_top_item()
		self.addTopLevelItem(top_item)
		top_item.set_child_item()

class TreeItem(QTreeWidgetItem):

	def __init__(self, parent, sg_task):
		super(TreeItem, self).__init__(parent)
		self.parent = parent
		self.is_top = True
		self.top_item = self
		self.sg_task = sg_task

	@property
	def scenepath(self):
		_shot = shot.Shot(sg_task=self.sg_task)
		return _shot.scenepath

	@property
	def code(self):
		return self.sg_task['code']

	@property
	def content(self):
		return self.sg_task['content']

	@property
	def assignees(self):
		assignees = ''
		if self.sg_task['task_assignees']:
			artist_list = []
			for artist in self.sg_task['task_assignees']:
				artist_list.append(artist['name'].split(' ')[0])
			assignees = ', '.join(artist_list)
		return assignees

	@property
	def start_frame(self):
		return str(self.sg_task['sg_cut_in'])

	@property
	def end_frame(self):
		return str(self.sg_task['sg_cut_out'])

	@property
	def status(self):
		return self.sg_task['sg_status_list']

	@property
	def status_name(self):
		return self.parent.Status.get(self.status, 'name')

	@property
	def status_icon(self):
		return self.parent.Status.get(self.status, 'icon')

	def set_top_item(self):
		self.setText(0, self.code)
		self.setText(1, self.status_name)
		self.setIcon(1, QIcon(self.status_icon))
		self.setText(2, self.content)
		self.setText(3, self.assignees)
		self.setText(4, self.start_frame)
		self.setText(5, self.end_frame)

	def set_child_item(self):
		if not os.path.isdir(self.scenepath):
			return
		for scene in os.listdir(self.scenepath):
			if not scene.endswith(('mb', 'ma')):
				continue
			if not self.code in scene:
				continue
			self.add_child_item(scene)

	def add_child_item(self, scene):
		child_item = QTreeWidgetItem(self)
		child_item.is_top = False
		child_item.top_item = self
		child_item.setText(0, scene)
		child_item.setIcon(0, QIcon(get_icon('maya.png')))
		child_item.setText(6, get_size(pathjoin(self.scenepath, scene)))
		child_item.setText(7, get_datetime(pathjoin(self.scenepath, scene)))

def main():
	try:
		win.close()
		win.deleteLater()
	except:
		pass
	global win
	win = MainWindow()
	win.show()