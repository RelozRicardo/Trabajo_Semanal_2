#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:31:02 2024

@author: ricardo
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

w0 = 1
qq1 = 0.54

qq2 = 1.31

K = 1000/330


my_tf = TransferFunction( [-K*K*w0*w0], [1 , 1/qq1 + 1/qq2 , 2 + 1/(qq1*qq2) , 1/qq1 + 1/qq2 , 1] )


plt.close('all')

bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq1) )

pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq1)) #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq1))