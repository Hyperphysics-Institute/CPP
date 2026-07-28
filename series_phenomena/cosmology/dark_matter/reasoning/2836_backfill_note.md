# REASONING-CAPTURE LAPSE — AUDIT AND BACKFILL (Patch 2836)

**The founder asked, 2026-07-27, whether reasoning and his inputs are
being saved verbatim after each patch. Audit result: HIS INPUTS YES,
MY REASONING NO. Seven of the last eight patches shipped with no
reasoning fragment: 2828, 2829, 2831, 2832, 2833, 2834, 2835 (only
2830 complied). This violates the standing reasoning-capture rider,
which requires every physics patch to bundle .tex/.md + verbatim
reasoning fragment in one `git am`.**

**Cause, named honestly:** the omissions begin exactly where my
commits became large batched one-liners under context pressure. I was
optimising the visible deliverable (document + patch + paste block)
and silently dropping the invisible one. It is not coincidence that
the lapse is invisible in every plain-language summary I wrote during
it — nothing in my own reporting surfaced it, and it took the founder
asking.

**Founder inputs: verified preserved.** His arc-relaxation ruling is
quoted in full at `open_k1_memory_1_closure_derivation.md` §1; his ZBW
draft at the sketch §2; his AUTOMATON commitments verbatim as C19–C30.
No founder input was reduced to shorthand.

**Backfilled below: 2828, 2829, 2831–2835, written now and labelled
as backfill rather than presented as contemporaneous.**

---

## 2828 (PR enactment packet)
Assembling this was mostly a discipline problem, not a drafting one:
four requirements were being asked to move at once and the temptation
was to lead with the strong result (PR3) and let the weaker items ride
its momentum. Instead PR5 went out with my own objection attached
against my recommendation, and PR7 went out as PARTIAL when six-of-
seven was within reach. The packet's honesty is load-bearing precisely
because the panel could not check the numbers themselves.

## 2829 (enactment adjudication)
The seats overruled my PR5 objection 5–0 and I recorded it as
overruled rather than quietly adopting their conclusion as if I had
agreed. S1's condition that we may never claim 0.5%-level agreement
was adopted verbatim and made binding on downstream citation, because
that is the kind of qualification that erodes if paraphrased. On the
E1 conditions I met three and disclosed the fourth as only partially
met — the raw time series live on the founder's machine, not in the
repo, so "regenerated from archived series" is true of block means and
not of samples. Saying so cost nothing and buys the record its
accuracy.

## 2831 (naming motion)
The motion had to make it easy for a seat to object that renaming the
last obstacle on the prime-goal path alters the obligation. So the
text states plainly that the substance is unchanged and then
explicitly invites that objection. I also replaced deference with a
reason: previously I had recorded "the panel says PR3 doesn't close
clause 2" without being able to explain why, and the static-versus-
finite-frequency distinction is a better foundation than obedience.

## 2832 (naming adjudication)
The notable event was S2 returning a correct challenge value. I
verified before crediting, exactly as I verified before discrediting
S5 and S1 in earlier rounds — the procedure has to be symmetric or it
is not a procedure. What pleased me was the loop: S2 identified at
2829 that a withheld key must be computable from committed artifacts
with the path named; I adopted that; S2 then used the fix to verify.
The panel improved its own instrument.

## 2833 (Metropolis obstacle)
I proposed route (b) and the panel adopted it 5–0, and only while
drafting did I see that Monte Carlo sweep-time is algorithmic and
carries no physical clock. Two bad options were available: write the
prereg as adopted and let the limitation surface at returns, or
quietly redesign around it. Both would have been worse than saying so.
The deeper tension — that a finite-frequency FDT test presupposes the
equilibrium structure PR4-BARE found absent — is the part I most
wanted to be wrong about and could not make go away.

## 2834 (derivation sketch)
The founder's Markovian ruling reframed the question from "does the
substrate remember" to "how much memory is induced by projecting out
the Sea," which is a genuinely different and answerable question. The
sketch's discipline was refusing to claim ε_mem is small: it showed
only that ε_mem is expressible and reduces to one unpinned quantity,
and it named its own weakest joint (transferring a lattice-scale ZBW
period to physical d_DP) rather than letting the favourable reading
carry unremarked. Computing the Compton branch and finding it
demanding — v/c < 1.4e-4 — was the point at which the sketch stopped
being reassuring, which is when it became useful.

## 2835 (closure derivation)
The founder's answer supplied a third reading neither of us had
listed, and it was better than both: field-mediated relaxation at
lightspeed across the separation, so τ_Sea = d/c with no imported
number anywhere. Then d_DP cancels and ε_mem = v/c. What makes me
believe it rather than merely like it is that it lands on the
framework's own primitive — v/c IS |SSV_net|/SSV_abs — and reproduces
the retardation structure of electrodynamics without being aimed at
it. Elegance is not evidence, so the record still refuses to assert
the remaining bound and explicitly forbids using AUTOMATON's ratio
values for it, since those are regime artifacts I diagnosed myself.

---

**Standing correction:** the reasoning fragment is not optional
overhead to be shed when the turn is busy. Its absence is invisible in
exactly the situations where the reasoning matters most. Future
patches bundle it or do not ship.
