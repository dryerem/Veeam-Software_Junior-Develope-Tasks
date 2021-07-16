# Veeam-Software_Junior-Developer-Tasks
Test assignments for the position Veeam Software_Junior Developer. In the future, it is planned to add solutions in other languages.

Task 1
Implement a program that copies files in accordance with
configuration file. The configuration file must be in xml format. For
each file in the configuration file must contain its name, source path and
the path where you want to copy.

Example
Config file:
<config>
    <file
        source_path = "C: \ Windows \ system32"
        destination_path = "C: \ Program files"
        file_name = "kernel32.dll"
    />
    <file
        source_path = "/ var / log"
        destination_path = "/ etc."
        file_name = "server.log"
    />
</config>

Task 2
Given a file containing filenames, a hashing algorithm (one of MD5 / SHA1 / SHA256) and
the corresponding hash sums calculated by the corresponding algorithm and indicated in
file separated by a space. Write a program that reads the given file and checks
integrity of files.
Example

Sums file:
file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906
file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709

Call example:
<your program> <path to the input file> <path to the directory containing
the files to check>

Output format:
file_01.bin OK
file_02.bin FAIL
file_03.bin NOT FOUND
file_04.txt OK
  
Task3 
Write a prototype of a test system consisting of two test cases. In this task
using a third-party module for test automation is discouraged.
A test system is a class hierarchy that describes test cases.
Each test case has:
Number (tc_id) and name (name)
Methods for preparing (prep), executing (run), and completing (clean_up) tests.
The execute method, which sets the general order of the test case execution and
handles exceptions.
All stages of the test case execution, as well as exceptional situations, should be
documented in the log file or standard output.

Test case 1: List of files
[prep] If the current system time, specified as an integer number of seconds from
the beginning of the Unix era, not a multiple of two, then it is necessary to interrupt the test case execution.
[run] List files from the current user's home directory.
[clean_up] No action required.

Test case 2: Random file
[prep] If the amount of RAM of the machine on which the test is executed is
less than one gigabyte, then it is necessary to interrupt the test case execution.
[run] Create a 1024 KB file test with random content.
[clean_up] Delete file test.
