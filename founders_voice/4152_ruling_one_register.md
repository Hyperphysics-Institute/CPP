# Founder Ruling — Each GP Stores ONE Vector in Its Register

**Patch:** 4152. **Date:** 19 September 2026. **Lane:** GR/QM.
**Answers:** TODO-4150-REGISTERCOUNT.

---

## Verbatim

> The GPs populate their register by computing/summing the DI-bits arriving from GPs arriving at a
> PSR distance. That register value is stamped onto the DI-bits that go out at one PSR and imprint
> a swath of GPs 10% of the PSR radius wide. The GP stamps the CP with the register value to direct
> its displacement direction and distance. Each GP computes one register vector, stores it, and
> imprints it on the DI-bits and, if present, on the CP. In short, each GP only stores one vector
> in its register.

---

## Reading

**One vector register, three uses:** populated by summing arrivals, stamped onto outgoing DI-bits,
and stamped onto the resident CP to direct its displacement. Not two objects.

This answers REGISTERCOUNT as **Reading 1** of Patch 4150 §3 — and it **overturns the premise the
audit has been running on since Patch 4142.** Worked out at Patch 4152
(`series_gravitation/audits/4152_one_register_consequences.md`): the ruling is consistent with the
corpus, including the one place that looked like a counterexample, but it means `SSV_disp` was a
distinction without a difference and must itself be retired.
