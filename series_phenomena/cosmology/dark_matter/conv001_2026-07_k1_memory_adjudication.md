# CONV-001 OPEN-K1-MEMORY-1 — ADJUDICATION (Patch 2837)

**K1 UPHELD 5–0 · K2 UPHELD 5–0 with amendment · K3 and K4
ADJUDICATED TO THE MINORITY (S1) against four seats, because those
four ratified a worker overclaim — the SECOND such event, same seat
catching it · K5 S1's structure adopted · **PR7 does NOT reach
seven-of-seven** · and the worker's challenge key is ruled DEFECTIVE
by its author.**

## K1 — Obstacle real, 5–0 (adopted wording, S1)

> **Route (b) on the PR3 Metropolis apparatus is withdrawn before
> preregistration. It would measure sampler dynamics rather than
> physical Moment dynamics. PR3's static result remains valid within
> its conditional Gibbs ensemble and is unaffected.**

S1's note recorded: because no prereg was frozen before the defect
surfaced, **no result requires voiding** — the obstacle cost nothing
but drafting time.

## K2 — Reframing accepted 5–0, with S1's amendment ADOPTED

> **The complete C22/C23 substrate dynamics is Markovian by
> specification when the full arc/field state is included.
> OPEN-K1-MEMORY-1 concerns the memory induced in the charge-only
> effective dynamics by projecting out those mediating degrees of
> freedom.**

**S1's qualification is binding:** Markovianity is a
*founder-specified structural premise*, valid iff the declared
instantaneous state contains every variable the next update needs.
The closure artifact must therefore **enumerate the complete Markov
state explicitly** — charge and DP-centre positions; SSV labels; arc/
field state; neighbour-relay state if independently persistent; any
phase variables ZBW evolution requires. *If an arc configuration
persists and affects later updates but is omitted from the declared
state, the reduced description is non-Markovian before the Sea
projection even begins.* Bookkeeping, not rebuttal — but it must be
done.

## K3 — ADJUDICATED TO THE MINORITY: v/c is the CONTROL PARAMETER, not the memory amplitude

S2, S3, S4, S5 accepted the derivation as stated. **S1 alone
identified that the worker again claimed more than was derived, and
S1 is right.**

What the derivation establishes is a **timescale ratio**:
τ_propagation/τ_charge = v/c. What it does NOT establish is
|F_mem|/|F_inst| = v/c as an equality. A Mori–Zwanzig memory term
F_mem(t) = ∫₀ᵗ K(s)X(t−s)ds has a magnitude depending not only on the
kernel's decay time but on **its amplitude and normalisation, its
moments, the observable being evolved, the coupling strength to the
eliminated modes, whether the leading order cancels by symmetry,
acceleration as well as velocity, and the spectrum of the resolved
motion.** Short kernel duration is evidence *for* a Markovian
approximation; it does not fix the size of the correction.

**ADOPTED (S1 wording, replacing the worker's §2 claim):**

> **Under C22 and the founder's arc-relaxation rule, v/c is the
> scale-independent small parameter governing the derivative
> expansion of projection-induced retardation at separation d. The
> leading memory correction is expected to be O(v/c), unless symmetry
> removes that order. Its coefficient and norm remain to be derived.**

The scale cancellation stands (mathematically correct). The
identification with electrodynamic retardation is **"plausible and
framework-coherent" but remains CONDITIONAL** until the reduced charge
equation or kernel is written explicitly — "retardation recovered"
may not be asserted unqualified.

**Worker note, recorded:** this is the second time S1 has caught the
worker converting "the parameter that controls X" into "the value of
X" (first: M1, "conserves no energy functional" from one tested
functional). Four seats ratified it both times. The pattern is the
worker's, not the panel's.

## K4 — ADJUDICATED TO THE MINORITY: clause 2 does NOT close on a velocity bound alone

Four seats would close clause 2 on v/c < 0.15; **S2 went further and
declared PR7 MET, seven of seven.** That is premature and is **not
enacted.** Given K3, a velocity bound constrains the *control
parameter*, not the *correction*; closing on it would close on a
condition that is necessary but not sufficient.

**ADOPTED two-stage structure (S1):**

