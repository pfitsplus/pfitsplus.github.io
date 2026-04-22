---
title: "Fluid Dynamics"
permalink: /research/fluid-dynamics/
---
## Introduction
The evolution of [protoplanetary disks](/research/protoplanetary-disks/) and the emergence of [planets](/research/planet-formation/) are governed by complex fluid dynamics spanning magnetized turbulence, multi-fluid dust–gas interactions, and radiation transport.
Our group develops and applies large-scale numerical simulations—using codes such as [Athena++](https://www.athena-astro.app/){:target="_blank"} and the [Pencil Code](http://pencil-code.nordita.org/){:target="_blank"}—to understand the instabilities, turbulent transport, and structural features that ultimately set the conditions for planet formation.

- Disk fluid dynamics couples gas, magnetic fields, radiation, and solid particles across wide ranges of scales
- Instabilities drive turbulence and generate large-scale structures (vortices, rings, spirals)
- Turbulent diffusion and dust settling regulate solid-particle concentrations in the planet-forming midplane
- Numerical experiments allow direct comparison with ALMA and other high-resolution observations

**Learn more:**
- [Research Overview](/research/)
- [Protoplanetary Disks](/research/protoplanetary-disks/)
- [Planet Formation](/research/planet-formation/)
- [Software Development](/research/#software-development)


## Dust–Gas Dynamics
In [protoplanetary disks](/research/protoplanetary-disks/), solid particles are aerodynamically coupled to the surrounding gas through drag forces that depend on particle size and local gas density.
The back-reaction of dust on the gas—particularly important when dust-to-gas ratios approach or exceed unity—drives phenomena such as the [streaming instability](#streaming), which plays a central role in concentrating solids and triggering [planetesimal formation](/research/planet-formation/#planetesimal-formation).

- Particle stopping times (Stokes numbers) govern the coupling strength between dust and gas
- Radial drift of pebbles toward pressure maxima can locally enhance dust-to-gas ratios
- Collective drag effects produce runaway clumping at moderate dust-to-gas ratios
- Feedback between multiple particle species (multispecies streaming) broadens the conditions for instability

**Learn more:**
- [Streaming Instability](#streaming)
- [Dust-gas dynamics driven by the streaming instability with various pressure gradients](https://ui.adsabs.harvard.edu/abs/2024MNRAS.529..275B/abstract){:target="_blank"} — Baronett et al. (2024)
- [Bridging Unstratified and Stratified Simulations of the Streaming Instability](https://ui.adsabs.harvard.edu/abs/2025ApJ...993...12L/abstract){:target="_blank"} — Lim et al. (2025)
- [Chao-Chin Yang](/team/yang-chao-chin/) — specialist in MHD and dust-gas dynamics


## Magnetohydrodynamics
Magnetic fields profoundly influence the dynamics of protoplanetary disks.
The [magnetorotational instability](#magnetorotational) (MRI) can sustain turbulence and angular momentum transport in sufficiently ionized regions, while Ohmic resistivity, ambipolar diffusion, and the Hall effect suppress MRI activity near the midplane, shaping the internal structure and accretion behavior of the disk.

- MRI-driven turbulence transports angular momentum outward, allowing disk material to accrete inward
- Non-ideal MHD effects create layered accretion structures with magnetically "dead zones"
- Magnetic field geometry affects the efficiency of magnetically driven disk winds
- Hall effect can introduce large-scale ordered magnetic fields aligned with or against disk rotation

**Learn more:**
- [Magnetorotational Instability](#magnetorotational)
- [Accretion](/research/protoplanetary-disks/#accretion)
- [Magnetically Driven Turbulence in the Inner Regions of Protoplanetary Disks](https://ui.adsabs.harvard.edu/abs/2024ApJ...972..128R/abstract){:target="_blank"} — Rea et al. (2024)
- [Jacob B. Simon](/team/simon-jacob/) — expert in magnetically driven accretion and MHD turbulence


## Radiation Hydrodynamics
The thermodynamic structure of [protoplanetary disks](/research/protoplanetary-disks/) is shaped by the transfer of radiation from the central star through disk gas and dust.
Accurately modeling this coupling—including the effects of dust opacity, disk flaring, and non-equilibrium radiative cooling—is essential for understanding thermally driven disk instabilities and for making realistic comparisons with observations.

- Stellar irradiation heats the disk surface; re-radiation and viscous heating warm the midplane
- Optically thick regions trap radiation and raise midplane temperatures, while optically thin regions cool efficiently
- Cooling timescales determine whether thermal perturbations grow (as in the VSI) or damp
- Radiative transfer models are needed to interpret continuum and line observations of disk structure

**Learn more:**
- [Thermodynamic Structure](/research/protoplanetary-disks/#thermodynamic-structure)
- [Vertical Shear Instability](#vertical-shear)
- [On the Mass Budget Problem of Protoplanetary Disks: Streaming Instability and Optically Thick Emission](https://ui.adsabs.harvard.edu/abs/2026ApJ...997..192G/abstract){:target="_blank"} — Godines et al. (2026)


## Instabilities
Protoplanetary disks are subject to a rich variety of hydrodynamic and magnetohydrodynamic instabilities that generate turbulence, drive structure formation, and influence the concentration and growth of solids.
The subsections below describe the main instabilities studied by our group.


### Magnetorotational
The magnetorotational instability (MRI) is triggered when a weak magnetic field threads a differentially rotating, conducting fluid.
It is one of the most studied and consequential mechanisms for driving turbulence and angular momentum transport in accretion disks, and our group investigates its behavior across the ionization conditions and non-ideal MHD regimes relevant to planet-forming disks.

- Requires a weak poloidal or toroidal magnetic field and a negative angular velocity gradient
- Grows on dynamical timescales (~orbital period) and saturates into MHD turbulence
- Non-ideal effects (Ohmic, ambipolar, Hall) strongly modify or suppress MRI in disk midplanes
- MRI-dead zones may foster large-scale pressure bumps and enhance dust trapping

**Learn more:**
- [Magnetohydrodynamics](#magnetohydrodynamics)
- [Magnetically Driven Turbulence in the Inner Regions of Protoplanetary Disks](https://ui.adsabs.harvard.edu/abs/2024ApJ...972..128R/abstract){:target="_blank"} — Rea et al. (2024)
- [Jacob B. Simon](/team/simon-jacob/) — specialist in MRI simulations


### Rossby Wave
The Rossby wave instability (RWI) develops at sharp radial extrema in the disk's potential vorticity—such as the edges of MRI dead zones or planet-opened gaps—rolling up into large, long-lived anticyclonic vortices.
These vortices efficiently trap dust particles, building up local solid-to-gas ratios that can trigger rapid [planetesimal formation](/research/planet-formation/#planetesimal-formation), and may produce the asymmetric dust features observed by ALMA.

- Triggered by a local extremum in a generalized potential vorticity profile
- Resulting vortices can survive for hundreds to thousands of orbital periods
- Observed as crescents or asymmetric emission in millimeter-wave disk images
- Vortices with self-gravity can form protoplanets on timescales shorter than classical models predict

**Learn more:**
- [Vortices](/research/protoplanetary-disks/#vortices)
- [On the Origin of Dust Structures in Protoplanetary Disks: Constraints from the Rossby Wave Instability](https://ui.adsabs.harvard.edu/abs/2023ApJ...946L...1C/abstract){:target="_blank"} — Chang et al. (2023)
- ["Halfway to Rayleigh" and Other Insights into the Rossby Wave Instability](https://ui.adsabs.harvard.edu/abs/2024ApJ...976..100C/abstract){:target="_blank"} — Chang & Youdin (2024)
- [Rapid Protoplanet Formation in Vortices: Three-dimensional Local Simulations with Self-gravity](https://ui.adsabs.harvard.edu/abs/2024ApJ...970L..19L/abstract){:target="_blank"} — Lyra et al. (2024)


### Streaming
The streaming instability (SI) arises from the mutual aerodynamic drag between inward-drifting solid particles and the sub-Keplerian gas in which they are embedded.
When dust-to-gas ratios exceed a threshold that depends on particle size and disk pressure gradient, the instability grows exponentially, driving solids into dense filaments and clumps that can collapse gravitationally into [planetesimals](/research/planet-formation/#planetesimal-formation).
The SI was first identified by [Youdin](/team/youdin-andrew/) & Goodman ([2005](https://ui.adsabs.harvard.edu/abs/2005ApJ...620..459Y/abstract){:target="_blank"}) and remains a cornerstone of modern planet formation theory.

- Operates on orbital timescales in the disk midplane where solids concentrate
- Clumping conditions depend on particle Stokes number and local metallicity (dust-to-gas ratio)
- Multi-species and stratified extensions broaden and modify SI behavior
- The subject of an ongoing [multi-code comparison project](/research/code-comparisons/)

**Learn more:**
- [Dust–Gas Dynamics](#dustgas-dynamics)
- [Planetesimal Formation](/research/planet-formation/#planetesimal-formation)
- [Code Comparisons: Streaming Instability](/research/code-comparisons/)
- [Dust-gas dynamics driven by the streaming instability with various pressure gradients](https://ui.adsabs.harvard.edu/abs/2024MNRAS.529..275B/abstract){:target="_blank"} — Baronett et al. (2024)
- [Streaming Instability and Turbulence: Conditions for Planetesimal Formation](https://ui.adsabs.harvard.edu/abs/2024ApJ...969..130L/abstract){:target="_blank"} — Lim et al. (2024)
- [A Comparative Study of the Streaming Instability: Unstratified Models](https://ui.adsabs.harvard.edu/abs/2026ApJ..1000..156L/abstract){:target="_blank"} — Baronett et al. (2026)


### Vertical Shear
The vertical shear instability (VSI) is excited in the outer, well-irradiated regions of protoplanetary disks where rapid radiative cooling allows the disk's vertical thermal gradient to drive a growing oscillation.
VSI-driven turbulence is relatively weak but pervasive, stirring the gas and lofting small dust grains; its effects on dust settling, particle concentration, and small-scale disk structure are active areas of investigation.

- Requires thermal relaxation timescales shorter than the orbital period
- Grows in the form of corrugation and breathing modes that break into turbulence
- Produces vertical diffusion of dust with implications for disk opacity and chemistry
- Interaction with the streaming instability and other instabilities is an open research question

**Learn more:**
- [Thermodynamic Structure](/research/protoplanetary-disks/#thermodynamic-structure)
- [Radiation Hydrodynamics](#radiation-hydrodynamics)
- [A High-resolution Simulation of Protoplanetary Disk Turbulence Driven by the Vertical Shear Instability](https://ui.adsabs.harvard.edu/abs/2024ApJ...977..272S/abstract){:target="_blank"} — Shariff & Umurhan (2024)
- [Length and Velocity Scales in Protoplanetary Disk Turbulence](https://ui.adsabs.harvard.edu/abs/2024ApJ...966...90S/abstract){:target="_blank"} — Sengupta et al. (2024)
