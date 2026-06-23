# Reasoning capture — Patch 2038: VTD-1 founder-delegated confirmation (bounded)

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

Thomas said the orthogonality question is outside his intuition and delegated the confirm to me, bounded:
approve and proceed *if the computation confirms it*. This is a moment to be careful, not eager. A founder
handing a mechanism call to the worker is exactly where overclaiming would do real damage to the trail.

So I split the question into the part computation can settle and the part it can't, and approved only the
first. Computation CAN settle it because it's an exclusion: SR-1's exact γ is externally validated, so I
treat that γ as the datum and ask which budget reading reproduces it. Linear gives γ = 1/(1−v/c) — falsified.
Quadrature/f_eff gives 1/γ exactly, and demanding internal-rate = 1/γ forces consumed = 1 − 1/γ = f_eff with
no free parameter — unique. So the linear competitor is ruled OUT and f_eff is the only survivor. That is a
real confirmation, computation-backed: VTD-1 PASSES at SR-1 strength, R2 condition (i) cleared at that
strength.

What I explicitly did NOT approve: the deeper substrate-mechanism claim — that the PCD cycle *literally*
partitions displacement into orthogonal subspaces, vs. f_eff being an effective partition the substrate must
reproduce. No numerical check decides that, so I don't get to confirm it on Thomas's behalf, even under
delegation. I carved it out as a refinement, noted it doesn't gate R2 (R2 needs only the effective γ(v),
which f_eff gives), and parked it for a later founder's-voice capture / OPEN-SR-9 fold. This keeps VTD-1 at
exactly SR-1's status: a validated effective factor whose primitive derivation App. H itself calls an
identification, not a geometric theorem. No stronger.

The temptation under delegation is to convert "the founder trusts my computation" into "therefore I've
settled the mechanism." I didn't. I settled the exclusion and named the boundary. R2 stays conditional-PASS;
the literal-orthogonality and medium-universality questions are live, and the CONV-001 round is next.

NO THEO. Owned greenfield path. Registry/R2-STATUS/SR.md edits deferred to integrator (batched).
