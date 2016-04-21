#!/usr/bin/env python

"""
setup.py file for MOODS
"""

from distutils.core import setup, Extension


tools_mod = Extension('MOODS._tools',
                           sources=['core/tools_wrap.cxx',
                                    'core/moods_tools.cpp',
                                    'core/moods_misc.cpp',
                                    'core/match_types.cpp'],
                           include_dirs=["core/"],
                           extra_compile_args=['-march=native', '-O3', '-fPIC', '--std=c++0x'],
                           )

scan_mod = Extension('MOODS._scan',
                           sources=['core/scan_wrap.cxx',
                                    'core/moods_scan.cpp',
                                    'core/motif_0.cpp',
                                    'core/motif_h.cpp',
                                    'core/moods_misc.cpp',
                                    'core/scanner.cpp',
                                    'core/moods_tools.cpp',
                                    'core/match_types.cpp'
                                ],
                           include_dirs=["core/"],
                           extra_compile_args=['-march=native', '-O3', '-fPIC', '--std=c++0x'],
                           )

parsers_mod = Extension('MOODS._parsers',
                           sources=['core/parsers_wrap.cxx',
                                    'core/moods_parsers.cpp',
                                    'core/moods_misc.cpp',
                                    'core/moods_tools.cpp'],
                           include_dirs=["core/"],
                           extra_compile_args=['-march=native', '-O3', '-fPIC', '--std=c++0x'],
                           )

setup (name = 'MOODS-python',
       version = '1.9.1a1',
       description = 'MOODS: Motif Occurrence Detection Suite',
       maintainer = "Janne H. Korhonen",
       maintainer_email = "janne.h.korhonen@gmail.com",
       url='https://www.cs.helsinki.fi/group/pssmfind/',
       license = "GPLv3 / Biopython license",
       ext_modules = [tools_mod, scan_mod, parsers_mod],
       packages = ["MOODS"],
)