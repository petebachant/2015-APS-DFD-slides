#!/usr/bin/env python
"""
This script copies figures into the local figures directory.
"""

import os
import shutil
from os.path import join

homedir = os.path.expanduser("~")
expdir = join(homedir, "Research", "Experiments")
foamrun_23x = join(homedir, "OpenFOAM", "pete-2.3.x", "run")
foamrun_24x = foamrun_23x.replace("2.3.x", "2.4.x")
foamrun_ext1 = join("media", "pete", "Data1", "OpenFOAM", "pete-2.3.x", "run")
foamrun_ext2 = foamrun_ext1.replace("Data1", "Data2")

figdirs = {"RVAT-baseline": join(expdir, "RVAT baseline", "Figures"),
           "RVAT-Re-dep": join(expdir, "RVAT Re dep", "Figures"),
           "AD": join(foamrun_24x, "actuatorSurface", "figures"),
           "CFD-pop": join(homedir, "Google Drive", "Research",
                           "CFD popularity", "figures"),
           "UNH-RVAT-turbinesFoam": join(foamrun_24x, "UNH-RVAT-turbinesFoam",
                                         "figures"),
           "RM2-turbinesFoam": join(foamrun_24x, "RM2-turbinesFoam", "figures"),
           "NTNU-HAWT-turbinesFoam": join(foamrun_24x, "NTNU-HAWT-turbinesFoam",
                                          "figures"),
           "NACAFoil": join(foamrun_24x, "NACAFoil", "figures")}

figlists = {"RVAT-baseline": [],
            "RVAT-Re-dep": [],
            "AD": [],
            "CFD-pop": [],
            "UNH-RVAT-turbinesFoam": ["meancontquiv.png", "kcont.png",
                                      "recovery-bar-chart.png",
                                      "perf-curves.png", "wake-profiles.png"],
            "RM2-turbinesFoam": ["perf-curves.png"],
            "NTNU-HAWT-turbinesFoam": ["perf-curves.png", "wake-profiles.png"],
            "NACAFoil": ["NACA-0012-0015-0018-0021-k-vs-cd.png"]}


for name, figlist in figlists.items():
    figdir = figdirs[name]
    for fig in figlist:
        oldfigpath = join(figdir, fig)
        newfigpath = os.path.join("figures", name + "_" + fig)
        if os.path.isfile(oldfigpath):
            shutil.copy2(oldfigpath, newfigpath)
            print("[x] {}: {} copied".format(name, fig))
        else:
            print("[ ] {}: {} not found".format(name, fig))
