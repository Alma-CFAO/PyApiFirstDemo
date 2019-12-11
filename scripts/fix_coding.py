# coding: utf-8

"""Add magic codding comment inside every python file without it."""

import glob
import optparse
import os
import os.path


def fixcodding(filepath):
    """Add magic codding comment in front of every python file without it."""
    file_content = open(filepath, "r").read()
    f = open(filepath, "w", newline="\n")

    if (
        "# -*- coding: utf-8 -*-" not in file_content and
        "# coding: utf-8" not in file_content
    ):
        new_content = "# coding: utf-8\n\n" + file_content
        f.write(new_content)
    else:
        f.write(file_content)

    f.close()


def main():
    """Find every python file recursively inside given directory and call fixcodding on them."""
    parser = optparse.OptionParser("fix_codding.py directory")
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
                        fixcodding(os.path.join(root, file))
        else:
            print(arg + " is not a valid directory.")


if __name__ == "__main__":
    """ Execute only if run as a script. """
    main()
