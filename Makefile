PROJECT=tghello

test:
	cd $(PROJECT) && python setup.py develop
	cd $(PROJECT) && nosetests
