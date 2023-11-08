# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:21:16 2023

@author: Leonardo.Hoinaski
"""
# Pacotes
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

# Caminho para meu arquivo netCDF com concentração de ozônio
path = r"C:\Users\Leonardo.Hoinaski\Documents\ENS410064\dados\BRAIN_ClippedCONC_O3_2019_07_02_11_to_2019_12_30_23.nc"

# Abrir arquivo netCDF4
data = nc.Dataset(path)

# Extraindo dados de ozônio
o3 = data['O3'][:]
lat = data['LAT'][:]
lon = data['LON'][:]
tflag = data['TFLAG'][:]

# Figura de um ponto em todos os tempos
fig,ax = plt.subplots()
ax.plot(o3[:,0,50,50])

# Figura de um tempo e todo o espaço
fig2,ax2 = plt.subplots()
ax2.pcolor(lon,lat,np.mean(o3[:,0,:,:],axis=0))
shp = gpd.read_file(r"C:\Users\Leonardo.Hoinaski\Documents\ENS410064\dados\BR_Municipios_2022\BR_Municipios_2022.shp")
shp.boundary.plot(ax=ax2)
