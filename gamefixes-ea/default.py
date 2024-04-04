""" Default file for EA game fixes
    This file is always executed for games that are identified as EA games,
    even if no game fix is present. It is run before game fixes are applied.
"""

from protonfixes import util

def main():
    """ global defaults
    """

    util.regedit_add('HKEY_LOCAL_MACHINE\\Software\\Electronic Arts\\EA Desktop', 'InstallSuccessful', 'REG_SZ', 'true', True)
    util.regedit_add('HKEY_LOCAL_MACHINE\\Software\\Origin', 'ClientPath', 'REG_SZ', 'C:/Windows/System32/conhost.exe')
