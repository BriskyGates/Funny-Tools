# -*- coding: utf-8 -*-

import sys
import subprocess


class CopyPath():
    """
    Main class to pass a path of target file to console.
    """

    def __init__(self, path):
        self.path = path

    def get_current_path(self):
        """
        Return path splits with slash.
        """
        path_2 = self.path.replace('\\', '/')
        return self.copy_to_clipboard(path_2)

    def copy_to_clipboard(self, txt):
        """
        Copy path and add double quote into clipboard.
        """
        cmd = 'echo "' + txt.strip() + '"|clip'
        return subprocess.check_call(cmd, shell=True)


if __name__ == '__main__':
    cp = CopyPath(sys.argv[1])
    cp.get_current_path()


