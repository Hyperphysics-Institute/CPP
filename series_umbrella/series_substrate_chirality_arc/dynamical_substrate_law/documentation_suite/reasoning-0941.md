# reasoning-0941 (verbatim, at-patch) — L4-C antisymmetric current construction

**Lane:** chirality (09xx), Patch 0941, 13 Sep 2026. **Artifact:** `l4c_antisymmetric_current.md`. **Verify:** `code/0941_l4c_antisymmetric_current.py` (8/8).

Expected a bookkeeping exercise: MA.2 subtracts the reverse rate along each edge, PCD says flux is out-minus-in, done. Went to check the edge set first (D-3: locate the object before building on it) and the exercise turned into the patch.

The twelve first-shell directions at a 600-cell vertex all sit at û·n̂ = −1/(2φ) — I had this from 0937 T1 and from F.1 Theorem 5.1, but had not drawn the consequence: they are all on one cone, so the set is not centrally symmetric, and −û is not an edge direction at v for any of the twelve. Σû = −(6/φ)n̂, length 3.708, nowhere near zero. So MA.2's r(−ê; v) has no referent if read as "the opposite edge at v". The axiom as written is ill-posed under its literal reading.

That also shows why the antisymmetry is not cosmetic. The naive Σ r(ê)ê gives −r₀(6/φ)n̂ at δ = 0 (T4) — a substrate current with no perturbation in the substrate. Unphysical before any parameter is chosen. So something must kill the isotropic part, and the antisymmetric combination is what does.

The repair is the Perceive/Displace split. GP perceives arrivals, computes SSV_net; CP displaces. Flux = departures − arrivals per edge. The arrival on edge {v,w} is imprinted at w and its travel direction seen at v is −û; its rate is the law evaluated at w. That is r(−û) — but ONLY if w carries the same r₀ and δ as v, which is exactly L4-B. So r(−ê;v) means the reverse traversal of the same edge governed by the law at the far end, and the antisymmetry is forced.

Checked rather than asserted (D-4): T5 over all 120 vertices, not just v_host; T6 the δ=0 cancellation at all 120; T8 denies L4-B at one neighbour and watches both fail. T8 is the one I would not have written a week ago — it establishes that L4-C consumes L4-B, which the 0646 decomposition lists as parallel items. They are not parallel.

Unplanned: T7. Computed the surviving current to confirm it was nonzero and found 2r₀δ Σ(û·n̂)û = (6/φ²)r₀δ n̂ — F.1 Theorem 7.1's α₁, to machine precision, parallel to n̂ with perpendicular residue 5e-19. Did not import it; it came out of Σ(û·n̂)û with û·n̂ constant at −1/(2φ) and Σû = −(6/φ)n̂. Recorded as a consistency check on the derivation, not as a new result — α₁ is already on file and this is the same number arrived at from the other side.

Scope held deliberately: the first-shell restriction is THEO-DSL-1's and is inherited, not re-derived (saying so rather than letting the patch look like it derived locality too). L4-A is untouched and is now the only F.2-free piece left, so Mechanism A is not discharged and V3/W3 stay conditional. No theorem registered — the unit is A+B+C together.
