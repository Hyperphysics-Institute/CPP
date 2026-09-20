# Founder Objection — the Spin-Mixing Loop Needs the Broadcast

**Patch:** 4182. **Date:** 20 September 2026. **Lane:** EW.
**Objects to:** Patch 4181 §1(a).

---

## Verbatim

> Is this true? It seems that there are two functions for the spin bit:
>
> * First function: if there is spin mixing, the GP_origin must stamp its DI-bits to broadcast to the
>   GP_PSR.
> * Second function: Having the GP broadcast DI-bits containing the integrated/computed spin makes
>   its spin available at the GP_PSR, where it will then mix with the spin of a CP on GP_PSR.
> * In short, it seems we need to stamp the spin/A_i from the GP_origin onto the local CP after the
>   computing/mixing is done, so the CP can inform GP_CP_hop, where its spin lands, and then the CP
>   can mix with the computed spin from that GP_CP_hop, and then hop to the next GP carrying that
>   computed spin. Etcetera.

---

## Reading

**He is right about the architecture and 4181 §1(a) was too quick.** The loop he describes — GP
computes a register, stamps outgoing DI-bits, those arrive and are summed at the next GP, that GP
stamps its resident CP, the CP hops carrying it — **requires the GP-held register, which is A3′'s
content, not merely AP-4's transport.** My separation of the two was wrong.

**But the loop's conditional is doing the work**: *"if there is spin mixing."* Patch 4182 takes the
loop at face value and computes what it implies.
