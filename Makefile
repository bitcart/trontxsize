all: ci

lint:
	ruff check

checkformat:
	ruff format --check

format:
	ruff format

test:
	pytest tests/ ${TEST_ARGS}

ci: checkformat lint test
