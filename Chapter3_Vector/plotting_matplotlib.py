import matplotlib.pyplot as plt

def plot(L, scale=4):
    plt.xlim([-scale, scale])
    plt.ylim([-scale, scale])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0)
    plt.axvline(0)
    for pt in L:
        plt.scatter(pt[0], pt[1], color='red')
    
    plt.show()


def plot_vec(v, tail=[0,0], scale=4, show=True):
    plt.xlim([-scale, scale])
    plt.ylim([-scale, scale])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0)
    plt.axvline(0)
    plt.arrow(tail[0], tail[1], v[0], v[1], head_width=0.3, head_length=0.2, fc='k', ec='k')
    if show:
        plt.show()

