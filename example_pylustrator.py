# import matplotlib and numpy as usual
import matplotlib.pyplot as plt
import numpy as np

# now import pylustrator
import pylustrator

# activate pylustrator
pylustrator.start()

# build plots as you normally would
np.random.seed(1)
t = np.arange(0.0, 2, 0.01)
y = 2 * np.sin(np.pi * t)
a, b = np.random.normal(loc=(5., 3.), scale=(2., 4.), size=(100,2)).T
b += a

plt.figure(1)
plt.subplot(131)
plt.plot(t, y)

plt.subplot(132)
plt.plot(a, b, "o")

plt.subplot(133)
plt.bar(0, np.mean(a))
plt.bar(1, np.mean(b))

# show the plot in a pylustrator window
#% start: automatic generated code from pylustrator
plt.figure(1).ax_dict = {ax.get_label(): ax for ax in plt.figure(1).axes}
import matplotlib as mpl
plt.figure(1).axes[0].set_position([0.125000, 0.551916, 0.307579, 0.328084])
plt.figure(1).axes[0].lines[0].set_color("#ff7f0e")
plt.figure(1).axes[0].lines[0].set_markeredgecolor("#ff7f0e")
plt.figure(1).axes[0].lines[0].set_markerfacecolor("#ff7f0e")
plt.figure(1).axes[1].set_position([0.125000, 0.110000, 0.307579, 0.328084])
plt.figure(1).axes[1].lines[0].set_color("#ff7f0e")
plt.figure(1).axes[1].lines[0].set_markeredgecolor("#ff7f0e")
plt.figure(1).axes[1].lines[0].set_markerfacecolor("#ff7f0e")
plt.figure(1).axes[2].set_xlim(-0.49, 1.49)
plt.figure(1).axes[2].set_xticks([0.0, 1.0])
plt.figure(1).axes[2].set_xticklabels(["0.0", "1.0"], fontsize=10.0, fontweight="normal", color="black", fontstyle="normal", fontname="DejaVu Sans", horizontalalignment="center")
plt.figure(1).axes[2].set_position([0.518934, 0.110000, 0.381066, 0.770000])
plt.figure(1).axes[2].patches[0].set_facecolor("#ff7f0e")
plt.figure(1).axes[2].patches[1].set_facecolor("#8e44ad")
#% end: automatic generated code from pylustrator
plt.show()
