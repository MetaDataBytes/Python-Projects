from functions import create_sierpinski_triangle, show_sierpinski_triangle

if __name__ == "__main__":
    """
    The Sierpiński triangle is a fractal with the overall shape of an equilateral 
    triangle, subdivided recursively into smaller equilateral triangles.
    """
    size = 1_000_000
    X, Y = create_sierpinski_triangle(size=size)
    show_sierpinski_triangle(X=X, Y=Y)