# coding: utf-8

"""Change every newlines to (posix/linux) style."""

import glob
import optparse
import os
import os.path


def posixlines(filepath):
    """Change given file newlines to posix/linux style (LF)."""
    fileContents = open(filepath, "r").read()
    f = open(filepath, "w", newline="\n")
    f.write(fileContents)
    f.close()


def main():
    """Find every python file recursively inside given directory and call posixlines on them."""
    parser = optparse.OptionParser("fix_endl.py directory")
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        parser.error("incorrect number of arguments")
    destination = args[0]

    for arg in glob.glob(destination):
        if os.path.isdir(arg):
            print("processing: " + arg)
            for root, dirs, files in os.walk(arg):
                for file in files:
                    if file.endswith(".py"):
                        posixlines(os.path.join(root, file))
        else:
            print(arg + " is not a valid directory.")


if __name__ == "__main__":
    """ Execute only if run as a script. """
    main()
