install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#fsdf

lint:
		pylint --disable=R,C app.py

deploy:
	echo "Go Go App!"
	eb deploy MIDS-IDS706-Project1-dev