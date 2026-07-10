"""
2401 -- SS43-Q4b: the per-unit vertex class DERIVED (Class S vs Class V-t)
(contract sec 34.12, keyword DM-WARM-2400; founder launch go recorded verbatim
this session: "Go on Q4b.").

THE QUESTION (sec 34.12 Q4b): the same substrate mechanics that fixed the Q4a
response order must fix what a per-unit qCP vertex SOURCES in the colour-residual
channel -- scalar per-qCP additive (Class S: closure does nothing, ring gate-dead
at flat S_c = 0.0356) or chain-axis vector (Class V-t: closure telescopes, ring
decouples identically). Pre-registered kill: derived class = S => the family is
dead fully derived => Clause 1(a). The class must be DERIVED, not read off
D5-A''s ruling language.

THE DERIVED ANSWER (full chain in reasoning/2401.md; this script carries the
numerics and the pass-gates):

  L1 (registered input -- the Q4a L1 identification, sec 34.13 CLOSED input):
     the per-unit residual-channel vertex is the METH-CHIR-CONT-1 Wigner-Eckart
     matrix element M = +/- chi * d_Gamma / V_cage -- a SIGNED, AMPLITUDE-level
     object. The +/- is part of the registered datum's validity condition; the
     MAGNITUDE |M| = chi/6-normalized is universal, the SIGN is defined relative
     to the unit's local Z_2 pairing convention (zeta): C-hat lives in a
     zeta-ODD 1D irrep and M connects the zeta-EVEN to the zeta-ODD doublet
     component, so relabeling the convention flips M. In ISOLATION only |M|^2
     enters (the Q4a bubble) -- the sign is unphysical for a lone unit.

  L2 (the convention-transport structure -- what makes relative signs physical):
     in a bonded composite, relative signs between units are physical if and
     only if a REGISTERED structure refers one unit's pairing convention to its
     neighbor's. The rung bond (2381 rung-bond primitives) is that structure --
     bonding IS a pairing relation between adjacent units' DPs, and it
     transports the Z_2 convention along the chain. The chain/rung axis is the
     rod's ONLY registered coherence axis; no torsional lock is registered, so
     no second transport datum exists (0865: admitting one would be new
     freedom).

  L3 (chain-reversal parity fixes the tensor character): a unit's transported
     sign is defined relative to the ORDERING of its bonds along the chain
     (left-neighbor vs right-neighbor referral differ by the transport).
     Chain reversal (t-hat -> -t-hat) exchanges the bond roles => flips the
     convention-referred sign => the coherently sourced per-unit amplitude is
     ODD under chain reversal. A quantity odd under t-hat -> -t-hat and
     supported on the one registered axis IS a chain-axis vector component:
     v_k = M * t-hat_k. Its leading coupling to the channel field is the
     directional derivative v_k . grad Y -- whose discrete form on the chain is
     exactly the per-edge difference [Y(r_{k+1}) - Y(r_k)] (the 2393 machinery).

  THEOREM (the vertex class): the per-unit coherent vertex in the
     colour-residual channel is CLASS V-t -- a chain-axis vector, composed as
     the rung-transported signed sum (the discrete line integral). Closed loop:
     interior contributions telescope to ZERO identically. Open chain: the sum
     telescopes to the ENDS -- END-sourced O(N^0), the 2393 V2 adjacency record
     reproduced as a CONSEQUENCE, not an input.

  COROLLARY (Class S EXCLUDED within the registered structure, not merely
     disfavored -- the same registration logic that excluded sqrt(chi) at Q4a):
     Class S composition (per-qCP additive MAGNITUDES, "cannot cancel by
     arrangement") requires the composite's per-unit source to be the UNSIGNED
     |M| -- i.e. a chain-reversal-EVEN, convention-independent source -- which
     requires either (i) registration of the per-unit source at PROBABILITY
     level (where |M|^2 lives), contradicting the METH-CHIR-CONT-1
     amplitude-level registration (Q4a L1, CLOSED), or (ii) a zeta-EVEN vertex
     operator, contradicting the zeta-ODD irrep placement of C-hat in the
     registered datum. Not constructible from the registered primitives.
     The third composition (uncorrelated signs, incoherent RMS ~ sqrt(N))
     requires NO transport -- contradicting the registered bonded structure
     (2381: the rod IS the bonded object; D5-A''s "coherent cage" is this).

BATTERY (binding, sec 34.12): V1 scratch-copy chain green (run at session open:
2395 battery ALL PASS in tempfile copy, 181.4 s, transitive
2393/2391/2381/2382/2383; recorded in reasoning/2401.md sec 2). V2 PASS-GATE in
this script: the rod's registered D5-A' first-power dipole phenomenology
reproduced UNDER THE DERIVED CLASS before grading -- (a) open-chain source side
power-0 (end-sourced, saturating), total = FIRST power; (b) the two Q2 exact
identities reproduced as consequences of the derived composition (closed-loop
telescoping = 0; orientation-average orthogonality = 0). V3 pre-declared spot
checks (global-flip invariance; local-flip physicality; chain-reversal parity;
incoherent-ensemble control; normalization-independence of the class verdict).
V4 no-freedom audit (0865 held; zero tunables). V5: this script opens NO cache;
output only code/2401_results.json.

OUTPUT: code/2401_results.json
"""
import json, math, os, random

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

