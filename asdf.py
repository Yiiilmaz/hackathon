import rasterio
from rasterio.plot import show

fp = r'./data/apg18e_1_0_0.tif'
img = rasterio.open(fp)
show(img, cmap='Set1')
