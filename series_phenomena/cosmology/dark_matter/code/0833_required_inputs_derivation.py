import numpy as np
# Grounding the three Era-2 inputs in the CPP corpus: m_qDP, residual fraction f, qDP statistics.
hbarc=197.327; alpha=1/137.036; phi=1.6180339887; lp=1.616e-35; SIDM=1.0; rc=1.0
# INPUT 1: mass scale. DP_sea appendix: E=alpha*hbar*c/(phi*l_p); claims E_eDP=88, E_qDP=3*88=264 (color factor).
rmin=phi*lp*1e15
print(f"[1] appendix r_min=phi*l_p={phi*lp:.2e} m -> E={alpha*hbarc/rmin:.2e} MeV (claims 88: off ~{alpha*hbarc/rmin/88:.0e}x)")
print(f"    88 MeV needs r_min={alpha*hbarc/88:.4f} fm (not Planck-scaled). RATIO clean: E_qDP=3*E_eDP -> m_qDP~264 MeV.")
print(f"    sigma/m at m=264 vs 300: realistic 0.17->{0.17*300/264:.2f}, worst 0.50->{0.50*300/264:.2f} cm^2/g (both<SIDM)")
# INPUT 3: statistics -> de Boer parameter
print("[3] qCP fermion (ZBW spin-1/2) => qDP boson. de Boer Lambda=hbar/(r_c sqrt(m*eps)), He-4~0.18 self-binds:")
for f in [0.05,0.10,0.20,0.50,1.00]:
    Lam=hbarc/(rc*np.sqrt(264.0*f*264.0))
    print(f"    f={f:.2f} eps={f*264:.0f} MeV  Lambda={Lam:.2f}  {'diffuse (>>0.18)' if Lam>0.5 else 'could bind'}")
print("    => light bosonic qDP medium too quantum to self-bind -> DIFFUSE robust; nugget needs Lambda<~0.2 (heavier).")
print("[2] f: bounded f<1 (residue<source, 0831/0832); estimate f~0.05-0.2 (vdW/nuclear analogy); needs qDP color")
print("    polarizability to derive -> scoped calculation (qCP separation r_min + color coupling -> induced-dipole).")