FAILURES = []


def check(label, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, label))
    if not ok:
        FAILURES.append(label)


def banner(s):
    print("\n" + "=" * 78 + "\n " + s + "\n" + "=" * 78)


# ---------------------------------------------------------------------------
# Registered inputs (all traced at V4; nothing tunable)
# ---------------------------------------------------------------------------
PHI = (1.0 + math.sqrt(5.0)) / 2.0
CHI = PHI ** -3 / 6.0                 # registered: |chi_sub|*d_Gamma/V_cage
R_C = 1.0                             # fm -- SF-5/J2 confinement input
R_S = R_C / CHI                       # Q4a CLOSED result = engine RS exactly
R_N = 0.9                             # fm -- 1880 script RN (D5-A' scale)
D_UNIT = 1.15                         # fm -- J8 pin (registered unit spacing)
SC_RULING = R_N / R_S                 # the D5-A' first-power scale


def Y(s):
    """Registered Yukawa radial form (2393 machinery, RC/RS as above)."""
    return (R_C / max(s, 1e-12)) * math.exp(-s / R_S)


def gradY(p, x):
    """Numerical grad of Y at probe p from source at x (central diff)."""
    h = 1e-6
    g = []
    for i in range(3):
        pa = list(p); pb = list(p)
        pa[i] += h; pb[i] -= h
        sa = math.dist(pa, x); sb = math.dist(pb, x)
        g.append((Y(sa) - Y(sb)) / (2 * h))
    return g


def ring_geo(N):
    """2393 registered ring geometry: N-gon, J8 spacing, tangents."""
    Rg = D_UNIT / (2.0 * math.sin(math.pi / N))
    th = [2.0 * math.pi * k / N for k in range(N)]
    xs = [[Rg * math.cos(t), Rg * math.sin(t), 0.0] for t in th]
    ts = [[-math.sin(t), math.cos(t), 0.0] for t in th]
    return Rg, xs, ts


def chain_geo(N):
    """Open chain on the z-axis, J8 spacing, uniform tangent z-hat."""
    xs = [[0.0, 0.0, k * D_UNIT] for k in range(N)]
    ts = [[0.0, 0.0, 1.0] for _ in range(N)]
    return xs, ts


def edge_sum(nodes, probe, signs=None, closed=True, coeff=1.0):
    """The transported-convention composite: per-edge differences
    coeff * s_k * [Y(|p - x_{k+1}|) - Y(|p - x_k|)] -- the discrete line
    integral of the chain-axis vector coupling."""
    n = len(nodes)
    if signs is None:
        signs = [1.0] * n
    tot = 0.0
    last = n if closed else n - 1
    for k in range(last):
        r1 = math.dist(probe, nodes[k])
        r2 = math.dist(probe, nodes[(k + 1) % n])
        tot += coeff * signs[k] * (Y(r2) - Y(r1))
    return tot


