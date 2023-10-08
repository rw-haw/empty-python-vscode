#%%
import skimage as ski
import matplotlib.pyplot as plt
import numpy as np
import imageio.v3 as iio

#%% 
"""ONLY IF RELOAD OF OWN MODULES IS REQUIRED,
I.E. YOU CHANGE CODE AND RERUN ANY CELL
Following example needs to be called after any changes in myModule
"""
# import myModule
# import importlib
# importlib.reload(myModule)
#%% Inline Plotting
image = ski.data.coins()
plt.imshow(image)
#%%
"""
CHANGE INLINE VS. QTAGG Plotting
"""
# SHOW Current Backend
import matplotlib
curr_backend = matplotlib.rcParams["backend"]
print(curr_backend)

# SWITCH Backend
if "inline" in curr_backend:
  %matplotlib qt
else:
  %matplotlib inline

curr_backend = matplotlib.rcParams["backend"]
print(curr_backend)
# USE QT-Backend
if "qtagg" in curr_backend.lower():
  plt.imshow(image)