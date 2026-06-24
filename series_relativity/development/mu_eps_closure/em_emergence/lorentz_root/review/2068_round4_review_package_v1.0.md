# CONV-001 review package — Round 4 (Patch 2068): the periodic Lorentz no-go and CPP's quasicrystal evasion

**Cycle-opening package (v1.0).** Self-contained: the inline content below is authoritative; the GitHub
links are provenance only. This reviews a **FINDING**, not a theorem — the standard is *"is the world-call
determination justified by what is actually shown, and is the substrate-structure claim sound?"* **NO THEO
is on the table; no status/registry move rides on this review.**

**Provenance (do not need to open — content is reproduced in full below):**
- Finding (blob): `https://github.com/Hyperphysics-Institute/CPP/blob/main/series_relativity/development/mu_eps_closure/em_emergence/lorentz_root/2068_round4_periodic_nogo_quasicrystal.md`
- Verify (raw): `https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_relativity/development/mu_eps_closure/em_emergence/lorentz_root/verify/2068_periodic_nogo_quasicrystal_evasion.py`

---

## §0. Context

**CPP** derives Standard-Model physics from Conscious Points executing Perceive–Compute–Displace (PCD)
cycles on a 600-cell substrate. The **exact-emergent-Lorentz root campaign** (OPEN-SR-10) asks whether the
PCD dynamics admit an **exact continuous SO⁺(3,1)** action on the emergent fields, across a continuum of
velocities and all directions. Three worlds: **W1** exact-discrete (the prize); **W2** exact only in the
continuum limit + a Planck-suppressed floor; **W3** a genuine obstruction (real preferred frame).

**Banked (Rounds 1–3, all panel-closed SOUND):** R2 killed the *static-geometric* boost (the 600-cell
budget partition is positive-definite ⇒ a **compact** rotation, M²=−I, not a boost). R3 showed the **causal
A3′ retarded broadcast** carries the **non-compact** hyperbolic boost (N²=+I) *in the continuum limit*, its
invariant a fixed **speed** c (cone slope). R3 reduced W1-vs-W2 **dominantly** to **discrete dispersion
isotropy**. **Round 4 is the decider.**

## §1. The claim under review

**There is a hard no-go for any *periodic* lattice — but it does not bite CPP, because the CPP substrate is
not periodic.**

- **Part A (periodic no-go).** Any regular periodic-lattice broadcast has a bounded, Brillouin-zone-periodic
  dispersion symbol D(k)=Σ w·Σ 2(1−cos(k·d)). It can neither equal ω=c|k| (unbounded) nor be exactly
  isotropic; finite shells suppress the icosahedral anisotropy tower (l=6,10,15,…) one harmonic at a time
  but never zero it. ⇒ **exact W1 impossible for a periodic substrate (⇒ W2).**
- **Part B (the evasion).** The CPP substrate is **not** periodic: SR-1 fixes it as a φ-self-similar nested
  600-cell hierarchy (R/a=φ at every level, down to ~l_P/10³⁰) — an icosahedral **quasicrystal** (aperiodic,
  no Brillouin zone). Independently, a 600-cell admits **no** periodic Euclidean 4-tessellation (Coxeter:
  the regular flat-4-space honeycombs are only {4,3,3,4}, {3,3,4,3}, {3,4,3,3}; {3,3,5} tiles S³/hyperbolic,
  not E⁴). So the substrate is non-periodic **by necessity** — in the no-go-evading class by construction.
  Aperiodicity is the known route discrete structures use to carry exact (statistical) Lorentz (causal sets
  via randomness; quasicrystals via deterministic self-similarity).
- **Determination.** **W3 EXCLUDED** (IR/continuum is Lorentz-invariant; any floor sub-Planck tiny). Answer
  is **W1 or W2**; the W1-vs-W2 line = **quasicrystal exact-Lorentz** on CPP's own substrate. **W1 NOT
  proven** — pinned to a single decidable Round-5 question.

## §2. The S1–S5 chain

- **S1.** Model the broadcast as translation-invariant hopping on a regular lattice ⇒ dispersion symbol
  D(k)=Σ_shells w·Σ_{d∈shell} 2(1−cos(k·d)); ω=√D.
