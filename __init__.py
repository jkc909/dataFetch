import code; 

MY_CONSTANT = 3521

def debug():
	code.interact(local=dict(globals(), **locals()))