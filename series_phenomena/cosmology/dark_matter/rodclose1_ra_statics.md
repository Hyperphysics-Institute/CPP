# OPEN-DM-RODCLOSE-1 R-A executed: the statics window — normalization walk, the frozen closure relation, the pre-registered comparisons, and the first derived DM formation epoch

**Patch 2542, 18 July 2026. Governed by `rodclose1_preregistration.md` (2541) ONLY. Artifact:
`code/2542_ra_statics_window.py` (all assertions pass). Blindness order enforced in both document and
code: §§1–3 are symbolic in L; §4 is the frozen comparison.**

## 1. The normalization walk (2541 input 2 — the Branch-I trigger did NOT fire)

The 2450 artifacts fully specify the stiffness: S(N) ≡ d²E/dκ² [MeV·fm²], full-rod, small-κ, on the
corrected perpendicular-plane (Frenet, arc-length) pure-bend family. Re-run this session, reproducing
the registered values exactly: S(8) = +138, S(16) = +291, chord-exact convention +263,
direction-symmetric. Per-length bending modulus B = S/(N·D): **B ∈ [14.29, 15.82] MeV·fm** (chord and
arc conventions; the N=8 value 15.0 sits inside — two-point ~L scaling coherent to 5%, the lineage's
own validation). Disclosed limitation: B is a small-κ measurement; closure curvature is
κ_ring = 2π/(L·D) (0.34 fm⁻¹ at the eventual comparison point) — the harmonic form is the
2541-frozen definition; anharmonicity at closure is unquantified in-lineage and carried in the ledger.

## 2. The symbolic bend energy and comparators

E_bend(L) = ½·B·(L·D)·κ_ring² = **2π²·B/(L·D)** (harmonic; monotone decreasing in L per the 2541 §4
entailment). Comparators per the §3 union rule — both defensible, both computed: f = 1 (per-collision
energy scale ~ kT) and f = 3/2 (mean translational KE). Accessibility: f·kT ≥ E_bend(L).

## 3. The FROZEN window objects (before any comparison)

- **Closure relation:** kT·L = 2π²·B/(f·D). Per comparator/convention: 245.3–271.5 (f=1),
  163.6–181.0 (f=3/2) MeV. **Frozen union: kT·L ∈ [163.6, 271.5] MeV.**
- **Accessibility bound:** L ≥ L_min(T) = [163.6, 271.5]/kT — one-sided (longer is easier; the 2541
  §4 entailment made this structural).
- **Survival floor:** rings closing at kT persist iff kT < E_endbond ∈ [40, 170] MeV (input 3).
- **Upper (long-rod) cutoff:** requires collision duration/frequency content → **Branch I, NB-S3a-1
  named** (pre-registered R-B/R-C expectation; confirmed — no statics-admissible long-rod content was
  found beyond the objects above).

**Consequence frozen before comparison: the statics alone yields a RELATION (a hyperbola in (T, L))
plus a one-sided bound — not a two-sided L-band. The L-SELECTION requires the kinetic limb. Per 2541
§6 this routes to the banked-partial reading, NOT the win-class 16-in-band reading.**

## 4. The pre-registered comparisons (window frozen above; 16 appears only here)

- **(a) The derived formation epoch:** closure at L = 16 requires **kT_form ∈ [10.2, 17.0] MeV**
  (union band; E_bend(16) = [15.3, 17.0] MeV). This is the first derived DM formation temperature in
  the programme — statics-strength, conditional on the consumed L = 16, harmonic, comparator-union.
  Physical placement: between the QCD transition (~150 MeV) and BBN (~1 MeV); ring mass 11.264 GeV ≫
  kT_form ⇒ non-relativistic at formation, CDM-like — consistent with the candidate's registered
  phenomenology without adjustment.
- **(b) Net closure energetics:** ΔE_close(16) = E_bend − E_endbond = **[−154.7, −23.0] MeV** —
  closure is strongly exothermic net of the end bond across the entire input-3 band.
- **(c) Survival self-consistency:** kT_form(hi) = 17.0 < 40 MeV = E_endbond(lo) ⇒ rings closing at
  the derived epoch survive it. CONSISTENT.