- **S2.** D(k) is a finite/periodic trig sum ⇒ bounded and BZ-periodic ⇒ cannot equal unbounded c|k|; the
  normalized phase speed √D/|k| collapses away from k=0 (verified: 0.998→0.797 at q=0.3→3.0). [A1]
- **S3.** Icosahedral anisotropy lives in harmonics l=6,10,15,…; a single z=12 shell ⇒ leading q⁴ (l=6);
  tuning a φ-shell cancels l=6 (×11 down) but leaves l=10 ⇒ finite shells never reach exact isotropy. [A2]
  ⇒ **exact W1 impossible for a periodic substrate.**
- **S4.** But CPP's substrate is φ-self-similar (SR-1) = aperiodic/quasicrystalline ⇒ no BZ ⇒ S2/S3's
  periodicity premise fails. The 600-cell has no periodic E⁴ tessellation anyway (Coxeter) ⇒ non-periodic by
  necessity. ⇒ the no-go is **evaded**, the deterministic analog of the causal-set randomness route.
- **S5.** ⇒ W3 excluded; W1-or-W2; the W1-vs-W2 line is quasicrystal exact-Lorentz (Round-5 target). W1 not
  proven; Part-B finite-shell numerics do **not** probe the aperiodic limit (stated in the script).

## §3. Triage points (attack these)

- **T1 — Scope / non-overclaim.** Is the finding honest that **W1 is NOT proven** (Part B is a structural
  evasion + corpus reading, not a demonstration)? Is upgrading W3 from "strongly disfavoured" (R3) to
  **"excluded"** justified?
- **T2 — Part-A no-go airtightness.** Is "bounded BZ-periodic symbol cannot be ω=c|k| or exactly isotropic"
  airtight for **any** periodic lattice, **including infinite-range** periodic broadcasts (still a Fourier
  series on the BZ)? Is the harmonic-tower argument (finite shells never exact) correct?
- **T3 — Part-B substrate-structure claim (load-bearing).** Is SR-1's "self-similar R/a=φ nested 600-cell"
  genuinely an icosahedral **quasicrystal** (aperiodic, no BZ)? Is the Coxeter fact (no periodic 600-cell
  E⁴ honeycomb) correct and correctly load-bearing? Is the flagged orientation-doc tension ("tessellated …
  per unit cell" vs self-similar-nested) real and **fairly** characterized (consistent under the aperiodic
  reading), not a "corpus is wrong" overreach?
- **T4 — Does aperiodicity actually evade the no-go?** Or is "no BZ ⇒ premise fails" too quick? Is the
  causal-set/quasicrystal-Lorentz analogy sound (aperiodic order ⇒ statistical isotropy)? Is the residual
  floor genuinely sub-Planck (~l_P/10³⁰)?
- **T5 — World-call + numerics scope.** Is the determination (W3 out; W1-or-W2 = quasicrystal-Lorentz) the
  right reading? Are the Part-B finite-shell numerics correctly **down-weighted** (don't probe the aperiodic
  limit)? Is an **early committed call** (ahead of Round 15) defensible or premature?

## §4. Verdict-flip criteria

The finding **flips** (not mere calibration) if any of: **(a)** the Part-A no-go is wrong — a periodic
lattice *can* be exactly Lorentz-invariant; **(b)** the substrate is actually periodic (Part B fails ⇒ the
no-go bites ⇒ forced W2); **(c)** "W3 excluded" is unjustified (a real preferred-frame channel survives);
**(d)** aperiodicity does **not** evade the no-go (quasicrystals can't carry exact/statistical Lorentz even
in principle). Wording on "excluded" vs "strongly disfavoured", the early-committed-call suggestion, and the
orientation-doc characterization are **calibration**, not flips.

## §5. Tiers (state which you used — PD-002)

- **INSPECTED** — read the argument/algebra, did not run code.
- **INDEPENDENTLY RECOMPUTED** — re-derived a step yourself (e.g. the icosahedral harmonic degrees l=6,10,…;
  the Coxeter list of regular Euclidean 4-honeycombs; the bounded-symbol argument).
- **SCRIPT-EXECUTED** — actually ran §7 and report outputs.

