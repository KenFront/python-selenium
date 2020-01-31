install:
	pip3 install -r ./requirements.txt
clear-reports:
	rm -rf -d ./reports/*.png
test:
	make clear-reports
	pytest -s --maxfail=0