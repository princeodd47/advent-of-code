VENV = poetry run
PYTEST_ARGS = -vv
PYTEST_TARGETS ?= "day_01"

.PHONY: test
test:
	-$(VENV) pytest $(PYTEST_ARGS) -k $(PYTEST_TARGETS)

.PHONY: clean
clean:
	@rm -rf .pytest_cache
	@rm -rf __pycache__
	@rm -rf aoc2015/__pycache__
	@rm -rf tests/__pycache__
