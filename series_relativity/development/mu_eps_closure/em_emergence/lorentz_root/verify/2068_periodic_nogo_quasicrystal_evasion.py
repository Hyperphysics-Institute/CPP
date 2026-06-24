#!/usr/bin/env python3
"""
2068 — Round 4 probe, CONSISTENCY-EVIDENCE ONLY (handover §7: numerics are never proof).

Round 3 reduced W1-vs-W2 (dominantly) to discrete dispersion isotropy of the broadcast.
Round 4: does the FULL 600-cell broadcast reach EXACT isotropy at finite a (W1) or only suppress
it (W2)?  The answer turns on the substrate's GLOBAL structure.

PART A — the PERIODIC no-go (the solid, numerical part). For ANY regular *periodic* lattice
   broadcast, the dispersion symbol D(k)=sum 2(1-cos(k.d)) is Brillouin-zone-PERIODIC and BOUNDED:
   (A1) it cannot equal the unbounded omega=c|k| -- exact linearity fails at the lattice scale;
   (A2) finite weighted shells SUPPRESS the leading icosahedral anisotropy harmonic but a tower
        (l=6,10,15,...) remains, so finite shells never reach EXACT isotropy.
   => EXACT W1 impossible for a periodic substrate; periodic => W2 (IR-emergent, icosa floor).

PART B — the EVASION (structural, not numerical here). The CPP substrate is NOT periodic: SR-1
   (Grid Resolution) fixes it as a "heavily nested array of self-similar 600-cell motifs" with
   "self-similar R/a=phi at every level" down to ~l_P/1e30 -- the golden-ratio self-similar
   (icosahedral QUASICRYSTAL) structure. Aperiodic order has NO Brillouin zone, so Part-A's
   periodicity premise FAILS -- the same way causal-set randomness evades the lattice no-go, but
   here deterministically via phi self-similarity. A full quasicrystal-dispersion computation is
   the Round-5 numerical target; here we only show the suppression trend that the dense aperiodic
   limit completes.
"""
import numpy as np
phi=(1+np.sqrt(5))/2

def icosa(r=1.0):
    pts=[]
    for a_,b_ in [(1,phi),(-1,phi),(1,-phi),(-1,-phi)]: pts+=[(0,a_,b_),(a_,b_,0),(b_,0,a_)]
    P=np.array(pts,float); return r*P/np.linalg.norm(P[0])      # 12 icosahedral directions, radius r

def symbol(shells,k): return sum(w*np.sum([2*(1-np.cos(k@d)) for d in D]) for D,w in shells)

