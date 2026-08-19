# The Integer in the Pipe

*The story of Spin II: how a naked factor of two — borrowed, unexplained, and carrying the entire weight of the electron's spin — was traced to its source and found to be not a measurement, not a fit, but a piece of integer arithmetic as old as music.*

---

## The Debt

Every theory carries debts, and the honest ones publish the ledger. At the close of the first spin paper, Conscious Point Physics had derived the electron's spin — the exact, awkward $\hbar/2$ — from the orbital motion of a captured dipole, using nothing but the inverse-square force law and one geometric input. But that input was doing enormous work. The captured pair's outer point was placed at exactly twice the radius of its inner point:

$$r_{\rm out} = 2\,r_{\rm in},$$

and from that single ratio everything followed: Kepler's law turned the radius ratio into the $2\sqrt{2}$ frequency ratio, the frequency ratio built the angular momentum, and the angular momentum came out to one half. The paper flagged the ratio as its open problem number one and called deriving it "the one remaining step required to make the spin derivation fully first-principles."

It is worth dwelling on how exposed this position is. A factor of two, sitting at the base of a derivation, is exactly the sort of thing a skeptic should probe first — because a factor of two is what you reach for when you need a derivation to work. If the ratio had been $1.87$, or $2.2$, or anything the data demanded, the whole edifice would be a fit wearing a theorem's clothes. The only fully honorable origins for such a number are the ones no one can adjust: symmetry, topology, integers. Spin II's job was to show the two belongs to that family. It does — and the derivation is short enough, and elementary enough, that this chapter can walk through essentially all of it.

## The Pipe

The setting is the electron's polarization cloud — the trembling, structured region the Dipole Sea builds around a bare point charge, introduced in the previous chapter. In this framework the cloud is not decoration; it is a *resonator*. Its radial compression field supports standing waves, the way a column of air in a pipe supports tones, and the physics of the paper is the physics of that pipe: what are its allowed vibrations?

A pipe's tones are fixed entirely by its two ends. The cloud's ends are fixed by the framework's rules. At the center sits the bare Conscious Point, and the framework's exclusion rule — its counterpart to the principle that two things cannot occupy one place — pins the wave to zero there. In the language of vibrating strings: the center is a clamped end, a *node*. At the outer edge, the cloud simply runs out. The thermal boundary — the radius at which the cloud's organized trembling dissolves into the sea's background agitation — sits at

$$r_{\rm th} = \frac{\hbar}{2 m_e c},$$

half the electron's reduced Compton wavelength, about $1.93 \times 10^{-13}$ meters. Nothing constrains the wave's amplitude there; the end is *free* — an antinode.

One end clamped, one end free. Every organist, every clarinetist, every student who has blown across a half-filled bottle knows this instrument. It is the stopped pipe, and its spectrum has been understood since the eighteenth century: the pipe fits a quarter of a wavelength, then three quarters, then five — always an odd number of quarter-waves, because the wave must leave the clamped end at zero and arrive at the free end at a maximum. Written for the cloud, the allowed modes are

$$\psi_n(r) = \sin(k_n r), \qquad k_n = \frac{(2n-1)\pi}{2\,r_{\rm th}}, \qquad n = 1, 2, 3, \ldots$$

The odd integers $1, 3, 5, \ldots$ — the stopped pipe's signature, the reason a clarinet sounds hollow where a flute sounds full — are now the mode numbers of the electron's dressing. No physics beyond the two boundary conditions has been used. This spectrum is inherited, essentially verbatim, from acoustics.

## The Trembling Clock

Why does the cloud end where it ends? The thermal radius $\hbar/2m_ec$ is doing quiet but essential work — it is the pipe's length, and a pipe's length sets all its tones — so it deserves a paragraph of physical grounding rather than a bare formula.

The deepest clue predates quantum mechanics proper. In 1924, in the thesis that gave every particle a wave, Louis de Broglie began from a postulate now mostly forgotten: that a particle of mass $m$ contains an internal *periodic phenomenon* — a clock — ticking at the frequency $mc^2/h$ given by equating Einstein's two great energy formulas, $mc^2 = h\nu$. For the electron that clock runs at about $10^{20}$ ticks per second, and de Broglie's wave was originally the traveling expression of this internal beat. Six years later Schrödinger found the trembling motion — Zitterbewegung — sitting in Dirac's equation at essentially this same frequency, as if the formalism were insisting on the clock whether anyone wanted it or not.

In Conscious Point Physics the clock is neither postulate nor formal artifact; it is the polarization cloud's actual oscillation. The bare point charge and the sea negotiate at the Compton frequency, and the negotiation has a natural reach. Organized trembling can extend outward only as far as coherence with the central beat can be maintained against the sea's background agitation; work out where the organized oscillation's energy density falls to the ambient thermal scale and the boundary lands at half the reduced Compton wavelength — $r_{\rm th} = \hbar/2m_ec$, about a fifth of a picometer. Beyond it, sea; within it, instrument. The electron's famous Compton scale, on this picture, is simply the size of its resonating chamber, and the heavier leptons — with faster clocks — have proportionally smaller chambers, which is the $1/m$ scaling the first paper's chapter noted. The pipe's length is set by the tick of de Broglie's clock.

