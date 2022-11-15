#!/usr/bin/env python
# coding: utf-8

# # Mitigation Model
# 
# # Section 1: Model Presentation
# 
# ## Section 1.1: State variables and law of motion
# 
# ### Section 1.1.1: Total capital:
# $$
# d \log K = (\mu_k + i - \frac{\kappa}{2} i^2 - \frac{\sigma_k^2}{2}) dt + \sigma_k dW
# $$
# 
# ### Section 1.1.2: Temperature anomaly:
# $$
# d Y = e(\theta_\ell dt + \varsigma dW)
# $$
# 
# ### Section 1.1.3: Technology Jump Intensity: 
# $$
# d\log \mathcal{I}_g = - \zeta dt + \Psi_0 (\frac{X}{\mathcal{I}})^{\Psi_1} dt - \frac{\sigma_g^2}{2} dt + \sigma_g dW 
# $$
# 
# ### Section 1.1.4: Damage
# 
# $$
# \bar{Y}_t= \begin{cases}Y_t, & t \leq \tau \\ Y_t-Y_\tau+\bar{y}, & t>\tau\end{cases}
# $$
# 
# ### Section 1.1.5: Damage Function
# 
# $$
# \log N_t=\Gamma\left(\bar{Y}_t\right)+\iota_n \cdot Z_t
# $$
# 
# where 
# 
# $$
# \Gamma(y)=\gamma_1 y+\frac{\gamma_2}{2} y^2+\frac{\gamma_3^{(m)}}{2} \mathbb{I}_{y \geq \bar{y}}(y-\bar{y})^2, \quad m=1,2, \ldots, 20
# $$
# 
# ### Section 1.1.6: Damage Jump Intensity
# 
# $$
# \mathcal{I}_d= \begin{cases}r_1\left(\exp \left(\frac{r_2}{2}(Y-\underline{y})^2\right)-1\right), & Y \geq \underline{y} \\ 0, & Y<\underline{y}\end{cases}
# $$
# 

# # Section 1.2: Damage jump and technology jump

# In[1]:


from IPython.display import Image
Image(filename='./figure/JumpStates.png')


