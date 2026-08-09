# E-1 EXECUTED — CLASSIFICATION OF THE AUTOMATON TRANSPORT IMPLEMENTATIONS AGAINST VERSION A / VERSION B (W-5)

**v1.1 (Patch 3036, 9 Aug 2026): CONV-013 Q4 ruling executed - E-1
CONDITIONALLY ADOPTED (AMEND 3/5 [GPT][DS][COP]; REJECT did not carry,
the rescue-by-reinterpretation charge resolving into amendment (2)).
The three enacted amendments are folded: (1) the 2887 finding now
carries the DUAL HISTORICAL RECORD (SS2.2a) - anomaly under the
superseded ontology / predicted negative control under the ratified
one, both readings preserved and dated [GPT]; (2) the negative-control
REPLICATION PROTOCOL is published and ONE INDEPENDENT SEEDED negative
control demonstrating the origin-deletion prediction is executed -
`code/3036_e1_negative_control.py`, 4/4: per-bit FCC walker, new code,
new seed; origin-deleted arm alpha = 0.483 (vs 2887's field-level
0.478 - two independent implementations, one exponent),
origin-retained contrast arm alpha = 0.994 in the SAME harness [COP;
discharges [DS]'s proof demand]; (3) the AUTOMATON-2 classification
carries an EXPLICIT WITHIN-MOMENT-ONLY scope statement (SS2.2, table)
[COP].**

**Patch 2991 (4 Aug 2026). Executes work-plan step E-1 of the
RELAY-MECH-1 charter (`relay_mech1_charter.md` §5, as amended 2957 →
2958: classify against Version A/B, the canonical post-fork
vocabulary). This was, at v1.0, a re-read/classification task: every number
cited in the v1.0 text is from a registered record (arc closure 2812;
front-class finding 2887; directed-relay execution 2889), with no new
computation performed. (v1.1 note: amendment (2) DID require a new
computation - the independent seeded negative control - and its verify
script `code/3036_e1_negative_control.py` is owed and supplied.) The charter names "the two
AUTOMATON relay implementations"; the corpus now carries THREE
registered transport implementations (the directed relay of 2888/2889
postdates the charter), and all three are classified — the complete
scope, not the literal one.**

## §1 — The canonical mechanisms (classification targets)

**Version B (ADOPTED, founder ruling 2958):** hop-by-hop EVEN-SPLIT
OUTWARD relay — one volley per GP per (sub-)Moment, split equally over
the edges that increase distance-from-origin (read from the DI-bit's
ORIGIN ADDRESS, P-1 content), equal hop count N to the PSR; DI-bits
reset per hop (V-2); count-like magnitude, no phase (AP-2, ratified
2989).

**Version A (SET ASIDE, same ruling):** direct addressed
GP_origin → GP_PSR broadcast in one step.

## §2 — Classification

### 2.1 AUTOMATON-1 (engine `code/2797_automaton1_engine.py`, founder Moment rule 14–18 + DR-1..3)

**Update rule (read from the engine):** each Moment, the payload at
every source point is transferred DIRECTLY to the radius-R shell,
uniformly over the |S_R| shell sites (`K = shell/S`); carriers erased;
SSV_net from radial unit vectors, SSV_abs from gross counts.

**Class: VERSION A** — the transport step is origin→shell in one
synchronous step with no intermediate GP mediation; this is the direct
broadcast the founder set aside.

**What its evidence bears on:** the registered inverse-square result
(V-1R: ratio-flat ±2.9%, Δp ≤ 0.022, 3/3 R, vs Ewald reference; arc
closure 2812 §1.1) is C-2 evidence at the SHELL-ARRIVAL level — the
counting 1/r² given uniform arrival over the shell. Version A and
Version B agree on exactly that endpoint distribution (B's N-hop
even-split composition lands uniformly by I_h equivariance, FACT G1),
so A-1's C-2 evidence is MECHANISM-CLASS-SHARED: it supports the
counting inverse-square under either transport and does not
discriminate A vs B. It is not C-1 evidence for either (a single-step
endpoint rule exhibits no transport to be ballistic or otherwise).

### 2.2 AUTOMATON-2 (engine `code/2802_automaton2_engine.py`, ratified C19–C30 spec)

**Update rule (read from the engine):** per-Moment kernel W_R =
`front_kernel(R)` — starting from the origin, R successive hops, each
splitting the weight EQUALLY over the strictly distance-increasing
12-neighbors (FCC adjacency, the 3D z=12 analog of the 600-cell
coordination), conservation exact (Σw = 1 asserted). Applied each
Moment by translation-invariant convolution; the resulting front Q is
re-aggregated and re-emitted the next Moment with the same kernel.

**SCOPE STATEMENT (v1.1, enacted amendment (3)):** every Version-B
classification claim for AUTOMATON-2 in this document - and every
piece of C-1/C-2 evidence credited to it - is WITHIN-MOMENT ONLY.
AUTOMATON-2 instantiates the Version B composition inside a single
Moment and instantiates NO registered mechanism class across Moments;
no multi-Moment claim of any kind is made on its behalf, and any
future citation of A-2 evidence must carry this scope qualifier.

**Class, WITHIN one Moment: VERSION B, in reduced form.** W_R is
exactly the R-fold composition of Version B's per-hop rule (even-split
+ outward-only + conservation); the translation-invariance reduction
precomposes the sub-Moment hops analytically instead of simulating
them tick-by-tick, which is exact for count-like content. The
registered pointwise inverse-square at R = 4 (±0.4%, Δp = 0.010,
3/3 R, tightening with hop count; 2812 §1.1) is therefore DIRECT C-2
evidence for the Version B composition, and the outward-only front at
exact graph distance R is the within-Moment expression of C-1.