## §6. Read your own row (reviewer-specific steer)

**Identity discipline (read first):** in §8, put **your own actual model name** in the REVIEWER field. **Do
not adopt another reviewer's label.** Attribute nothing to a name other than your own.

- **ChatGPT —** press **T2** and **T3** hardest. Is the Part-A no-go theorem-grade (incl. infinite-range)?
  And is the substrate-structure claim (φ-self-similar = quasicrystal = aperiodic; Coxeter no-E⁴-tessellation)
  correct and correctly load-bearing? You are the rigor anchor on whether Part B is sound or hand-wave.
- **Grok —** **SCRIPT-EXECUTED** if you can. Run §7; confirm the phase-speed collapse (0.998→0.797), the
  single-shell q⁴, and the tuned-2-shell ×11-but-nonzero suppression. Independently check the icosahedral
  harmonic tower (lowest invariant l=6, then 10, 15) and the Coxeter regular-Euclidean-4-honeycomb list.
- **Copilot —** press **T4** and **T5**. Does aperiodicity genuinely evade the no-go, or just relocate it?
  Is the causal-set/quasicrystal analogy sound, and is the floor truly sub-Planck? Is the world-call
  determination right and the early-committed-call suggestion appropriately hedged?
- **Gemini (optional) —** press **T1** and the **foundational flag**. Is W1's non-proof properly hedged? Is
  flagging the orientation-doc tension appropriate, or overstepping? Is "W3 excluded" earned?

## §7. The verify code (full)

```python
#!/usr/bin/env python3
"""
2068 — Round 4 probe, CONSISTENCY-EVIDENCE ONLY (numerics are never proof).
PART A — periodic no-go: bounded BZ-periodic symbol can't be omega=c|k| (A1); finite shells suppress the
         icosahedral anisotropy tower one harmonic at a time, never zero it (A2). => periodic => W2.
PART B — evasion: the CPP substrate is phi-self-similar (SR-1) = icosahedral quasicrystal (aperiodic, no
         BZ) => Part-A premise fails. Full quasicrystal-approximant dispersion = Round-5 (not done here).
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

# PART A1 — bounded periodic symbol: phase speed collapses toward the BZ edge.
sh1=[(icosa(1.0),1.0)]
rng=np.random.default_rng(0); u=rng.standard_normal((400,3)); u/=np.linalg.norm(u,axis=1,keepdims=True)
ref=np.mean([np.sqrt(max(symbol(sh1,1e-3*kh),0))/1e-3 for kh in u])
for q in [0.3,1.0,2.0,3.0]:
    g=np.mean([np.sqrt(max(symbol(sh1,q*kh),0))/q for kh in u])/ref
    print(f"q={q:4.1f}: v_phase={g:.4f} (exact Lorentz needs 1.0000 at ALL q)")

# PART A2 — finite shells suppress one harmonic at a time, never zero the tower.
qref=0.15; a_single=aniso(sh1,qref); best=(1e9,0)
for w2 in np.linspace(-1.5,1.5,301):
    a=aniso([(icosa(1.0),1.0),(icosa(phi),w2)],qref)
    if not np.isnan(a) and a<best[0]: best=(a,w2)
print(f"single shell aniso(q={qref})={a_single:.3e}; best 2-shell={best[0]:.3e}; x{a_single/max(best[0],1e-30):.0f} but NONZERO")
```

(Full file, incl. the Part-B structural notes and conclusion banner, at the raw URL above.)

## §8. Response format

```
REVIEWER: <your ACTUAL model name — do not use another reviewer's label>
OVERALL: <SOUND | SOUND-WITH-CALIBRATION | FLIP>
TIER USED: <INSPECTED | INDEPENDENTLY RECOMPUTED | SCRIPT-EXECUTED>
T1 scope / non-overclaim:
T2 Part-A no-go airtightness:
T3 Part-B substrate-structure claim:
T4 does aperiodicity evade the no-go:
T5 world-call + numerics scope:
STRONGEST OBJECTION:
WORLD-CALL LANGUAGE (W3-excluded / W1-or-W2 / early-call):
SCRIPT OUTPUT (if SCRIPT-EXECUTED):
OTHER NOTES (calibration for v1.1):
```
