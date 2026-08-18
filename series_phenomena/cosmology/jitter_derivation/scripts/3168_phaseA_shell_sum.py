#!/usr/bin/env python
"""Patch 3160 -- D-JITTER-1 Phase A: the paired-Sea shell sum.
Frozen statements in D_JITTER_1_charter.md S3 (written first).
Deterministic under seed."""
import numpy as np

def fib_sphere(n, rot):
    i = np.arange(n)+0.5
    phi = np.arccos(1-2*i/n); theta = (np.pi*(1+5**0.5)*i + rot) % (2*np.pi)
    return np.stack([np.sin(phi)*np.cos(theta), np.sin(phi)*np.sin(theta),
                     np.cos(phi)], 1)

def one_config(rng, K, fb, fpair, ds=1.0):
    F = np.zeros(3); Fm = np.zeros(3); Fd = np.zeros(3)
    for k in range(2, K+1):
        n = 12*k*k
        u = fib_sphere(n, rng.uniform(0, 2*np.pi))
        r = k*ds*(1 + rng.uniform(-0.05, 0.05, n))          # the PSR band
        bound = rng.random(n) < fb
        # free charges: shell-neutral alternating signs
        q = np.where(bound, 0.0, 1.0); s = np.ones(n); s[1::2] = -1
        q *= s
        mono = (q[:,None]*u/r[:,None]**2).sum(0)
        # dipoles: random orientation p, field ~ p/r^3 (magnitude proxy)
        m = bound.sum()
        if m:
            p = fib_sphere(m, rng.uniform(0, 2*np.pi))
            rd = r[bound]
            dip = (fpair*ds*p/rd[:,None]**3).sum(0)
        else:
            dip = np.zeros(3)
        F += mono + dip; Fm += mono; Fd += dip
    return F, Fm, Fd

def run(K, fb=0.47, fpair=0.5, M=100, seed=5):
    rng = np.random.default_rng(seed)
    Fs, Ms_, Ds = [], [], []
    for _ in range(M):
        F, Fm, Fd = one_config(rng, K, fb, fpair)
        Fs.append(F); Ms_.append(Fm); Ds.append(Fd)
    Fs = np.array(Fs)
    sig = float(np.linalg.norm(Fs.std(0)))
    se = sig/np.sqrt(2*(M-1))
    s_m = float(np.linalg.norm(np.array(Ms_).std(0)))
    s_d = float(np.linalg.norm(np.array(Ds).std(0)))
    return sig, se, s_m, s_d      # units: F_nn = 1/ds^2 = 1 at ds=1

if __name__ == "__main__":
    print("D-JITTER-1 Phase A: R(K) = sigma_far/F_nn  (fb=0.47, band 5%, M=100)")
    prev = None
    for K in (4, 8, 16, 32):
        sig, se, sm, sd = run(K)
        print(f"  K={K:3d}: R = {sig:.4f} +/- {se:.4f}   (monopole part {sm:.4f}, dipole part {sd:.4f})")
        if K == 16: prev = sig
        if K == 32:
            d = (sig-prev)/prev*100
            print(f"  convergence: R(32)-R(16) = {d:+.2f}% of R(16)  -> "
                  f"{'CONVERGENT (frozen criterion <= 5%)' if abs(d)<=5 else 'NON-CONVERGENT -> model incomplete as posed'}")
