#!/usr/bin/env python3
"""3176_polarization_to_force_conversion.py — THE MISSING FACTOR.

AUDIT QUESTION (Patch 3176). The band `SUST_REF = 2.6e-3` used to judge
Route B, Route C and the β-ladder is `0.026·β` at β = 0.10, taken from
`sketches/beta_zero_control_record.md` §3. There, 0.026·β is the
amplitude of the motion-proportional (a1) component of **p_x = the Sea
pair's dipole moment** (`p = plus - minus` in `2914_response_field.py`),
inner ring ρ ∈ [1,3] — a DISPLACEMENT of Sea-pair members.

`sust_B` is a **FORCE on the source**: `F = src_net[0]`, the axial
component of Σ_e q_src·q_e·û /(4π(R²+SOFT2)) evaluated at the source.

The founder's ruling (21 Aug 2026): a coupling DOES exist — "every CP's
position converts to source force" — but it is 1/r³-suppressed and
configuration-dependent, with dipole cancellation applying or not
depending on separation vs distance. So the conversion factor is a
computable geometric quantity, NOT unity. The transplant used unity.

THIS SCRIPT COMPUTES THE FACTOR, using the engine's exact force law and
the exact 2914 Sea geometry (`build_sea_sym`, the geometry in which
0.026 was measured). No new campaign; no engine legs; pure geometry.

METHOD (frozen before the number is seen):
  1. Build the 2914 Sea (class A and B, seeds 4,5,6 — the 2918 grid).
  2. Impose a UNIT axial polarization increment on inner-ring pairs
     only (ρ ∈ [1,3]), matching what 0.026·β describes: each inner-ring
     pair's separation vector gains δp_x = A along +x, A = 0.026·β.
  3. Compute the source's axial force EXACTLY (engine amp law, both
     members, no dipole approximation) with and without δp.
  4. F_CONV ≡ ΔF_x / A  — the factor that carries a polarization
     amplitude into a force. The band SHOULD have been
     |F_CONV| · 0.026 · β, not 0.026 · β.

DISCLOSED LIMITATION: the 0.026 figure is quoted for the inner ring
only; the full a1 spatial profile is not archived in a form this script
can read. Applying it to inner-ring pairs alone is the faithful reading
of the quoted number. If outer rings carry same-sign a1 polarization,
|F_CONV| grows; if opposite-sign, it shrinks. The script therefore also
reports the all-ring variant as a bound, and both are reported — neither
is selected.
"""
import os, sys
import numpy as np
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
EM = os.path.normpath(os.path.join(
    HERE, '../../../../flagship_papers/electromagnetism/code'))


def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(EM, fn))
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


eng = _load('eng', '2902_mobile_sea_engine.py')
# 2907 imports numba via 2906; build_sea_sym is self-contained, so it is
# lifted here VERBATIM from 2907_round3_driver.py lines 16-45 (checked
# character-identical at Patch 3176) to avoid the numba dependency.
_src = open(os.path.join(EM, '2907_round3_driver.py')).read()
_i = _src.index('def build_sea_sym')
_j = _src.index('\ndef ', _i + 10)
_ns = {'np': np, 'eng': eng, 'D0': eng.D0}
exec(compile(_src[_i:_j], '2907_build_sea_sym', 'exec'), _ns)


class _R3:
    build_sea_sym = staticmethod(_ns['build_sea_sym'])


r3 = _R3()

SOFT2 = eng.SOFT2
BETA_REF = 0.10
A_REF = 0.026 * BETA_REF          # the quoted amplitude at the band's β


def axial_force_at_source(plus, minus, src=np.zeros(3)):
    """Exact engine force law, static (no retardation): the axial
    component of the SSV_net at the source from every Sea CP.
    q_src = +1; plus members q=+1, minus members q=-1."""
    out = 0.0
    for arr, qe in ((plus, +1.0), (minus, -1.0)):
        d = src[None, :] - arr                  # source minus emitter
        R = np.linalg.norm(d, axis=1)
        amp = 1.0 / (4 * np.pi * (R * R + SOFT2))
        ux = d[:, 0] / np.where(R > 0, R, 1.0)
        out += float(np.sum(qe * 1.0 * amp * ux))
    return out


def run():
    print("=" * 74)
    print("POLARIZATION -> FORCE CONVERSION FACTOR (Patch 3176)")
    print("engine law: amp = 1/(4*pi*(R^2+SOFT2)); exact two-member sum")
    print(f"quoted amplitude A = 0.026*beta = {A_REF:.4e} at beta={BETA_REF}")
    print("=" * 74)
    rows = []
    for cls in ('A', 'B'):
        for seed in (4, 5, 6):
            sea, qs = r3.build_sea_sym(cls, seed)
            Np = len(sea) // 2
            plus, minus = sea[:Np].copy(), sea[Np:].copy()
            cen = 0.5 * (plus + minus)
            rho = np.hypot(cen[:, 1], cen[:, 2])
            inner = (rho >= 1.0) & (rho <= 3.0)
            F0 = axial_force_at_source(plus, minus)
            xi = cen[:, 0]      # axial offset; source sits at x = 0
            for label, mask, prof in (
                    ('inner-U', inner, np.ones(Np)),
                    ('all-U', np.ones(Np, dtype=bool), np.ones(Np)),
                    ('inner-O', inner, np.sign(xi)),
                    ('all-O', np.ones(Np, dtype=bool), np.sign(xi))):
                # -U = UNIFORM axial polarization increment.
                # -O = ODD (sign(xi)) increment — the parity the 2918
                #      record reports for the persistent map
                #      ("persistent map is ODD-dominated"). Parity is the
                #      dominant uncertainty: a uniform increment nearly
                #      cancels by fore/aft symmetry, an odd one adds.
                #      BOTH are reported; neither is selected.
                w = prof * mask
                p2, m2 = plus.copy(), minus.copy()
                p2[:, 0] += 0.5 * A_REF * w
                m2[:, 0] -= 0.5 * A_REF * w
                F1 = axial_force_at_source(p2, m2)
                conv = (F1 - F0) / A_REF
                rows.append((cls, seed, label, int(mask.sum()), F0,
                             F1 - F0, conv))
    print(f"{'cls':>3} {'seed':>4} {'profile':>8} {'Npair':>6} "
          f"{'F0':>12} {'dF':>12} {'F_CONV':>10}")
    for r in rows:
        print(f"{r[0]:>3} {r[1]:>4} {r[2]:>8} {r[3]:>6} "
              f"{r[4]:12.4e} {r[5]:12.4e} {r[6]:10.4f}")

    for label in ('inner-U', 'all-U', 'inner-O', 'all-O'):
        c = np.array([r[6] for r in rows if r[2] == label])
        band_should = abs(c.mean()) * A_REF
        print(f"\n[{label}] F_CONV = {c.mean():.4f} ± {c.std():.4f} "
              f"(n={len(c)})")
        print(f"[{label}] band as transplanted : {A_REF:.4e}")
        print(f"[{label}] band as it should be : {band_should:.4e} "
              f"(= |F_CONV| x {A_REF:.4e})")
        if band_should > 0:
            print(f"[{label}] transplanted/corrected ratio : "
                  f"{A_REF / band_should:.3f}")
    print("\nMeasured beta-ladder response at beta=0.10: 9.1406e-04")
    print("Compare against the CORRECTED band above, not against "
          f"{A_REF:.4e}.")
    print("=" * 74)


if __name__ == '__main__':
    run()
