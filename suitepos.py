print('hello, World!')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
F = np.load('F.npy', allow_pickle=True)
Fneu = np.load('Fneu.npy', allow_pickle=True)
spks = np.load('spks.npy', allow_pickle=True)
stat = np.load('stat.npy', allow_pickle=True)
ops =  np.load('ops.npy', allow_pickle=True)
ops = ops.item()
iscell = np.load('iscell.npy', allow_pickle=True)

im = np.zeros((ops['Ly'], ops['Lx']))
coor = np.zeros((2, 175), dtype=int)
for n in range(0,175):
   # ypix = stat[n]['med'][1] #[~stat[n]['overlap']]
   # xpix = stat[n]['med'][2] #[~stat[n]['overlap']]
    coor[:,n]= stat[n]['med']
   # coor[n,1] = xpix
   # im[ypix,xpix] = n+1
'''
c = plt.imshow(im)
plt.colorbar(c)
plt.show()
'''
df = pd.DataFrame(coor)
file_path = "my_data.xlsx"
df.to_excel(file_path, index=False)
#print(coor)


