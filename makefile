install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
	
pin:
	python3 -m pip install --user dist/*.whl

pif:
	python3 -m pip install --user --force-reinstall dist/*.whl

run:
	poetry run gendiff -h

publish:
	poetry publish --dry-run