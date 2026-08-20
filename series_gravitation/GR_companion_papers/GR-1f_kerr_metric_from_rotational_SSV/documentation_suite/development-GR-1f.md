# Development log — GR-1f (The Kerr Metric from Rotational SSV)

**STATUS: reconstructed.** GR-1f predates the vignette convention; the
March 2026 authoring is thin because nothing was recorded at the time.

## March 2026 — rotation, and a conjecture converted

**Vignette 1 — one more channel.** GR-1c had noted that rotating bodies
require vorticity in SSV_net and registered the full Kerr derivation as
an open problem. This paper took it up by adding an azimuthal component
to the broadcast — k(SSV_net)_φ = GJ sin²θ/(c²r³), from the same 12-edge
selection rule already generating the scalar — and mapping it through
the LSP to the off-diagonal term g_tφ. The Lense–Thirring limit came out
exact, matching Gravity Probe B to 0.3%, and J = 0 recovered
Schwarzschild exactly rather than asymptotically.

**Vignette 2 — the result the paper is really about.** The Kerr bound
J ≤ GM²/c fell out of a causality requirement. Every LSP broadcast
propagates at exactly c and the Absolute Moment tick is the minimum time
interval, so the azimuthal pattern velocity at the outer horizon,
v_φ = ac/r₊, must not exceed c — and that condition reduces
algebraically to a ≤ M. In general relativity the same bound is a
consequence of cosmic censorship, a conjecture still undecided after
fifty years. Here it is a theorem about what a lattice with a fixed tick
can support. The paper states this plainly in a remark, and it is the
most ambitious claim in the gravitational arc.

**Vignette 3 — consistency, honestly labelled.** The full
Boyer–Lindquist metric is shown *consistent* with the mechanism at all
orders, not derived from it; obtaining Σ and Δ from the CPP field
equation is registered as `op:allorders`. The same distinction GR-1's
ledger would later draw between solutions and equations is already being
drawn here, for a single metric.

## August 2026 — renamed and formatted

**Vignette 4 — c11 becomes GR-1f.** The arc reorganization (Patch 3230)
moved the paper into `GR_companion_papers/`; the W-A pass (Patch 3273)
added the CP/GP Signature subsection. No content changes.

## Session 152, 20 Aug 2026 — the suite

**Vignette 5 — a batch that never got a closing pass.** Two of this
paper's four open problems — the Kerr–Newman extension and
superradiance — were delivered by GR-1g and GR-1h, both dated the same
March week. The papers were written in immediate succession and nobody
went back to update the earlier list once the later ones existed. This
is a different failure from the one found in GR-1b and GR-1c, which were
overtaken by work done months later: here the solutions arrived almost
at once, and what was missing was a cross-reference pass across a batch.
Recorded, not edited, consistent with the boundary held since Patch 3283.

**Vignette 6 — and a question raised for the reviewers who haven't come
yet.** The Kerr bound rests on treating the azimuthal SSV's *pattern*
velocity as a physical propagation speed subject to subluminality.
Whether that is the right object to constrain — rather than a group or
signal velocity — carries the whole theorem, and no external round has
ever examined it. The suite names it as the first thing a panel should
attack, alongside a cross-arc note: the c_* suppression near the
exclusion radius is exactly the kind of effect a bound built from a
near-horizon velocity reaching c would feel.
