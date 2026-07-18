# NB-F-1-T — mandatory input audit (handover step (i)–(iii)): what the corpus registers, at what depth, for the three-term ΔE_b decomposition, E_act, and the composition step

**Patch 2536, 18 July 2026. Status: AUDIT ONLY — no derivation performed, no reading taken.**
**Executed per the 2534/2535 handover's mandatory-first-step instruction; findings recorded before the
pre-registration (next patch). Grep provenance: every claim below was grepped in the live clone this
session; file/line anchors given.**

## (i) Bond lengths, stiffnesses, ZBW statics

**(i-1) DP internal binding scales — REGISTERED at DM-lane derivation depth (0880; re-confirmed in-situ
at 2452):** E_eDP = 88 MeV, E_qDP = 264 MeV = 3·E_eDP (color factor 3), E_hDP = 152 MeV =
√(E_eDP·E_qDP). The element mass identity 4·264 + 4·88 = 1408 MeV (SF-3 constituent ladder; 2452
zero-parameter mass lock) uses these values exactly. **Caveat travelling with them (0834/TODO-016):**
the *ratio* structure is clean and derived from charge geometry; the *absolute* scale has an
unreconciled r_min question in the DP-Sea appendix (flagged for founder flagship edit). For a
channel-energy comparison the ratio structure suffices; the caveat is carried, not resolved here.

**(i-2) E_ee (the e–e edge/scission bond) — NOT pinned.** Registered only as a band: E_ee = η_screen ·
1.44 MeV with η_screen ∈ [~6×10⁻⁴, 1] ⇒ E_ee ∈ [0.8 keV, 2 MeV] (0865 robust shoulder; the E_bond-pin
make-or-break, handover 2026-06-28, did not close — it reduces to the shared SSV-charge-sum root,
OPEN-FP-SF-2-η-adjacent). Ordering E_qq > E_ee is sign-certain (screening geometry). **Depth: banded,
not derivation-strength.** NOTE the scale tension to be handled honestly in the prereg: (i-1)'s E_eDP =
88 MeV is the eDP *internal* binding; (i-2)'s E_ee ∈ [0.8 keV, 2 MeV] is the *inter-element edge* bond
in the DM-1 aggregate lane. These are different bonds in different structures; which one prices the
tetra's e–e edge is itself a registration question the prereg must not silently decide.

**(i-3) E_qq — map-strength window only.** 40–170 MeV (DM-lane harmonic/Morse well map, 2444/dance
lane); ~66 MeV core reference; ~600 MeV transverse-fracture wall (SF-5 G3). **Depth: band/map, not a
pinned number.**

**(i-4) Lengths:** l_unit = 0.589 fm (glossary, derivation-strength via f_π and α_s convergent routes;
lattice edge 0.364 fm); a_q = 1.15 fm element edge, R_e = 1.301 fm coat radius (Candidate-B
registration); qDP bond length 1.0–1.3 fm (0835, λ ≈ ℏc/E_hDP ≈ 1.3 fm). **No registered equilibrium
bond lengths for the free eDP, free qDP, or tetra edges at the tetra's own scale** — the distortion
term's δℓ inputs are unregistered.

**(i-5) Stiffnesses:** no registered bond stiffnesses (k in ½k·δℓ²) at derivation strength anywhere in
the corpus. Dance-lane well parameters exist at simulation-input depth only. Inertias ARE pinned:
m_qCP = 132, m_eCP = 44 MeV/c² (2496 blind statics pin; 2452 in-situ derivation, convergent) — usable
for E_act path dynamics IF stiffnesses were available; they are not.

**(i-6) ZBW statics:** Part I §3's "Each attractive bond stores ZBW energy, probably an ℏ unit of
action" (founders_vision.md line 53) is **vision-tier and self-qualified ("probably")** — not
promotable to a number without Branch T. No quantitative ZBW-per-bond registration exists elsewhere.

## (ii) SSV_abs quantitative formalization (for the color-in-tetra term)

**NONE registered.** SSV_abs appears at structural/qualitative strength throughout
(programme_orientation: sets local c, time dilation; SR sector: Lorentz from SSV_abs/PSR; 2028 scalar-
SSV universality grounding) — but **no formula converting SSV_abs stress into bond-energy deepening
exists anywhere in the corpus.** The color-in-tetra term therefore has: sign (−) registered at founder
authority (§6f Second Addendum: SSV_abs-deepened q–q binding); **magnitude unregistered, with no
registered route to it short of the SSV charge-sum framework** (the same root that blocked the E_bond
pin, (i-2)).

## (iii) The storage-asymmetry term (ZBW-storage vs compression-storage)

**No registered discriminating input.** ZBW side: vision-tier "probably ℏ" only ((i-6)). Compression
side: the 2534 founder ruling registers the *mechanism* (attractive tension holds compressed repulsion;
disassembly refunds as KE) at founder-ruling strength, with **no quantitative model**. Whether the
stored quantum in an attractive ZBW bond and the stored compression in a repulsive edge are equal,
and what asymmetry survives at second order, has zero registered content. Sign stays "?".

## Audit verdict (feeds the prereg directly)

1. **One live quantitative route exists:** the leading-order channel comparison via the registered DP
   scales (i-1) + the 2532/2534 theorem-grade leading-order structure. Everything else is banded,
   vision-tier, or absent.
2. **The three second-order terms:** distortion (+) — sign theorem-grade (positive-definite), magnitude
   Branch-I (no lengths/stiffnesses, (i-4)/(i-5)); color-in-tetra (−) — sign founder-registered,
   magnitude Branch-I ((ii)); storage asymmetry (?) — wholly Branch-I ((iii)).
3. **E_act:** requires the minimum-barrier assembly path through asymmetric configurations where the
   2532 cancellation fails — needs the same unregistered stiffnesses plus path dynamics. Expected
   Branch-I.
4. **The composition step:** rate-vs-ambient comparison = NB-S3a-1 territory; constructing rates
   in-campaign = Branch T by the standing 2521 pre-commitment. Pre-registered honestly as the expected
   Branch-I terminus even on a computed ΔE_b.
5. **Bond-identity question surfaced ((i-2) note):** which registered scale prices the tetra's e–e and
   q–q edges (DP-internal 88/264 vs aggregate-edge band) must be adjudicated ONCE, from registration
   depth, in the prereg — before any number is used.
