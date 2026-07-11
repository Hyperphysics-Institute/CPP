# (C) population route: does the 2382 cascade derive the coring population, and can it hide?
# Three registered numbers decide it.

f_dimer_coring = 0.99      # 2344: passing dSph-coring population is N=2 at ~99% mass fraction
f_dimer_xqc    = 0.034     # 2374 D2/D3: dimer contamination of summed-XQC must be < 3.4% to hide
# 2382 derived closed-product weights (representative baseline, phi/eps central, v_f=1):
cascade = {
  "r=5.0": {3:0.7826, 4:0.2168, 5:0.0007},   # dominant N=3 ring
  "r=7.5": {4:0.0919, 5:0.7896, 6:0.1173, 7:0.0013},
  "r=9.0": {5:0.121, 6:0.6979, 7:0.1763, 8:0.0047},
}
f_dimer_cascade_max = 0.034   # 2382: residual w(2) < 0.034 across the live corner (rings dominate)

print("="*70)
print("(C) POPULATION ROUTE — THE VISE")
print("="*70)
print(f"  coring demand      : f_dimer >= {f_dimer_coring:.2f}   (2344, to carry steep dSph)")
print(f"  XQC/DD hiding      : f_dimer <  {f_dimer_xqc:.3f}  (2374 D2/D3 contamination bound)")
print(f"  -> coring and hiding are MUTUALLY EXCLUSIVE by x{f_dimer_coring/f_dimer_xqc:.0f}")
print()
print(f"  cascade DERIVES    : f_dimer <= {f_dimer_cascade_max:.3f}  (2382) -> sides with HIDING,")
print("                       product is CLOSED-RING dominant (N=3-6), not dimers:")
for r,w in cascade.items():
    peak = max(w, key=w.get)
    print(f"      {r}: dominant N={peak} ring ({w[peak]*100:.0f}%);  dimer(N=2) share ~ 0 (<3.4% residual)")
print()
print("  The population that CORES (99% dimers) is NOT the derived one.")
print("  The population that is DERIVED (rings N=3-6) is the corridor that")
print("  DIED for coring at Q5 (2413). No population both derives AND cores.")
print("="*70)
print("RESULT: (C) closed by derivation. Ring coring is not deliverable by a")
print("        formation-derived population. Combined with elastic corridor death")
print("        (Q5/2413) and |SSV| capture death candidate-blind (2418): the ring")
print("        family cannot core the dwarfs by ANY derivable mechanism.")
print("        Successor -> (B): CDM-like/collisionless ring; cores (if real) baryonic.")
print("="*70)