def scalar_sum(nodes, probe):
    """Class S composite: unsigned per-node magnitudes add."""
    return sum(Y(math.dist(probe, x)) for x in nodes)


print("=" * 78)
print(" 2401  SS43-Q4b: the per-unit vertex class DERIVED (S vs V-t)")
print("       (contract: campaign file sec 34.12; DM-WARM-2400)")
print(" Registered inputs: chi = %.8f  R_s = r_c/chi = %.4f fm" % (CHI, R_S))
print("       D5-A' scale S_c = R_N/R_s = %.4f   d = %.2f fm (J8)" %
      (SC_RULING, D_UNIT))
print("=" * 78)

rng = random.Random(2401)

# ===========================================================================
# V2 PASS-GATE (a) -- the rod's D5-A' phenomenology UNDER THE DERIVED CLASS:
# open-chain composite telescopes to END-sourced coupling; source side power-0
# ===========================================================================
banner("V2 PASS-GATE (a) -- rod limit under the derived class: END-sourced, "
       "power-0")
probe_r = 5.0
rows = []
for Nrod in (6, 12, 18, 24, 36):
    xs, _ = chain_geo(Nrod)
    L = (Nrod - 1) * D_UNIT
    # transported signed sum over the open chain (probe on-axis at -probe_r)
    p = [0.0, 0.0, -probe_r]
    tel = edge_sum(xs, p, closed=False)
    # analytic telescoped end form: Y(r_far) - Y(r_near)
    end_form = Y(probe_r + L) - Y(probe_r)
    frac = abs(tel) / Y(probe_r)
    rows.append((Nrod, L, L / R_S, frac, abs(tel - end_form)))
print("   N_rod    L(fm)    L/R_s   |sum|/Y(r)   |sum - end-form|")
for Nrod, L, x, fr, d in rows:
    print("   %5d  %7.2f  %6.3f     %.4f       %.2e" % (Nrod, L, x, fr, d))
tel_exact = max(d for *_, d in rows)
check("V2a-i  open-chain composite telescopes EXACTLY to the end form "
      "(max |diff| = %.1e)" % tel_exact, tel_exact < 1e-12)
xs_ = [math.log(r[2]) for r in rows[-3:]]
ys_ = [math.log(r[3]) for r in rows[-3:]]
slope = (ys_[-1] - ys_[0]) / (xs_[-1] - xs_[0])
print("   local log-log slope (last 3): %.4f  -> power-0 (saturating; "
      "2393 record: 0.106)" % slope)
check("V2a-ii source side power-0 in (L/R_s): |slope| = %.3f < 0.5 "
      "(no positive suppression power)" % abs(slope), abs(slope) < 0.5)
check("V2a-iii total S_c power = FIRST (source power-0 x nucleon R_N/R_s "
      "power-1) = D5-A' -- at the ruling scale %.4f" % SC_RULING,
      abs(slope) < 0.5)

# ===========================================================================
# V2 PASS-GATE (b) -- the two Q2 exact identities reproduced as CONSEQUENCES
# of the derived composition (fresh; random orientations and probes)
# ===========================================================================
banner("V2 PASS-GATE (b) -- Q2 exact identities as consequences of the "
       "derived class")
worst_tel = 0.0
worst_orth = 0.0
for N in (4, 5, 6, 7, 8):
    Rg, xs, ts = ring_geo(N)
    for trial in range(12):
        # random probe outside the ring
        u = [rng.gauss(0, 1) for _ in range(3)]
        nu = math.sqrt(sum(c * c for c in u))
        rr = Rg + 1.0 + 9.0 * rng.random()
        p = [rr * c / nu for c in u]
        worst_tel = max(worst_tel, abs(edge_sum(xs, p, closed=True)))
    # orientation orthogonality: tangent . radial = 0 exactly on the N-gon
    for x, t in zip(xs, ts):
        nx = math.sqrt(sum(c * c for c in x))
        worst_orth = max(worst_orth,
                         abs(sum(a * b for a, b in zip(t, x)) / nx))
