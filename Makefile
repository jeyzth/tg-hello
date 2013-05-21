PROJECT=tghello

test:
	cd $(PROJECT) && python setup.py develop
	cd $(PROJECT) && nosetests

run:
	cd $(PROJECT) && paster serve development.ini