# ## Section 1.2.1 Post-Damage Jump, Post-Technology Jump $V^{(m, I I)}$
# 
# $$
# V^{(m, I I)}(\log K, Y, \log N)=\phi^{(m, I I)}(\log K, Y)-\log N
# $$
# 
# $$
# 0=\max _{i_k} -\phi^{(m, I I)}+\delta \log \left(\alpha-i_k\right)+\delta \log K \\
# +\frac{\partial \phi^{(m, I I)}}{\partial \log K}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}\right]+\frac{\partial^2 \phi^{(m, I I)}}{\partial \log K^2} \frac{\left|\sigma_k\right|^2}{2}
# $$
# 
# ## Section 1.2.2 Pre-Damage Jump, Post-Technology Jump $V^{I I}$
# 
# 
# $$
# V^{(I I)}(\log K, Y, \log N)=\Phi^{(I I)}(\log K, Y)-\log N
# $$
# 
# $$
# 0=\max _{i_k} -\Phi^{(I I)}+\delta \log \left(\alpha-i_k\right)+\delta \log K \\
# +\frac{\partial \Phi^{(I I)}}{\partial \log K}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}\right]+\frac{\partial^2 \Phi^{(I I)}}{\partial \log K^2} \frac{\left|\sigma_k\right|^2}{2}
# $$
# 
# 
# ## Section 1.2.3 Post-Damage Jump, Pre-Technology Jump $V^{m}$
# 
# $$
# V^{(m)}\left(\log K, Y, \log \mathcal{I}_g, \log N\right)=\phi^{(m)}\left(\log K, Y,\log  \mathcal{I}_g\right)-\log N
# $$
# 
# $$
# 0=\max _{e, i_k, i_g} \min _{\omega_{\ell}: \sum_{\ell=1}^L \omega_{\ell}=1, g} -\delta \phi^{(m)}+\delta \log \left(\alpha-i_k-i_g \exp \left(-\log K+\log \mathcal{I}_g\right)-\alpha \bar{\vartheta}\left[1-\left(\frac{e}{\alpha \bar{\lambda} K}\right)\right]^\theta\right)+\delta \log K \\
# +\frac{\partial \phi^{(m)}}{\partial \log K}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}\right]+\frac{\partial^2 \phi^{(m)}}{\partial \log K^2} \frac{\left|\sigma_k\right|^2}{2} \\
# +\frac{\partial \phi^{(m)}}{\partial Y} \sum_{\ell=1}^L \omega_{\ell} \theta_{\ell} e+\frac{\partial^2 \phi^{(m)}}{\partial Y^2} \frac{|\varsigma|^2}{2} e^2 \\
# +\frac{\partial \phi^{(m)}}{\partial \log \mathcal{I}_g}\left(-\zeta+\Psi_0\left(x \frac{K}{\mathcal{I}_g}\right)^{\Psi_1}-\frac{\sigma_g^2}{2}\right)+\frac{\sigma_g^2}{2} \frac{\partial^2 \phi^{(m)}}{\partial \log \mathcal{I}_g^2}\\
# -\left(\left[\gamma_1+\gamma_2 y+\gamma_3^m\right] \sum_{\ell=1}^L \omega_{\ell} \theta_{\ell} e+\left[\gamma_2+\gamma_3^m\right] \frac{|\zeta|^2}{2} e^2\right) \\
# +\xi_a \sum_{\ell=1}^L \omega_{\ell}\left(\log \omega_{\ell}-\log \pi_{\ell}\right) \\
# +\xi_g \mathcal{I}_g(1-g+g \log g)+\mathcal{I}_g g\left(\Phi^{(I I)}-\Phi\right)
# $$
# 
# 
# 
# ## Section 1.2.4 Pre-Damage Jump, Pre-Technology Jump $V$
# $$
# V\left(\log K, Y, \log \mathcal{I}_g, \log N\right)=\Phi\left(\log K, Y,\log  \mathcal{I}_g\right)-\log N
# $$
# 
# $$
# 0=\max _{e, i_k, i_g \omega_{\ell}: \sum_{\ell=1}^L \omega_{\ell}=1, g, f_m} -\delta \Phi+\delta \log \left(\alpha-i_k-i_g \exp \left(-\log K+\log \mathcal{I}_g\right)-\alpha \bar{\vartheta}\left[1-\left(\frac{e}{\alpha \bar{\lambda} K}\right)\right]^\theta\right)+\delta \log K \\
# +\frac{\partial \Phi}{\partial \log K}\left[\mu_k+i_k-\frac{\kappa}{2} i_k^2-\frac{\left|\sigma_k\right|^2}{2}\right]+\frac{\partial^2 \Phi}{\partial \log K^2} \frac{\left|\sigma_k\right|^2}{2} \\
# +\frac{\partial \Phi}{\partial Y} \sum_{\ell=1}^L \omega_{\ell} \theta_{\ell} e+\frac{\partial^2 \Phi}{\partial Y^2} \frac{|\zeta|^2}{2} e^2 \\
# +\frac{\partial \Phi}{\partial \log \mathcal{I}_g}\left(-\zeta+\psi_0\left(i_g\right)^{\psi_1}-\frac{\left|\sigma_{g}\right|^2}{2}\right)+\frac{\left|\sigma_{g}\right|^2}{2}\frac{\partial^2 \Phi}{\partial \log \mathcal{I}_g^2} \\
# -\left(\left[\gamma_1+\gamma_2 Y\right] \sum_{\ell=1}^L \omega_{\ell} \theta_{\ell} e+\gamma_2 \frac{|\zeta|^2}{2} e^2\right) \\
# +\xi_a \sum_{\ell=1}^L \omega_{\ell}\left(\log \omega_{\ell}-\log \pi_{\ell}\right) \\
# +\xi_g \mathcal{I}_g(1-g+g \log g)+\mathcal{I}_g g\left(\Phi^{(I I)}-\Phi\right) \\
# +\xi_d \mathcal{I}_d\left(1-f_m+f_m \log f_m\right)+\mathcal{I}_d \sum_{m=1}^M \pi_d^m f_m\left(\phi^{(m, I I)}-\Phi\right) .
# $$