## Two Seats

Now bring in the passenger. The captured dipole of Spin I is two points — a positive point that the central charge attracts, a negative point that it repels — and both must ride somewhere in this vibrating cloud without being thrown.

The paper states the seating requirements as a definition, and each follows from the sign of the force. The *positive* point, pulled inward, can rest only where the wave's displacement is at a maximum — an interior *antinode* — the balance point where the oscillating field's restoring push vanishes and the effective potential flattens. The *negative* point, pushed outward, can rest only where the wave's displacement is zero — an interior *node* — where the oscillating force averages away over each trembling cycle and no cumulative drift accumulates. One passenger point needs a crest to sit in; the other needs a still point.

A reader may reasonably pause at the second requirement — *stability at a node of an oscillating field* — because it sounds backwards; surely a point should settle where the field is strong, not where it vanishes? But stability in rapidly oscillating fields has its own counterintuitive rulebook, and physics has a famous exhibit. In 1951 Pyotr Kapitza showed that a pendulum whose pivot is vibrated rapidly up and down will balance *upside down* — stably — because the fast oscillation, averaged over its cycle, manufactures an effective potential with a minimum where the static problem had none. The same time-averaging logic operates in ion traps, which hold charged particles at field nulls of radio-frequency fields, and it operates here: for the repelled outer point, the displacement node is the one radius where the trembling field's push averages to zero over each Compton cycle, leaving no net drift in either direction. The crest holds the attracted point the way a potential well holds anything; the still point holds the repelled point the way Kapitza's vibration holds his inverted pendulum. Both seats are seats because the cloud never stops trembling.

So the question "where does the captured dipole orbit?" becomes a question about the pipe's geography: which mode offers both an interior antinode and an interior node?

Walk the spectrum. Mode 1 — the fundamental, a single quarter-wave — rises from zero at the center to its maximum at the boundary and does nothing else. Its only node is the clamped center; its only antinode is the free edge. No interior seats at all: the fundamental cannot host the passenger. Mode 2 — three quarter-waves, $\psi_2 = \sin(3\pi r / 2 r_{\rm th})$ — is the first mode with an interior life. Set its derivative to zero and the sine's argument to $\pi/2$: the interior antinode sits at exactly

$$r = \frac{r_{\rm th}}{3}.$$

Set the sine itself to zero and the argument to $\pi$: the interior node sits at exactly

$$r = \frac{2\,r_{\rm th}}{3}.$$

One third of the way out, a crest. Two thirds of the way out, a still point. Both seats exist, in the right order — the attracted point inside, the repelled point outside — and Mode 2 is the *lowest* mode offering them: mode energies grow as the square of the odd integers, $1, 9, 25, \ldots$, so Modes 3 and higher offer more seats but at higher cost, and the minimum-energy principle selects the cheapest mode that satisfies the tenancy. The passenger rides Mode 2.

## The Arithmetic

And now the paper's centerpiece, which takes one line. The inner point anchors at the antinode, the outer at the node:

$$\frac{r_{\rm out}}{r_{\rm in}} = \frac{2 r_{\rm th}/3}{r_{\rm th}/3} = 2.$$

The thermal radius cancels. Look at what remains and — just as important — what does not. The electron's mass entered only through $r_{\rm th}$, and $r_{\rm th}$ is gone. Planck's constant: gone. The charge, the force strength, the speed of light: gone. The two is the ratio of the sine function's first zero to its first maximum in the three-quarter-wave mode — the numbers $\pi$ and $\pi/2$ in the argument, divided. It is the same species of fact as "the octave is a ratio of two to one," which the Pythagoreans discovered on a stretched string twenty-five centuries ago and which is true on every string, in every hall, at every scale, because it is not a fact about strings. It is a fact about integers wearing a wave.

This is what it means to pay off a factor of two honorably. The ratio at the base of the electron's spin is not measured, not fitted, not adjustable even in principle. The paper states the result as a theorem and appends the remark that deserves italics: the ratio is *independent of all physical constants*. If tomorrow's experiments revised the electron's mass or the fine-structure constant, every radius in these papers would move — and the two would not, because the two was never physics in the adjustable sense. It was the geography of the first sine mode with an interior node.

And with it, the previous paper's whole chain becomes anchored arithmetic. The radius ratio of two, fed through the inverse-square law, yields $2^{3/2} = 2\sqrt{2}$ — so the frequency ratio that looked like a peculiar irrational is revealed as an integer raised to Kepler's exponent. The angular momentum built from it comes out at $\hbar/2$. Reading the two papers as one argument: *the electron's spin is one half because the lowest standing wave that can seat a captured dipole is the three-quarter-wave mode, and the zeros of a sine wave fall where they fall.*

