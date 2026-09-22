# TODO-4188-F5SCOPE, Verified: the Conclusion Holds, the Premise Was Wrong

> **⚠ §1 STEP 2 WITHDRAWN — Patch 4212.** The founder: *"No quark has a tetrahedral cage except the
> strange quark. The only lepton with a tetrahedral cage is the Muon."* My reading of SM-3 line 123
> as "quarks have the K3 graph" is withdrawn; the discarded session's step 2 stands, and step 1 is
> now in question. Step 3 and the disposition hold. See `4212_cage_assignments_conflict.md`.

**Patch:** 4211. **Lane:** EW. **Session:** 236.
**Verify:** `series_standard_model/code/4211_cabibbo_from_mass_ratio.py`.
**Closes:** TODO-4188-F5SCOPE (the claim from the discarded Session 235). **Result:** F5 stays routed
to OPEN-SM-11; the route is right, the stated reason was a paraphrase drift; the inheritance model
gives the vertex a concrete form.

---

## 1. The claim, against SM-3 as written

- **Claim step 1** — *K3 → TBM works for leptons because the three generations share the tetrahedral
  cage.* **Holds.** SM-3 Thm (K3 Koide): leptons' masses are purely K3 ZBW modes.
- **Claim step 2** — *quarks share no cage base graph across generations, since strong mass
  dominates.* **False as stated.** SM-3 line 123 speaks of *"the tetrahedral quark cage"*; quarks
  **have** the same K3 base graph. SM-3 §"Why quarks do not satisfy Koide" says what actually
  breaks: *"qDP chain binding energy (~99% of proton mass), inter-cage bonding, and cage-depth
  scaling … break the K3 spectral symmetry."* The **graph** is shared; the **spectrum** is
  dominated by strong-sector terms that are not K3-symmetric.
- **Claim step 3** — *so CKM is a W-vertex mismatch between up- and down-type cage eigenstructures,
  routed to OPEN-SM-11.* **Holds, and the corrected step 2 makes it sharper:** both quark types are
  K3 + a large generation-diagonal strong term. A generation-diagonal dominant term gives each type
  a mass eigenbasis close to the *same* generation basis — **which is why CKM is near the identity
  while PMNS, pure K3, is near tribimaximal.** The residual K3 admixture is the misalignment.

## 2. What the inheritance model adds

At the vertex the departing orbital DP is a **down-type** eigenstate of its cage; the core's refill
forms an **up-type** eigenstate. Under G-EW-INHERIT-4205 the CKM element is the overlap between
those two eigenstructures at the refill — a definite object, not a "statistical suppression" (SF-2
§5.6 wording). The strong term being generation-diagonal is the reason the refill usually lands in
the same generation.

## 3. The target, not a result — rows verbatim (D-11)

```
sqrt(m_d/m_s) = 0.224   measured |V_us| = 0.2243   sin(theta_C)
sqrt(m_u/m_c) = 0.041   (the up-sector piece; the two enter with a relative phase)
Reading: the Cabibbo angle is the misalignment between the down-type and up-type mass eigenbases,
each = strong-dominated (generation-diagonal) + a K3 ZBW admixture; the admixture sets the angle.
```

The textbook relation sin θ_C ≈ √(m_d/m_s) is exactly what a "small K3 admixture on a diagonal
strong term" picture predicts in the SM's own language. **Whether CPP reproduces it is OPEN-SM-11's
first computable question, with SF-3's masses as input.** Not attempted here.

## 4. Disposition

F5 goes to panel on the inherited-open framing, as the entry proposed, **with step 2 corrected in the
brief.** CP phase (the 65.5° with no derivation chain, 4103) is untouched by this.

## 5. PD-008

No convenient branch. Attack: §1's reading of "tetrahedral quark cage" at SM-3 line 123 should be
confirmed in context by the next window; §3 quotes a phenomenological relation as a target only.
