# Copyright (c) 2018 Gregory Oschwald
# Change for CudaLint: Medvosa
# License: MIT

import os

import shlex
import tempfile

from cuda_lint import Linter, util, options

def sl3_util_climb(start_dir, limit=None):
    """
    Generate directories, starting from start_dir.
    If limit is None, stop at the root directory.
    Otherwise return a maximum of limit directories.
    """
    right = True

    while right and (limit is None or limit > 0):
        yield start_dir
        start_dir, right = os.path.split(start_dir)

        if limit is not None:
            limit -= 1


def sl3_util_find_file(start_dir, name, parent=False, limit=None, aux_dirs=[]):
    """
    Find the given file by searching up the file hierarchy from start_dir.
    If the file is found and parent is False, returns the path to the file.
    If parent is True the path to the file's parent directory is returned.
    If limit is None, the search will continue up to the root directory.
    Otherwise a maximum of limit directories will be checked.
    If aux_dirs is not empty and the file hierarchy search failed,
    those directories are also checked.
    """
    for d in sl3_util_climb(start_dir, limit=limit):
        target = os.path.join(d, name)

        if os.path.exists(target):
            if parent:
                return d

            return target

    for d in aux_dirs:
        d = os.path.expanduser(d)
        target = os.path.join(d, name)

        if os.path.exists(target):
            if parent:
                return d

            return target

#-----------------------------------------------------------------------------

class PerlCritic(Linter):
    
    cmd = 'perl /Users/alme/Downloads/Perl-Critic-1.138\ 2/bin/perlcritic '
    syntax = ('Perl')
    defaults = {
        'selector': 'source.modernperl, source.perl'
    }

    
    #-----------
    
    """Provides an interface to perlcritic."""

    executable = 'perl'
    regex = r'\[.+\] (?P<message>.+?) at line (?P<line>\d+), column (?P<col>\d+).+?'

    

    def cmd(self):
        """Return a tuple with the command line to execute."""

        command = [self.executable, '/Users/alme/Downloads/Perl-Critic-1.138\ 2/bin/perlcritic', '--verbose', '8']

        return command
