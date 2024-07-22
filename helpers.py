import numpy as np
import matplotlib.pyplot as plt

def uniformly_sample_array(array, n_samples):
    """
    Uniformly sample n_samples from array. Useful for previewing animations.

    Example:
        x = np.linspace(0, 100, 1000)
        n_samples = 10
        sampled_x = uniform_sample_array(x, n_samples)
        print(len(sampled_x))
        print(sampled_x)

    Output:
        10
        [  0.          11.11111111  22.22222222  33.33333333  44.44444444
          55.55555556  66.66666667  77.77777778  88.88888889 100.        ]
    """
    # Generate y evenly spaced indices over the range of the array length
    indices = np.linspace(0, len(array) - 1, n_samples, dtype=int)

    # Use the indices to sample from x
    sampled_x = array[indices]

    return sampled_x

def bump_function(inner_bound, outer_bound):
    """
    The smooth bump function centered at 0 and have f([-a, a])=1, f(R - [-b, b])=0, from Tu's book and https://math.stackexchange.com/a/2064866/429591

    Here, a is inner_bound and b is outer_bound
    """

    f = lambda x: np.where(x <= 0, 0, np.exp(-1/x))
    g = lambda x: f(x) / (f(x) + f(1 - x))
    h = lambda x: g((x-inner_bound**2) / (outer_bound**2 - inner_bound**2))
    k = lambda x: h(x ** 2)
    # rho = lambda x: 1 - k(x)
    def rho(x):
        try:
            return 1 - k(x)
        except ZeroDivisionError:
            return 1 - k(x + 1e-6)
    return rho

def one_d_smoothing_function(left, right, rounding_side_lengths=0.5):
    return lambda x: bump_function((right - left) / 2 - rounding_side_lengths,  (right - left) / 2 )(x - (left + right) / 2)

if __name__ == "__main__":
    # Testing uniformly_sample_array
    x = np.linspace(0, 100, 1000)
    n_samples = 10
    sampled_x = uniformly_sample_array(x, n_samples)
    print(len(sampled_x))
    print(sampled_x)

    # Testing bump_function
    plt.xlim(-5, 5)
    plt.plot(np.linspace(-5, 2, 500), one_d_smoothing_function(-4, -1, 1)(np.linspace(-5, 5, 500)))