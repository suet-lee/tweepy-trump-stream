from stream import *
import os
import sys

pid = str(os.getpid())
pidfile = 'tmp/stream.pid'
mkdirIfNotExists('tmp')

if os.path.isfile(pidfile):
	print '%s already exists, exiting' % pidfile
	sys.exit()

file(pidfile, 'w').write(pid)
try:
	getStream()
finally:
    os.unlink(pidfile)

print 'Successful stream :>'
