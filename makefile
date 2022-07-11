install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff
	
pin:
	python3 -m pip install --user dist/*.whl

pif:
	python3 -m pip install --user --force-reinstall dist/*.whl

run:
	poetry run gendiff -h