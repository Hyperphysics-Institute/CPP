#!/usr/bin/env python3
# PATCH 2559 -- FORM-L-2 R-A. New cells L in {22,26} under reach-S (2557 machinery
# verbatim via code/2557_reregistration_reach_s.py definitions); L=20/24 consumed FROZEN
# from the 2557 corrected table (prereg S2 no-re-roll rule). Readings per prereg S3.
# This file is the executed stage script recorded verbatim (run log in reasoning/2559.md).
import json, time, numpy as np
src=open('series_phenomena/cosmology/dark_matter/code/2557_reregistration_reach_s.py').read()
g={}; exec(src.split("t0=time.time()")[0],g)
t0=time.time()
scaffold_L=g['scaffold_L']; ssv=g['ssv_vectors']; dance=g['dance_v8']; RS=g['build_reach_S']; D=g['D']
FLOOR=2.0
FROZEN={20:{100:+192.6,50:+179.3,25:+181.1}, 24:{100:-18.8,50:-12.9,25:-16.8}}
new={}
for L in (22,26):
    kapL=2*np.pi/(L*D)
    Pr,Cr,SPr=scaffold_L(L,kapL); Ps,Cs,SPs=scaffold_L(L,0.0)
    FREF=max(np.linalg.norm(ssv(Pr,Cr,SPr),axis=1).max(),np.linalg.norm(ssv(Ps,Cs,SPs),axis=1).max())
    new[L]={}
    for dtf,idt in ((1/100,100),(1/50,50),(1/25,25)):
        Er=dance(Pr,Cr,SPr,FREF,dtf,RS); Es_=dance(Ps,Cs,SPs,FREF,dtf,RS)
        new[L][idt]=float(Es_.mean()-Er.mean())
tab={20:FROZEN[20],22:new[22],24:FROZEN[24],26:new[26]}
GRID=[20,22,24,26]
intervals={idt:[] for idt in (100,50,25)}
for idt in (100,50,25):
    for i in range(len(GRID)-1):
        a=tab[GRID[i]][idt]; b=tab[GRID[i+1]][idt]
        if a>FLOOR and b<-FLOOR: intervals[idt].append((GRID[i],GRID[i+1],'+-'))
        if a<-FLOOR and b>FLOOR: intervals[idt].append((GRID[i],GRID[i+1],'-+'))
stable = all(len(v)==1 and v[0][2]=='+-' for v in intervals.values()) and len(set(v[0][:2] for v in intervals.values()))==1
assert stable, "prereg S3: bracket not union-stable"
print("bracket:", intervals[100][0][:2], "| table:", tab)
