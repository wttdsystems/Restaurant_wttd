.PHONY: linter
linter:
	@.venv/bin/pflake8

.PHONY: fmt
fmt:
	@.venv/bin/isort Restaurant core
	@.venv/bin/black Restaurant core

.PHONY: tests
tests:
	@.venv/bin/pytest -vv