**Class, ACROSS Moments: NEITHER.** The engine reduces the field to
scalar Q at each Moment boundary and re-steers outward from the
CURRENT front (translation invariance), i.e., it DROPS the origin
address at every Moment boundary. Finding 2887 measured the
consequence: <r> ~ t^0.478, diffusive, no light cone.

### SS2.2a - The 2887 finding: the DUAL HISTORICAL RECORD (v1.1, enacted amendment (1))

Both readings are the record; neither erases the other.

**Reading 1 - as registered (pre-2957 ontology): ANOMALY.** At its
registration the 2887 diffusive result stood as an unexplained
failure of a ratified engine to exhibit the expected light cone. That
status was real, was earned by measurement, and is preserved here as
history: under the ontology in force at the time, the finding was an
anomaly, full stop.

**Reading 2 - under the ratified ontology (2957 P-1 / synthesis v2):
PREDICTED NEGATIVE CONTROL.** P-1 makes the origin address the
load-bearing content whose retention steers the ballistic front;
A-2's multi-Moment dynamics deletes precisely that content at every
Moment boundary, and synthesis v2 (2957 SS4) predicts exactly this
consequence for address-free re-emission: no address, no light cone.
Under the ratified reading the same measurement is a confirming
control of the Version B logic.

**Why Reading 2 is not rescue-by-reinterpretation (the [COP]/[DS]
demand, discharged by measurement):** a reinterpretation earns
evidential standing only if the reinterpreting prediction survives an
INDEPENDENT test it could fail. Executed at this patch:
`code/3036_e1_negative_control.py` (protocol published in the script
header; frozen verdict bands; seeded, deterministic, replication
exact). A per-bit FCC walker - new code, independent of both the
field-level A-2 engine and the 2888/2889 directed relay - runs the
origin-DELETED dynamics and the origin-RETAINED dynamics in the same
harness: deleted arm <r> ~ t^0.483 (diffusive; independently
convergent with 2887's field-level 0.478), retained arm
<r> ~ t^0.994 (ballistic), ratio 11.5x at T = 200, within-Moment
ballisticity in both arms. The prediction discriminates and lands
where the ratified ontology says: the reclassification is a tested
claim, not a relabeling. The transition Reading 1 -> Reading 2 is
dated (ontology 2957; classification 2991; independent control 3036)
and the anomaly period remains on the books.

### 2.3 The DIRECTED RELAY (execution 2888/2889, `automaton_directed_relay_execution.md`)

**Update rule (from the execution record):** each bit persists in its
initial FCC direction across Moments — per-bit direction memory
carried through Moment boundaries.

**Class: VERSION B multi-Moment front, PROXY implementation.**
⟨r⟩/t = √2 exactly at every Moment, fitted p = 1.0000 — the ballistic
front (C-1) at multi-Moment scale. Honest caveat: the implementation
carries DIRECTION, not ORIGIN ADDRESS. For straight-line propagation
from a point source the two coincide (outward-from-origin IS the
initial direction), so at this test's geometry the directed relay
instantiates the Version B ballistic class; they would differ under
multi-source superposition or any scattering event, where the address
(not the stale direction) defines "outward." The proxy is adequate
for the C-1 front-class verdict and inadequate as a general Version B
engine; registered as such.

## §3 — The classification table

| Implementation | Within-Moment class | Across-Moment class | C-1 (ballistic) | C-2 (inverse-square) |
|---|---|---|---|---|
| AUTOMATON-1 (2797 shell) | Version A (direct broadcast) | — (endpoint rule) | no bearing | YES, shell-level, mechanism-class-shared (±2.9%) |
| AUTOMATON-2 (2802 front kernel) | **Version B (reduced/precomposed) - WITHIN-MOMENT ONLY (v1.1 scope, SS2.2)** | NEITHER (address dropped) → 2887, dual record SS2.2a: anomaly (as registered) / **predicted negative control** (ratified ontology; independently demonstrated, `code/3036_e1_negative_control.py`) | within-Moment only | **YES, direct Version-B composition (±0.4%, tightens with hops) - within-Moment only** |
| Directed relay (2888/2889) | — (per-bit rule) | **Version B class, proxy (direction ≡ address at this geometry)** | **YES, p = 1.0000 exact** | not measured in that execution |

**Charter §6 outcome:** the implementations DO instantiate the
mechanism classes (no roadblock branch); conservative outcome →
rides to the combined completed-package review (CONV-013) per the
frozen convention.

## §4 — Two structural observations registered

**(O-1) The ratified AP-2 content is what LICENSES the engines'
field-level reductions.** Both engines aggregate DI-bit content into
scalar count fields and convolve. That reduction is exact ONLY for
count-like, phase-free content (P-2 + P-1, ratified 2989): a field of
counts loses nothing under aggregation, whereas carried phase would
have made amplitude aggregation a different physics. The AUTOMATON
engines were implicitly no-phase all along; their registered successes
are consistency evidence FOR the AP-2 ontology, banked retroactively.

**(O-2) Neither engine implements EQUALIZATION (P-4) or the V-2
imprint/reset protocol at per-bit grain.** Both impose exact kernel
conservation (unlimited emission capacity); the uniform-emission
premise that equalization exists to MAINTAIN is assumed, not derived.
The reservoir dynamics and the signal/reservoir exemption are
therefore UNTESTED by every registered implementation — E-2 territory
(already scoped at 2958: 1/r² counting, degree-6 residual, N-hop
ballistics, remainder sensitivity) plus a reservoir/equalization toy
as a natural E-2 extension. Of E-2's scoped items, E-1 finds already
evidenced: 1/r² counting (A-2, ±0.4%), within-Moment N-hop ballistics
(A-2 front at exact graph distance), multi-Moment ballistics (directed
relay, proxy grade). Not yet measured: degree-6 anisotropy residual;
remainder-rule sensitivity; equalization dynamics.

## §5 — Ledger

Nothing moves: six of seven; PR7 PARTIAL (1B OPEN, gated
C-5(i–iii)-review + MEAS-2); B7 holds; Candidate (B) 79.5%
PROVISIONAL-FAVORABLE; 2855 PROVISIONAL; d_DP ceiling ACTIVE; nothing
minted. New: E-1 EXECUTED (this record); 2887 finding reclassified
anomaly → predicted negative control; O-1/O-2 registered; E-2 scope
note. Campaign RUNNING.
