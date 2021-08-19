from setuptools.command.install import install
import os
import sys


class PostInstallCommand(install):

    def run(self):
        install.run(self)

        from pyshortcuts import make_shortcut, platform

        if platform.startswith('win'):
            bindir = 'Scripts'
            make_shortcut(script=f"{os.path.join(sys.prefix, bindir, 'pylabeler-script.py')}",
                          executable='pythonw',
                          name='PyLabeler')
        else:
            bindir = 'bin'
            make_shortcut(script=f"{os.path.join(sys.prefix, bindir, 'pylabeler')}",
                          terminal=False,
                          name='PyLabeler')
