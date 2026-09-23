# F3's |W| on the Proton's True Spin State: Exactly Half the Product-State Value

**Patch:** 4245. **Lane:** EW. **Session:** 238. **Closes:** TODO-4240-F3STATE.
**Verify:** `series_standard_model/code/4245_f3_W_on_the_true_spin_state.py`.

## Rows verbatim (D-11)

```
sum_i V_i = 0.0e+00 (action-reaction)
|W| product state (4134) = 1.1654   |W| true J=1/2 state = 0.5827   ratio = 0.5000
identity: with sum V = 0, W = sum s_i V_i = (s_d - s_u) V_d: product (-1-1) = -2 V_d, true (-1/3-2/3) = -1 V_d -> exactly half
rms <n.W> per nucleon: 4134 0.67 -> 0.34 (expectation value; operator fluctuations not included)
4136 E1 bound: eps <= 8.6e-08 -> 1.7e-07;  g <= 2.6e-07 -> 5.1e-07  (Langevin, eps = g/3)
-> isotropy result <n.W> = 0 unchanged (independent of the spin state); bounds loosen by exactly 2; the 'excluded by seven orders' reading unchanged.
```

## Result

4134 computed W = Σ s_i V_i on the product state (+1, +1, −1); the proton's J = ½ state (4240 Part A) has
⟨2s_i⟩ = (+2/3, +2/3, −1/3). Because Σ V_i = 0 (action–reaction, 4134 C6b) and the two u's share one spin expectation,
W = (s_d − s_u)V_d, so the true-state |W| is **exactly half**: 0.5827 against 1.1654. Consequences: 4134's isotropy result
⟨n·W⟩ = 0 is unchanged (it never depended on the spin state); the per-nucleon rms of the expectation value halves
(0.67 → 0.34); 4136's E1 bounds loosen by exactly 2 (ε ≤ 1.7×10⁻⁷, g ≤ 5.1×10⁻⁷) and still exclude an ordinary-strength
coupling by over six orders. No verdict moves. The rms is of the expectation value; the operator's quantum fluctuation
about it is a different quantity and was not the object 4134 or 4136 used.
