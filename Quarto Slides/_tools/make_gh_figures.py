"""Static versions of the GH-structure illustrations (used in the PDF slides).
Baseline: exponentiated Weibull hazard with scale 1, shape 0.5, power 5 (unimodal)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def h_ew(t, sigma=1.0, kappa=0.5, alpha=5.0):
    z = (t / sigma) ** kappa
    Fw = 1 - np.exp(-z)
    fw = kappa / sigma * (t / sigma) ** (kappa - 1) * np.exp(-z)
    F = Fw ** alpha
    f = alpha * Fw ** (alpha - 1) * fw
    return f / (1 - F)

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "axes.spines.top": False, "axes.spines.right": False})
t = np.linspace(1e-3, 10, 800)
cols = ["#C8B3F5", "#A57BEF", "#341B51", "#7E3FE3", "#5A189A"]
for name, label, vals, fun in [
    ("gh-time", r"$\beta_1$", [-1, -0.5, 0, 0.5, 1], lambda b: h_ew(t * np.exp(b))),
    ("gh-level", r"$\beta_2$", [-1, -0.5, 0, 0.5, 1], lambda b: h_ew(t) * np.exp(b)),
]:
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for b, c in zip(vals, cols):
        lw, ls = (2.6, "-") if b == 0 else (1.8, "-")
        ax.plot(t, fun(b), color=("#341B51" if b == 0 else c), lw=lw, ls=("--" if b == 0 else ls),
                label=f"{label} = {b:g}" + (" (baseline)" if b == 0 else ""))
    ax.set_xlabel("$t$"); ax.set_ylabel("hazard"); ax.set_xlim(0, 10); ax.set_ylim(bottom=0)
    ax.legend(frameon=False, fontsize=10)
    for ext in ("svg", "pdf"):
        fig.savefig(f"figures/{name}.{ext}", bbox_inches="tight", transparent=True)
    plt.close(fig)
print("max baseline hazard", h_ew(t).max(), "at", t[h_ew(t).argmax()])
