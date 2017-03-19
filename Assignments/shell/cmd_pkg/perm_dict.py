import os

def perm_dict(val):
	dict={7:'rwx',6:'rw-',5:'r-x',4:'r--',3:'-wx',2:'-w-',1:'--x'}
	return dict[1]