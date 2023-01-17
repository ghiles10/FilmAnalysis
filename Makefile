# Variables
APP=src/notebook/app_final.sh
REQS=requirements.txt

install: 
	pip install -r $(REQS)

run: install
	bash $(APP)

lint: install
	pip install pylint
	pylint --disable=R,C src/

test: 
	pip install pytest==7.0.1 
	pytest

all: install run lint test