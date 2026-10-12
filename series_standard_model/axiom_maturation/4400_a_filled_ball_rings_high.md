# The Founder Chooses STOP: the DI-Bits at Full Thickness Halt the Fall, So a Black Hole Is a Filled Ball. Computed With a Full Interior, a Uniform Filled Ball Rings About 20% High in Pitch in Both Interior Clocks Tried. That Agrees With 3644 A1 and 3703's Extrapolation of 3702, and Puts His Picture in Conflict With the Measured Ringdown

**Patch:** 4400. **Lane:** foundations, with GR. **Session:** 242.
**Founder input:** `founders_voice/4400_dibits_full_thickness_stop_the_fall.md` (answers 4399 §7).
**Script:** `series_standard_model/code/4400_filled_ball_ringdown.py`.
**Critic:** a fresh-context critic returned ACCEPT WITH CHANGES (verbatim in
`series_standard_model/reviews/2026-10-01_session_242_critic_returns_verbatim.md`). It reproduced the headline
independently, and required: a multi-mode fit, removing an artifact column, a corrected explanation, credit to 3644 A1,
a narrower scope, and a fuller founder question. All eight required changes are taken in.

## 1. His answer

The DI-bits at full thickness prevent the CPs from falling further toward the centre, so the mass does not collect in
a tiny dense centre. In 3703's terms that is **STOP**: matter halts where the DI-bit shell first fills the Planck sphere,
and the black hole is a ball filled with CPs out to the 8m/3 floor. It is the corpus's earlier static-core picture
(3374, 3640; the flat-core statics of 3636), and it gives his 4399 gravity curve (largest at the edge, zero at the
centre).

3703 chose the other reading, **DRAIN** (matter keeps falling to a Planck-density core). That was itself a physics
choice, made because a filled ball was estimated to shift the ringdown pitch by about 20%: 3702 tabulated a proxy with
an ingoing horizon up to 30% of the mass in the shell (+18.6%), and 3703 extrapolated to a filled ball. Before treating
his answer against 3703, the ringdown of a filled ball was computed directly.

## 2. The computation (script)

- **Method:** axial ℓ = 2 gravitational waves, followed in time through the whole object: Chandrasekhar and Ferrari's
  axial equation inside the matter, regular at the centre, and Regge–Wheeler outside. A uniform ball at R = 8M/3, not
  spinning. A pulse is sent in and the ringing is recorded far away. Mode values come from a multi-mode (matrix-pencil)
  fit.
- **Validation:** for Einstein's black hole the same code gives 0.3737 − 0.0890i, the exact value. The critic found the
  results unchanged across grid spacings, fit windows and source and observer positions.

| object | pitch | damping | waveform match with the black hole (time-aligned) |
|---|---|---|---|
| Einstein's black hole | 0.3737 | 0.0890 | 1 |
| absorbing surface at 8M/3 | −5% | **+45%** | 0.99 |
| **filled ball, Einstein's interior** (4399 A: clocks ½ → ¼) | **+20%** | −32% | 0.80 |
| **filled ball, Planck sphere pinned** (4399 B: clocks ½ throughout) | **+21%** | +19% | 0.84 |
| GW250114's box (conv042 L8; a Kerr box, used here at zero spin for scale only) | ±2.4% | −14.5% / +17.6% | |

**In both interior clocks tried, a uniform filled ball rings about 20% high in pitch.** That is far outside the
measured box, though the box is for a spinning black hole and these numbers are for zero spin. The result **agrees in
sign and size with 3644 A1** (the wave carried through a filled interior, polar waves: +23% pitch, −32% damping at zero
spin), and with 3703's extrapolation of 3702, by a different method (axial waves, a full interior, no horizon). The
absorbing surface damps too fast, in the same direction as 3644's surface absorber and by more in the axial case.

**Why:** the wave does not cross the ball. Inside the matter the barrier the wave feels stays at least as high as at the
light ring, so nothing leaks inward. The wave is turned back by the ball's rising barrier just behind the light ring
(about 0.65R in A, at the edge in B), and the absorbing horizon is gone. A shorter, closed cavity raises the pitch. The
return trip (about 11M in A, 4M in B) is shorter than one ringing cycle (about 17M), so it merges into the ringing; there
is no separate echo.