The paper's verification section grounds the abstractions in meters, and the numbers are worth recording. The pipe's length: $1.93 \times 10^{-13}$ meters. Mode 2's wavenumber times that length: $3\pi/2 = 4.712$, three quarter-waves exactly. The inner seat, a third of the way out: $0.64 \times 10^{-13}$ meters. The outer seat, two thirds out: $1.29 \times 10^{-13}$ — twice the inner figure to every decimal computed, because it could not be otherwise. There is a pleasure specific to verifying arithmetic like this, the pleasure of watching a table confirm what a proof already guaranteed, and the paper indulges it deliberately: in a programme whose reviewers execute the verification scripts themselves, a theorem is not finished until a machine that doesn't care about the theorem agrees with it.

## The Gear Ratio

One puzzle of scale remains, and the paper meets it head-on because a careful reader will trip over it otherwise. Spin II's seats are at one third and two thirds of the thermal radius — femtometer-scale positions, deep in the Compton regime, around $0.6 \times 10^{-13}$ meters for the inner seat. But Spin I's force-balance derivation placed the passenger's inner orbit at $2.27 \times 10^{-12}$ meters — thirty-five times farther out, up toward the Bohr regime. Both numbers came from sound arguments. Which is the orbit?

The paper's answer is that the two calculations describe the same $2{:}1$ structure expressed at two coupled scales — the wave's geometry and the orbit's dynamics — and it computes the conversion factor exactly:

$$\frac{r_{\rm in}({\rm orbital})}{r_{\rm in}({\rm wave})} = \frac{6}{\alpha \cdot 4(1+\sqrt{2})^2} \approx 35.27,$$

where $\alpha \approx 1/137$ is the fine-structure constant. The appearance of $\alpha$ here is exactly right, and a physicist's eyebrow should relax rather than rise on seeing it: $\alpha$ is precisely the constant whose job is to connect the Compton scale to the Bohr scale — the Bohr radius *is* the reduced Compton wavelength divided by $\alpha$. The wave lives on the Compton side; the force balance lives on the Bohr side; the fine-structure constant is the gear between them, appearing with the same inevitability with which it appears between an atom's size and its electron's intrinsic length. Whether the full factor of $35.27$ — the $6$, the $4(1+\sqrt{2})^2$ — has a deeper geometric meaning in the lattice's symmetry is registered as an open question, not smoothed over. The ratio structure is exact; the scale bridge is computed; the bridge's *meaning* is unfinished business, and the paper says so.

## The Ledger

Spin II closes with four open problems, and two of them repay attention because of what became of them.

The second is internal honesty about the mode selection: the minimum-energy argument that seats the passenger in Mode 2 is sound as far as it goes, but a full account would derive the selection from the complete energy landscape — binding energy, thermal disruption and all — rather than from mode energetics alone. The fourth is a door left open upward: Modes 3, 5, 7 offer more seats at higher energy, and whether those excited configurations correspond to anything in nature — excited orbital states, or even the heavier leptons — is marked "under investigation," a speculation correctly labeled as one.

The first open problem, though, is the arc's hinge, and it contains — visible in retrospect — a mistake. The entire derivation, the paper concedes, is performed in the continuum: a smooth spherical cloud, a smooth radial wave. But this framework's space is not smooth; it is a lattice, and the wave actually lives inside one lattice point's territory. The paper duly promises a successor to check the geometry there, estimates the corrections at an unmeasurable $10^{-44}$, and — in the very sentence making the promise — names the territory's shape wrongly, calling it a 24-cell. It was an inherited guess, a prior computational convenience mistaken for physics, and it sat in the open-problems section the way the factor of two had once sat in Spin I: unexamined load-bearing structure. The successor paper, when it finally came — five months late, by a route nobody planned — began by discovering it had never been written, continued by discovering the March computation had solved the wrong problem, and turned on a founder's ruling that retired the 24-cell for the true territory: a regular dodecahedron, the twelve-sided room of the next chapter. There the promised check became something better than a check — a proof that the room's symmetry *forbids* every alternative to the mode this paper selected by energy.

That is the arc's shape, seen whole: Spin I borrowed a two and confessed the debt; Spin II paid it in integers and confessed a smaller debt — the continuum — in the same breath; Spin III paid that one in group theory. Each paper's open-problems section was the next paper's assignment. A theory earns trust not by having no debts but by keeping the ledger where everyone can read it, and by the debts getting smaller.

## Coda: The Oldest Move in Physics

There is a reason the result in this paper feels, once seen, almost inevitable, and the reason is historical. Reducing a physical quantity to the ratio of small integers in a standing wave is the oldest exact move in science — older than the concept of a law of nature. The Pythagoreans did it for consonance on a string. The organ builders did it for the stopped pipe's odd harmonics. Balmer did it, without knowing why it worked, for the hydrogen lines; Bohr explained him by putting integer counts of the electron's wave around the nucleus; de Broglie universalized it by giving every particle a wave to count with. Each time, a number that had seemed contingent — tunable, empirical, one value among possible others — turned out to be arithmetic in disguise.

Spin II's claim is that the factor of two beneath the electron's spin is another member of that lineage. The half that scandalized 1925 traces back, through Kepler's exponent, to the positions of a zero and a maximum in the first sine mode with an interior seat — to $\pi$ over $\pi/2$. Whether the surrounding framework is right is a larger question, with a ledger of its own. But the two, at least, will never need adjusting. Integers don't.
