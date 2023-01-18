import matplotlib.pyplot as plt

plt.xlabel("X")
plt.ylabel("Y")

def generate_bresenham_circle(x0, y0, radius):
  # P0(x0, y0) radius = promień
  x = radius
  y = 0
  err = 0

  points = []

  while x >= y:
    # 8 punktów okręgu (ośmiokrotna symetria)
    points.append((x0 + x, y0 + y))
    points.append((x0 + y, y0 + x))
    points.append((x0 - y, y0 + x))
    points.append((x0 - x, y0 + y))
    points.append((x0 - x, y0 - y))
    points.append((x0 - y, y0 - x))
    points.append((x0 + y, y0 - x))
    points.append((x0 + x, y0 - y))

    y += 1
    err += 1 + 2*y
    if 2*(err-x) + 1 > 0:
      x -= 1
      err += 1 - 2*x

  print(points)

  return points

def main():
    points = generate_bresenham_circle(0, 0, 20)

    # plot the points
    plt.scatter([x for x, y in points], [y for x, y in points])

    # reference circle
    circle = plt.Circle((0, 0), 20, fill=False)
    plt.gcf().gca().add_artist(circle)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
