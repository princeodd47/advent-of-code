VENV = poetry run
PYTEST_ARGS = -vv

.PHONY: test
test:
	-$(VENV) pytest $(PYTEST_ARGS)

.PHONY: clean
clean:
	@rm -rf .pytest_cache
