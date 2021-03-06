.PHONY: clean run test

clean:
	rm -rf output

run:
	@/cygdrive/c/Users/yuxiangw/AppData/Local/Programs/Python/Python38/python main.py config.json

win_test:
	@/cygdrive/c/Users/yuxiangw/AppData/Local/Programs/Python/Python38/python -m tests.command_tests -v
	@/cygdrive/c/Users/yuxiangw/AppData/Local/Programs/Python/Python38/python -m tests.job_tests -v
	@/cygdrive/c/Users/yuxiangw/AppData/Local/Programs/Python/Python38/python -m tests.config_tests -v
	@/cygdrive/c/Users/yuxiangw/AppData/Local/Programs/Python/Python38/python -m tests.serial_tester_tests -v
	@/cygdrive/c/Users/yuxiangw/AppData/Local/Programs/Python/Python38/python -m tests.parallel_tester_tests -v
	# logger_tests depends on above tests
	@/cygdrive/c/Users/yuxiangw/AppData/Local/Programs/Python/Python38/python -m tests.logger_tests -v

linux_test:
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.command_tests -v
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.job_tests -v
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.config_tests -v
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.serial_tester_tests -v
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.parallel_tester_tests -v
	# logger_tests depends on above tests
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.logger_tests -v
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.model_tests -v
	@/lan/cva/hsv-apfw/yuxiangw/common/bin/python3.8 -m tests.model_config_tests -v

