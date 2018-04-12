clean:
	@rm -f .coverage 2> /dev/null
	@find . -name "*.pyc" -delete
	@find . -name "*.swo" -delete
	@find . -name "*.swp" -delete
	@find . -name "__pycache__" -delete
	@rm -rf jsviewer.egg-info/ 2> /dev/null

devinstall:
	pip install --editable .
