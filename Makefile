install:
		pip3 install -r ./requirements.txt
clean-reports:
		rm -rf -d ./reports/*.png
start:
		python3 setup.py