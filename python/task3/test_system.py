#!/usr/bin/env python3
import time
import sys
import os
import logging
import logging.config

# my import 
import utils
from exceptions import UnixTimeException, AmountMemoryException, AmountFileSizeException


class Test:
    """
    This is the base class for creating and using tests.
    :param tc_id: number of the test (str)
    :param tc_name: name of the test (str)
    """
    def __init__(self, tc_id: str, tc_name: str):
        self.tc_id = tc_id
        self.tc_name = tc_name
    
    def prep(self) -> None:
        """Check the conditions required for the test."""
        pass

    def run(self) -> None:
        """Run the test itself."""
        pass

    def clean_up(self) -> None:
        """Execute test completion."""
        pass

    def execute(self) -> None:
        """Starts the test execution in the following order: 
            1. Check the conditions required for the test; 
            2. Run the test itself; 
            3. Execute test completion.
        :return: None
        """
        self.prep()
        self.run()
        self.clean_up()

    def get_id(self) -> str:
        """Returns the test number
        :return: test bumber (str)
        """
        return self.tc_id

    def get_name(self) -> str:
        """Returns the test name
        :return: test name (str)
        """
        return self.name


class ListOfFilesTest(Test):
    """
    This test should only run if the time that has passed since the beginning of the Unix epoch is a multiple of two. 
    The goal is to simply list the files in the user's home folder.
    :param tc_id: number of the test (str)
    :param tc_name: name of the test (str)
    """
    def __init__(self, tc_id: str, tc_name: str):
        super(ListOfFilesTest, self).__init__(tc_id, tc_name)
        self.logger = logging.getLogger('ListOfFilesTest')
        self.logger.setLevel(logging.DEBUG)

        self.fh = logging.FileHandler('ListOfFilesTest.log')
        self.fh.setLevel(logging.DEBUG)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.ERROR)

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def prep(self) -> None:
        """
        We return an exception if the time that has passed since the beginning of the epoch is not a multiple of two.
        """
        current_time = int(time.time())
        self.logger.debug(f"Elapsed time since the beginning of the era - {current_time}")
        if current_time % 2 != 0:
            self.logger.exception("The time since the beginning of the epoch must be even")
            raise UnixTimeException("The time since the beginning of the epoch must be even")

    def run(self) -> None:
        """List all folders and files in the current user's home directory."""
        print("Home dir: ")
        home = utils.homedir()
        for file in home:
            print("- " + file)
        self.logger.debug(f"User home folder file list - {home}")

    def clean_up(self) -> None:
        """No action required"""
        pass


class RandomFileTest(Test):
    def __init__(self, tc_id: str, tc_name: str):
        super(RandomFileTest, self).__init__(tc_id, tc_name)
        self._MAXBUFFSIZE: int = 1024000  # bytes
        self.current_path: str = os.path.abspath(os.path.dirname(__file__))
        self.create_path: str = os.path.join(self.current_path, 'test.txt')
        self.create_path = os.path.normpath(self.create_path)

        self.logger = logging.getLogger('RandomFileTest')
        self.logger.setLevel(logging.DEBUG)

        self.fh = logging.FileHandler('RandomFileTest.log')
        self.fh.setLevel(logging.DEBUG)

        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.ERROR)

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def prep(self) -> None:
        """Returning an exception if the user has less than 1 gigabyte of RAM on the pc."""
        gb: int = 1000
        ram: int = utils.ram()
        self.logger.debug(f"This computer has RAM installed: {ram}")

        if ram < gb:
            self.logger.exception("You must have more than 1 gigabyte")
            AmountMemoryException("You must have more than 1 gigabyte")

    def run(self) -> None:
        """Create a file named test and fill it with garbage."""
        with open(self.create_path, "w+", encoding="utf-8") as file_write:
            # If the value is 1024, we will get an exception, because the size will be slightly higher
            randstr = utils.randstr(self._MAXBUFFSIZE - 100)

            if sys.getsizeof(randstr) > self._MAXBUFFSIZE:
                self.logger.exception("The file size must not exceed 1024 kb")
                raise AmountFileSizeException("The file size must not exceed 1024 kb")

            file_write.write(randstr)
            self.logger.debug("The file was created.")

    def clean_up(self) -> None:
        """Delete the created file."""
        os.remove(self.create_path)
        self.logger.debug(f"The file was deleted.")


if __name__ == "__main__":

    # run first test
    try:
        lof_test_case = ListOfFilesTest(1, "lof")
        lof_test_case.execute()
        print("[DEBUG] - First Test - OK.")
    except Exception as e:
        print("[DEBUG] - First Test - FAIL. See Logs.")

    # run second test
    try:
        rand_file_case = RandomFileTest(2, "rand")
        rand_file_case.execute()
        print("[DEBUG] - Second Test - OK.")
    except Exception as e:
        print("[DEBUG] - Second Test - FAIL. See Logs.")

    sys.exit(0)