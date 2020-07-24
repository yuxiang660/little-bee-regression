.PHONY: clean run test

clean:
	rm -rf output

run:
	@python3.8 main.py

test:
	@python3.8 -m tests.command_tests -v
	@python3.8 -m tests.job_tests -v
	@python3.8 -m tests.serial_tester_tests -v
	@python3.8 -m tests.logger_tests -v
	@python3.8 -m tests.config_tests -v