> **OPEN-K1-MEMORY-1A — ANALYTIC CONTROL PARAMETER: MET.** Under
> C22/C23, projection-induced retardation is controlled by the
> scale-independent parameter v/c.
>
> **OPEN-K1-MEMORY-1B — SUBDOMINANCE BOUND: OPEN.** Derive the
> kernel-to-instantaneous-force bound
> |F_mem|/|F_inst| ≤ C_mem(v/c) + O(v²/c²) — or, if the first-order
> term cancels by symmetry, at O(v²/c²) — specifying C_mem, the norm,
> the state class, and the frequency/acceleration range independently
> of the measured ambient velocity; **and** bound the ambient physical
> Sea v/c without using AUTOMATON regime-artifact values.

**Threshold, adopted:** the operative criterion is
**δ_mem ≡ |F_mem|/|F_inst| ≤ 0.15**, not a velocity ratio. The
permissible velocity bound then *follows* as v/c ≤ 0.15/C_mem. A
provisional screening bar of v/c ≤ 0.15 is retained but **labelled
NECESSARY, NOT SUFFICIENT**: passing it authorises the analytic
closure calculation; it does not mark clause 2 met.

**LEDGER: PR7 remains PARTIAL. Six of seven stands. S2's
seven-of-seven is not enacted.**

## K5 — S1's three-level structure adopted; a THIRD route identified

Rejection of the v/c-only closure does **not** force FEM-blocked
status. Three levels, in order:
1. **Analytic reduced-dynamics** — derive the retarded charge-only
   equation or a controlled kernel bound from C22/C23. No Gibbs/FDT
   implementation required.
2. **Direct deterministic Moment-dynamics** — perturb the actual
   time-evolving substrate **with Moments as the physical clock**,
   rather than a Metropolis sampler. **This route was identified by
   S1 and by no one else, including the worker.** It is neither the
   withdrawn route (b) nor FEM.
3. **FEM-class** — required only if C22/C23 prove quantitatively
   insufficient for either of the above.

> **OPEN-K1-MEMORY-1 becomes FEM-blocked only if C22/C23 are
> insufficient to derive or simulate a normalised reduced memory
> correction.** It is *related to* but *not identical with*
> OPEN-PR4-C23C24: PR4-COMPLETED needs an energy and equilibrium/bath
> structure, whereas a causal-retardation bound may be derivable from
> deterministic field propagation without Gibbs thermodynamics.

## Execution integrity — **the worker's challenge key was DEFECTIVE; NO execution credit issued**

S2 and S3 both returned **1061**, which is correct. **Neither is
credited, and the fault is the worker's:** the key asked for
λ̄_C/d_DP, and **that exact value is published in
`open_k1_memory_1_derivation_sketch.md` §3 — one of the three
documents the packet linked.** S2 stated it computed "from the
committed constants of Patch 2834 §3" — i.e. from the file containing
the answer. S3 stated openly that it computed from constants supplied
in the packet and declared "EXECUTION AND REASONED-UNVERIFIED."
**Both were honest about their method; the key simply could not
distinguish execution from reading.**

**This is a repeat of the flaw the worker itself diagnosed at 2813**
("publishing complete ranges enables plausible fabrication") — fixed
for ranges, then reintroduced by publishing the challenge answer in a
linked artifact. **Standing rule, tightened:** a withheld key must be
computable from committed artifacts **but its value must appear in
none of them, and in no document the dispatch links.** S1, S4
declared REASONED-UNVERIFIED. **No fabrication in this round; four
consecutive clean rounds.**

## S1's ruling on the backfilled reasoning — adopted

> The seven backfilled fragments remain clearly marked as
> retrospective reconstruction. Their absence weakens provenance for
> claims depending on the worker's undocumented decision path, but
> does not weaken a self-contained derivation checkable line by line.
> Load-bearing claims are judged from frozen premises, explicit
> equations, stated limitations, and reproducible calculations — not
> from reconstructed internal narrative.

## Standing

PR1 MET/retired · PR2 MET · PR3 MET · PR4-BARE MET-NEGATIVE
(PR4-COMPLETED = OPEN-PR4-C23C24) · PR5 MET · PR6 MET · **PR7
PARTIAL — OPEN-K1-MEMORY-1A MET, 1B OPEN.** Six of seven. The
remaining gap is now sharply specified: **derive C_mem, and bound
ambient physical v/c.** Founder decision B7 holds.
