# CPP Potential Solutions Registry

Tracks specific candidate mechanisms for open problems.
Distinct from the open problems register (which states *what* is open)
— this records *how it might be solved* before the idea is lost.

Format: each entry gives the OP it targets, the mechanism, its origin,
and the tractability estimate.

---

## PS-1: Grok's exact-volume + PSR + interference mass ladder
**Targets:** OP-SS-1 (quark mass ladder)  
**Origin:** Grok, 24 March 2026 session  
**Status:** Concept sound; numerical implementation not yet verified  
**Mechanism:**  
The structural quark mass for cage depth n is:

    M_q(n) = Σ_{l=1}^{n}  N_l · E_eDP · V_l^proj · (r_eff^(n)/r_l)³ · C_n

where:
- `V_l^proj` = exact 3D-projected Voronoi volume of 600-cell shell l
- `r_eff^(n)` = PSR-compressed radius from multi-shell SSV
- `C_n = |Σ_{m=0}^{n} e^{i·2πm/φ²}| / n` = inter-shell phase cancellation

**Why it was deferred:** Grok's mass table (112, 1480, 4620, 195000 MeV) 
was verified by Sonnet and Opus to be PDG × 1.15 — fabricated, not computed 
from the stated formula. The concept was not tested with actual computed values.

**What needs to be done to test it:**
1. Compute the exact 3D-projected Voronoi volumes for shells 1–4 from
   600-cell vertex coordinates
2. Compute C_n numerically for n=1,2,3,4 (already done: 0.72, 0.24, 0.36, 0.07)
3. Evaluate the full formula with these numbers and compare to PDG
4. If within ~20%, apply the derived ZBW correction

**Tractability:** One focused session with code. High priority.

---

## PS-2: Aharonov-Bohm self-energy loop for Koide phase θ
**Targets:** OP-SM-7d (Koide phase θ from SSV dynamics)  
**Origin:** Claude Sonnet, Session E, 24 March 2026  
**Status:** Identified as tractable; not yet attempted  
**Mechanism:**  
The eCP at apex V4 exchanges virtual DPs with the base vertices {V1,V2,V3}
via the K3 triangle loop. If there is a magnetic-like flux Φ through the
K3 triangle (from the ZBW orbital angular momentum), the self-energy
acquires an Aharonov-Bohm phase:

    δE_AB = f(sea_strength) · e^{i·Φ/Φ₀}

where Φ₀ = hc/e is the flux quantum. This phase would select a preferred
orientation θ in the antibonding subspace.

**Physical picture:** The ZBW orbital circulates around the K3 triangle.
The circulation generates an effective magnetic flux. The eCP at V4,
exchanging DPs with the base, picks up the AB phase from this flux.
This is analogous to the Berry phase in molecular systems.

**The computation needed:**
1. Compute the effective magnetic flux from the ZBW circulation on K3
   (ω_ZBW × Area_K3)
2. Compute the self-energy diagram: V4 → V_i → V_j → V_k → V4 (triangle loop)
3. Extract the AB phase and check if it equals 2.267° = Δθ

**Key question:** Is the ZBW orbital on K3 chiral? If the three modes
have a preferred circulation direction (e.g., from the 3D orientation of
the tetrahedral cage in the 600-cell), the AB flux is non-zero.

**Connection to existing results:**
- The critical angle 3π/4 comes from the K3 stability condition (derived)
- The correction Δθ ≈ (5/4)sea² is fitted to 0.15% — the AB phase
  should reproduce this coefficient if the mechanism is correct

**Tractability:** Medium. Requires computing the K3 triangle area in
physical units (from r_conf and the 600-cell geometry) and a one-loop
self-energy diagram. One focused session.

---

## PS-3: Löwdin downfolding with non-uniform apex coupling
**Targets:** OP-SM-7d (Koide phase θ)  
**Origin:** Claude Sonnet, Session E, 24 March 2026  
**Status:** Analytically ruled out for uniform coupling; may work for
             non-uniform coupling  
**Mechanism:**  
Session E showed that the uniform apex coupling v = (1,1,1)/√3 decouples
completely from the antibonding modes (they are dark to V4). However, if
the coupling is NON-UNIFORM — e.g., if the eCP ZBW orbital creates a
non-trivial SSV pattern on the base vertices — then the Löwdin downfolding
H_eff(E) = A_K3 - (1/E)·v·v^T would have v with antibonding components,
breaking the degeneracy.

**What would make the coupling non-uniform:**
- If the eCP at V4 is in a ZBW eigenstate that preferentially couples
  to one antibonding direction (a self-consistency requirement)
- If the 600-cell embedding breaks the symmetry between V4-V1, V4-V2, V4-V3
  at higher order in sea_strength

**Tractability:** Low for this session. Would require knowing the full
600-cell vertex coordinates and computing the exact SSV coupling between V4
and each base vertex in the 4D geometry projected to 3D.

---

## PS-4: Electroweak identification of θ with PMNS phase
**Targets:** OP-SM-7d (Koide phase θ)  
**Origin:** Claude Sonnet, Session E, 24 March 2026  
**Status:** Speculative; requires electroweak sector development  
**Mechanism:**  
The Koide phase θ appears in the charged lepton mass matrix in exactly
the position occupied by the CP-violating phase δ_CP in the PMNS matrix.
If θ = f(δ_CP, θ_PMNS mixing angles), then θ is not derived from the
lepton cage geometry alone — it requires the full electroweak sector.

**Known numbers:**
- θ_Koide = 132.73°
- PMNS δ_CP ≈ 197° (NuFIT best fit) — not directly related
- But the FULL PMNS phase structure might produce θ_Koide through a
  combination of charged lepton and neutrino rotation matrices

**Tractability:** Low until OP-EW-1 is further developed.

---

## PS-5: φ¹¹ and φ¹⁷ exponent derivation
**Targets:** OP-SM-5 (lepton mass mechanism) / OP-SM-7d  
**Origin:** Computed from observed masses, Session B, 24 March 2026  
**Status:** Empirical observation; no derivation yet  
**Mechanism:**  
m_μ/m_e ≈ φ¹¹ to 3.8% and m_τ/m_e ≈ φ¹⁷ to 2.7%.
The exponents 11 = z - 1 (coordination number z=12 minus 1) and
17 = z + 5 (z plus icosahedral faces per vertex).

**What a derivation would look like:**
- Show that the lepton mass ratio involves φ raised to a power
  determined by the 600-cell coordination geometry
- 11 = z - 1 removes the apex contribution (1 less than full coordination)
- 17 = z + 5 adds the first icosahedral shell contribution

**Connection to Paper 4:** If φ¹¹ can be derived, it provides an
independent check of the Koide formula predictions. Currently the
3.8% deviation from exact φ¹¹ is consistent with higher-order corrections.

**Tractability:** Medium. Would require a group-theoretic analysis of
the 600-cell adjacency structure.

---

*Last updated: 24 March 2026*  
*Next: PS-1 (Grok's mass ladder) and PS-2 (AB self-energy) are the*
*highest-priority items for the next focused session.*
