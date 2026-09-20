# Founder Correction — the CP Does Report Its Attributes to Its GP

**Patch:** 4166. **Date:** 20 September 2026. **Lane:** EW.
**Corrects:** Patch 4165 §2.

---

## Verbatim

> Is this true? The CP must communicate its presence to the GP for computation of the DI-bit
> imprint. The CP on the GP would also need to communicate its axial vector to the GP so that it can
> sum its influence with the DI-bits received each Moment. Thus, the question is: How does the GP
> axial vector from the external GPs mix with the axial vector currently imprinted on the CP? One
> concept is that the two add, the environmental axial vector and the CP axial vector mix in some
> proportion, and that is the axial vector carried by the CP to its next location after the V_i
> displacement.

---

## Reading

**He is right and Patch 4165 §2 is wrong.** If the GP did not know its resident CP's attributes it
could not imprint them on outgoing DI-bits — and then a charge could not radiate its presence at
all, so EM would not work. The register is **(own CP) + (arrivals)**, and 4165's "the CP's own A is
not in its own GP's register" is withdrawn.

His second half is a **new proposal**: a spin-evolution rule in which the CP's carried A is updated
each Moment by mixing with the environmental axial vector. Worked out at Patch 4166
(`axiom_maturation/4166_register_composition.md`) — it is allowed, it is bounded very tightly by
measured spin coherence, and it gives the A_i register the second job that TODO-4165-CHANNELJOB was
asking for.