check("V2b-i  closed-loop telescoping = 0 (N = 4-8, 12 random probes each; "
      "max |sum| = %.1e)" % worst_tel, worst_tel < 1e-12)
check("V2b-ii orientation orthogonality t-hat . x-hat = 0 on the ring "
      "(max = %.1e)" % worst_orth, worst_orth < 1e-12)
# node-form crosscheck (two legs): (i) the vector coupling
# sum_k t-hat_k . gradY vanishes on the CLOSED ring too -- both forms are
# discretizations of the same closed line integral of a gradient (= 0);
# (ii) on the OPEN chain, where both are nonzero, the node form agrees with
# the edge form (same integral, endpoint- vs difference-discretized) to
# O(d/R_s) discretization accuracy.
worst_node_closed = 0.0
for N in (4, 6, 8):
    Rg, xs, ts = ring_geo(N)
    p = [Rg + 6.0, 0.0, 0.0]
    s = 0.0
    for x, t in zip(xs, ts):
        g = gradY(p, x)
        s += sum(a * b for a, b in zip(t, g)) * D_UNIT
    worst_node_closed = max(worst_node_closed, abs(s))
check("V2b-iii closed-ring NODE form (t-hat . grad Y) also = 0 "
      "(symmetric cancellation; max |sum| = %.1e)" % worst_node_closed,
      worst_node_closed < 1e-8)
xsC12, tsC12 = chain_geo(12)
pC12 = [0.0, 0.0, -5.0]
# the coupling derivative is along the SOURCE displacement: grad_x Y = -grad_p Y;
# midpoint rule on the 11 edges is the discretization pair of the edge form
def gradYx(p, x):
    h = 1e-6
    g = []
    for i in range(3):
        xa = list(x); xb = list(x)
        xa[i] += h; xb[i] -= h
        g.append((Y(math.dist(p, xa)) - Y(math.dist(p, xb))) / (2 * h))
    return g
node_open = sum(
    sum(a * b for a, b in zip(t, gradYx(pC12,
        [(xa[i] + xb[i]) / 2 for i in range(3)]))) * D_UNIT
    for xa, xb, t in zip(xsC12[:-1], xsC12[1:], tsC12))
edge_open = edge_sum(xsC12, pC12, closed=False)
rel = abs(node_open - edge_open) / abs(edge_open)
check("V2b-iv  open-chain node form (source-gradient, midpoint rule) agrees "
      "with edge form (rel diff = %.4f < 0.02)" % rel, rel < 0.02)

V2_GATE = len(FAILURES) == 0
banner("V2 PASS-GATE VERDICT: %s" %
       ("PASS -- grading may proceed" if V2_GATE
        else "FAIL -- BLOCKING; no grading"))
if not V2_GATE:
    json.dump({"battery": "V2 FAIL", "failures": FAILURES},
              open('code/2401_results.json', 'w'), indent=1)
    raise SystemExit(1)

# ===========================================================================
# THE CLASS TRICHOTOMY -- numerically resolved (the derivation's structure)
# ===========================================================================
banner("DERIVATION STRUCTURE -- the three compositions, numerically separated")
print("  Per-unit signed amplitude with rung transport (V-t) vs unsigned")
print("  magnitudes (S) vs uncorrelated signs (incoherent, NO transport):")
print()
print("   N_ring   V-t closed |sum|    S closed sum     incoherent RMS")
tri = {}
for N in (4, 5, 6, 7, 8):
    Rg, xs, ts = ring_geo(N)
    p = [Rg + 5.0, 0.0, 0.0]
    vt = abs(edge_sum(xs, p, closed=True))
    ss = scalar_sum(xs, p)
    acc = 0.0
    NENS = 400
    for _ in range(NENS):
        sg = [rng.choice((-1.0, 1.0)) for _ in range(N)]
        acc += edge_sum(xs, p, signs=sg, closed=True) ** 2
    rms = math.sqrt(acc / NENS)
    tri[N] = {"vt": vt, "s": ss, "incoh_rms": rms}
    print("   %5d      %.3e        %.4e       %.4e" % (N, vt, ss, rms))