# # Section 2: Execution Time Table
# 
# ## Section 2.1: Post-Damage Part 
# 
# 
# | Grid Step Size | Learning Rate| $\psi_0$ | $\psi_1$ | Time (Algorithem-Improved)|Time (Interpolation-Accelerated + Algorithem-Improved)|
# |---|---|---|---|---|---|
# |0.2, 0.2, 0.2 | 0.1   |0.005   |0.5    |0 days 00 hr 03 min 10 sec-0 days 00 hr 05 min 12 sec|NA|
# |0.2, 0.2, 0.2 | 0.1   |0.008   |0.5    |0 days 00 hr 03 min 01 sec-0 days 00 hr 05 min 01 sec|NA|
# |0.2, 0.2, 0.2 | 0.1   |0.010   |0.5    |0 days 00 hr 02 min 50 sec-0 days 00 hr 04 min 53 sec|NA|
# |0.2, 0.2, 0.2 | 0.1   |0.012   |0.5    |0 days 00 hr 02 min 45 sec-0 days 00 hr 04 min 47 sec|NA|
# |0.2, 0.2, 0.2 | 0.008 |0.005   |0.8    |0 days 00 hr 26 min 43 sec-0 days 00 hr 33 min 16 sec|NA|
# |0.2, 0.2, 0.2 | 0.008 |0.008   |0.8    |0 days 00 hr 28 min 07 sec-0 days 00 hr 32 min 15 sec|NA|
# |0.2, 0.2, 0.2 | 0.008 |0.010   |0.8    |0 days 00 hr 25 min 59 sec-0 days 00 hr 32 min 03 sec|NA|
# |0.2, 0.2, 0.2 | 0.008 |0.012   |0.8    |0 days 00 hr 25 min 36 sec-0 days 00 hr 31 min 27 sec|NA|
# |0.05, 0.05, 0.05 | 0.008   |0.005   |0.5    |1 days 12 hr 28 min 32 sec-3 days 03 hr 15 min 04 sec|1 days 11 hr 30 min 15 sec-2 days 14 hr 21 min 56 sec|
# |0.05, 0.05, 0.05 | 0.008   |0.008   |0.5    |1 days 09 hr 26 min 15 sec-2 days 08 hr 27 min 09 sec|1 days 06 hr 03 min 53 sec-2 days 13 hr 29 min 52 sec|
# |0.05, 0.05, 0.05 | 0.008   |0.010   |0.5    |1 days 11 hr 19 min 32 sec-2 days 07 hr 39 min 55 sec|1 days 03 hr 49 min 05 sec-2 days 05 hr 33 min 19 sec|
# |0.05, 0.05, 0.05 | 0.008   |0.012   |0.5    |1 days 06 hr 29 min 59 sec-2 days 05 hr 06 min 25 sec|1 days 03 hr 17 min 19 sec-2 days 04 hr 49 min 46 sec|
# |0.05, 0.05, 0.05 | 0.005 |0.005   |0.8    |2 days 08 hr 45 min 19 sec-4 days 18 hr 51 min 47 sec|2 days 01 hr 28 min 05 sec-3 days 18 hr 32 min 26 sec|
# |0.05, 0.05, 0.05 | 0.005 |0.008   |0.8    |2 days 04 hr 02 min 00 sec-4 days 17 hr 03 min 18 sec|2 days 00 hr 52 min 21 sec-3 days 16 hr 50 min 42 sec|
# |0.05, 0.05, 0.05 | 0.005 |0.010   |0.8    |2 days 01 hr 26 min 29 sec-4 days 16 hr 13 min 56 sec|1 days 20 hr 25 min 51 sec-3 days 04 hr 35 min 42 sec|
# |0.05, 0.05, 0.05 | 0.005 |0.012   |0.8    |2 days 06 hr 41 min 55 sec-3 days 16 hr 21 min 05 sec|2 days 01 hr 52 min 42 sec-3 days 15 hr 22 min 34 sec|
# |0.05, 0.05, 0.05 | 0.008 |0.005   |0.8    |1 days 13 hr 24 min 54 sec-NonConvergent |1 days 08 hr 48 min 37 sec-1 days 21 hr 50 min 03 sec|
# |0.05, 0.05, 0.05 | 0.008 |0.008   |0.8    |NonConvergent |1 days 07 hr 08 min 21 sec-1 days 20 hr 07 min 57 sec|
# |0.05, 0.05, 0.05 | 0.008 |0.010   |0.8    |NonConvergent |1 days 05 hr 44 min 14 sec-1 days 20 hr 07 min 17 sec|
# |0.05, 0.05, 0.05 | 0.008 |0.012   |0.8    |NonConvergent |1 days 05 hr 35 min 10 sec-1 days 18 hr 42 min 39 sec|
# 
# ## Section 2.2: Pre-Damage Part 
# 
# | Grid Step Size | Learning Rate| $\psi_0$ | $\psi_1$ | Time (Algorithem-Improved)|Time (Interpolation-Accelerated + Algorithem-Improved)|
# |----|---|---|---|---|---|
# |0.2, 0.2, 0.2 | 0.005   |0.005   |0.5    |0 days 00 hr 40 min 56 sec|NA|
# |0.2, 0.2, 0.2 | 0.005   |0.008   |0.5    |0 days 00 hr 41 min 15 sec|NA|
# |0.2, 0.2, 0.2 | 0.005   |0.010   |0.5    |0 days 00 hr 41 min 58 sec|NA|
# |0.2, 0.2, 0.2 | 0.005   |0.012   |0.5    |0 days 00 hr 58 min 32 sec|NA|
# |0.2, 0.2, 0.2 | 0.005 |0.005   |0.8    |0 days 01 hr 02 min 12 sec|NA|
# |0.2, 0.2, 0.2 | 0.005 |0.008   |0.8    |0 days 01 hr 04 min 20 sec|NA|
# |0.2, 0.2, 0.2 | 0.005 |0.010   |0.8    |0 days 00 hr 57 min 11 sec|NA|
# |0.2, 0.2, 0.2 | 0.005 |0.012   |0.8    |0 days 00 hr 56 min 30 sec|NA|
# |0.05, 0.05, 0.05 | 0.005 |0.005   |0.5    |1 days 14 hr 23 min 38 sec||
# |0.05, 0.05, 0.05 | 0.005 |0.008   |0.5    |1 days 11 hr 37 min 35 sec||
# |0.05, 0.05, 0.05 | 0.005 |0.010   |0.5    |1 days 13 hr 07 min 00 sec||
# |0.05, 0.05, 0.05 | 0.005 |0.012   |0.5    |1 days 13 hr 43 min 41 sec||
# |0.05, 0.05, 0.05 | 0.005 |0.005   |0.8    |1 days 19 hr 52 min 10 sec||
# |0.05, 0.05, 0.05 | 0.005 |0.008   |0.8    |1 days 14 hr 17 min 51 sec ||
# |0.05, 0.05, 0.05 | 0.005 |0.010   |0.8    |1 days 16 hr 26 min 54 sec ||
# |0.05, 0.05, 0.05 | 0.005 |0.012   |0.8    |1 days 15 hr 30 min 41 sec ||
# 
# 

