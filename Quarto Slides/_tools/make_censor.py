"""Redraws the censoring diagram (figures/censor.svg for HTML, figures/censor.pdf for PDF)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

EVENT, CENS, INK, MUTED = "#C62828", "#1F6FB5", "#341B51", "#6B6676"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})

fig, ax = plt.subplots(figsize=(8, 4.6))
end = 10
# (start, stop, status) for four individuals, top to bottom
people = [(0.3, end, "censored"), (0.0, 8.2, "event"), (2.2, 7.6, "censored"), (0.3, 5.5, "event")]
for k, (a, b, s) in enumerate(people):
    y = len(people) - k
    col = EVENT if s == "event" else CENS
    ax.plot([a, b], [y, y], color=col, lw=3, solid_capstyle="round")
    if s == "event":
        ax.plot(b, y, "o", ms=12, color=col)
    else:
        ax.plot(b, y, "o", ms=11, mfc="white", mec=col, mew=3)
    ax.text(b + 0.25, y + 0.18, s, color=col, va="bottom", ha="left", fontsize=13)

ax.axvline(end, color=INK, lw=2, ls="--")
ax.text(end, 0.25, "End of follow-up", color=INK, ha="center", va="top", fontsize=12)
ax.set_xlim(-0.4, 12.2); ax.set_ylim(0.3, 4.8)
ax.set_xlabel("Time", color=MUTED); ax.set_ylabel("Individuals", color=MUTED)
ax.set_xticks([]); ax.set_yticks([])
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(MUTED)
for ext in ("svg", "pdf"):
    fig.savefig(f"figures/censor.{ext}", bbox_inches="tight", transparent=True)
