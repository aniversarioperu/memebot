.PHONY: clean-pyc clean-build docs clean

docs:
	rm -f docs/memebot.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ memebot
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
