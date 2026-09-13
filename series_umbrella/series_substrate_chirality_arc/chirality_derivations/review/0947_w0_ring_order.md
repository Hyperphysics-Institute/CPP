# 0947 — Which ring order does empirics select? The criterion is right, but it points away from a chiral ring

**Lane:** chirality (09xx). **Patch:** 0947, 13 Sep 2026. **Layer:** 2/3 bookkeeping, single pass. **Verify:** `chirality_derivations/code/0947_w0_ring_order_empirical.py` (6/6). **Founder instruction, 13 Sep 2026:** *"The handedness should reflect empirics; that was the intent of the order; the order that reflects the reality of the W⁰ handedness."*

## Short answer

**Empirics is the right criterion, and applied honestly it selects an achiral ring — most likely the alternating one.** Three things stand in the way of a chiral order, and the first is the one that matters.

## 1. The W⁰ is not an observable

The W⁰ is the neutral member of the SU(2)_L triplet — a **gauge eigenstate** (W³), not a mass eigenstate. It mixes with B⁰ through the weak mixing angle to give the physical Z and the photon. **No experiment measures a W⁰**, so there is no "reality of the W⁰ handedness" to read off directly. What is measured is the *coupling*: the weak interaction is maximally parity-violating, V−A, coupling only to left-handed fermions.

This is not a quibble about words. It means the empirical criterion cannot be applied to the ring order by inspection; it has to be applied through a consequence, which is what §3 does.

## 2. The empirical chirality anchor in this sector is already spent

CPP already cashes the weak sector's parity violation: the bracelet inherits the substrate pseudoscalar χ through Substrate-Locality Unification, giving `|M^W| = χ/6 = 0.0393` against the empirical `Δp_LR ≈ 0.04` — agreement to **1.6%** (T5, THEO-SD-CHIR-1, `capotauro.tex`). That is the substrate handle for V−A, and it is the paper's primary empirical prediction.

If the ring order were *also* assigned a handedness to account for the same parity violation, the programme would be spending one observable twice. A chiral ring order would need its **own** distinct signature to earn its place — not a share of Δp_LR.

## 3. What a chiral order actually predicts, and why it fails

This is the decisive step, and it runs through χ rather than around it.

The substrate carries a definite pseudoscalar χ whose sign is fixed by FI-C-9. χ is **odd** under every one of the 60 orientation-reversing elements of the vertex stabiliser (T2). So **once χ ≠ 0, the lattice reflections are not symmetries of the physical substrate** — they are symmetries of the bare geometry only. That has a sharp consequence for counting states:

| arrangement | stabiliser in D₆ | with reflections | reflections off (χ ≠ 0) |
|---|---|---|---|
| `eqeqeq` alternating | 6, contains C₃ | 1 state | **1 state** |
| `eeeqqq` blocked | 2, no C₃ | 1 state | **1 state** |
| `eeqeqq` **chiral** | 1, no reflection | 1 state | **2 inequivalent states** |

(T1, T3.) The chiral class splits under the proper subgroup; the achiral classes do not. So **a chiral ring order predicts two inequivalent neutral ring states, split at order χ** (T4). The Standard Model has exactly one neutral weak gauge eigenstate. There is nothing for the second state to be — and unlike W^±, it cannot be absorbed as a charge partner, since the W⁰ is neutral and self-conjugate.

**An achiral order predicts one state. That is what is observed.** So empirics, applied through the only route available, selects an achiral ring.

## 4. Between the two achiral orders

The structural argument above does not separate them; it only excludes the chiral pair. One further consideration, offered as a **lead and not a derivation**: the alternating order `eqeqeq` retains a stabiliser of order 6 **including the C₃ rotation**, while the blocked order `eeeqqq` retains only an order-2 subgroup and no C₃ (T1, T6). The Weak Sector lane's bracelet carries D₆; the alternating order preserves the most of it, and preserves the three-fold rotation in particular, which is the symmetry the K₃-base arguments in the same corpus run on (Finding C-W37, the C₃ of SM-1 Theorem 1's δ = 1/3). **A physical selector between the two achiral orders is not on file, and I have not invented one.**

## 5. What I have not done

I have not written an arrangement into the corrigendum. The founder's criterion — follow empirics — is satisfied by *an achiral order*, and the structural evidence within that favours alternating, but the last step from "achiral" to "alternating" rests on a symmetry-economy lead rather than an observable. **The W entries in SM-2 keep the composition ruled at 0945 and remain silent on order**, which is correct: silence is accurate, and an unjustified order would not be.

## 6. Question back

Given the above, two options, and the choice is the founder's:

1. **Adopt the alternating order** `qDP–eDP–qDP–eDP–qDP–eDP` as the W⁰ ring, on the symmetry-economy grounds of §4, and record it as a structural assignment pending an observable — the same epistemic status as SM-2's N_k assignments.
2. **Leave the order unspecified** in SM-2, recording only that it must be achiral (§3), until something selects between alternating and blocked.

Either is defensible. Option 2 is the more conservative and is what the file currently reflects.

## 7. Disposition

- **No verdict moves.** THEO-SD-CHIR-1 and `|M^W| = χ/6` untouched; THEO-CHIR-MERGE-2 unaffected; V3/W3 stand and remain conditional on Mechanism A.
- **No THEO/ID/prediction registered.** §3 contains a falsifiable statement — a chiral ring would double the neutral weak gauge eigenstate — but it is a consistency argument against an option, not a prediction of the programme.
- **Owed:** the founder's choice between §6(1) and §6(2); thereafter, at most a one-line addition to corrigendum edit (f).
