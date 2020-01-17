VENV = poetry run
PYTEST_ARGS = -vv
PYTEST_TARGETS ?= "day_10"
INTCODE_DAYS = "intcode or day_02 or day_05 or day_07 or day_09"

.PHONY: test
test:
	-$(VENV) pytest $(PYTEST_ARGS) -k $(PYTEST_TARGETS)

.PHONY: test-all
test-all:
	-$(VENV) pytest $(PYTEST_ARGS)

.PHONY: test-intcode
test-intcode:
	-$(VENV) pytest $(PYTEST_ARGS) -k $(INTCODE_DAYS)

.PHONY: clean
clean:
	@rm -rf .pytest_cache
	@rm -rf __pycache__
	@rm -rf aoc2019/__pycache__
	@rm -rf tests/__pycache__