def aniso(shells,q,nd=600,seed=1):
    rng=np.random.default_rng(seed)
    g=rng.standard_normal((300,3)); g/=np.linalg.norm(g,axis=1,keepdims=True)
    c2=np.mean([symbol(shells,1e-4*u)/1e-8 for u in g])
    if abs(c2)<1e-12: return np.nan
    u=rng.standard_normal((nd,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
    v=np.array([np.sqrt(max(symbol(shells,q*kh),0)/abs(c2))/q for kh in u])
    m=v.mean()
    return (v.max()-v.min())/m if abs(m)>1e-30 else np.nan

print("="*72); print("PART A — the periodic no-go (numerical)"); print("="*72)

# (A1) bounded periodic symbol: phase speed collapses toward the BZ edge -> exact omega=c|k| fails.
sh1=[(icosa(1.0),1.0)]
rng=np.random.default_rng(0); u=rng.standard_normal((400,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
ref=np.mean([np.sqrt(max(symbol(sh1,1e-3*kh),0))/1e-3 for kh in u])
print("  mean phase speed (normalized to 1 as q->0) vs q=|k|a:")
for q in [0.3,1.0,2.0,3.0]:
    g=np.mean([np.sqrt(max(symbol(sh1,q*kh),0))/q for kh in u])/ref
    print(f"     q={q:4.1f}:  v_phase = {g:.4f}   (exact Lorentz needs 1.0000 at ALL q)")
print("  -> bounded BZ-periodic symbol; v_phase collapses at the lattice scale. A trig polynomial")
print("     cannot equal the unbounded |k|, so EXACT omega=c|k| is impossible for ANY periodic lattice.")

# (A2) finite shells suppress the leading harmonic but never zero the tower.
qref=0.15
a_single=aniso(sh1,qref)
# scan a 2nd icosahedral shell (radius phi) weight; find the value that MINIMIZES anisotropy at qref
ws=np.linspace(-1.5,1.5,301); best=(1e9,0)
for w2 in ws:
    a=aniso([(icosa(1.0),1.0),(icosa(phi),w2)],qref)
    if not np.isnan(a) and a<best[0]: best=(a,w2)
print(f"\n  anisotropy at q={qref}:")
print(f"     single icosahedral shell           : {a_single:.3e}   (leading icosahedral harmonic, l=6)")
print(f"     best-tuned 2 shells (radii 1, phi)  : {best[0]:.3e}   (leading l=6 ~cancelled; residual = next harmonic l=10)")
print(f"     suppression factor                  : x{a_single/max(best[0],1e-30):.0f}, but NONZERO")
print("  -> each added/tuned shell kills ONE more icosahedral harmonic (l=6, then 10, then 15,...).")
print("     The tower is infinite, so a FINITE shell sum never reaches EXACT isotropy. EXACT W1 is")
print("     impossible for a periodic substrate; the realized world there is W2 (icosahedrally tiny floor).")

print("\n"+"="*72); print("PART B — the evasion (structural)"); print("="*72)
print("  The Part-A no-go assumes a PERIODIC lattice (a Brillouin zone). The CPP substrate is NOT")
print("  periodic: SR-1's canonical 'nested 600-cell hierarchy' is phi-self-similar at every level")
print("  (R/a=phi), i.e. an icosahedral QUASICRYSTAL (aperiodic; dense phi-Fourier-module; NO BZ).")
print("  Aperiodic order is the known route by which a DISCRETE structure evades the lattice-Lorentz")
print("  no-go (causal sets: via randomness; quasicrystals: via deterministic aperiodic self-similarity).")
print("  Numerical note (honest): a finite shell tower is still 'crystal-like' and does NOT probe the")
print("  aperiodic limit -- adding icosahedral shells only suppresses harmonics one at a time (Part A2).")
print("  The decisive computation is the dispersion of an icosahedral-quasicrystal APPROXIMANT (a dense")
print("  cut-and-project / phi-inflation point set) and whether its structure factor is EXACTLY")
print("  isotropic at finite resolution. That is the Round-5 target -- NOT done here.")

print("\n"+"="*72)
print("CONCLUSION (consistency-evidence, NOT proof):")
print(" A. EXACT W1 is impossible for any PERIODIC regular-lattice broadcast (bounded BZ-periodic")
print("    symbol; infinite icosahedral anisotropy tower). Periodic substrate => W2.")
print(" B. The CPP substrate is NOT periodic -- it is the phi-self-similar (quasicrystalline) nested")
print("    600-cell hierarchy (SR-1), which has no Brillouin zone and EVADES the Part-A no-go. So W1")
print("    is NOT ruled out; it is pinned to the quasicrystal-Lorentz question on the corpus substrate.")
print(" => W3 (real O(1) preferred frame) EXCLUDED (IR/continuum is Lorentz-invariant); any floor is")
print("    sub-Planck-nesting (~l_P/1e30) tiny; the exact W1-vs-W2 line = quasicrystal exact-Lorentz")
print("    (Round-5 target). Determination: W1-or-W2 with W3 excluded; W2 if periodic-approx, W1 viable")
print("    specifically BECAUSE the substrate is golden-ratio self-similar / quasicrystalline.")
