import numpy as np 
import matplotlib.pyplot as plt 
%matplotlib inline
import homcloud.interface as hc
import pandas as pd
 
#input to the height information measured by AFM, 512 X 512 pixel
pict = np.loadtxt("AFM_image.txt")
 
#showing the image measured by AFM
pict.shape
plt.imshow(pict, "gray")

#making persistent diagram 
hc.PDList.from_bitmap_levelset(pict, "sublevel", save_to="Persistent diagram.pdgm")

#input to the numerical information for 0th persistent homology analysis
pd = hc.PDList("Persistent diagram.pdgm").dth_diagram(0)

#showing persistent diagram
pd.histogram(x_range=(0, 120), x_bins=100).plot(colorbar={"type": "log", "max": 100}) 
