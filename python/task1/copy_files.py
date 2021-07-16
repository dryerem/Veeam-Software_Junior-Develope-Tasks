#!/usr/bin/env python3
import sys
import os
import shutil as sh
import xml.etree.ElementTree as ET


def copy_files(root: ET.Element) -> None:
    """This method copies all files to a new location according to the config.
    :param: root - xml.Element
    :return: None
    """

    if type(root) != ET.Element:
        raise TypeError("Pass the parameter incorrectly, pass - xml.etree.ElementTree.Element")

    for child in root:
        source_path: str = os.path.join(child.attrib.get('source_path'), child.attrib.get('file_name'))
        source_path = os.path.normpath(source_path)
        destination_path: str = child.get('destination_path')

        try:
            sh.copyfile(source_path, destination_path)
        except IOError as error:
            print(error)
        else:
            print(f"[SUCCESS] - File - {source_path} copied successfully!\n")


def main() -> int:
    """Entry point.
    :param: None
    :return: status code
    """
    
    if os.path.isfile('config.xml'):
        tree = ET.parse('config.xml')
        copy_files(tree.getroot())
    else:
        print("[ERROR] - Config file could not be found")
        return -1

    return 0


if __name__ == "__main__":
    sys.exit(main())