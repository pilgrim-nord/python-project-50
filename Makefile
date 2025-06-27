install:
	uv sync

build:
	uv build

gendiff:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

force-install:
	uv tool install --force-reinstall dist/*.whl

lint:
	uv run ruff check gendiff

lint-with-fix:
	uv run ruff check gendiff --fix

check: test lint

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml