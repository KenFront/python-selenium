install:
	pip3 install -r ./requirements.txt

clear-reports:
	rm -rf -d ./reports/*.png
	rm -rf ./reports/assets
	rm -rf ./reports/test_results.html

run-all-test:
	make clear-reports
	pytest -s --maxfail=0 --html=reports/test_results.html