# OPEN-DM-PAIRING-KINETICS-1 — the transition graph in words, fixed from the founder's four answers (Patch 3510) — and the fork that must be ruled before p is computed

**Patch 3510, 11 Sep 2026. DM block, from the EU window under PD-006.** Sources: `founders_voice/3509_…part1.md`, `founders_voice/3510_…part2.md`. **No rate computed; no reading taken.** Charter §5 readings stand as pre-registered.

## §1 The graph
| step | object | epoch | rule (founder) | cohesion | H1? |
|---|---|---|---|---|---|
| (a) hop | CP on a stacked GP | Planck, every Moment | random hop; **landing biased** toward q-dominant stacks by the strong-channel affinity, polarity-blind, stronger than e–e | none — an SCP is whoever landed together | no |
| (b) concentrate | like-polarity qCPs | Planck | attracted, cluster, do not bond as a DP | none | no |
| (c) pair | +qCP with −qCP landing together | Planck, probability ∝ occupancy, **falling with dilution** | forms a qDP, ZBW-oscillating | **yes — first cohesive object** | no |
| cutoff | unpaired residue | when occupancy drops below what a hop needs to find a partner | residue frozen (S3-M1's inventory, now mechanised) | — | no |
| (d) aggregate / dress | qDP → DP-entities; frozen +qCPs → quarks | **later, low occupancy** (2543's MeV bend-close belongs here) | bare qCP cannot organise a quark in a high-SCP crowd; dressing needs dilution | yes | **yes** |

**Consequence for p (qualitative, not a result):** denser regions stay crowded longer and pair longer, leaving a smaller *fraction* unpaired — **sub-linear p**, the shape the 3936 band needs, now as a consequence of the picture. The value is the first computation (§3).

## §2 The fork — ruled on file, registered as a D-7 item so it is never conflated
"The unpaired +qCPs that become baryons" has two readings with different p:
1. **S3-M1 (2520, founder):** U_q is the unpaired *+q population itself*; every leftover +qCP becomes a quark; the antibaryon channel is absent by the chirality tilt. n_B ∝ residue; p = the dilution-cutoff exponent (sub-linear). **This is the founder's Q2 answer (incomplete pairing) and is what is on file.**
2. **Excess reading:** if pairing ran to completion, the leftover would be the + over − *excess*; with the χ handle a uniform substrate constant, n_B ∝ n_q, p = 1, and C-5 fails by ~5×.
**Rule for the framework:** compute the *residue*; the chirality tilt acts on what the residue *becomes* (which sign's leftovers are consumed), not on the residue's size. Any worker who finds p → 1 must first check they have not slid to reading 2.

## §3 The first computation, now specifiable — **PERFORMED at Patch 3512:** `kinetics1_residue_computation.md` (D1′ read; D1 reduced to the terminal dilution condition; C-5 conditional)
Residue fraction of one species under affinity-biased Poisson landing, with occupancy falling by the count law. Inputs, all registered: occupancy n̄ and its dilution (3890, the count law); per-GP emission (AP-4); the Q–Q vs Q–E/E–E landing asymmetry (3902, α_s vs α); the Moment as the step. Output: U_q(n_q) and its local exponent p, read against [0.21, 0.48] per charter D1. **No cross-section is invented; there is no σv** — the founder's picture replaces σv with a landing probability, which is what makes this tractable under PD-007. The expansion rate entering the dilution must be the engine's H ∝ N_rem form, not A_s-normalised (charter §6).

Second computation, after the first: the qDP population at cutoff (feeds the dial x, D3) — the same calculation read for the paired rather than the unpaired species.

---
## §4 Fork RESOLVED (Patch 3511) — and what it changes
**Founder ruling:** anti-quarks form from the −qCP residue symmetrically; annihilation follows; n_B is the excess. **Corpus fact:** n₊ = n₋ exactly at every occupation (`early_universe/neutrality_grounding.md`), so **no initial surplus exists to inherit** — the p = 1 branch of §2 is closed by the corpus, not by assumption. The asymmetry is therefore **dynamical, acting on the residues after they exist**: n_B = a · R(n_q), with R the residue the dilution cutoff leaves (this framework computes it, for both signs) and a the asymmetry fraction (the asymmetry sector supplies it; the corpus's one registered handle is Capotauro's χ, Δp_LR = χ/6, a substrate constant). **If a is composition-independent, p is the residue exponent and the D1 band test is unchanged.** Pre-registered addition: **D1′ — the framework must also report whether R₊/R₋ is composition-dependent under the affinity bias (polarity-blind per 3509, so expected not); if it is, that dependence enters p and is read as part of D1.**

**Consequences flagged, not executed:** (i) S3-M1's retro-predictions (2520 §2: clouds = n_b, hDP-B excess = 2n_b, U_q consumed = 3n_b) were derived with no anti-quark channel and **must be re-derived** with symmetric residues and annihilation before the RELIC-1 sink ledger is used again — charter D4 now reads "reproduce the *re-derived* sinks"; (ii) annihilation at the dressing epoch is a **second, late, composition-dependent photon channel** (energy ∝ R ∝ n_q^p) — noted against OPEN-EU-PHOTON-GENESIS-1, whose 3936 model assumed all release at reheating; (iii) whether the founder's conformational asymmetry and Capotauro's χ are one object is an **FP-lane question**, registered here, not answered.

---
## §5 The founder's reply to the 3512 question (Patch 3513) — the repulsive era, the trio, and a changed residue mechanism
Source: `founders_voice/3513_planck_epoch_dispersal.md` (verbatim walk-and-talk, 12 Sep). **(a) Branch (i) selected in mechanism:** once every CP has its own GP, *like-charge repulsion* drives the expansion — the **repulsive era** — so dilution continues past the count law's end. **Rate not given**; 3512 §3 showed p is set by that rate, so D1 is still not readable. **(b) The third does not spoil the pair — it is captured** as a weakly bound **trio** (K1 of 3512 is the wrong kernel; K2 direction, with the third *bound*). **(c) The residue mechanism is refined:** naked qCPs are the *thirds knocked off trios* by collisions in the repulsive/thermal era, then cocooned by polarised DPs (Q4 mechanised); the cutoff row of §1 now reads "leftover inventory sequestered into trios; the quark feedstock is the knock-off yield." Pairing does not go to completion (branch (ii) negative in the founder's picture). Annihilation and its photon confirmed with a mechanism sketch (3511-ii). **Pressure flag, not a reading** (`code/3513_trio_landing_flag.py`): if the trio inventory were set by one Poisson landing at n̄ = 1, it scales as n_q² (super-linear, above the band); the band, if it comes at all, comes from the repulsive-era *dynamics* — how long trios form and break before the freeze — i.e. the same unregistered rate. **Cross-lane flag:** the like-charge push named as the driver is the quantity the EU lane found cancelled pairwise by the DP sea's binding (3805, reheat_budget_recut); not resolved here.
