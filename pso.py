###############################################################################
# Name:             Bhavik Bhagat
# Email:            x2020coq@stfx.ca
# Student ID:       202002911
# Course:           csci340, assignment_3: Particle Swarm Optimization
###############################################################################


# load the required modules
# using pyswarms library -> https://pyswarms.readthedocs.io/en/latest/

import matplotlib.pyplot as plt
import numpy as np
import pyswarms as ps
import random

from pathlib import Path
from pyswarms.utils.functions import single_obj as sfx
from pyswarms.utils.plotters import (plot_cost_history, plot_contour)
from pyswarms.utils.plotters.formatters import Mesher

MAX_PARTICLES = 20

def global_optima():
    # creating some functions list to be optimized
    # sphere
    functions = (
        sfx.sphere,
        sfx.beale,
        sfx.booth,
        sfx.matyas,
        sfx.levi,
        sfx.eggholder,
        sfx.schaffer2,
        sfx.rastrigin,
        sfx.threehump,
        sfx.rosenbrock
    )

    # global optimization
    for i, f in enumerate(functions, 1):
        # hyper parameter tuning of swarms required a dict with required components
        # w: inertia parameter, c1: cognitive parameter, c2: social parameter
        # n: number of neighbors to consider (should be <n_particles> at max)
        # p: minkowski distance, 1 for Manhattan, 2 for Euclidean distance
        # k: number of neighbors, for local optimization
        # initializing parameters randomly
        parameters = {
            "w": random.randint(5, 9) / 10,
            "c1": random.randint(2, 5) / 10,
            "c2": random.randint(2, 5) / 10
        }

        # instantiate the optimizer by passing necessary arguments
        optimizer = ps.single.GlobalBestPSO(
            n_particles=MAX_PARTICLES // 2, dimensions=2, options=parameters
        )

        # call the optimize function, we are using sphere here as function
        cost, final_pos = optimizer.optimize(f, iters=100, n_processes=8)

        # to store the results of visualization
        result_path = Path("results").resolve()
        plt_name = result_path.joinpath(f'{i}.png')
        gif_name = result_path.joinpath(f'{i}.gif')

        # cost plot
        plot_cost_history(cost_history=optimizer.cost_history)
        plt.title(
            f'Function: {f.__repr__()}\n'
            f'Parameters: {parameters.items()}\n'
            f'Cost: {np.round(cost, 4)}, '
            f'Final Position: {np.round(final_pos, 4)}'
        )

        plt.savefig(plt_name)

        # animation of particles
        # instantiate the mesher with the function to be optimized
        m = Mesher(func=f)

        # make the animation
        animation = plot_contour(
            pos_history=optimizer.pos_history,
            mesher=m,
            mark=(0, 0)
        )

        # save the animation
        animation.save(gif_name, fps=30, writer="imagemagick")

    return None


def local_optima():
    # creating some functions list to be optimized
    # sphere
    functions = (
        sfx.sphere,
        sfx.beale,
        sfx.booth,
        sfx.levi,
        sfx.eggholder,
        sfx.schaffer2,
        sfx.rastrigin,
        sfx.threehump,
        sfx.rosenbrock
    )
    # modifications Local Neighborhood
    # 1. Number of neighbors k, chosen randomly between 3-MAX_PARTICLES/2
    # 2. Velocity Clamp: randomly between min 0-0.1, max 0.1-0.5
    # local optimization
    for i, f in enumerate(functions, 11):
        # hyper parameter tuning of swarms required a dict with required components
        # w: inertia parameter, c1: cognitive parameter, c2: social parameter
        # n: number of neighbors to consider (should be <n_particles> at max)
        # p: minkowski distance, 1 for Manhattan, 2 for Euclidean distance
        # k: number of neighbors, for local optimization
        # initializing parameters randomly
        parameters = {
            "w": random.randint(5, 9) / 10,
            "c1": random.randint(2, 5) / 10,
            "c2": random.randint(2, 5) / 10,
            "k": random.randint(3, MAX_PARTICLES // 2),
            "p": 2
        }

        # for velocity clamping
        velocity = (random.randint(0, 1) / 10), (random.randint(1, 5) / 10)

        # instantiate the optimizer by passing necessary arguments
        optimizer = ps.single.LocalBestPSO(
            n_particles=MAX_PARTICLES,
            dimensions=2,
            options=parameters,
            velocity_clamp=velocity
        )

        # call the optimize function, we are using sphere here as function
        cost, final_pos = optimizer.optimize(f, iters=100, n_processes=8)

        # to store the results of visualization
        result_path = Path("results").resolve()
        plt_name = result_path.joinpath(f'{i}.png')
        gif_name = result_path.joinpath(f'{i}.gif')

        # cost plot
        plot_cost_history(cost_history=optimizer.cost_history)
        plt.title(
            f'Function: {f.__repr__()}\n'
            f'Parameters: {parameters.items()}\n'
            f'Cost: {np.round(cost, 4)}, '
            f'Final Position: {np.round(final_pos, 4)}'
        )

        plt.savefig(plt_name)

        # animation of particles
        # instantiate the mesher with the function to be optimized
        m = Mesher(func=f)

        # make the animation
        animation = plot_contour(
            pos_history=optimizer.pos_history,
            mesher=m,
            mark=(0, 0)
        )

        # save the animation
        animation.save(gif_name, fps=30)

    return None


if __name__ == "__main__":
    global_optima()
    local_optima()
