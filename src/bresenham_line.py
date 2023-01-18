import matplotlib.pyplot as plt

plt.xlabel("X")
plt.ylabel("Y")

def generate_bresenham_line(x1, y1, x2, y2):

    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy / float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    print(f"x = {x}, y = {y}")

    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        #print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()

def main():
    generate_bresenham_line(10, 10, 20, 20)

if __name__ == "__main__":
    main()