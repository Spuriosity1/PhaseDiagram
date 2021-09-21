# -*- coding: utf-8 -*-

from setuptools import setup

setup(
        name="PhaseDiagram",
        version="0.1",
        packages=['PhaseDiagram'],
        package_dir={
            'PhaseDiagram': 'src',
        },
        licence="GPLv3+",
        author="Spuriosity1",
        description="Adaptive-grid phase diagram calculation and plotting routines",
        url="https://github.com/Spuriosity1/PhaseDiagram",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: OS Independent",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering :: Physics",
            ],
    )
