#!/usr/bin/env python3
"""
Patch 4171 — TODO-4165-CHANNELJOB pressed to a conclusion: does the A_i channel
earn its place?

The amendment's case at 4120 was STRUCTURAL, not empirical: A_i "completes" A3'
over the FULL point group I_h, because the original enumeration used the
ROTATION group I -- under which polar and axial 3-vectors are the same irrep
T_1 -- while under I_h they are inequivalent, T_1u and T_1g.

THAT ARGUMENT IS SOUND AS FAR AS IT GOES. This patch asks how far it goes.
"""
out=[]
def say(s=""): print(s); out.append(s)

say("R1  what LSP' contains, with parity labels made explicit")
say("    Phi  = g_tt   no spatial index   -> parity EVEN  -> A_g   (l=0)  dim 1")
say("    V_i  = g_ti   one spatial index  -> parity ODD   -> T_1u  (l=1)  dim 3")
say("    Q_ij = g_ij   two spatial indices-> parity EVEN  -> H_g   (l=2)  dim 5")
say("    A_i  (Patch 4120)                -> axial        -> T_1g  (l=1)  dim 3")
say("    total after the amendment: 1 + 3 + 5 + 3 = 12 components")
say()

say("R2  the completeness question the amendment's own argument raises")
say("    If the defect was that the ROTATION-only enumeration cannot see parity,")
say("    then the fix is to enumerate l <= 2 with BOTH parities. Doing that:")
say(f"    {'l':>3}{'even-parity irrep':>20}{'odd-parity irrep':>20}{'in the packet?':>26}")
rows=[(0,"A_g  (scalar)","A_u  (PSEUDOSCALAR)","Phi yes / A_u NO"),
      (1,"T_1g (axial vector)","T_1u (polar vector)","A_i yes / V_i yes"),
      (2,"H_g  (tensor)","H_u  (ODD RANK-2)","Q_ij yes / H_u NO")]
for l,ev,od,st in rows:
    say(f"    {l:>3}{ev:>20}{od:>20}{st:>26}")
say()
say("    **TWO parity partners are missing after the amendment: A_u (dim 1) and")
say("    H_u (dim 5). The amendment added the third, T_1g.** Neither of the two")
say("    is added, and neither is discussed.")
say()

say("R3  so the structural argument proves more than the amendment does")
say("    Either:")
say("      (a) there is a principle that selects T_1g and excludes A_u and H_u")
say("          -- in which case it is not 'completeness', it is that principle,")
say("          and the principle is what should be stated; or")
say("      (b) completeness is the argument, and A3' is STILL incomplete after")
say("          the amendment -- by two channels, dims 1 and 5.")
say("    The corpus states (a) nowhere I have found. 4113's text is about T_1u")
say("    vs T_1g specifically and does not address l = 0 or l = 2.")
say()

say("R4  what the missing two would be, physically")
say("    A_u, a PSEUDOSCALAR broadcast: the parity partner of Phi = g_tt. A")
say("    scalar that changes sign under reflection -- structurally an axion-like")
say("    channel. If it existed it would give a P-odd term with NO axial vector")
say("    needed, which would compete directly with b as the source of chirality.")
say("    H_u, an ODD RANK-2: the parity partner of the radiative tensor. It would")
say("    be a parity-odd gravitational-wave polarisation -- and those ARE bounded,")
say("    tightly, by LIGO/Virgo birefringence searches.")
say("    So the two missing channels are not idle: one competes with the")
say("    amendment's own mechanism, the other is already constrained by data.")
say()

say("R5  VERDICT on CHANNELJOB")
say("    The A_i channel's EMPIRICAL case is weak and this session established")
say("    how weak: its jobs are (a) sourcing A1.A2, i.e. ordinary magnetism the")
say("    corpus already had, and (b) a spin-evolution term bounded at 5e-47 per")
say("    Moment (4170). Neither is a distinctive prediction.")
say("    Its STRUCTURAL case -- completeness over I_h -- is sound in form but")
say("    INCOMPLETE IN APPLICATION: the same argument demands A_u and H_u, which")
say("    the amendment does not add and the corpus does not exclude.")
say()
say("    **That is not a refutation of chi_4. It is a statement that the")
say("    amendment's two supports are each weaker than they looked: the empirical")
say("    one is near-empty, and the structural one, taken seriously, asks for")
say("    three channels rather than one.**")
say("    The honest recommendation: before chi_4 is ratified beyond provisional,")
say("    either state the principle that selects T_1g alone, or add the other two")
say("    and face the H_u bound from gravitational-wave birefringence.")
open('/tmp/4171.txt','w').write('\n'.join(out))