# # Section 3: Graphical Comparison
# 
# ## Section 3.1: Different $\psi_0$ and $\psi_1$

# In[2]:


from PIL import Image
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
import numpy as np
from IPython.display import display, HTML

get_ipython().run_line_magic('matplotlib', 'inline')

@interact
def image(psi0=[0.005, 0.008, 0.010, 0.012], psi1=[0.5, 0.8], graphtype=['RD', 'Capital Investment', 'Emission', 'Temperature Anomaly', 'Technology jump intensity', 'Distorted probability of first technology jump', 'Distorted probability of damage changes', 'True probability of first technology jump', 'True probability of damage changes'], Gridsize = ['0.2_0.2_0.2','0.05_0.05_0.05']):
    Figure_Dir = './figure/2jump_step_'+Gridsize+'/'

    if graphtype == 'RD':
        filename = Figure_Dir+"RD,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'Capital Investment':
        filename = Figure_Dir+"CapI,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'Emission':
        filename = Figure_Dir+"E,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'Temperature Anomaly':
        filename = Figure_Dir+"TA,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'Technology jump intensity':
        filename = Figure_Dir+"Ig,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'Distorted probability of first technology jump':
        filename = Figure_Dir+"PIgd,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'Distorted probability of damage changes':
        filename = Figure_Dir+"PIdd,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'True probability of first technology jump':
        filename = Figure_Dir+"TPIg,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'
    if graphtype == 'True probability of damage changes':
        filename = Figure_Dir+"TPId,"+"psi0={:.3f},psi1={:.3f}" .format(
            psi0, psi1)+'.png'

    userimage = Image.open(filename)
    return userimage


