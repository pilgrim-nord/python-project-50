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

check: test lint
