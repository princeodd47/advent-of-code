VENV = poetry run
PYTEST_ARGS = -vv

.PHONY: test
test:
	-$(VENV) pytest $(PYTEST_ARGS)

.PHONY: clean
clean:
	@rm -rf .pytest_cache
	@rm -rf __pycache__
	@rm -rf aoc2019/__pycache__
	@rm -rf tests/__pycache__