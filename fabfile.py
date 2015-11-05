from fabric.api import *

#env.users='orusulea'

env.hosts=['orusulea@newgate.cs.ucl.ac.uk']


def testing():
	run('touch ahahahah_it_works.txt')