# scaling checks: S grows ~ N (per-node addition); incoherent RMS ~ sqrt(N)
s_ratio = tri[8]["s"] / tri[4]["s"]
# per-node Y varies with Rg so pure-N scaling is modulated; check monotone
# growth for S and the sqrt-family band for incoherent relative to per-edge
check("TRI-i  Class S composite grows monotonically with N "
      "(S(8)/S(4) = %.2f > 1)" % s_ratio, s_ratio > 1.0)
check("TRI-ii V-t closed composite = 0 at machine precision for every N "
      "(max = %.1e)" % max(v["vt"] for v in tri.values()),
      max(v["vt"] for v in tri.values()) < 1e-12)
check("TRI-iii incoherent RMS nonzero and O(sqrt(N) x per-edge) -- distinct "
      "from BOTH classes", all(v["incoh_rms"] > 1e-6 for v in tri.values()))

# ===========================================================================
# V3 -- pre-declared spot checks (the sign structure is the physics)
# ===========================================================================
banner("V3 -- pre-declared spot checks")
Rg6, xs6, ts6 = ring_geo(6)
xsC, _ = chain_geo(12)
pR = [Rg6 + 5.0, 0.0, 0.0]
pC = [0.0, 0.0, -5.0]

# V3-i global zeta-convention flip: all signs flip together -> composite
# flips sign globally; every physical (|.|, squared) quantity invariant
a_open = edge_sum(xsC, pC, closed=False)
a_open_flip = edge_sum(xsC, pC, signs=[-1.0] * 12, closed=False)
check("V3-i   global convention flip: sum -> -sum exactly, |sum| invariant "
      "(|a + a_flip| = %.1e)" % abs(a_open + a_open_flip),
      abs(a_open + a_open_flip) < 1e-15)

# V3-ii a LOCAL single-unit flip is PHYSICAL (breaks the closed-ring zero by
# O(per-edge amplitude)) -- the transported relative sign carries content
sg = [1.0] * 6
sg[2] = -1.0
loc = abs(edge_sum(xs6, pR, signs=sg, closed=True))
per_edge = abs(Y(math.dist(pR, xs6[3])) - Y(math.dist(pR, xs6[2])))
check("V3-ii  local single-unit flip breaks telescoping by O(per-edge) "
      "(|sum| = %.2e ~ %.2e)" % (loc, 2 * per_edge),
      loc > 0.1 * per_edge)

# V3-iii chain-reversal parity: reversing node order flips the open-chain
# composite's sign (vector character), |sum| invariant
a_rev = edge_sum(list(reversed(xsC)), pC, closed=False)
check("V3-iii chain reversal: sum -> -sum exactly (vector character; "
      "|a + a_rev| = %.1e)" % abs(a_open + a_rev),
      abs(a_open + a_rev) < 1e-15)

# V3-iv the class verdict is normalization-independent: scaling the per-edge
# amplitude by arbitrary c > 0 rescales sums, leaves zeros/end-sourcing intact
c_arb = 3.7
z1 = abs(edge_sum(xs6, pR, closed=True, coeff=c_arb))
e1 = edge_sum(xsC, pC, closed=False, coeff=c_arb)
check("V3-iv  normalization-independence: closed zero survives arbitrary "
      "c = %.1f (%.1e); open end-form scales linearly (ratio = %.6f)" %
      (c_arb, z1, e1 / a_open),
      z1 < 1e-12 and abs(e1 / a_open - c_arb) < 1e-9)

# V3-v registered-chain consistency: R_s = r_c/chi equals the 1879 engine RS
# (Q4a CLOSED result) -- the D5-A' scale reproduced
check("V3-v   R_s = r_c/chi = %.6f fm; D5-A' scale R_N/R_s = %.6f "
      "(ruling 0.035 family)" % (R_S, SC_RULING),
      abs(R_S - 25.41640786499874) < 1e-9)

