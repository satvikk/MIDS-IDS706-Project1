install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py
	
test:
	python -m pytest -vv test_app.py