# In[3]:


from PIL import Image
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
import numpy as np
from IPython.display import display, HTML

get_ipython().run_line_magic('matplotlib', 'inline')


@interact
def image(xi_a=[1000., 0.0002, 0.0002], xi_g=[1000., 0.05, 0.025], psi0=[0.005], psi1=[0.5], graphtype=['RD', 'Capital Investment', 'Emission', 'Temperature Anomaly', 'Technology jump intensity', 'Distorted probability of first technology jump', 'Distorted probability of damage changes', 'True probability of first technology jump', 'True probability of damage changes', 'Distored Probability of Damage Models', 'Distorted Probability of Climate Models'], Gridsize=['0.1_0.1_0.1', '0.05_0.05_0.05'],BC=['Whole','Only Before Hitting 1.5 Celusis Degree']):
    Figure_Dir = './figure/2jump_step_0.1_0.1_0.1_LR_0.005_xiagComparisonSlide/'

    if BC=='Whole':
        Common=''
    elif BC == 'Only Before Hitting 1.5 Celusis Degree':
        Common = ',BC'
    if graphtype == 'RD':
        filename = Figure_Dir+"RD,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Capital Investment':
        filename = Figure_Dir+"CapI,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Emission':
        filename = Figure_Dir+"E,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Temperature Anomaly':
        filename = Figure_Dir+"TA,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Technology jump intensity':
        filename = Figure_Dir+"Ig,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Distorted probability of first technology jump':
        filename = Figure_Dir+"PIgd,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Distorted probability of damage changes':
        filename = Figure_Dir+"PIdd,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'True probability of first technology jump':
        filename = Figure_Dir+"TPIg,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'True probability of damage changes':
        filename = Figure_Dir+"TPId,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Distored Probability of Damage Models':
        filename = Figure_Dir+"Gamma3,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    if graphtype == 'Distorted Probability of Climate Models':
        filename = Figure_Dir+"ClimateSensitivity,"+"xia={:.4f},xig={:.3f},psi0={:.3f},psi1={:.3f}".format(
            xi_a, xi_g, psi0, psi1)+Common+'.png'
    # print(filename)
    userimage = Image.open(filename)
    return userimage


# In[4]:


from PIL import Image
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
import numpy as np
from IPython.display import display, HTML

get_ipython().run_line_magic('matplotlib', 'inline')


@interact
def image(xi_a=[[1000., 0.0002, 0.0002]], xi_g=[[1000., 0.05, 0.025]], psi0=[[0.005]], psi1=[[0.5]], graphtype=['RD', 'Capital Investment', 'Emission', 'Temperature Anomaly', 'Technology jump intensity', 'Distorted probability of first technology jump', 'Distorted probability of damage changes', 'True probability of first technology jump', 'True probability of damage changes', 'Distored Probability of Damage Models', 'Distorted Probability of Climate Models'], Gridsize=['0.1_0.1_0.1', '0.05_0.05_0.05'], BC=['Whole', 'Only Before Hitting 1.5 Celusis Degree']):
    Figure_Dir = './figure/2jump_step_0.1_0.1_0.1_LR_0.005_xiagComparisonSlide/'

    if BC == 'Whole':
        Common = ''
    elif BC == 'Only Before Hitting 1.5 Celusis Degree':
        Common = ',BC'
    if graphtype == 'RD':
        filename = Figure_Dir +             "RD,xia={},xig={},psi0={},psi1={}" .format(
                xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'Capital Investment':
        filename = Figure_Dir+"CapI,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'Emission':
        filename = Figure_Dir+"E,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'Temperature Anomaly':
        filename = Figure_Dir+"TA,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'Technology jump intensity':
        filename = Figure_Dir+"Ig,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'Distorted probability of first technology jump':
        filename = Figure_Dir+"PIgd,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'Distorted probability of damage changes':
        filename = Figure_Dir+"PIdd,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'True probability of first technology jump':
        filename = Figure_Dir+"TPIg,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    if graphtype == 'True probability of damage changes':
        filename = Figure_Dir+"TPId,xia={},xig={},psi0={},psi1={}" .format(
            xi_a, xi_g, psi0, psi1) + Common+'.png'
    print(filename)
    userimage = Image.open(filename)
    return userimage


# In[ ]:




