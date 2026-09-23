# Critic on 4219/4220: Nothing Load-Bearing Rests on 4219; the One Stale Artefact Was PRED-O-42's Row, Amended

**Patch:** 4252. **Lane:** EW. **Session:** 238. **Closes:** TODO-4222-CRITIC item (ii) — and with it TODO-4222-CRITIC.
**Verify (record audit):** `series_standard_model/code/4252_critic_4219_4220_residues.py`.

## 1. Audit — rows verbatim (D-11)

```
- 4219 s2 'item 4 passes by the persistent counter-imprint'
    -> RETIRED at 4228: the sign is the created singlet's; 4219's mechanism appears only in the arc's own records (4219, 4226-4228, where it is retired) and todolist history; no paper, registry or later derivation uses it
- 4219 s1 founder clarifications: quark spin = orbital L of its DP about the core; nubar's L = the mutual spin of its DP's two CPs
    -> VALID and consistent with 4228/4229: the released orbital, unanchored, IS a mutual spin about the pair's centre (SF-4's unanchored ZBW, r = hbar c / m_nu)
- 4220 s2 'lambda magnitude and sign both go to the wake mechanism (CONJ-FP-1)'
    -> SUPERSEDED at 4228 (|lambda| = 1 at the vertex; 1.275 is nucleon structure) and 4244 (the breath, g_A = 1.406): CONJ-FP-1 carries nothing of lambda now
- PRED-O-42 row (predictions.md, registered 4219)
    -> STALE on three points -> amended in this patch: basis names G-EW-INHERIT-4205 (superseded in the allocation clause by G-EW-SWAP-4228); item 4 'UNTESTED' (passed 4228); nubar = 'refill partner' (it is the released orbital)
- SF-2 v1.08 s5.7.1
    -> already rewritten at 4228 (steps 3, 5, 6, postdiction); no 4219 wording found (grep 'counter-imprint', 'wake': 0 hits)
- TODO-4203-GA
    -> re-scoped at 4228; nothing of 4219 remains in it

VERDICT: 4220's reversion was correct and complete; 4219 leaves no load-bearing residue; the one stale artefact was the
PRED-O-42 row, now amended. Item (ii) closed.
```

## 2. Verdict

4220 reverted 4219's claim correctly: the founder's "indefinitely" was about the new orbital and the antineutrino, not
the wake, and the item was rightly returned to untested. Since then 4228 passed item 4 on different grounds (the created
singlet's sign) and 4244 moved λ's magnitude to the breath, so 4219's counter-imprint and 4220's "goes to the wake"
are both history with no dependents. What 4219 leaves standing is its two founder clarifications, which are consistent
with 4229's ledger. The PRED-O-42 row in `predictions.md` still carried the 4219-era basis (G-EW-INHERIT-4205 as
ratified; item 4 untested; ν̄ = refill partner) and is amended in this patch to the 4228 state; the falsifier is
unchanged (any confirmed 0νββ). **TODO-4222-CRITIC is now fully discharged: (i) 4250, (ii) 4252, (iii) 4249.**

## 3. PD-008

Convenient: close the item with a sentence. The check that made it a patch: the registry row a reader would cite was
stale in three places, and a registry is read by people who never open the arc's records.
