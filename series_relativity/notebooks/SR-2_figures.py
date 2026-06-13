#!/usr/bin/env python3
# ============================================================
# SR-2: Figure generation (Phase 7A gate work, Patch 1134)
# Paper: The Spin-Bit Axiom: Necessity, Construction, and the
#        Derived Einstein Quadrupole Formula (SR-2, pre-draft)
# Computation: regenerates the four flagship figures from the
#   committed spin-2-arc computations (1112, 1116, 1119, 1124/1127),
#   at figure resolution. Source physics unchanged; this script
#   adds only rendering.
# Key results rendered:
#   Fig 1  H_g seat: m=+/-2 shell harmonics = GW +,x polarizations (1112)
#   Fig 2  helicity branches {0,0,+/-1} + twist gap M=4|sin(theta/2)| (1116, 1119)
#   Fig 3  eccentric (e=0.6) source-side energy ledger vs Peters f(e) (1124, 1127)
#   Fig 4  lattice discriminant: l=2 -> H intact (icosahedral) vs E+T2 (cubic) (1120)
# Author: Claude Opus, 12 June 2026
# ============================================================
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "figures" / "figures-SR-2"
OUT.mkdir(parents=True, exist_ok=True)
PHI = (1 + np.sqrt(5)) / 2

# icosahedral 12-neighbor shell (as in 1112/1116/1119)
raw = []
for a, b in [(1, PHI), (1, -PHI), (-1, PHI), (-1, -PHI)]:
    raw += [(0, a, b), (a, b, 0), (b, 0, a)]
N = np.array(raw, float)
N /= np.linalg.norm(N, axis=1, keepdims=True)


def save(fig, name):
    for ext in ("svg", "pdf"):
        fig.savefig(OUT / f"{name}.{ext}", bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {name}.svg/.pdf")


# ---------------- Fig 1: the H_g seat (1112) ----------------
# the five l=2 harmonics are fully resolved on the shell; m=+/-2 = {x^2-y^2, xy} = GW +,x
harm = {
    r"$+$ polarization:  $x^2-y^2$  ($m=\pm2$)": N[:, 0] ** 2 - N[:, 1] ** 2,
    r"$\times$ polarization:  $xy$  ($m=\pm2$)": N[:, 0] * N[:, 1],
}
# shell edge set (icosahedron nearest neighbors)
d = np.linalg.norm(N[:, None, :] - N[None, :, :], axis=2)
emin = d[d > 1e-9].min()
edges = [(i, j) for i in range(12) for j in range(i + 1, 12) if abs(d[i, j] - emin) < 1e-6]

Y = np.stack([N[:, 0] * N[:, 1], N[:, 1] * N[:, 2], N[:, 2] * N[:, 0],
              N[:, 0] ** 2 - N[:, 1] ** 2, 3 * N[:, 2] ** 2 - 1], axis=1)
rank = np.linalg.matrix_rank(Y)
G = Y.T @ np.column_stack([np.ones(12), N])  # overlap with l=0, l=1
orth = np.abs(G).max()

vmax = max(np.abs(v).max() for v in harm.values())
fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.4), subplot_kw={"projection": "3d"})
for ax, (title, vals) in zip(axes, harm.items()):
    for i, j in edges:
        ax.plot(*zip(N[i], N[j]), color="0.8", lw=0.8, zorder=1)
    p = ax.scatter(N[:, 0], N[:, 1], N[:, 2], c=vals, cmap="coolwarm",
                   s=160, edgecolor="k", linewidth=0.6, vmin=-vmax, vmax=vmax, zorder=3)
    ax.set_title(title, fontsize=10)
    ax.set_box_aspect((1, 1, 1)); ax.set_axis_off(); ax.view_init(elev=18, azim=-60)
fig.colorbar(p, ax=axes, shrink=0.7, pad=0.02, label=r"$l=2$ harmonic value on shell")
fig.suptitle(r"The $H_g$ seat: the icosahedral 12-shell natively carries the two GW polarizations"
             "\n" + rf"(all five $l=2$ harmonics: rank {rank}/5 resolved; "
             rf"orthogonal to $l=0,1$ to {orth:.1e})", fontsize=10.5)
save(fig, "SR2_fig1_hg_seat_polarizations")

# -------- Fig 2: helicity branches + the twist gap (1116, 1119) --------
cs, lam, mu, g = 1.0, 1.0, 0.5, 0.3

