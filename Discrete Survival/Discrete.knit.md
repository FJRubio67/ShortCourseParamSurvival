---
title: " ``Discrete survival analysis'' "
author: "--"
#date: "2026-03-02"
#date: "--"
format:
  html:
    toc: true
    code-fold: true
  pdf: default
  docx: default
editor: source
bibliography: references.bib
---


# Discrete survival analysis

Suppose that event times can only happen at times $\tau_1,\dots,\tau_K,\infty$, where $\infty$ means that no event was observed within $[0,\tau_K]$. Events can only occur at each time point $\tau_j$. The survival function at time $k$ in this context is defined analogously to the continuous case:

```{=tex}
\begin{align*}
S(k) &= \Pr(T>k).
\end{align*}
```

However, the discrete-time hazard function at time $k$ is a conditional probability.

```{=tex}
\begin{align*}
h(k) &= \Pr(T=k \mid T \geq k).
\end{align*}
```

Some useful relationships are presented below (which are derived from the above definition and the definition of conditional probability:

```{=tex}
\begin{align*}
 \Pr(T=k) &=  h(k)S(k-1),\\
 S(k) &= S(k-1)(1-h(k)),\\
 S(k) &= \prod_{j=1}^k (1-h(j)).
\end{align*}
```

Taking logarithms on both sides we get

```{=tex}
\begin{align*}
 \log S(k) &= \sum_{j=1}^k \log(1-h(j)).
\end{align*}
```

This leads to the expression of the cumulative hazard:

```{=tex}
\begin{align*}
H(k) = - \log S(k) = -\sum_{j=1}^k \log(1-h(j)).
\end{align*}
```



# Pooled logistic model

Consider the model for the hazard (probability of receiving treatment)

```{=tex}
\begin{align*}
\mbox{logit}\, h(k \mid \mathbf{X}_{ik})&= \mbox{logit}\, \Pr( T = k \mid T \geq k, \mathbf{X}_{ik} ) \\
&= \alpha_k + \mathbf{X}_{ik},
\end{align*}
```

where $\alpha_k$ are the time-specific intercepts (baseline hazard), and $\mathbf{X}_{ik}$ are the covariates.


# Sequential Propensity Scores as Discrete-Time Hazards

## Setup

- Let $T$ be the time of treatment initiation: $T \in \{1, \dots, K, \infty\}$.  
- Define $A_k = 1$ if the individual is treated at time (window) $k$, 0 otherwise.  
- Let $\bar A_{k-1} = 0$ indicate not treated before month $k$.  
- Let $\bar L_k$ be the covariate history up to month $k$ (if available, otherwise we may need to use baseline covariate values).

By construction:

$$
A_k = 1 \iff T = k
$$

## Discrete-Time Hazard Function

The **discrete-time hazard of treatment** at time-window $k$ is:
  
$$
h(k \mid \bar L_k) = \Pr(T = k \mid T \ge k, \bar L_k)
$$

Interpretation: probability of receiving treatment in time-window $k$, conditional on not having been treated yet.


## Sequential Propensity Score
  
The **sequential propensity score** is defined as:
  
$$
e_k(\bar L_k) = \Pr(A_k = 1 \mid \bar A_{k-1} = 0, \bar L_k)
$$

Notice that:
  
$$
\{T \ge k\} \equiv \{\bar A_{k-1} = 0\}
$$

  Therefore:
  
$$
\boxed{
      e_k(\bar L_k) = h(k \mid \bar L_k)
}
$$

**Implication:** estimating a sequential propensity score is equivalent to estimating the discrete-time hazard of treatment.


## Connection to Weights
  
The probability of a specific treatment history up to month $k$ can be factorized as:
  
$$
\Pr(T = k \mid \bar L_k)   =  h(k \mid \bar L_k) \prod_{j<k} \big(1 - h(j \mid \bar L_j)\big).
$$

To check: **inverse probability weights** in longitudinal causal inference.


