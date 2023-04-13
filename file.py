# -*- coding: utf-8 -*-

import json
import time
import os

def dirs(path):
	if not os.path.isdir(path):
		os.makedirs(path)
	return path

def open_folder(path):
	if os.path.isdir(path):
		os.startfile(path)

def json_write(path, data):
	f = open(path, 'w')
	f.write(json.dumps(data, indent=4))
	f.close()

def json_read(path):
	f = open(path, 'r')
	data = json.loads(f.read())
	f.close()
	return data

def get_datetime(path):
	return str(time.strftime("%Y.%m.%d %I:%M %p", time.localtime(os.path.getmtime(path))))

def get_size(path):
	getSize = os.path.getsize(path)
	return "%.2f MB" % (getSize / (1024.0 * 1024.0))

def get_extension(path):
	return os.path.splitext(os.path.basename(path))[1][1:]

