install:
	pip3 install -r ./requirements.txt
clear-reports:
	rm -rf -d ./reports/*.png
start:
	make clear-reports
	python3 setup.py
test:
	pytest