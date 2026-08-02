#!/usr/bin/env python3
"""PATCH 2919 design check (STATUS: same-session capture at Patch 2925 --
run inline before the 2919 commit, committed at session close per s15.15).
Data-blind conditioning of the Round-3 regressor matrix."""
import numpy as np
pts = [(0.04,125),(0.07,107),(0.10,100),(0.14,89),(0.20,63),(0.0,63),(0.0,125)]
X = np.array([[1.0, 1.0/T, b, b**3] for b,T in pts])
Xs = X/np.linalg.norm(X,axis=0)
print('design condition number (col-normalized): %.1f' % np.linalg.cond(Xs))
print('singular values:', np.round(np.linalg.svd(Xs)[1],3))
