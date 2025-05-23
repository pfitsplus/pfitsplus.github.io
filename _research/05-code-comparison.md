---
title: "Code Comparison"
permalink: /research/code-comparison/
---
## Streaming Instability

The [streaming instability](/research/fluid-dynamics/#streaming-si) is a promising mechanism within [protoplanetary disks](/research/protoplanetary-disks/) to drive [planetesimal formation](/research/planet-formation/#planetesimal-formation) from mm- to cm-sized pebbles which result from [dust coagulation](/research/planet-formation/#dust-coagulation).
Since its discovery by [Youdin](/team/youdin-andrew/) & Goodman ([2005](https://ui.adsabs.harvard.edu/abs/2005ApJ...620..459Y/abstract){:target="_blank"}), several [hydrodynamics codes](/research/#software-development) have explored the parameters, non-linear properties, and implications of this aerodynamic instability that requires [feedback between dust and gas momenta](/research/fluid-dynamics/#dustgas-dynamics).
However, the non-trivial differences between numerical techniques (e.g., finite difference or finite volume) and dust modeling (e.g., as a pressureless fluid or as Lagrangian particles) can make it difficult to disentangle unique scientific results from the potential idiosyncrasies of a particular code or implementation.
In an effort to address these issues, we are leading a comprehensive comparison of various multipurpose codes across some of the key models and problems previously studied in investigations into the streaming instability.


### [<i class='fa-solid fa-file-pdf'></i>](/assets/docs/research/code-comparison/si/sicc_problem_set.pdf){:target="_blank"} [Problem Set](/assets/docs/research/code-comparison/si/sicc_problem_set.pdf){:target="_blank"}

We invite users and developers of hydrodynamics codes who wish to contribute to this project to review the Streaming Instability Code Comparison Problem Set ([PDF](/assets/docs/research/code-comparison/si/sicc_problem_set.pdf){:target="_blank"}).
As this document continues to be developed, including the addition of new problems in future revisions, please contact [Stanley A. Baronett](/team/baronett-stanley/) with any questions or feedback that may be helpful toward future revisions.


### [<i class='fab fa-fw fa-github'></i>](https://github.com/pfitsplus/sicc){:target="_blank"} [GitHub Repository](https://github.com/pfitsplus/sicc){:target="_blank"}

Figure scripts and source code files related to this project can be found in our [__pfitsplus/sicc__](https://github.com/pfitsplus/sicc){:target="_blank"} GitHub repository.
For more information, please see the repository [README](https://github.com/pfitsplus/sicc/blob/main/README.md){:target="_blank"}.


### [<i class='fab fa-fw fa-google-drive'></i>](https://drive.google.com/drive/folders/14GiJq2lyPePPaCrZzzELsCou5rLTza0v?usp=sharing){:target="_blank"}  [Google Shared Drive](https://drive.google.com/drive/folders/14GiJq2lyPePPaCrZzzELsCou5rLTza0v?usp=sharing){:target="_blank"}

The problem data outputted by contributing codes should be uploaded to our designated [Google Shared Drive](https://drive.google.com/drive/u/1/folders/14GiJq2lyPePPaCrZzzELsCou5rLTza0v){:target="_blank"}.
Anyone with the link can view and comment on the contents, but please contact [Stanley A. Baronett](/team/baronett-stanley/) to request access to add files.
Further details on the structure and contents of submission data can be found in Section 1.1.2 of the [Problem Set](#-problem-set).


### Problem BA
From Baronett et al. (in preparation)


#### Fiducial Grid Resolution

{% include figure image_path='/assets/images/research/code-comparison/si/BA-512_snapshots.png' caption='**Figure 1.1.** Dust density snapshots for Problem BA at a grid resolution of 512².
Each row shows the code labeled along the left margin.
In alphabetical order from top to bottom, the upper group implements an average of one (1) Lagrangian particle per grid cell, and the lower group implements a pressureless dust fluid.
Each column shows the simulation time in local orbital periods $$T$$ labeled along the top margin.
The color scale at the bottom right shows the dust density $$\rho_\mathrm{d}$$ relative to the initially uniform gas density $$\rho_\mathrm{g,0}$$ and applies to all snapshots.
Radial $$x$$ and vertical $$z$$ coordinates are in units of the vertical gas scale height $$H_\mathrm{g}$$.' %}

{% include figure image_path='/assets/images/research/code-comparison/si/BA-512_time_series.png' caption='**Figure 1.2.** Maximum dust densities $$\max(\rho_\mathrm{d})$$ as a function of time for Problem BA at a grid resolution of 512².
The units for density and time are the initially uniform gas density $$\rho_\mathrm{g,0}$$ and the local orbital period $$T$$, respectively.
The top panel uses a similar cadence for each time series.
The bottom panel shows the simple moving average $$\mathrm{SMA}$$ with a sampling window of $$10T$$.
Dotted lines show codes that implement an average of $$n_\mathrm{p} = 1$$ Lagrangian particle per grid cell, solid lines show codes with pressureless dust fluids, and line colors show different codes.' %}

{% include figure image_path='/assets/images/research/code-comparison/si/BA-512_CDF.png' caption='**Figure 1.3.** Cumulative distribution functions of the dust density for Problem BA at a grid resolution of 512².
In the upper panel, lines show densities time-averaged over the saturation state $$\overline{\rho_\mathrm{d}}$$, line colors different codes, and shaded areas the $$1\sigma$$ time variability.
In the lower panel, lines and shaded areas show the meta-average $$\overline{\overline{\rho_\mathrm{d}}}$$ and standard deviation, respectively, of $$\overline{\rho_\mathrm{d}}$$ in the upper panel for each dust implementation.
Dust densities are relative to the initially uniform gas density $$\rho_\mathrm{g,0}$$.
Dotted lines show codes that implement an average of $$n_\mathrm{p} = 1$$ Lagrangian particle per grid cell and solid lines codes with pressureless dust fluids.' %}


##### Additional Particles

{% include figure image_path='/assets/images/research/code-comparison/si/BA-512-np9_snapshots.png' caption='**Figure 1.4.** Similar to Figure [1.1](#higher-particle-resolution:~:text=Permalink-,Figure%201.1.,-Dust%20density%20snapshots) except for only codes that implement an average of $$n_\mathrm{p} = 9$$ Lagrangian particles per grid cell.' %}

{% include figure image_path='/assets/images/research/code-comparison/si/BA-512-np9_time_series.png' caption='**Figure 1.5.** Similar to Figure [1.2](#higher-particle-resolution:~:text=.-,Figure%201.2.,-Maximum%20dust%20densities) except comparing only Lagrangian-particle implementations with dashed lines showing an average of $$n_\mathrm{p} = 9$$ particles per grid cell.' %}

{% include figure image_path='/assets/images/research/code-comparison/si/BA-512-np9_CDF.png' caption='**Figure 1.6.** Similar to Figure [1.3](#higher-particle-resolution:~:text=show%20different%20codes.-,Figure%201.3.,-Cumulative%20distribution%20functions) except comparing only Lagrangian-particle implementations with dashed lines showing an average of $$n_\mathrm{p} = 9$$ particles per grid cell.' %}


#### Higher Grid Resolution

{% include figure image_path='/assets/images/research/code-comparison/si/BA-1024_snapshots.png' caption='**Figure 1.7.** Similar to Figure [1.1](#higher-particle-resolution:~:text=Permalink-,Figure%201.1.,-Dust%20density%20snapshots) except at a grid resolution of 1024².' %}

{% include figure image_path='/assets/images/research/code-comparison/si/BA-1024_time_series.png' caption='**Figure 1.8.** Similar to Figure [1.2](#higher-particle-resolution:~:text=.-,Figure%201.2.,-Maximum%20dust%20densities) except with dashed lines showing grid resolutions of 1024².' %}

{% include figure image_path='/assets/images/research/code-comparison/si/BA-1024_CDF.png' caption='**Figure 1.9.** Similar to Figure [1.3](#higher-particle-resolution:~:text=show%20different%20codes.-,Figure%201.3.,-Cumulative%20distribution%20functions), except grid resolutions at 1024² appear as dashed and darker lines in the upper and lower panels, respectively.' %}


### Problem AB

{% include figure image_path='/assets/images/research/code-comparison/si/AB-1024_snapshots.png' caption='**Figure 2.1.** Similar to Figure [1.1](#higher-particle-resolution:~:text=Permalink-,Figure%201.1.,-Dust%20density%20snapshots) except for Problem AB at a grid resolution of 1024².' %}

{% include figure image_path='/assets/images/research/code-comparison/si/AB-1024_time_series.png' caption='**Figure 2.2.** Similar to Figure [1.2](#higher-particle-resolution:~:text=.-,Figure%201.2.,-Maximum%20dust%20densities) except for Problem AB at a grid resolutions of 1024².' %}

{% include figure image_path='/assets/images/research/code-comparison/si/AB-1024_CDF.png' caption='**Figure 2.3.** Similar to Figure [1.3](#higher-particle-resolution:~:text=show%20different%20codes.-,Figure%201.3.,-Cumulative%20distribution%20functions), except for Problem AB at a grid resolutions of 1024².' %}
