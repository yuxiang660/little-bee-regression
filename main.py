from tester import SerialTester, Config
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Regression Test')
    # positional argument for the configuration file of the regression test
    parser.add_argument('config_file', help='configuration file of the regression test')

    args = parser.parse_args()

    t = SerialTester(Config(args.config_file))
    t.one_click_run()
    t.log()
