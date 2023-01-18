import matplotlib.pyplot as plt

plt.xlabel("X")
plt.ylabel("Y")

def generate_bresenham_line(x_1, y_1, x_2, y_2):

    x, y = x_1, y_1
    delta_x = abs(x_2 - x_1)
    delta_y = abs(y_2 -y_1)

    gradient = delta_y / float(delta_x)

    if gradient > 1:
        delta_x, delta_y = delta_y, delta_x
        x, y = y, x
        x_1, y_1 = y_1, x_1
        x_2, y_2 = y_2, x_2

    p = 2 * delta_y - delta_x
    print(f"x = {x}, y = {y}")

    # Initialize the plotting points
    x_coordinates = [x]
    y_coordinates = [y]

    for k in range(2, delta_x + 2):
        if p > 0:
            y += 1 if y < y_2 else y - 1
            p += + 2 * (delta_y - delta_x)
        else:
            p += + 2 * delta_y

        x += 1 if x < x_2 else x - 1

        print(f"x = {x}, y = {y}")
        x_coordinates.append(x)
        y_coordinates.append(y)

    plt.plot(x_coordinates, y_coordinates)
    plt.scatter(x_coordinates, y_coordinates, s = 50, c = 'green')
    plt.grid(True)
    plt.show()

def main():
    generate_bresenham_line(1, 1, 3000, 1000)

if __name__ == "__main__":
    main()