# Reasoning capture — Patch 1113 (spin-2 construction, Step 2: the Q_ij broadcast law)

**Protocol:** `templates/reasoning_capture_protocol.md`. Reasoning behind the broadcast-law finding.

## The task
Step 2 = the Q_ij broadcast law: does the PCD cycle emit a propagating quadrupole (-> spin-2 mode), or
does the substrate choke? Recognized 'broadcast law' hides two separable questions: (i) can the
shell-sum propagate a rank-2 field; (ii) does the GP have a quadrupole d.o.f. to broadcast.

## The chain
1. (i) The icosahedral shell-sum (1108) gives L f -> grad^2 f via sum(v_i v_j)=4I. This acts
   COMPONENT-WISE -- it's rank-agnostic. So a broadcast Q_ij would get Box Q_ij = source, same operator
   as scalar/vector. Verified the helicity-2 part {Q_xx-Q_yy, Q_xy} is traceless+transverse -> with
   Box Q=0 it propagates at c = the GW +,x modes. So PROPAGATION is native; the 1112 falsifier
   ('can't carry/propagate at c') does NOT fire.
2. (ii) But the LSP is scalar(1)+vector(3) -- a point has no rank-2 part. Q_ij (5) is NOT a gradient of
   the vector (1109). So Q_ij is a genuinely NEW d.o.f. The 600-cell H_g (l=2) rep is the geometric
   slot (1112), but carrying it is a foundational LSP extension, not a consequence of scalar+vector.

## Verdict
op:einstein (a) closure localizes to ONE foundational question: does the GP carry a quadrupole d.o.f.
Q_ij? If yes (postulate/motivate) -> shell-sum propagates it, helicity-2 = GW, rest is source coupling
+ GR-recovery. If substrate is genuinely scalar+vector only -> CPP can't contain tensor gravity and the
GW-polarization tension is STRUCTURAL. Honest middle ground: propagation native, d.o.f. is a postulate.

## What I did NOT claim
- NOT a closure of (a). Adding Q_ij to the LSP is a genuine foundational postulate, not a derivation.
- Did not claim CPP 'has' spin-2: I showed the shell-sum WOULD propagate it IF the GP carries it.
- NO VERDICT MOVED.

## Honest architectural statement
As currently axiomatized, CPP's substrate carries scalar+vector gravity; the graviton-analog (l=2 shape
mode) is not contained in it. The 600-cell has the right geometric slot (H_g), so the extension is
natural, but it IS an extension. This is a significant, clarifying fact about the programme.

## Next
Step 3: is there independent CPP motivation for a GP quadrupole d.o.f.? (DP-sea polarization tensor;
CP spin state; whether PCD physically excites the H_g mode). That decides postulate-vs-derivation.

## Confidence
- Solid (computed): shell-sum rank-agnostic -> Box Q for a broadcast tensor; helicity-2 = TT = GW;
  LSP has no rank-2 part.
- Open: whether a GP quadrupole d.o.f. is independently motivated in CPP (Step 3) -- the crux.
