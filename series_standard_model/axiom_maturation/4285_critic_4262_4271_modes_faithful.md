# PD-008 Critic of 4262 and 4271: Both Implementations Faithful; Free-Nucleon Mode Conditional Sharpened

**Patch:** 4285. **Lane:** EW → strong (TODO-4284-MODECRITIC, final critic item). **Session:** 240.
**Verify:** `series_standard_model/code/4285_critic_modes_geometry_check.py`. All checks PASS.
**Critiques:** 4262 (u's diagonal mode, g_A 1.333 → 1.310) and 4271 (μ_n correction, neutron frame, free-nucleon g_A 1.294–1.297).

## 1. 4262 — the u's diagonal mode

### 1.1 What the critic must check

The detail handover §4 flags 4262 and 4271 as modes "adopted from founder pictures, which help g_A." The test is
whether each implementation goes beyond its picture. For 4262, the critical steps are: (a) the geometric claim
about the 30.3° angle; (b) the equal-width rule that sets the new mode's ground-state spread equal to the radial
mode's; and (c) the conclusion that both ups are held.

### 1.2 The geometry (D-11 cross-check)

4262 §1 states the u's two in-plane mode lines (u–d edge and u–u line) are 30.3° apart, with sin 30.3° = 0.505.

From SS-2's frame (u–d = 0.620 fm, u–u = 1.071 fm), law of cosines at u₁:

```
cos θ = r_uu / (2 × r_ud) = 1.0710 / 1.2400 = 0.8637
θ = 30.26 deg  (fragment rounds to 30.3 deg — correct to 1 d.p.)
sin(30.3 deg) = 0.5045 ≈ 0.505  (fragment correct to 3 sig figs)
```

The claimed geometry is verified. The transverse component 0.505 × r_ZBW is the mode's spread across the
previously unlocalised axis, which is the number that enters R_u.

### 1.3 The equal-width rule

The fragment says: under route (H) every ZBW mode runs at the Compton frequency, so the diagonal mode has the
same ground-state width as the radial one "whatever the strength of the charge-only binding."

This is a genuine consequence of the pass-through ruling (4265), not an additional postulate:
- Route (H): ω = m_q c²/ħ (fixed by mass).
- Pass-through at speed c: ω × amplitude = c → amplitude = ħc / (m_q c²) = ħ/(m_q c) = r_ZBW.
- r_ZBW depends on m_q only. A weaker binding changes the ZBW phase in that mode's well, not its amplitude.

**The only question the equal-width rule leaves open is WHETHER a mode exists at all.** If no binding holds u_e
toward the diagonal −qCP, the mode is absent; the width of a non-existent mode is irrelevant. That is the filed
question in 4262 §4.

### 1.4 The filed question: u_e's diagonal pull

At 4262 §3(ii): u_e sits at the −eCP vertex; its diagonal is the −qCP, where u_q already sits. The charge
balance there is −2/3 (from −qCP) + 2/3 (from u_q's core) = 0. If the pull is charge only, it cancels. 4262 §4
asks the founder: is the attraction strong-force (u_e's +qCP core pulled toward the −qCP vertex regardless of u_q
being there) or charge-only (and therefore zero)?

4262's last row gives the alternative: with u_e unheld, g_A = 1.369 (+7.4%) before exchange. This is a large
difference from 1.310, and the exchange cannot be computed for the unheld state.

4263 answered this question in passing ("no bound and no loose quarks, only oscillating ones; a quark falls into
superposition with ... the diagonal vertex when open") but did not explicitly address the u_q-blocking scenario.
**The question is still open.** The critic leaves it exactly as filed at 4262 and adds nothing.

### 1.5 Verdict on 4262

The implementation is faithful to the founder's "attracted to (ZBW oscillation with) the diagonal negative
vertices" ruling. The geometry is verified. The equal-width rule is route-(H) mechanics. The one real gap (u_e's
diagonal) was explicitly filed with its alternative row. Nothing in the implementation overreaches the picture.

**The convenience is in the picture itself.** If the founder's ruling is accepted as stated, the diagonal mode
follows, and 1.310 is the zero-parameter result. Reversing it requires a different reading of 4262 or a new
ruling.

---

## 2. 4271 — μ_n correction, neutron frame, free-nucleon diagonal mode

### 2.1 Neutron frame

4271 §1 derives: u on −qCP, d₁ on +qCP, d₂ on +eCP, −eCP open. This is obtained by applying 4270's seat rules
("up bonds to 2 of 4 vertices, minus only; down to 4 of 4") and the standard beta-decay SU(3) flip (the quark
that migrates is the +qCP core). **This is unambiguous.** The like pair (dd) sits on the repulsive (+,+) diagonal;
the odd quark (u) sits at the apex. The neutron is the proton's mirror.

The SS-2 conflict (three minus vertices for a two-minus hTetra; u on a plus vertex) is correctly noted and
superseded. The filing of a paper correction is required.

### 2.2 The μ_n role-correction

Scripts 4244–4269 computed μ_n = (4μ_d − μ_u)/3 with R assigned by flavour: R_like = R_u (proton's like pair),
R_odd = R_d (proton's odd quark). In the neutron's own frame the d's are the like pair and the u is the odd quark,
so R must be assigned by role. The correction is:

```
4262 ruled state, m_q fitted to mu_p:
  old (flavour): mu_n = -1.884  (-1.5%)
  corrected (role): mu_n = -1.871  (-2.2%)
```

This is unambiguous — it follows from the neutron-as-mirror with no additional assumption — and it is the **correct
reading** of 4270. The −2.2% result is worse than the −1.5% the scripts reported, which is an honest finding.

### 2.3 The free-nucleon diagonal mode

In a free proton the +eCP vertex is open. 4271 §3 claims the odd quark (d) then gains a diagonal mode toward the
open +eCP, by the same logic as 4262 applied to the u. The founder's 4270 text is:

> "The down quark **may be able to take turns** residing at every vertex (even the empty +eCP vertex if the
> neutron is free/unbonded). **This depends upon** the neutron's linear −eCP being able to localise on one side of
> its +qCP core, away from the −qCP or −eCP vertex."

The founding language has two features that matter:

1. **"May be able to"** — this is a possibility ("if the neutron is free") and a conditional, not an unambiguous
   ruling. Compare 4262's "attracted to (ZBW oscillation with)" — that is a definite statement.

2. **An unverified condition** — the d's access to the +eCP "depends upon" its linear −eCP localising correctly.
   4271 does not check this condition.

4271 §5 (PD-008) already acknowledged this: "It is adopted because it follows directly from the founder's 4270
rule and 4262's mode rule, both founder statements, not because of the improvement." That framing is exactly right,
and the critic endorses it. What the critic adds is a sharpening of the contrast:

- **4262's diagonal mode** for both ups rests on a **definite ruling** ("attracted to"). It is a ruling.
- **4271's diagonal mode** for the odd quark rests on a **conditional possibility** ("may be able to"). It is an
  inference subject to the unverified localisation condition.

The distinction does not overturn 4271's result; it sets its epistemic status. The free-nucleon g_A 1.294–1.297
should be read as: *if the d's linear −eCP can localise away from its vertex when the +eCP is open, then the odd
quark gains a diagonal mode, and g_A shifts to this bracket.* The μ_n moves the other way (−2.2% to −2.7%,
recorded in 4271 §4), which is cost acknowledged.

### 2.4 Geometry check (D-11)

The verify script confirms:
- Neutron dd edge 1.0692 fm vs proton uu edge 1.0710 fm: −0.17% (4271 row (1) correct).
- Mode shift: −0.013 to −0.016 in g_A relative to the bound-nucleon value (4271 rows confirmed).

All rows were computed at SS-2's frame. 4284 established that SS-2's frame misses r_p by +11.6% at one m_q.
The mode shift itself is roughly frame-independent (it is set by the angle subtended by the open vertex, scanned
0–90° in 4271 to give the 0.003 spread). The base g_A shifts with the frame per 4284 table D; at a smaller
frame t the bound-nucleon g_A is lower, and the free-nucleon g_A follows proportionally.

### 2.5 Verdict on 4271

- **Neutron frame and μ_n role-correction: solid.** Both follow unambiguously from 4270's seat rules with no
  added assumptions. The μ_n worsening is honestly recorded.

- **Free-nucleon diagonal mode: reasonable inference, conditional.** It follows from "down bonds to 4/4" applied
  symmetrically to the free proton, but "may be able to" is weaker than 4262's "attracted to," and the
  localisation condition is not verified. 4271's PD-008 correctly calls it a convenient branch. No reversal.

---

## 3. Interaction with 4284

4284 showed that g_A is unpinned (1.242–1.282) once the frame is not fixed by r_p. All of 4262's and 4271's g_A
values were computed at SS-2's frame, which 4284 places at +11.6% on r_p. The mode mechanism findings (the angle,
the exchange term, the equal-width rule, the role correction) are frame-independent; the numbers attached to them
are not. **The mode results should be cited as "at SS-2's frame."**

Nothing in 4262 or 4271 is reversed by 4284. The modes are correctly implemented; the frame in which they were
evaluated is the one needing revision.

---

## 4. PD-008 (my own branches)

The convenient framing would be: "both implementations are faithful, so both g_A values stand." The honest content:

- 4262's 1.310 is conditional on u_e being held by the strong force (the filed question). If u_e is not held,
  the number before exchange is 1.369, and the exchange cannot be applied in the same form.
- 4271's 1.294–1.297 is conditional on the d's localisation at the +eCP and uses a frame that misses r_p. At
  a frame consistent with one m_q the base g_A is lower; the mode shift is the same but the starting point is not
  the same.

Neither of these is a reason to withdraw the results as records. They are reasons not to treat them as predictions
until the open conditions are settled.

**NOTHING-DEFERRED** — this patch closes TODO-4284-MODECRITIC. The remaining open items are already in
todolist.md: TODO-4284-RPFLOOR (what closes r_p), TODO-4284-PAULIFRAME (Pauli energy vs hTetra bonds),
TODO-4284-SF2V109 (SF-2 paper edits), TODO-4264-PASSTHROUGH (i)(ii) (quark orbital well, nucleon moments at g).
No new deferrals arise here.
