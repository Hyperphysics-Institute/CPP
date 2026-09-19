# SSV_net Is Two Objects Under One Name — TODO-4141-SSVROLE Resolved

**Patch:** 4142. **Lane:** EW/GR. **Session:** 234.
**Resolves:** TODO-4141-SSVROLE. **Relocates (does not close):** TODO-4140-BIVECTOR.
**Verify:** `series_standard_model/code/4142_ssvrole_resolved.py`.

---

## 1. The corpus's own force equation settles it

GR-1a (*Newtonian gravity from SSV*), verbatim:

> *"The force on a second mass m′ in this SSV gradient is F = m′c² · k · ∇(ΔSSV_grav)"*

and, in the same paper: *"A test particle in free fall moves along the local SSV **gradient**."*

So in CPP's own gravity derivation the broadcast quantity is **potential-like** and what a body
responds to is its **gradient** — a derived field. This is settled by construction, not by analogy
to GR.

## 2. Two objects, one name

| | object | kind | evidence |
|---|---|---|---|
| **role 2** | LSP′ component V_i = g_ti (and Φ = g_tt) | **potential** | glossary: "g_tt", "gravitomagnetism"; GR-1a: force = k∇(ΔSSV) |
| **role 1** | what a CP displaces by | **field** | A1′: *"one Displace step per its GP's computed SSV_net"* |

A potential and its gradient differ by a derivative and transform differently. GR-1a uses both and
distinguishes them correctly in the *scalar* sector; the vector sector inherits the same structure,
with V_i = g_ti the gravitomagnetic potential and the response built from E^G = −∇Φ − ∂_t V and
B^G = ∇ × V.

**"SSV_net" in the A1′ Displace clause is not the LSP′ component V_i.** The corpus has been using
one token for a potential and for a field.

## 3. Proposed disambiguation

- **SSV_net^pot** := the LSP′ l=1 broadcast component, V_i = g_ti. Potential-like. What GPs broadcast.
- **SSV_net^disp** := the vector a CP actually displaces by in one Moment, built from derivatives of
  the broadcast potentials. Field-like. What the A1′ Displace clause means.

Every corpus use of "SSV_net" should resolve to one of these. **Existing text is not rewritten by
this patch** — that audit is separate work, registered below. This is a corpus-wide terminology
ruling and the founder should see it, though it is derivable and therefore mine to propose (PD-008).

## 4. Which one does b contract A with?

The corpus never says. But b is a statement about the CP's **own motion** (founder, 4097: a free
particle's arcs persist, a confined quark's are severed), so the intended object is
**SSV_net^disp**. **Strongly indicated, not proven** — and it is exactly the kind of step I
overstated at 4140, so it is recorded at the strength it has.

## 5. This relocates the bivector question; it does not close it

4141's objection was correct **against role 2**: V_i = g_ti sits in the traceless *symmetric*
rank-2 tensor and cannot be half of an antisymmetric one. That stands.

**Under role 1 the objection does not apply.** SSV_net^disp is not a component of h_μν at all — it
is an attribute *of the CP*. And so is A_i. Two attributes of one object, one polar/boost-like and
one axial/rotation-like, is precisely the M_μν shape 4140 wanted, and it is a much more natural
home for it than the broadcast packet.

**It is not thereby answered.** Whether the CP's (A, SSV_net^disp) actually transform as one
antisymmetric object under a boost is the *same unproven step* as at 4140, now correctly located.
I am not writing "forced" a second time.

## 6. PD-008 — the convenient branch, marked

The convenient move was to let §5 read as a restoration of 4140: *the objection was against the
wrong object, the structure is fine after all.* Two patches ago I would have written that. What
§5 actually establishes is that the question is **live again in a better place** — which is worth
having, and is not the same as an answer. The next window should check §4's "strongly indicated"
and §5's "more natural home" and see whether either is doing work it has not earned.

## 7. What is owed

- **TODO-4142-SSVAUDIT** — audit every corpus use of "SSV_net" and resolve it to ^pot or ^disp.
  Touches SR-1, GR-1 and companions, the glossary, A1′/A3′ text, and the χ₄ patches. Mechanical but
  wide; no physics moves.
- **TODO-4140-BIVECTOR** stays open, relocated to the CP's own attributes.

A3G-2: still **not firing, not passing** — unchanged by this patch. Suite four of nine. χ₄
provisionally adopted. **F5 remains the blocker.**
