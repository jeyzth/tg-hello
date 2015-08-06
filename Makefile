PROJECT=tghello
setup:
	cd $(PROJECT) && python setup.py develop
	cd $(PROJECT) && paster setup-app development.ini

test:
	cd $(PROJECT) && python setup.py develop
	cd $(PROJECT) && nosetests

run:
	cd $(PROJECT) && paster serve development.ini