**Relation to the literature:** Cardoso, Franzin and Pani (2016) found that horizonless objects ring like a black hole
at first, followed by echoes. That needs a surface very close to 2M, where the cavity is long compared with the ringing
time. At 8m/3, just inside the light ring at 3M, the cavity is only a few M long, so there is no black-hole-like first
phase to separate out: the ringing is the ball's own mode (the axial w-modes of ultracompact uniform stars,
Chandrasekhar and Ferrari 1991; Kokkotas 1994). So there is no conflict with their result.

**Scope and caveats:**
- **Axial waves only.** The dominant (2,2) ringing is polar, and inside matter the polar waves couple to the fluid (owed;
  3644 A1's polar number points the same way).
- **Zero spin;** the measured box is Kerr's (owed at χ = 0.68).
- **Uniform density.** Other profiles his 4399 curve allows shift the numbers (owed).
- **Option C** of 4399 (waves riding the DP sea's clock inside a filled ball) was not computed (owed).
- **B's edge membrane** may add a junction term to the axial equation (not checked).

## 3. Where that leaves his picture

The corpus has now priced a filled ball (STOP) against the ringdown in every way it has a model for:
- **turned back by the ball:** about 20% high in pitch (3644 A1; 3703's extrapolation of 3702; this patch);
- **absorbed at the edge:** dies 30–45% too fast (3644; this patch);
- **partly reflected at the edge:** no passive surface law fits both measured modes; only Einstein's region itself does
  (3670).

**In every reading tried so far, STOP fails the measured ringdown.** DRAIN with 3675's reading (waves travel on the DP
sea's field, with the mass deep inside 2M) matches, but by construction: it reproduces Einstein's response at the
surface, and 3675 is still PROPOSED, pending triangulation. DRAIN carries its own open cost (3703 owed item 8, neutron
stars under DRAIN).

STOP could still be rescued if, for waves, the inside of the edge behaved as though the mass were deep inside, while the
matter stays put. The corpus's two-clock idea (3675, 3703) separates what waves ride on from what matter feels. But the
DP sea's field inside a ball follows the shell theorem, his own Newton count: it depends on where the CPs are. A rescue
would need a mechanism by which a filled ball looks empty to gravitational waves. None is known (owed, as the only open
route).

## 4. Status, under PD-006

- **The founder's STOP is filed as his stated picture.** It is physics, and his to decide.
- **3703's DRAIN stays the provisional working reading**, because it is the only one the corpus has that matches the
  measured ringdown. It was itself a physics choice and stays provisional until he answers §6. Nothing is registered or
  withdrawn; the conflict is stated here, in the todolist and in the frontier.
- **If STOP is kept,** 3702's bound, 3703's DRAIN selection, 3675's wave picture and PRED-O-40's withdrawn tidal signature
  would reopen, and the neutron-star flat-core statics (3634–3637), derived under STOP, would stand again.

## 5. Answer to his message

I understand the picture: the full DI-bit shell is a floor the CPs can't pass, so they pile up and fill the ball. The
problem is the ringing. I computed it directly: a ball filled to the edge rings about 20% higher in pitch than a black
hole, whether its inner clocks keep slowing or stay at half rate. The measured ringing of merged black holes matches
Einstein's to within a few percent. A filled ball turns incoming waves back close behind the light ring, so it rings
like a short closed pipe. A black hole swallows them, and that is what the data hear.

## 6. Question to the founder (physical picture)

When the merged black hole rings, gravitational waves run into it. **In your picture, what happens to a gravitational
wave that reaches the full DI-bit shell at the edge?**
- Is it turned back by the ball, at the edge or partway in? That rings about 20% too high.
- Is it absorbed at the edge? That makes the ringing die out too fast.
- Is it partly reflected and partly absorbed at the edge? No single setting matches both measured tones.
- Or does it keep going inward and disappear, as if the mass were deep inside, even though the CPs are stopped at the
  edge? Only this matches the measurements, and it would need something that lets waves pass the stopped CPs without
  coming back.

## 7. PD-008

- **Convenient branch for the founder's picture, ruled out:** "3702 was only a proxy estimate, so STOP is fine." The
  direct computation gives about 20% with a full interior too.
- **Convenient branch for the corpus, not taken:** "DRAIN stays, the founder is wrong." His picture is filed, DRAIN is
  provisional, and the one route by which STOP could survive is named.
- Nothing registered.
