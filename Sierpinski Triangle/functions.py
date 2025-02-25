import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import random

def create_sierpinski_triangle(size: int) -> tuple[list[float], list[float]]:
    """
    PURPOSE: create a sierpinski triangle\n
    ARGUMENT: size: the number of points to use in making the sierpinski triangle\n
    RETURN: X: list of x coordinates, Y: list of y coordinates\n
    """
    X, Y, origin_points = [0], [0], [(0, 0), (5, 10), (10, 0)]
    for _ in range(size - 1):
        random_limit = random.choice(origin_points)
        X.append((X[-1] + random_limit[0]) / 2)
        Y.append((Y[-1] + random_limit[1]) / 2)
    return X, Y

def show_sierpinski_triangle(X: list[float], Y: list[float]) -> None:
    """
    PURPOSE: show the sierpinski triangle by ploting the provided coordinates\n
    ARGUMENT: X: x coordinates, Y: y coordinates\n
    RETURN: None\n
    """
    mplstyle.use('dark_background')
    plt.subplots_adjust(left=0, right=0.9, top=0.96, bottom=0, wspace=0, hspace=0)
    plt.axis('off')
    plt.axis('equal')
    plt.title(f"Sierpinski Triangle | Points: {len(X):,}")
    plt.scatter(X, Y, s=0.5, c="red")
    plt.show()