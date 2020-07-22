run:
	@python3.8 main.py

test:
	@python3.8 -m tests.command_tests -v
	@python3.8 -m tests.job_tests -v
	@python3.8 -m tests.sequencer_tests -v