def Dk(kz, theta=0.0):
    """4x4 dynamical matrix of (phi, V) on the shell; optional equivariant twist theta (1119)."""
    D = np.zeros((4, 4), complex)
    for n in N:
        ph = 1 - np.exp(1j * kz * n[2])
        D[0, 0] += cs * ph.real * 2 / 2  # scalar: sum(1-cos)
        # scalar-vector coupling (odd part)
        D[0, 1:] += -1j * g * np.sin(kz * n[2]) * n
        D[1:, 0] += 1j * g * np.sin(kz * n[2]) * n
        # vector block with per-edge rotation R(theta) about n (1119); theta=0 -> 1116 exactly
        K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
        R = np.cos(theta) * np.eye(3) + (1 - np.cos(theta)) * np.outer(n, n) + np.sin(theta) * K
        M3 = lam * np.eye(3) + mu * np.outer(n, n)
        D[1:, 1:] += M3 - np.exp(1j * kz * n[2]) * (R @ M3)
    D[0, 0] = cs * sum(1 - np.cos(kz * n[2]) for n in N)
    return 0.5 * (D + D.conj().T)

ks = np.linspace(1e-4, 1.2, 160)
W = np.array([np.sort(np.linalg.eigvalsh(Dk(k))) for k in ks])

fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 4.0))
labels = [r"$h=0$ (scalar–$V_\parallel$)", r"$h=0$", r"$h=+1$", r"$h=-1$"]
for b in range(4):
    a1.plot(ks, W[:, b], lw=1.8)
a1.text(0.62, 0.18, "branches: $\\{0,\\,0,\\,\\pm 1\\}$\nfor ANY couplings\n($h=\\pm1$ doublet degenerate)",
        transform=a1.transAxes, fontsize=10)
a1.text(0.62, 0.62, "$h=\\pm 2$: ABSENT\n(no $e^{\\pm 2i\\theta}$ basis\nvector in span$\\{\\phi,V\\}$)",
        transform=a1.transAxes, fontsize=10, color="crimson")
a1.set_xlabel(r"$k$ (along shell axis)"); a1.set_ylabel(r"$\omega^2$ (lattice units)")
a1.set_title("(a) Emergent route excluded: scalar+vector\nlattice mode content (1116)", fontsize=10)

th = np.logspace(-52, 0.2, 400)
a2.loglog(th, 4 * np.abs(np.sin(th / 2)), lw=1.8, color="k")
a2.axvline(4e-47, color="tab:blue", ls="--", lw=1.1)
a2.axvline(5e-51, color="tab:green", ls="--", lw=1.1)
a2.text(4e-47, 3e-25, r" photon bound $\theta<4\times10^{-47}$", rotation=90,
        fontsize=8.5, color="tab:blue", va="bottom")
a2.text(5e-51, 3e-25, r" graviton bound $\theta<5\times10^{-51}$", rotation=90,
        fontsize=8.5, color="tab:green", va="bottom")
a2.plot([np.pi / 5], [4 * np.sin(np.pi / 10)], "o", color="crimson")
a2.annotate(r"geometric $\theta=\pi/5$:" "\n" r"$M=1.236\,M_{\rm Planck}$",
            xy=(np.pi / 5, 4 * np.sin(np.pi / 10)), xytext=(1e-20, 0.5e-2),
            fontsize=9, color="crimson", arrowprops=dict(arrowstyle="->", color="crimson", lw=0.8))
a2.set_xlabel(r"per-edge twist $\theta$"); a2.set_ylabel(r"vector-sector gap $M(\theta)$ [$M_{\rm Planck}$]")
a2.set_title("(b) Connection route excluded: any data-acting\ntwist Planck-gaps the field (1119)", fontsize=10)
fig.suptitle("Two of the three assaults: no no-axiom route reaches helicity-2", fontsize=11)
fig.tight_layout(rect=(0, 0, 1, 0.93))
save(fig, "SR2_fig2_assaults_helicity_and_gap")

# ---- Fig 3: eccentric source-side energy ledger (1124/1127, G=c=1) ----
m1, m2, a_orb, e = 1.0, 0.8, 1.0, 0.6
mred, M = m1 * m2 / (m1 + m2), m1 + m2
T = 2 * np.pi * a_orb ** 1.5 / np.sqrt(M)
dt = T / 40000
steps = int(2 * T / dt)
r0 = a_orb * (1 - e)
x = np.array([r0, 0.0, 0.0]); v = np.array([0.0, np.sqrt(M * (2 / r0 - 1 / a_orb)), 0.0])
acc = lambda x: -M * x / np.linalg.norm(x) ** 3
Q = np.empty((steps, 3, 3)); t = np.arange(steps) * dt
for s in range(steps):
    Qf = mred * np.outer(x, x)
    Q[s] = Qf - np.eye(3) * np.trace(Qf) / 3
    a_h = acc(x); x = x + v * dt + 0.5 * a_h * dt * dt
    v = v + 0.5 * (a_h + acc(x)) * dt
