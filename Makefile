build:
	rm -rf dist
	rm -rf *.egg-info
	python -m build

deploy:
	twine upload dist/*
