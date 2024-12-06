clean:
	rm -rf __pycache__

run:
	python main.py

test:
	python -m unittest *_test.py
