import subprocess
import getpass
import random
import string
import os

from sys import platform


def ram() -> int:
    """Returns the amount of RAM on the computer in gigabytes.
    :return int: amount of RAM
    """
    capacity: int
    if platform == "linux" or platform == "linux2":
        capture = subprocess.run(['cat', '/proc/meminfo', '|', 'grep', '"MemTotal"'], capture_output=True)
        capture = capture.stdout.decode('utf-8').split()
        capture.remove("MemTotal:")
        capture.remove("kB")
        capacity = capture[0] / 1000  # to mb
        capacity = capacity / 1000  # to gb

        return int(capacity)

    elif platform == "darwin":
        capture = subprocess.run(['/usr/sbin/system_profiler', 'SPHardwareDataType', 'grep', '"Memory"'], capture_output=True)
        capture = capture.stdout.decode('utf-8').split()
        capture.remove("Memory:")
        capture.remove("GB")
        capacity = capture[0] 
        
        return int(capacity)
    
    elif platform == "win32":
        capture = subprocess.run(['wmic', 'MEMORYCHIP', 'get', 'Capacity'], capture_output=True)
        capture = capture.stdout.decode('utf-8').replace('Capacity', '').split()
        capacity = sum([int(x) for x in capture])

        return int(capacity / 1024 ** 2)

def homedir() -> list:
    """Returns a list of files and directories in the user's home folder.
    returns: None
    """

    dirs: list
    user: str = getpass.getuser()
    if platform == "linux" or platform == "linux2":
        dirs = os.listdir(f'/home/{user}')

    elif platform == "darwin":
        dirs = os.listdir(f'/Users/{user}')
    
    elif platform == "win32":
        dirs = os.listdir(f'C://Users//{user}')

    return dirs

def randstr(length: int) -> str:
    """Returns a string from a random character set.
    :param len: Length of return string
    :return: random string"""
    
    i: int = 0
    result_string: str = ""
    while i < length:
        rand = random.randint(0, len(string.ascii_letters) - 1)
        result_string += string.ascii_letters[rand]

        i += 1

    return result_string


if __name__ == "__main__":
    """
    Tests
    """
    print(ram())
    print(homedir())
    print(randstr(20))
    print(randstr(200))
    print(randstr(20000))