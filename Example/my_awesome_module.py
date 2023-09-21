import numpy as np
import matplotlib.pyplot as plt

def generate_data(N=1, centre=[0., 0.], std=1.):
    '''
    Generate N points randomly sampled from a 2D normal distribution,
    centred at centre and with standard deviation std.
    Returns a Nx2 array.
    '''
    # Initialise the generator
    rng = np.random.default_rng()

    # Generate the N points
    data = rng.normal(loc=centre, scale=std, size=[N, 2])

    return data


def show_data(data):
    '''
    Display data in a scatter plot.
    '''
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Create the scatter plot
    ax.plot(data[:, 0], data[:, 1], 'ro', markersize=5, alpha=0.5)

    # Label the plot and axes
    ax.set(title='My beautiful data',
            xlabel='x coordinate',
            ylabel='y coordinate',
            xlim=[data[:, 0].min(), data[:, 0].max()],
            ylim=[data[:, 1].min(), data[:, 1].max()])

    ax.grid()

    # Show the resulting plot
    plt.show()
