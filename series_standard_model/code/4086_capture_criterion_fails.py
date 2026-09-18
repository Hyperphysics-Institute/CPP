"""4086 (EW lane) -- the capture distinction TESTED. It does not separate weak from strong.

4085 registered this as the most valuable open item: if the weak interaction is special because it CAPTURES
a CP (SF-2 section 5) while EM acts through DP-sea polarisation (SF-6), then linearity in the helicity bit
would follow from capture and F2/F3 would stop being clauses.

THE TEST is whether "capture" actually singles out the weak interaction in CPP's own corpus. It does not:
SF-2's own framework confines quarks and builds the Z and H as CAGES -- the strong sector captures too.

N1  verify the SF-2 structures the audit rests on (orbit sizes, shell counts) so the comparison is grounded.
N2  the audit: which interactions capture, and what each reads.
N3  the sharper criterion that does separate them -- and why it is still a stipulation.
N4  the honest comparison with the Standard Model, which settles how bad the remaining clauses are.
"""
import numpy as np, itertools
phi=(1+5**.5)/2

def build600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in itertools.permutations(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build600(); N=len(V); em=1/phi
D=np.linalg.norm(V[:,None]-V[None],axis=2)
shells=sorted(set(np.round(D[0][D[0]>1e-9],6)))
print("N1  SF-2 structures, verified independently")
print(f"    first shell (W bracelet ring lives here): {int(np.sum(np.abs(D[0]-shells[0])<1e-6))} vertices (SF-2 Thm 4.2: 12)")
print(f"    second shell (H dodecahedral cage):       {int(np.sum(np.abs(D[0]-shells[1])<1e-6))} vertices (SF-2 Thm 4.3: 20)")
print(f"    no shell with V in (12,20):               {not any(12 < int(np.sum(np.abs(D[0]-s)<1e-6)) < 20 for s in shells)}  (SF-2 Thm 4.4 mass gap)")
assert int(np.sum(np.abs(D[0]-shells[0])<1e-6))==12 and int(np.sum(np.abs(D[0]-shells[1])<1e-6))==20

print("\nN2  THE AUDIT -- does 'capture' single out the weak interaction?")
rows = [
 ("weak  (W bracelet, SF-2 sec 5)", "YES -- external charge captured at the D6 centroid", "the captured CP's own state"),
 ("strong (quark confinement, cages)", "YES -- quarks confined in cage structures",        "the confined CPs' states"),
 ("EM    (SF-6 DP-sea polarisation)", "NO  -- polarises the sea, captures nothing",        "displacement magnitudes"),
]
print(f"    {'interaction':34s} {'captures?':52s} reads")
for a,b,c in rows: print(f"    {a:34s} {b:52s} {c}")
print("    => capture separates EM from the other two, but NOT weak from strong.")
print("       SF-2's own framework builds the Z (icosahedral cage) and H (dodecahedral cage) by confinement,")
print("       and confines quarks. The criterion I proposed at 4085 FAILS to do the work asked of it.")

print("\nN3  the sharper criterion, and why it is still a stipulation")
print("    What IS unique to the weak interaction: it TRANSMUTES the captured particle (flavour/species")
print("    change; SF-2's charged-current channels), whereas confinement binds without transmuting.")
print("    But 'only transmuting processes read the bit' is the same stipulation in new words -- it names")
print("    the weak interaction rather than deriving why it alone is linear in b.")

print("\nN4  THE HONEST COMPARISON -- how bad is the remaining clause?")
print("    In the STANDARD MODEL, that only the weak interaction violates parity is ALSO not derived: it is")
print("    the choice that SU(2) acts on left-handed doublets -- a representation assignment, stipulated.")
print("    So F2/F3 leave CPP no worse off than the SM on this point.")
print("    F5 is different. The SM does not predict the Jarlskog invariant either -- it is a free parameter.")
print("    But CPP's standard is ZERO free parameters, so leaving J unexplained is a gap BY CPP'S OWN")
print("    STANDARD, not by the SM's. That asymmetry of standards is the honest summary of where the")
print("    axiom stands.")
