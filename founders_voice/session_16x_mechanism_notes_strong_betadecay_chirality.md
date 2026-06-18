# Founder's Mechanism Notes — Strong Sector, Beta Decay, Chirality

*Thomas Lee Abshier, ND — first-person mechanism record. Session 16x exploratory arc (June 2026).*

**What this file is.** This is the mechanical-sequential, billiard-ball-and-cue-stick version of each physical mechanism I worked out this session — the *final* form of each, with the missteps stripped out, written the way I would explain it to a person across the table. These are the pictures I want sitting behind our papers. I am stating them as mechanisms, not as derivations: each one is a physical story consistent (so far) with the rest of the corpus and with the experimental facts, but none has yet been forced from the substrate by mathematics. The honest status of each is recorded at the end of its section so no one — including me — mistakes a picture for a proof.

---

## 1. Color charge and the SU(3) hop (strong sector)

**The objects.** The core of a baryon is a hybrid tetrahedron — an hTetra — built from a type-A hDP (a +qCP bonded to a −eCP) and a type-B hDP (a −qCP bonded to a +eCP). It has four vertices. The up and down quarks themselves have *no* cage: each is a central qCP with a radial ZBW eCP and a DP cloud. (Only the strange quark carries its own surrounding tetrahedron, and that is not what builds the baryon core.) In a proton (uud), three quarks occupy three of the four hTetra vertices; the fourth vertex is open and is an eCP. In a neutron (udd) the occupancy differs, but the frame is the same: three quarks on three vertices, one vertex open.

**The mechanical sequence.**
1. Each quark's central qCP bonds to an hTetra vertex of opposite character — by electrostatic charge alone on some, by electrostatic plus strong force on others — and every bond is a ZBW oscillation: the quark trembles in and out against its vertex, State 1 (away) to State 2 (superimposed) and back.
2. **Color is which vertex a quark is bonded to.** It is not a property painted on the quark; it is the quark's relationship to the frame — which seat it is in.
3. A quark can change seats. Under the multi-body forces of the cage — the gradient one quark's position imposes on another's surroundings — a quark's next ZBW excursion can land it superimposed on a *different* vertex than the one it left. That seat-change is a hop.
4. The hops among three seats have exactly one grammar. There are six seat-changing hops (the three vertex-pairs, each with a "here-to-there" and "there-to-here" channel) and two seat-balancing modes (shifts among the three without a swap). Six plus two.
5. The ZBW oscillation is the *cue stick*: it is the physical muscle that performs the hop. The hop is the move; the trembling carries it.

**Status.** The *algebra* of these hops — that six edge-moves plus two diagonal-moves among three labeled seats close exactly into SU(3), eight gluons forced by the three-ness — is proven, and it is old: it is SS-1b's theorem, which assumes only that the three color states are the three base vertices. What is *new and not yet proven* is that my ZBW vertex-hopping is the physical realization of those generators — the mechanism SS-1b leaves open as `op:strong_primitive`. It is a candidate carrier, rich enough to be the right one, not yet shown to *force* the algebra from substrate geometry alone. Picture, not proof. (Note also the open seam between this baryon-hTetra frame and SS-1b's per-quark color-cage frame; reconciling the two is part of closing `op:strong_primitive`.)

---

## 2. W-boson catalysis of neutron beta decay

**The objects.** A down quark is a +qCP core, a radial ZBW −eCP, and an orbital ZBW qDP — it is an up quark wearing one extra radial −eCP. In a neutron (udd), the two down quarks are bound to positive vertices (a +qCP vertex and a +eCP vertex). The W⁰ is a virtual bracelet: twelve CPs, six hDPs — three eDPs and three qDPs — the qCPs bonded end-to-end into a ring with the eDPs chaperoning the chain alongside, plus-to-minus. It assembles by chance superposition out of the DP Sea, flickers in and out, and is large enough that its spontaneous formation is rare — which is why a free neutron lasts about ten minutes.

**The mechanical sequence.**
1. One down quark's radial ZBW −eCP, in its oscillation, passes the *edge* of a W⁰ bracelet — glancing it from outside, never threading the center (see §3 for why the center is forbidden).
2. The passing −eCP repels the minus pole and attracts the plus pole of the edge eDPs, rotating them about the axis of its passage. Two of the three eDPs are dislodged from their chaperone alignment with the qDP ring (the qCPs are too strongly chained to be torn loose by a passing −eCP; the eDPs are not).
3. One dislodged, now-spinning eDP is captured by the down's −eCP as its orbital ZBW pair. That gives the −eCP a spin, and it polarizes a cloud of the local DP Sea around itself — it has become a full electron: core (−eCP), spin (orbital eDP), cloud. This is the beta particle.
4. The second dislodged eDP is freed from the bracelet entirely, acquires its own velocity collinear with the original −eCP's motion, and departs as an independent spinning unit — the neutrino (see §3 for its handedness).
5. Charge is borrowed during this: the W⁰ momentarily becomes W⁻ as it mediates, and returns the charge to the products.
6. The down's central +qCP is now unbuffered against the positive vertex it was bound to. It binds briefly to the W's qCP chain, which loads the chain with extra plus repulsion; the open −eCP vertex of the hTetra is now more attractive to that +qCP than the loaded chain is, so the +qCP leaves the W and bonds to the open −eCP vertex.
7. The down has become an up, bonded on what was the open vertex. The vertex it left (the +eCP vertex) is now the new open vertex the proton needs. The neutron (udd) is now a proton (uud).
8. The W, stripped of two eDPs and with no DP-cloud mass to sustain it, dissipates back into the DP Sea.

