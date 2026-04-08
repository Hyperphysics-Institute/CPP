# ============================================================
# Spectral Dimension Extraction for SM8 Cage Graph
# ============================================================
# This notebook loads the GPU‑generated return‑probability CSV
# and fits  P(t) ~ t^{-d_s/2}  to extract the spectral dimension d_s.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Load return‑probability CSV
# ------------------------------------------------------------
df = pd.read_csv("nb02_SM8_600cell_2ring_return_prob.csv")

t_vals = df["t"].values
P_t = df["P"].values

print("Loaded", len(t_vals), "time steps")
print("Columns:", df.columns.tolist())

# ------------------------------------------------------------
# Plot return probability (log‑log)
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
plt.loglog(t_vals[1:], P_t[1:], 'o-', markersize=3)
plt.xlabel("t")
plt.ylabel("P(t)")
plt.title("Return probability (log-log)")
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.show()

# ------------------------------------------------------------
# Choose scaling window
# ------------------------------------------------------------
t_min, t_max = 50, 500
print("Scaling window:", t_min, "to", t_max)

mask = (df["t"] >= t_min) & (df["t"] <= t_max)
print("Number of points in window:", mask.sum())

# ------------------------------------------------------------
# Extract log–log data
# ------------------------------------------------------------
x = np.log(df["t"][mask])
y = np.log(df["P"][mask])

print("log(t) range:", x.min(), "to", x.max())
print("log(P) range:", y.min(), "to", y.max())

# ------------------------------------------------------------
# Fit slope and compute spectral dimension
# ------------------------------------------------------------
slope, intercept = np.polyfit(x, y, 1)
d_s = -2 * slope

print(f"Slope m = {slope:.6f}")
print(f"Spectral dimension d_s = {d_s:.6f}")

# ------------------------------------------------------------
# Plot fitted line
# ------------------------------------------------------------
plt.figure(figsize=(6,4))
plt.loglog(df["t"], df["P"], 'o', markersize=2, label="data")

x_fit = np.linspace(np.log(t_min), np.log(t_max), 200)
y_fit = slope * x_fit + intercept
plt.loglog(np.exp(x_fit), np.exp(y_fit), 'r-', label=f"fit (d_s={d_s:.3f})")

plt.xlabel("t")
plt.ylabel("P(t)")
plt.legend()
plt.title("Spectral Dimension Fit")
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.show()

# ------------------------------------------------------------
# Save a copy of the return-probability data
# ------------------------------------------------------------
output_path = "nb02_SM8_return_prob_data_current_graph_copy.csv"
df.to_csv(output_path, index=False)
print("Saved CSV to:", output_path)
