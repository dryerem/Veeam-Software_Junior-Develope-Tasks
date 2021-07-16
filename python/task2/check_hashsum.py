#!/usr/bin/env python3
import sys
import os
import hashlib


def check_hash(filepath: str, obj: list) -> None:
    """This method checks if hashes match.
    :param filepath: File location path
    :param obj: Argument list
    obj[0] - filename
    obj[1] - hash_method
    obj[2] - hash_string
    :return: none
    """

    path = os.path.join(filepath, obj[0])
    path = os.path.normpath(path)
    try:

        with open(path, "r", encoding="utf-8") as check_file:
            check_file = check_file.read()

            hash_object = hashlib.new(obj[1])  # create a hash object with a need hash method
            hash_object.update(check_file.encode())  # create hash string

            if hash_object.hexdigest() == obj[2]:  # Checking that the hashes match
                print(f"{obj[0]}\tOK")
            else:
                print(f"{obj[0]}\tFAIL")

    except IOError as error:
        if error.args[0] == 2: #  file not found
            print(f"{obj[0]}\tNOT FOUND")
        else:
            print(error)  # other error
             

def main() -> int:
    """Entry point.
    :param: None
    :return: status code
    """
    _help = """Call example:\n <your program> <path to the input file> <path to the directory containing the files to check>"""

    if len(sys.argv) != 3:
        if sys.argv[1] == "--help":
            print(_help)
            return 0

        print("[ERROR] - Invalid number arguments. Please type --help to see help.")
        return -1

    path_to_input_file: str = sys.argv[1]  # The path to the file that contains the list of scanned files
    path_to_containing_files: str = sys.argv[2]  # The path where the scanned files are located
    
    if os.path.isfile(path_to_input_file) is False:
        print("[ERROR] - File does not exist")
        return -1
    
    with open(path_to_input_file, "r", encoding="utf-8") as input_file:
        input_file = input_file.readlines()
        for line in input_file:
            check_hash(path_to_containing_files, line.split())

    return 0


if __name__ == "__main__":
    sys.exit(main())
