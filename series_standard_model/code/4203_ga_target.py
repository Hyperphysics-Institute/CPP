#!/usr/bin/env python3
"""4203 -- what the refill-sense bias must be to give the measured g_A.
Let f = net counter-circulation (as a fraction, -1..1) that the local Sea at the core radius carries,
relative to the departed DP, when the core captures its new DP. P(opposite) = (1+f)/2, P(same) = (1-f)/2.
Measured GT:F = 3 g_A^2 : 1, the 3 being the three triplet orientations.  Two readings of where the 3 sits."""
gA = 1.2754
for name, ratio in (('per-state (the 3 is counted separately, in the geometry)', gA**2),
                    ('overall (opposite:same counts all three triplet states)', 3 * gA**2)):
    f = (ratio - 1) / (ratio + 1)
    print(f"{name:62s} opposite:same = {ratio:.2f}  ->  f = {f:.3f}")
print("\nSign requirement in either reading: the Sea at the core radius must be COUNTER-circulating")
print("relative to the departed DP -- i.e. the departed orbital's neighbours retain the partner sense it induced.")