**Status.** This is a complete, self-consistent mechanical story, and that is exactly what to be cautious about — a story with this many parts can be arranged to fit any ending. It reproduces the *kind* of event (d→u, electron + neutrino, charge and lepton-number conserved) but it does not yet reproduce the measured *rate* (which is fixed by the Fermi constant; our W-mass scale rides on a fitted dilution factor, `op:dilution`, not a derived one). The W⁰-bracelet machinery is, for now, a physical picture, not a calculation. Picture, not proof.

---

## 3. Neutrino generation and the handedness of the weak force

**The claim.** The neutrino comes out left-handed essentially every time — its spin axis lies along its line of flight (a spinning coin thrown face-forward, not a wheel rolling on its rim), and the same handedness, near-totally, in every decay. I hold that this is *generated*, not inherited, and that three things lock it.

**The three locks.**
1. **Sign — locked by polarity.** The handedness of the eDP rotation is set by the sign of the passing charge: a −eCP repels minus poles and attracts plus poles, turning every eDP it passes the *same* way, regardless of which side it passes on or which way it travels. Because every neutron decay liberates a −eCP, every neutrino gets the same-sign handedness. The sign cannot vary.
2. **Magnitude — locked by quantization.** Spin comes in whole units. The freed eDP either takes on a full unit of angular momentum and exists as a neutrino, or it does not form. There is no fractional neutrino, so there is no partially-polarized neutrino.
3. **Axis — locked by glancing transit.** The −eCP passes the *edge* of the bracelet, along an axis, and the eDPs it spins rotate about that axis — so the resulting spin lies *along* the line of flight (longitudinal). A passage through the *center* of the bracelet would instead produce a rolling-tire spin, transverse to the motion — the wrong handedness geometry. The measured fact that neutrino helicity is essentially total tells us the transit is *always* glancing and *never* central.

**Why the center is never threaded (the donut-hole exclusion).** The quark cannot fit through the hole. Two real masses cannot occupy the same place; the W bracelet's central aperture is too small to admit the down quark's core. The proof that the interaction is necessarily external is the top quark, which is the largest cage of all and still decays *through* the W — so being inside the W is not required for the interaction, and therefore the interaction is an outside, glancing one for every particle. The center is excluded by size.

**Status.** Sign and magnitude I take to be locked by polarity and quantization. The axis lock, and the maximality (~100% and not merely partial) that follows from it, depend on the glancing-transit geometry — and that geometry depends on the donut-hole exclusion, which is currently *blocked from being a clean calculation* on two counts: the W's aperture is not independently derived (it rides on the fitted dilution factor `op:dilution`), and "the size of a quark" is ambiguous in the corpus between a cage-extent and a motion-extent that order the particles oppositely (which also strains the top-quark argument). So: the sign is solid, the magnitude is solid, the *maximality* is a strong picture resting on two unpinned numbers. This is the place where, honestly, the derivation is not yet a derivation. (See also TODO-018: our shipped EW-2/EW-5 chirality fraction is both internally inconsistent and short of maximal — that number needs fixing regardless.)

---

## 4. Magnetism as the rotation of the Dipole Sea, and the origin of chirality

**The claim.** The magnetic field is not a fundamental field of nature. It is the name we give to the *rotational response of the Dipole Sea to a moving charge*. And the handedness of the world — the thing the right-hand rule encodes — is not a twist stamped into the universe at the beginning. It is manufactured, fresh, by every charge that moves.

**The mechanical sequence.**
1. Space is not empty; it is packed with dipoles (the DP Sea).
2. A bare charge moves through it. As it passes a dipole, it draws the opposite pole toward itself and pushes the like pole away. The dipole turns about its own center.
3. The *sense* of that turning, relative to the charge's line of travel, is fixed — the same every time — by the charge's direction of motion and its sign. Point your thumb along the charge's motion; your fingers curl the way the dipoles turn.
4. All the dipoles around the charge's path turn the same coordinated way, wrapping its line of travel in a toroidal spin. That curl *is* the magnetic field. The field is not a new substance; it is the picture of the DP Sea spinning around a moving charge.
5. Reverse the sign of the charge and the poles attract and repel oppositely, so the dipoles turn the other way and the field reverses. The field's direction is a consequence of the charge's polarity, not an independent property of nature.
6. The field acts on iron because iron has free electrons that a region of spinning dipoles can push and pull. And the effect is reciprocal: a *moving* DP Sea passing a stationary free charge induces motion in that charge, the same way a moving charge induced rotation in the dipoles — this is induction.

**Why this matters for chirality.** There is no need for a primordial, inflationary handedness imprinted on the universe and somehow reflected in every electromagnetic interaction — a thing I had long held only because I saw no alternative. Chirality is simply what charges-moving-through-dipoles *produce*. The center of each dipole is the rotation axis; the rotational relationship to the charge's motion is one sense or the other depending purely on polarity; and that is the whole of it. The world's handedness falls out for free, from the most ordinary thing there is: a charge in motion.

**Status.** This is the mechanism I am most confident in as a *picture*, and the one I most want made into a derivation, because if the curl-wraps-velocity geometry can be shown to force the right-hand rule exactly — and to force the *maximal* longitudinal handedness of §3 — then the same idea closes both the magnetic-field question and the parity-violation question at once. It is a picture seeking its proof. (To be written up for the chirality window and as reference material for SF-6.)

---

*Recorded as the founder's mechanical account, to sit behind the formal papers as they are written. Each mechanism is a billiard-ball story consistent with the corpus and the experiments; each awaits the mathematics that would force it. — TLA*
