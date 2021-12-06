---
title: "Bifurcation Theory: A Brief Examination"
subtitle: "Source: https://github.com/varshakrishnakumar/Bifurcation-Theory-Examination"
date: \today
author: "Varsha Krishnakumar, varshak3@illinois.edu"
footnote: "Source: https://github.com/varshakrishnakumar/Bifurcation-Theory-Examination"
---  
## Abstract

This paper briefs basic understanding of *Bifurcation* and the *Bifurcation Theory*. It delves into examples of Local Bifurcation and details the behavior of unstable, stable, and semi-stable equilibrium solutions. Visualizations of considered vector fields are also analyzed with respect to their Ordinary Differential Equation (ODE) form. Two applications - computer virus infections and astrophysics - and their utilization of Bifurcation principles will be briefed. 

---

## I. An Introduction to Bifurcation Theory

In a *dynamical system*, a **bifurcation** is a qualitative change in behavior produced by varying parameters (known as *bifurcation parameters* in the system's dynamics. Within a family of Ordinary Differential Equations (ODEs), **Bifurcation Theory** imparts a strategy for investigating bifurcations that can occur. In a general case, the local stability properties of equilibria (or other invariants) at a bifurcation enforces changes in the dynamical system's behavior.[^1]

[^1]: Guckenheimer, J., “Bifurcation,” Scholarpedia: http://www.scholarpedia.org/article/Bifurcation. 

Considering the autonomous system of Ordinary Differential Equations:

$$ \dot{x} = f(x, \lambda),     x \in \mathbb{R}^n,     \lambda \in \mathbb{R}^p $$

A **bifurcation** happens at parameter $\lambda = \lambda _0$ if there are other parameter values close to $\lambda _0$ with different behavior of dynamics from those at $\lambda _0$. For example, there may be a nuance in the number of stability of equilibrium points. When a *bifurcation diagram* of a system is produced, the $\lambda$ parameter space can be divided into regions of *topologically equivalent systems* (that is, systems that have similar dynamic behavior). 

Conventionally, bifurcations are divided into two types: Local bifurcations and Global bifurcations. Since the objective of this examination is a simple overview, local bifurcations will be examined further in the upcoming sections. 

### II. Basic Case of Bifurcation: Local Bifurcation

Suppose a differential equation of this form is considered

$$ \frac{du}{dt} = f(u, \mu) $$

Here, $u$ is a function dependent on the parameter $t$ (signifying time), and $f$ is a vector field dependent on $u$ and $\mu$. From the structure of this ODE form, $\mu$ represents the bifurcation parameter. 

For each initial condition of the ODE, there must exist a unique solution for the equation. It must also be assumed that $C^k$ represents the class of the vector field, with $k >= 2$, and satisfies:

$$ f(0, 0) = 0,  \frac{\partial f}{\partial u} (0,0) = 0 $$

The first condition indicated that $u = 0$ is an equilibrium equation at $\mu = 0$. Varying parameter $\mu$ can provide an interesting set of bifurcation diagrams to study, as local bifurcations can occur in close vicinity of this equilibrium condition. 


### II.A. Local Bifurcation: Saddle-Node

Consider the following autonomous Ordinary Differential Equation[^2]:

[^2]: "Intro to bifurcation theory": https://www.math.ksu.edu/~albin/teaching/math340_fall2018/slides/03_bifurcations.html. 

$$ \frac{dx}{dt} = f(x) = x^2 + r $$

The behavior of $f(x)$ is dependent on the parameter $r$.

When $r < 0$, there are two equilibrium solutions: a stable equilibrium at $x(t) = - \sqrt{- r}$, and an unstable equilibrium $x(t) = \sqrt{- r}$. The stable equilibrium solution is always less than the unstable solution. 

When $r > 0$, there are no equilibrium solutions. However, at $r = 0$, there is one unique semi-stable equilibrium solution called the *Saddle-Node Bifurcation*. 

An example of the ODE field when $r = -1$ is shown in *Figure 1*. Instances of the ODE field when $r = 1$ and $r = 0$, as well as a sample program for trial purposes, is provided on the main GitHub Repository.[^3]

![Saddle-Node Bifurcation Diagram when r = - 1](plot-snapshots\saddlenodept1.png#left){#fig:saddlenodept2 width=80% height=50%}

[^3]: "Bifurcation Theory Examination": https://github.com/varshakrishnakumar/Bifurcation-Theory-Examination/plot-snapshots




### II.B. Local Bifurcation: Transcritical

Consider the following Ordinary Differential Equation:

$$ \frac{dx}{dt} = f(x) = rx - x^2 = x(r - x) $$

In this particular case, $x = 0$ and $x = r$ is always an equilibrium solution. As the value of $r$ changes, the behaviour of the solution curves change as well. 

When $r < 0$, $x = 0$ is a stable equilibrium solution, while $x = r$ is an unstable solution. When $r > 0$, $x = 0$ is an unstable equilibrium solution, while $x = r$ is a stable solution.

At $r = 0$, a semi-stable equilibrium solution is found. 

![Transcritical Bifurcation Diagram when r = - 1](plot-snapshots\transcritical1.png#left){#fig:saddlenodept2 width=80% height=50%}

### II.C. Local Bifurcation: Pitchfork 

Consider the following Ordinary Differential Equation:

$$ \frac{dx}{dt} = f(x) = rx - x^3 = x(r - x^2) $$

In this particular case, $x = 0$ and $x = \pm \sqrt{r}$ is always an equilibrium solution. When $r < 0$, $x = 0$ is a stable equilibrium solution, and the only equilibrium solution present. When $r >= 0$, $x = 0$ is an unstable equilibrium solution, while $x = \pm \sqrt{r}$ are stable solutions.

![Pitchfork Bifurcation Diagram when r = - 1](plot-snapshots\pitchfork1.png#left){#fig:saddlenodept2 width=80% height=50%}


## III. Brief Examination of Bifurcation Applications

### III.A. Bifurcation Principles Applied to a Computer Virus Model

Often, computer virus propagation models are studied using a Susceptible-Infected-External (*SIE*) model.[^4] A specific case of bifurcation, the *Hopf* bifurcation, is used.[^5] Computer viruses are significant threats to basic security on the Internet, and have hence caused a variety of setbacks in numerous fields reliant on Internet information. 

The SIE model can be represented in the form below [^6]:

$$ \frac{dS(t)}{dt} = -\delta S(t) - \eta S(t)I(t) - \gamma_1 S(t) + \alpha_2 I(t) + \gamma_2 E(t) $$

$$ \frac{dI(t)}{dt} = \eta S(t)I(t) - \delta I(t) - \alpha_1 I(t) - \alpha_2 I(t) $$

$$ \frac{dE(t)}{dt} = -\delta E(t) - \gamma_2 E(t) + \gamma_1 S(t) + \alpha_1 I(t) + \epsilon $$

Here, $S(t)$, $I(t)$ and $E(t)$ denote the behavior of susceptible computers, infected computers and external computers, respectively. $\delta$ is the rate at which each computer dies out, $\epsilon$ is the birth rate of external computers. Finally, $\alpha_1$, $\alpha_2$, $\gamma_1$, $\gamma_2$ and $\eta$ are the states' transmission rates.

An example of how this principle can be applied is the concept of infection delay. Since there is a period of time from when the virus enters a host to when it is active, an infection delay can exist from infected to infectious computers. [^7] Correspondingly, the values $\tau_1$, infection delay, and $\tau_2$, recovery delay, can be used to model the infection. 

![Behavior and Phase Portrait of Infection Delay (Song et al., 2014)](plot-snapshots\applications\computervirusmodel.jpg#left){#fig:computervirusmodel width=80% height=80%}

In *Figure 4*, the conditions $\tau_1 = 0$ and $\tau_2 = 4$ are assumed. Given this state, the virus infection equilibrium is asymptotically stable. 

[^4]: Zhang, Z., Bi, D., "Bifurcation analysis in a delayed computer virus model with the effect of external computers": https://doi.org/10.1186/s13662-015-0652-y

[^5]: Judson, T. W., “The ordinary differential equations project,” The Hopf Bifurcation: http://faculty.sfasu.edu/judsontw/ode/html-20200801/nonlinear04.html. 

[^6]: Chen, JY, Yang, XF, Gan, CQ, "Propagation of computer virus under the influence of external computers: a dynamical model".

[^7]: Song, H., Wang, Q., and Jiang, W., “Stability and Hopf bifurcation of a computer virus model with infection delay and recovery delay,” Journal of Applied Mathematics: https://www.hindawi.com/journals/jam/2014/929580/#EEq1.2. 

While the present research on computer virus models is detailed, most models do not completely explain all dynamics of the ODE models of computer viruses. Predictably, there are numerous unreviewd factors that could affect computer virus models.  


### III.B. Bifurcation Principles Applied to Astrophysics

In star systems, there is often a wide variety of instable mechanisms which can lead to bifurcation phenomena in stars. [^8] During the course of a star's evolution, one family of equilibrium solutions can become unstable, correspondingly leading to the bifurcation of a secondary family of equilibrium solutions. Rotationally induced turbulent diffusion (for example, the effects of atmospheric extension by rotation and stellar winds) can lead to a wide bifurcation in stellar evolution.

The consequences of the bifurcation effect on stellar instabilities are potentially important to the use of Artificial Intelligence (AI) in rotational velocity observations in the future. 

[^8]: Sattinger, D. H., Group theoretic methods in bifurcation theory, Berlin: Springer-Verlag, 1979. 