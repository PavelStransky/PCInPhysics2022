import random
import numpy as np

def random_direction_2d():
    """ Generates a random direction in the 2D plane """
    phi = random.uniform(0, 2 * np.pi)
    return np.array([np.cos(phi), np.sin(phi)])

def random_direction_gaussian(dimension):
    """ Generates random direction in the dimension-dimensional space 

        References:
        [1] M.E. Muller, A note on a method for generating points uniformly on n-dimensional spheres,
                Communications of the Asociation for Computing Machinery 2, 19 (1959)
        [2] G. Marsaglia, Choosing a Point from the Surface of a Sphere,
                The Annals of Mathematical Statistics 43, 645 (1972)
    """
    random_vector_gaussian = np.random.normal(size=dimension)
    return random_vector_gaussian / np.linalg.norm(random_vector_gaussian)
    
def minimize(function, step_size=0.01, initial_condition=(0, 0), max_failed_steps=100):
    """ Simple minimization method using random walk.

    Arguments:
    function -- function to minimize
    max_failed_steps -- number of steps to stop the calculation
    """

    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    failed_steps = 0                    # Number of consecutive steps in which we haven't moved (criterion to stop the minimization) 
    num_steps = 0                       # Total number of steps

    while failed_steps < max_failed_steps:
        new_position = position + step_size * random_direction_2d()
        newf = function(new_position)

        if newf < f:
            position = new_position
            f = newf

            path.append(position)

            failed_steps = 0

        else:
            failed_steps += 1        # Rejected step

        num_steps += 1

    print(f"Minimum = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)

def minimize_metropolis(function, dimension=2, temperature=1, step_size=0.01, initial_condition=None, max_steps=20000):
    """ Simple minimization method using random walk and Metropolis algorithm.

    Arguments:
    function -- function to minimize
    dimension -- dimensionality of the function
    temperature -- temperature of the Metropolis algorithm
    initial_condition -- the starting point; if None, initial conditions chosen randomly from a box of size given by initial_condition_box
    max_steps -- total number of steps
    """
    if initial_condition is None:       # Random initial condition within box of size given by initialConditionBox
        initial_condition = np.zeros(dimension)
    
    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    num_steps = 0                    # Total number of steps

    while num_steps < max_steps:
        new_position = position + step_size * random_direction_gaussian(dimension)
        newf = function(new_position)
        C = np.exp((f - newf) / temperature)    # Boltzmann coefficient (for step down C > 1)

        if C > np.random.rand():
            position = new_position
            f = newf

            path.append(position)

        num_steps += 1

    print(f"Minimum (Metropolis) = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)