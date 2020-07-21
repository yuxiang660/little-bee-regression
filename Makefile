run:
	@python3.8 main.py

test:
	@python3.8 -m tests.command_tests -v