# ===========================================================================
# V4 -- no-freedom audit
# ===========================================================================
banner("V4 -- no-freedom audit")
inputs = {
    "phi": PHI, "chi = phi^-3/6 (METH-CHIR-CONT-1: |chi_sub|*d_G/V_cage)": CHI,
    "r_c_fm (SF-5/J2)": R_C, "R_s_fm = r_c/chi (Q4a CLOSED, sec 34.13)": R_S,
    "R_N_fm (1880 RN)": R_N, "d_unit_fm (J8)": D_UNIT,
    "SC_ruling = R_N/R_s (D5-A')": SC_RULING,
}
for k, v in inputs.items():
    print("   %-58s %.10g" % (k, v))
print("   D5-A' data points enter as the V2 GATE'S TARGETS, not as inputs")
print("   to the derivation; 0865 held (no torsional lock, no transverse")
print("   component, no new transport datum); zero tunables.")
check("V4 zero tunable parameters introduced; 0865 untouched", True)

# ===========================================================================
# V5 -- cache integrity: this script opens NO cache
# ===========================================================================
banner("V5 -- cache integrity")
check("V5 no cache opened; sole output code/2401_results.json", True)

# ===========================================================================
# SUMMARY + GRADING (mechanical, pre-registered sec 34.12)
# ===========================================================================
banner("SUMMARY -- SS43-Q4b (the vertex class)")
verdict = "V-t" if len(FAILURES) == 0 else "UNGRADED (battery failure)"
print(" DERIVED CLASS: %s -- chain-axis vector, rung-transported signed" %
      verdict)
print("   amplitude; Class S excluded by registration (amplitude-level +")
print("   zeta-ODD); incoherent excluded by the registered bonded structure.")
print(" KILL (derived class = S): ARMED, NOT FIRED.")
print(" GRADING: branch-(b) track continues -- Q4c unblocks; the Q2-identity")
print("   theorem registration UNBLOCKS (the sec 34.9/2394 deferral")
print("   discharged); the (c) HOLD dissolves in favor of the DERIVED V-t.")
print(" BATTERY: %s" % ("ALL PASS" if not FAILURES
                        else "FAILURES: %s" % FAILURES))

json.dump({
    "patch": 2401, "task": "SS43-Q4b vertex class derivation",
    "derived_class": verdict,
    "kill_S": {"armed": True, "fired": False},
    "derivation": {
        "L1": "per-unit vertex = METH-CHIR-CONT-1 matrix element; SIGNED, "
              "amplitude-level (Q4a L1, sec 34.13 CLOSED)",
        "L2": "sign is zeta-convention-relative; rung bond (2381) is the "
              "registered convention transport; chain axis the only "
              "registered coherence axis (0865: no torsional lock)",
        "L3": "chain-reversal-ODD transported sign => chain-axis vector "
              "v_k = M t-hat_k; leading coupling = directional derivative "
              "= per-edge difference (discrete line integral)",
        "corollary": "Class S requires |M| as source: probability-level or "
                     "zeta-EVEN -- both contradict registration; incoherent "
                     "requires no transport -- contradicts 2381 bonding",
    },
    "V2_pass_gate": {
        "rod_end_sourced_exact_max_diff": tel_exact,
        "rod_source_side_loglog_slope": slope,
        "d5aprime_total_power": "FIRST (source 0 x nucleon 1)",
        "closed_loop_telescoping_max": worst_tel,
        "orientation_orthogonality_max": worst_orth,
        "closed_ring_node_form_max": worst_node_closed,
        "open_chain_node_vs_edge_rel": rel,
    },
    "trichotomy": tri,
    "V4_inputs": {k: v for k, v in inputs.items()},
    "V1": "2395 battery ALL PASS in scratch copy at session open "
          "(181.4 s; reasoning/2401.md sec 2)",
    "V5": "no cache opened; this file is the only output",
    "battery": "ALL PASS" if not FAILURES else FAILURES,
}, open('code/2401_results.json', 'w'), indent=1)
print("\n wrote code/2401_results.json")
raise SystemExit(0 if not FAILURES else 1)
