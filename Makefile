install:
	pip install -r requirements.txt
	python3 -m venv ~/.venv
	source ~/.venv/bin/activate
	
lint:
	pylint --disable=R,C app.py
	
test:
		python -m pytest -vv test_app.py