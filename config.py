# -*- coding: utf-8 -*-

import os
from join import pathjoin

# icon
ICON_PATH = pathjoin(os.path.dirname(__file__).replace('\\', '/'), 'icons')
def get_icon(name):
	return pathjoin(ICON_PATH, name)

# project info
TAG_EPISODE = 'ep'
TAG_SCENE = 's'
TAG_CUT = 'c'

# shotgrid project id
SG_PROJECT = {'type': 'Project', 'id': "project number"}

'''
using shotgrid template
'''
# animation task list
ANI_CONTENTS = ['layout', 'blocking', 'detail', 'final']