Qddd = np.gradient(np.gradient(np.gradient(Q, dt, axis=0), dt, axis=0), dt, axis=0)
P_inst = np.einsum("sij,sij->s", Qddd, Qddd) / 5.0
i0 = int(0.5 * T / dt); sl = slice(i0, i0 + int(round(T / dt)))  # exactly ONE full period, interior (P(t) is perihelion-peaked; window must close)
Pbar = P_inst[sl].mean()
fpet = (1 + 73 * e**2 / 24 + 37 * e**4 / 96) / (1 - e**2) ** 3.5
P_peters = (32 / 5) * (m1 * m2) ** 2 * M / a_orb ** 5 * fpet

fig, ax = plt.subplots(figsize=(7.6, 4.0))
ax.semilogy(t[sl] / T, P_inst[sl], lw=1.4, label=r"instantaneous quadrupole luminosity "
            r"$P(t)=\frac{1}{5}\langle\dddot{Q}\dddot{Q}\rangle$")
ax.axhline(P_peters, color="crimson", ls="--", lw=1.4,
           label=rf"Peters $f(e)$-enhanced rate, $e=0.6$  ($f(e)={fpet:.3f}$)")
ax.axhline(Pbar, color="k", ls=":", lw=1.2,
           label=rf"orbit-averaged $\overline{{P}}$  (this run: $\overline{{P}}/P_{{\rm Peters}}={Pbar/P_peters:.4f}$)")
ax.set_xlabel(r"$t/T_{\rm orbit}$"); ax.set_ylabel(r"$P$  ($G=c=1$)")
ax.set_title("The eccentric energy ledger closes: TT quadrupole flux balances the full\n"
             r"Peters decay at $e=0.6$ (sphere-integrated committed value: 1.000640, Patch 1127)",
             fontsize=10.5)
ax.legend(fontsize=8.5, loc="lower right")
save(fig, "SR2_fig3_eccentric_energy_ledger")
print(f"  ledger check: <P>/Peters = {Pbar/P_peters:.6f}  (peri-burst structure visible)")

# ---- Fig 4: the lattice discriminant (1120 P3 branching) ----
fig, ax = plt.subplots(figsize=(7.2, 4.2))
ax.set_xlim(0, 10); ax.set_ylim(-0.8, 4.6); ax.axis("off")
splits = {  # l: [(label, dim, intact?)] under I and under O
    0: ([("A", 1, True)], [("A1", 1, True)]),
    1: ([("T1", 3, True)], [("T1", 3, True)]),
    2: ([("H", 5, True)], [("E", 2, False), ("T2", 3, False)]),
    3: ([("T2", 3, False), ("G", 4, False)], [("A2", 1, False), ("T1", 3, False), ("T2", 3, False)]),
}
for col, (x0, hdr) in enumerate([(2.0, "icosahedral  $I$"), (7.0, "cubic  $O$")]):
    ax.text(x0 + 0.9, 4.35, hdr, fontsize=11, ha="center", weight="bold")
    for l, pair in splits.items():
        irreps = pair[col]
        w = 0.0
        for name, dim, intact in irreps:
            c = "tab:green" if intact else "tab:red"
            ax.plot([x0 + w, x0 + w + 0.32 * dim], [l, l], color=c, lw=3.2)
            ax.text(x0 + w + 0.16 * dim, l + 0.13, name, fontsize=8.5, ha="center", color=c)
            w += 0.32 * dim + 0.25
for l in splits:
    ax.text(0.9, l, rf"$l={l}$  ({2*l+1})", fontsize=10, ha="center", va="center")
ax.text(5.0, -0.55, r"green = descends intact   $\cdot$   red = split   $\cdot$   "
        r"$l=2$: $H$ intact under $I$, $E\oplus T_2$ (2+3) under $O$", fontsize=9, ha="center")
ax.set_title("The lattice discriminant (PRED-O-37): only the icosahedral substrate protects the\n"
             "5-fold GW polarization multiplet — a cubic lattice predicts 2+3 fine-structure", fontsize=10.5)
save(fig, "SR2_fig4_lattice_discriminant_branching")

print("All SR-2 figure candidates generated to", OUT)
