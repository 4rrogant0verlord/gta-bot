import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch
COLOR = {
    True:  '#6699cc',
    False: '#ff3333'
    }
def v_color(ob):
    return COLOR[ob.is_valid]
def plot_coords(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, 'o', color='#999999', zorder=1)
fig = plt.figure(1, figsize=(20,10), dpi=90)
ax = fig.add_subplot(121)
ext = [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)]
int = [(1, 0), (0.5, 0.5), (1, 1), (1.5, 0.5), (1, 0)][::-1]
polygon = Polygon(ext)#, [int])
# plot_coords(ax, polygon.interiors[0])
plot_coords(ax, polygon.exterior)
patch = PolygonPatch(polygon, facecolor=v_color(polygon), edgecolor=v_color(polygon), alpha=0.5, zorder=2)
ax.add_patch(patch)
ax.set_aspect(1)
import matplotlib.pyplot as plt
plt.show()

