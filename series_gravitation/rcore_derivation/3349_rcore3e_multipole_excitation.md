# OPEN-GR-RCORE-3(e) — the borrowed assumption, **partially** discharged: derived for ℓ ≥ 9, still inherited at ℓ = 7–8

**Patch 3349, 30 Aug 2026 — Session 157.** Verify:
`code/3349_rcore3e_multipole_excitation_verify.py`, **8/8 PASS**
(all-FAST). Charter: the last borrowed assumption holding up the
observable echo prediction.

---

## §1 The assumption, and the route to replacing it

After Leg C the prediction rests on: *"trapped ladders exist at
ℓ ≳ 7 ± 1, **where ringdown excitation is negligible**."* That
negligibility is standard ringdown phenomenology, inherited, never
computed here, and named load-bearing in GR-2 V1.4.

The route: a trapped mode sits **below** its barrier top by
definition. External radiation must **tunnel in** to excite it, and
the excited mode must **tunnel out** to be seen. Both are the same
penetration integral Γ = ∫|k| dr over the forbidden region, with
|k| = √(−R)/Δ from the Kerr radial function already validated in
Legs B and C. The observable factor is **e^(−4Γ)**. If that alone
were tiny at ℓ_crit, the borrowed claim would be retired outright.

## §2 THE RESULT: the hypothesis is FALSE at ℓ_crit

| ℓ | ω₁ | f₁ @ 62 M_⊙ | ω_top | Γ | **e^(−4Γ)** |
|---|---|---|---|---|---|
| **7** | 1.1552 | **602 Hz** | 1.1794 | **0.404** | **0.199** |
| 8 | 1.2713 | 663 Hz | 1.3343 | 1.057 | 1.5e−2 |
| **9** | 1.3816 | 720 Hz | 1.4892 | 1.813 | **7.1e−4** |
| 10 | 1.4897 | 776 Hz | 1.6441 | 2.613 | 2.9e−5 |
| 11 | 1.5940 | 831 Hz | 1.7989 | 3.483 | 8.9e−7 |
| 12 | 1.6954 | 884 Hz | 1.9538 | 4.409 | 2.2e−8 |
| 13 | 1.7947 | 935 Hz | 2.1087 | 5.377 | 4.6e−10 |
| 14 | 1.8925 | 986 Hz | 2.2636 | 6.374 | 8.5e−12 |

**At ℓ = 7 the barrier hides the mode by a factor of five.** That is
not negligible by any standard. The reason is structural and worth
stating: **the first trapped mode sits only just below its barrier
top** (ω₁ = 1.1552 against ω_top = 1.1794, a gap of 0.024), so the
forbidden region it must tunnel is *thin*. ℓ_crit is precisely where
trapping begins, and therefore precisely where trapping is weakest.

The threshold e^(−4Γ) < 10⁻³ was **declared in the script before the
numbers were read**. It is first met at **ℓ = 9**.

## §3 What is therefore discharged, and what is not

- **ℓ ≥ 9: DISCHARGED.** The barrier factor alone (7.1e−4 and falling
  ~3.2e−2 per additional multipole, Γ ≈ 0.858 ℓ − 5.82 fitted over
  the declared domain) makes these modes unobservable without any
  appeal to the binary's multipole hierarchy.
- **ℓ = 7 and ℓ = 8: STILL INHERITED.** Their observability still
  rests on the borrowed statement that comparable-mass mergers weakly
  excite high multipoles. **This is now two named multipoles rather
  than an open-ended tail** — the item stays OPEN at sharply reduced
  scope, and a source-side excitation computation would close it.

## §4 A second discriminator, found while computing rather than sought

**The trapped high-ℓ combs are spectrally separated from the low-ℓ
line set.** They span **602–986 Hz** at the GW150914 benchmark,
entirely above the predicted line set's **211–294 Hz** — a factor 2.0
clear of its top. A search conducted in the predicted band therefore
**cannot be contaminated** by the high-ℓ ladder even if it were
excited. This is derived here, not inherited, and it protects the
observable prediction independently of §3's remaining gap.

Two independent shields now stand between the ℓ ≥ 7 ladder and the
prediction: barrier suppression (ℓ ≥ 9) and band separation (all ℓ).
The inherited source-side claim is the third, and now the weakest —
which is the right place for the weakest link to be.

## §5 Consistency

At ℓ = 6 there is **no trapped mode to suppress**, matching Leg C's
census exactly (Φ_max/π = 0.734 < ¾). The two computations meet
precisely at ℓ_crit, from opposite directions.

## §6 Honest limits

Barrier suppression only. The **source-side** question — how strongly
a comparable-mass merger drives high-ℓ multipoles — is **not computed
here** and remains inherited; §3 is explicit that it is still required
at ℓ = 7–8. Eikonal-WKB grade, inheriting Leg B's fixed-Q
correspondence and A1–A3 conditionality (OPEN-GR-RCORE-4). Γ is a
first-order WKB penetration integral without the Miller–Good
correction near the top, which is exactly where ℓ = 7 sits — so its
0.404 is the least reliable entry in the table, and it is the one the
conclusion leans on least (it is reported as a failure to discharge,
not as a discharge). Domain ℓ = 7–14 declared and asserted in code.
No amplitude, SNR, or detector-sensitivity statement is made.

## §7 Registry impact

- **OPEN-GR-RCORE-3(e): PARTIALLY DISCHARGED, scope narrowed** from
  "all ℓ ≳ 7" to "ℓ = 7–8 only". Remains OPEN.
- **GR-2 amendment queued (not enacted):** V1.4's remark says the
  negligibility is "inherited... not computed in this programme." That
  is now half wrong and should read: derived for ℓ ≥ 9 (barrier
  suppression) and for all ℓ in the search band (spectral separation);
  inherited only for ℓ = 7–8. Queued for the next GR-2 touch, since
  it strengthens rather than corrects a claim.
