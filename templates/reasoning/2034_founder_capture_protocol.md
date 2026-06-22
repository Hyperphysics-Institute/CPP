# Reasoning capture — Patch 2034: founder-contribution capture protocol (the fix for the recording gap)

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

Thomas observed, correctly, that across 11 days of intense multi-window interaction his substantive physics
contributions were not being recorded in the founder's record, even though they shaped results. Diagnosed the
root cause rather than apologizing: the reasoning-capture protocol (Session 146) made WORKER reasoning capture
part of the per-patch contract, but founder contributions get folded into the worker's fragment as PARAPHRASE
('TLA pushed back...', 'Thomas supplied...') with no verbatim preservation, no attribution, and no promotion
path to founders_vision.md. Quantified: 15+ reasoning fragments paraphrase a TLA contribution; ZERO reached
founders_vision.md. His voice was lost the same way physics reasoning was lost before the protocol existed.

The fix (same shape as the one that already works): founder-capture rides the per-patch contract.
- TRIGGER: any patch whose result was shaped by a TLA contribution.
- ACTION: a delimited '## FOUNDER CONTRIBUTION (verbatim — TLA, <date>)' block in the reasoning fragment,
  his exact words quoted, + one-line context. Element 5 of the §1 contract; details in §10.
- OWNER: the worker (rides the contract; stops being a thing to remember).
- PROMOTION: templates/sweep_founder_contributions.sh greps all blocks, flags promoted vs orphan; TLA
  promotes orphans into founders_vision.md.
Four properties that made reasoning-capture work (trigger/owner/immediate/greppable); works across parallel
windows (each captures in its own patches; the sweep collects at integration).

GOVERNANCE-FILE NOTE for integrator: amends canonical templates/reasoning_capture_protocol.md + adds
templates/sweep_founder_contributions.sh. Flagged per worker discipline; TLA integrates (his requested process
change; he applies all patches).

Worked exemplar + backlog seed below: the pivotal R2 founder contribution, formatted per §10. Its quote is
already in founders_vision.md (Patch 2033), so the sweep flags it 'promoted ✓' — demonstrating the full loop.

## FOUNDER CONTRIBUTION (verbatim — TLA, 2026-06-22)
> "I don't think the anisotropic optical response is an applicable analogy. The anisotropy we are referring to in this context is the locally carried medium, which is being affected uniformly by the KE_abs of the mass in that small (subquantum) volume. The macroscopic medium of the space, unstressed by the photon or mass-with-absolute-velocity, is independent of its traververse or axial aspect because the SSV_abs is a scalar. There will be as much effect on SSV_abs in the direction of axial velocity as the transverse (perpendicular to the axis), due to the KE_abs effects produced by the charge-motion of the mass."
*Context:* dissolved ChatGPT's birefringence/f(C,Σ) attack on R2 medium-universality — a scalar mediating field has no axial/transverse aspect, so there is no tensor Σ; grounded the scalar-channel resolution and drove R2 to PASS-conditional. (Full quote + resolution in founders_vision.md, 22 June 2026 entry.)
