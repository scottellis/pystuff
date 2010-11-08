#!/usr/bin/env python

import os


def search(arg, dirname, fnames):
	process = True

	if arg.has_key('exclude'):
		for e in arg['exclude']:
			if dirname.find(e) >= 0:
				process = False
				break;

	if process:
		for f in fnames:
			keep = True

			if arg.has_key('pattern'):
				keep = False

				for p in arg['pattern']:
					if f.find(p) >= 0:
						keep = True
						break

			if keep:
				full = dirname + '/' + f

				if not os.path.isdir(full):
					print full, os.path.getsize(full)
					arg['count'] = arg['count'] + 1
					arg['size'] = arg['size'] + os.path.getsize(full)


def summarize(arg):
	print 'Total Count:', arg['count']
	print 'Total Size: ',

	size = arg['size']

	if size < 1000:
		print size
	elif size < 1000000:
		print size / 1000.0, 'kB'
	elif size < 1000000000:
		print size / 1000000.0, 'MB'
	else:
		print size / 1000000000.0, 'GB'
	

search_arg = {}
search_arg['count'] = 0
search_arg['size'] = 0

search_arg['pattern'] = list()
search_arg['pattern'].append('.pdf')

search_arg['exclude'] = list()
search_arg['exclude'].append('.git')

os.path.walk('/home/scott', search, search_arg)

summarize(search_arg)


