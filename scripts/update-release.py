#!/usr/bin/env python

import getopt, sys
import re
import subprocess


def usage():
    print(
        """
        You can use the scripts as follows
        ./update-release.py -v v1.5.0
        """
    )


def replace_on(file, pattern, new_value):
    with open(file, "r+") as file:
        content = file.read()
        new_content = re.sub(pattern, new_value, content)
        file.seek(0)
        file.write(new_content)


def replace_version_on_config_py(version: str):
    file_name = "doc/source/conf.py"
    replace_on(file_name, r"release = '(\d+).(\d+).(\d+)'", f"release = '{version}'")


def replace_version_on_setup_py(version: str):
    file_name = "setup.py"
    replace_on(file_name, r"version='(\d+).(\d+).(\d+)'", f"version='{version}'")


def replace_version_on_changelog_gen(version: str):
    file_name = ".github_changelog_generator"
    replace_on(
        file_name, r"future-release=v(\d+).(\d+).(\d+)", f"future-release={version}"
    )


def update_versiono_pyproject_toml(version: str):
    shell(["poetry", "version", version])


def shell(command):
    return subprocess.run(command, text=True)


def main():
    version = None
    try:
        options, args = getopt.getopt(sys.argv[1:], "v:", ["version="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    for option, value in options:
        if option in ("-v", "--version"):
            version = value
        else:
            assert False, "Unhandled option"

    if not version:
        usage()
        sys.exit(2)

    version_number = version[1:] if "v" in version else version
    replace_version_on_setup_py(version_number)
    replace_version_on_config_py(version_number)
    replace_version_on_changelog_gen(version)
    update_versiono_pyproject_toml(version_number)


if __name__ == "__main__":
    main()