- **(d) The carried kT_form ≈ 16.5 keV (2541 input 5):** demands L_min ∈ [~9.9×10³, 1.6×10⁴] planes —
  **INCONSISTENT with L = 16 by ~3 orders. RECORDED, not repaired** (per the 2541 §6 frozen note).
  Diagnosis offered for founder adjudication: the 16.5 keV value entered the corpus tied to the now-
  retired hTetra epoch anchor; the §6g bending anchor supplies its own epoch. Formal retirement of the
  carried value is a physics adjudication — routed to the founder, not taken here.
- **(e) Cross-lineage echo (NOT an input; consumes nothing):** the dance-lane ring−straight result
  (−68.8 ± 6.5 MeV, 2455 lineage, a different functional including the strong-sector wells) sits
  INSIDE the ΔE_close(16) band; the back-implied E_endbond ≈ 85 MeV lies within input 3's band and
  within ~17% of the 102 MeV contact lock. Recorded as an echo; nothing promoted on it.
- **Fence note:** no new √5 enters this derivation; α_s = 5/(8φ) appears upstream inside the
  registered 2450 functional (pre-existing lineage), noted per procedure.

## 5. Reading (per 2541 §6, frozen)

**BANKED PARTIAL.** Delivered: the closure relation kT·L ∈ [163.6, 271.5] MeV; the derived
conditional formation epoch kT_form(L=16) ∈ [10.2, 17.0] MeV; net-exothermic closure; survival
self-consistency; the 16.5 keV inconsistency recorded. Blocked: the two-sided L-selection — **Branch I
with the long-rod kinetic cutoff as the named blocker (NB-S3a-1)**. The win-class 16-in-band reading
does NOT fire (the statics cannot select L; asserting it did would be the trap in kinetic dress). No
composition reading (2541 §0 scope limit; none taken). No dispatch (partial, not a closed window);
the T_form result joins the standing disclosure package for whenever a win-class dispatch next fires.

## 6. Conditionality ledger (travels with every use of these numbers)

Harmonic extrapolation from small-κ stiffness to closure curvature (unquantified anharmonicity);
B from a two-point L-scaling (5% coherence); comparator union spread (factor 3/2); E_endbond carried
as the full [40, 170] MeV band; L = 16 consumed, not derived (blindness protocol honored — the
formation-side route to 16 remains open pending the kinetic limb); kinetic limbs Branch I throughout.

---

## 7. REVISION RIDER (Patch 2552, 18 July 2026 — licensed by the ENDBOND-3 banked pin, 2551)

The dance-strength closure measurement (OPEN-DM-ENDBOND-3, `endbond3_ra_curve.md`) pins
the net closure energetics directly: **ΔE_close(16) = [−137.5, −128.9] MeV (±2 MeV
chaotic-floor rider)**, superseding this document's §4(b) statics-band value
[−154.7, −23.0] — a collapse from a 132 MeV width to ~9 MeV, landing inside the old band.
Consequences, per the 2548/2550 pre-registered propagation:

- **§4(b) net closure energetics: REVISED to the dance pin.** Closure is strongly
  net-exothermic with no barrier at the registered grid resolution (κ* = 0, dt-stable);
  the ratchet picture strengthens — no impulse threshold required at this resolution.
- **Survival margin: COLLAPSED accordingly** (the closed ring sits 129–138 MeV below the
  straight rod at dance strength; the statics-side survival floor is superseded by the
  direct measurement).
- **kT_form(L=16) ∈ [10.2, 17.0] MeV: EXPLICITLY NOT COLLAPSED** — the band is
  comparator/convention-dominated (2544 §0, 2548 §0, restated at every step); the closure
  relation kT·L ∈ [163.6, 271.5] MeV and the epoch band stand unrevised.
- **E_endbond as a separate carried quantity:** the [40, 170] input-3 band is superseded
  FOR NET-CLOSURE USES by the direct ΔE_close pin (the dance does not decompose bend from
  bond — barrier-free curve); the mixed-lineage orientation arithmetic (statics E_bend +
  dance ΔE_close → implied seam bond [144, 155] MeV) is carried for orientation only,
  NOT a pin (2551 §4).
- Conditionality ledger (§6): unchanged in kind; the L = 16 consumption now additionally
  cites the ENDBOND-3 use under the same rider.
