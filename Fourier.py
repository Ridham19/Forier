import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import window


def f(x):
    return x*x  # function: x^2
    # example for other funtions👇🏼
    # return x
    # return np.sin(x)

#  Fourier series coefficients
def a0(T):
    return (2 / T) * quad(lambda x: f(x), 0, T)[0]

def an(n, T):
    return (2 / T) * quad(lambda x: f(x) * np.cos(2 * np.pi * n * x / T), 0, T)[0]

def bn(n, T):
    return (2 / T) * quad(lambda x: f(x) * np.sin(2 * np.pi * n * x / T), 0, T)[0]

#  Fourier series approximation
def fourier_series(x, n_terms, T):
    a0_val = a0(T) / 2
    result = a0_val
    for n in range(1, n_terms + 1):
        result += an(n, T) * np.cos(2 * np.pi * n * x / T) + bn(n, T) * np.sin(2 * np.pi * n * x / T)
    return result


# Parameters
T = 10  # Period of the function; don't make it too big
n_terms = 50  # Number of terms in the Fourier series; Don't keep it > 50

# Create an array of x values
x = np.linspace(0, T, 1000)

# Compute the Fourier series approximation
y = fourier_series(x, n_terms, T)

# Plot the original function and its Fourier series approximation
plt.plot(x, f(x), label='Original Function')
plt.plot(x, y, label='Fourier Series Approximation')
plt.title('Fourier Series Representation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.savefig("output.jpeg")
plt.show()


window.main()
