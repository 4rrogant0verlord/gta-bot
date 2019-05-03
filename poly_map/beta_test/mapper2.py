import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch

BLUE = '#6699cc'

def plot_coords(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, 'o', color='#999999', zorder=1)

img=mpimg.imread('../../gtasa-blank-vector.png')
fig,ax = plt.subplots(1)
ganton = [(1438, 1186), (1438, 1239), (1337, 1239), (1337, 1186), (1438, 1186)]
imgplot = plt.imshow(img)
ganton = Polygon(ganton)
plot_coords(ax, ganton.exterior)
patch = PolygonPatch(ganton, facecolor=BLUE, edgecolor='none', alpha=0.7, zorder=2,)
ax.add_patch(patch)
ax.set_aspect(1)
plt.show()