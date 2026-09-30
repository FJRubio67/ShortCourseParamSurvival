import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import lognorm

INK="#1D2B45"; ORANGE="#E3661B"; TEAL="#23767E"; GREY="#8A93A3"; PAPER="#FBFBF9"
plt.rcParams.update({"svg.fonttype":"none",
  "font.family":["IBM Plex Sans","Helvetica Neue","Arial","DejaVu Sans"],
  "font.size":17,"axes.edgecolor":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,
  "text.color":INK,"axes.spines.top":False,"axes.spines.right":False,
  "figure.facecolor":"none","axes.facecolor":"none"})

# --- Bathtub curve -------------------------------------------------------
t=np.linspace(0.01,10,600)
early=0.35*(t)**(-0.6)*np.exp(-t/0.8)
random_=np.full_like(t,0.25)
wear=0.012*(t/4)**5
h=early+random_+wear
fig,ax=plt.subplots(figsize=(9,4.2))
ax.axvspan(0,2.2,color=TEAL,alpha=0.08,lw=0); ax.axvspan(7.2,10,color=ORANGE,alpha=0.08,lw=0)
ax.plot(t,h,color=INK,lw=3)
ax.set_ylim(0,1.6); ax.set_xlim(0,10)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("Time in service"); ax.set_ylabel("Hazard  h(t)")
ax.text(0.35,1.45,"Early failures",ha="left",fontsize=19,color=TEAL,weight="bold")
ax.text(0.35,1.30,"defects, poor installation",ha="left",fontsize=15.5,color=TEAL)
ax.text(4.3,0.52,"Random failures",ha="center",fontsize=19,weight="bold")
ax.text(4.3,0.41,"accidental loads, third-party damage",ha="center",fontsize=11.5)
ax.text(8.75,1.45,"Wear-out",ha="right",fontsize=19,color=ORANGE,weight="bold")
ax.text(8.75,1.30,"corrosion, fatigue, ageing",ha="right",fontsize=15.5,color=ORANGE)
fig.tight_layout(); fig.savefig("images/bathtub.svg",transparent=True); fig.savefig("/tmp/bathtub.png",facecolor="white"); plt.close(fig)

# --- Hazard shapes catalogue ---------------------------------------------
t=np.linspace(0.005,5,600)
def weib(t,k,lam=1.5): return (k/lam)*(t/lam)**(k-1)
def lnorm_h(t,mu=0.3,s=0.6):
    d=lognorm(s,scale=np.exp(mu)); return d.pdf(t)/d.sf(t)
def pgw(t,sig,nu,gam): return nu/(gam*sig**nu)*t**(nu-1)*(1+(t/sig)**nu)**(1/gam-1)
fig,axs=plt.subplots(1,4,figsize=(13,3.4))
ax=axs[0]
for k,lab,c in [(2.2,"increasing",ORANGE),(1,"constant",GREY),(0.6,"decreasing",TEAL)]:
    ax.plot(t,weib(t,k),lw=2.6,color=c,label=lab)
ax.set_title("Weibull",loc="left",weight="bold",fontsize=15); ax.set_ylim(0,3); ax.legend(frameon=False,fontsize=14)
ax=axs[1]; ax.plot(t,lnorm_h(t),lw=2.6,color=INK)
ax.set_title("Lognormal: unimodal",loc="left",weight="bold",fontsize=15); ax.set_ylim(0,1.6)
ax=axs[2]; ax.plot(t,pgw(t,20,0.7,0.181),lw=2.6,color=ORANGE)
ax.set_title("PGW: bathtub",loc="left",weight="bold",fontsize=15); ax.set_ylim(0,2)
ax=axs[3]; ax.plot(t,pgw(t,0.6,2.5,8),lw=2.6,color=TEAL)
ax.set_title("PGW: unimodal",loc="left",weight="bold",fontsize=15); ax.set_ylim(0,0.45)
for ax in axs: ax.set_yticks([]); ax.set_xticks([]); ax.set_xlabel("t")
axs[0].set_ylabel("h(t)")
fig.tight_layout(); fig.savefig("images/hazard-shapes.svg",transparent=True); fig.savefig("/tmp/hazard-shapes.png",facecolor="white"); plt.close(fig)
print("ok")

# --- Title-slide curve (decorative bathtub line, no axes) ----------------
t=np.linspace(0.02,10,600)
h=0.35*t**(-0.6)*np.exp(-t/0.8)+0.25+0.012*(t/4)**5
fig=plt.figure(figsize=(16,4)); ax=fig.add_axes([0,0,1,1])
ax.plot(t,h,color=ORANGE,lw=4,solid_capstyle="round")
ax.set_xlim(-0.2,10.2); ax.set_ylim(0,1.5); ax.axis("off")
fig.savefig("images/title-curve.svg",transparent=True); plt.close(fig)
