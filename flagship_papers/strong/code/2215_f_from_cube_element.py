#!/usr/bin/env python3
"""
OPEN-SS-42 (patch 2215, strong/geometry lane): f from the CUBE element cross-section (0886) -> pinned dG*_nuc.
=============================================================================================================
Executes the 2214 handover: derive f = (exposed-core spine-face solid angle)/4pi from the DM element cross-section.
The element is a CUBE (0886: cross-section = cube face = the 4 hTetra arms / 8 qCP; one axial rung = one cube;
eCP coat screens the transverse faces). f follows from the cube's orientational combinatorics (|O|=24), NOT a
free acceptance cone. dG*_nuc = (n*-1)*|ln f|*kT_form, n* ~ 2-4 (OPEN-SS-41a). Win 6.0-6.9; kill <~4 or >~9.

RESULT: the E_qq spine distinguishes 1 of the cube's 3 axes (2 spine faces + 4 coat-screened transverse faces),
so f in the discrete bracket [1/12, 1/3]: f_steric = 8/24 = 1/3 (spine face axial, 4-fold cross shape), down to
f_reg = 2/24 = 1/12 if the E_qq color pattern forces rotational registration. This PINS the verdict structure:
(i) OVER-CORED KILL EXCLUDED (f >= 1/12 => dG* <= 7.5 kT < 9); (ii) the geometric DEFAULT (4-fold shape, coat-
blocking only, f=1/3) is UNDER-CORED (dG* ~ 1-3 kT, N_form = 3^(n*-1) ~ 3-27); (iii) the dwarf WINDOW is reached
ONLY in the corner f ~ 1/9-1/12 AND n* ~ 4 (dG* ~ 6.6-7.5 kT, N_form ~ 730-1720). Honest lean: UNDER-CORED unless
E_qq spine-face color registration breaks the 4-fold symmetry AND n*~4. Decider: the cube-face color-pattern
symmetry (an SU(3)/color-cage sub-question). NOT the clean confirm-in-window the sequence hoped for. Cluster
sigma/m ~ 1/v^2 branch stands as the parameter-free submittable prediction regardless.
"""

