---
title: "Bifurcation Theory: A Brief Examination"
subtitle: "Source: https://github.com/varshakrishnakumar/Bifurcation-Theory-Examination"
date: \today
author: "Varsha Krishnakumar, varshak3@illinois.edu"
footnote: "Source: https://github.com/varshakrishnakumar/Bifurcation-Theory-Examination"
---  

## I. An Introduction to Bifurcation Theory

In a *dynamical system*, a **bifurcation** is a qualitative change in behavior produced by varying parameters (known as *bifurcation parameters* in the system's dynamics. Within a family of Ordinary Differential Equations (ODEs), **Bifurcation Theory** imparts a strategy for investigating bifurcations that can occur. In a general case, the local stability properties of equilibria (or other invariants) at a bifurcation enforces changes in the dynamical system's behavior.[^1]

[^1]: Guckenheimer, J., “Bifurcation,” Scholarpedia: http://www.scholarpedia.org/article/Bifurcation. 

Considering the autonomous system of Ordinary Differential Equations:

$$ \dot{x} = f(x, \lambda),     x \in \mathbb{R}^n,     \lambda \in \mathbb{R}^p $$

A **bifurcation** happens at parameter $\lambda = \lambda _0$ if there are other parameter values close to $\lambda _0$ with different behavior of dynamics from those at $\lambda _0$. For example, there may be a nuance in the number of stability of equilibrium points. When a *bifurcation diagram* of a system is produced, the $\lambda$ parameter space can be divided into regions of *topologically equivalent systems* (that is, systems that have similar dynamic behavior). 

Conventionally, bifurcations are divided into two types: Local bifurcations and Global bifurcations. Since the objective of this examination is a simple overview, local bifurcations will be examined further in the upcoming sections. 

### I.I Basic Case of Bifurcation: Local Bifurcation

Suppose a differential equation of this form is considered

$$ \frac{du}{dt} = f(u, \mu) $$

Here, $u$ is a function dependent on the parameter $t$ (signifying time), and $f$ is a vector field dependent on $u$ and $\mu$. From the structure of this ODE form, $\mu$ represents the bifurcation parameter. 

For each initial condition of the ODE, there must exist a unique solution for the equation. It must also be assumed that $C^k$ represents the class of the vector field, with $k >= 2$, and satisfies:

$$ f(0, 0) = 0,  \frac{\partial f}{\partial u} (0,0) = 0 $$

The first condition indicated that $u = 0$ is an equilibrium equation at $\mu = 0$. Varying parameter $\mu$ can provide an interesting set of bifurcation diagrams to study, as local bifurcations can occur in close vicinity of this equilibrium condition. 


### I.I.A Local Bifurcation: Saddle-Node

Consider the following autonomous Ordinary Differential Equation[^2]:

[^2]: "Intro to bifurcation theory": https://www.math.ksu.edu/~albin/teaching/math340_fall2018/slides/03_bifurcations.html. 

$$ \frac{dx}{dt} = f(x) = x^2 + r $$

The behavior of $f(x)$ is dependent on the parameter $r$.

When $r < 0$, there are two equilibrium solutions: a stable equilibrium at $x(t) = - \sqrt{- r}$, and an unstable equilibrium $x(t) = \sqrt{- r}$. The stable equilibrium solution is always less than the unstable solution. 

When $r > 0$, there are no equilibrium solutions. However, at $r = 0$, there is one unique semi-stable equilibrium solution called the *Saddle-Node Bifurcation*. 

### I.I.B Local Bifurcation: Transcritical

Consider the following Ordinary Differential Equation:

$$ \frac{dx}{dt} = f(x) = rx - x^2 = x(r - x) $$

In this particular case, $x = 0$ and $x = r$ is always an equilibrium solution. As the value of $r$ changes, the behaviour of the solution curves change as well. 

When $r < 0$, $x = 0$ is a stable equilibrium solution, while $x = r$ is an unstable solution. When $r > 0$, $x = 0$ is an unstable equilibrium solution, while $x = r$ is a stable solution.

At $r = 0$, a semi-stable equilibrium solution is found. 

### I.I.C Local Bifurcation: Pitchfork 

Consider the following Ordinary Differential Equation:

$$ \frac{dx}{dt} = f(x) = rx - x^3 = x(r - x^2) $$

In this particular case, $x = 0$ and $x = \pm \sqrt{r}$ is always an equilibrium solution. When $r < 0$, $x = 0$ is a stable equilibrium solution, and the only equilibrium solution present. When $r >= 0$, $x = 0$ is an unstable equilibrium solution, while $x = \pm \sqrt{r}$ are stable solutions.


## II. A Brief Examination of Bifurcation Theory's Applications

Do something here
