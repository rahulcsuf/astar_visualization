import numpy as np
import matplotlib.pyplot as plt

def plot(grid: np.array, start: tuple[int], goal: tuple[int], route: list[list[int]]):
  x_coords, y_coords = [], []

  for i in (range(len(route))):
    x = route[i][0]
    y = route[i][1]
    x_coords.append(x)
    y_coords.append(y)

  # plot map and path
  fig, ax = plt.subplots(figsize=(20, 20))
  ax.imshow(grid, cmap=plt.cm.get_cmap('Greys'))
  ax.scatter(start[1], start[0], marker="*", color="green", s=200)
  ax.scatter(goal[1], goal[0], marker="*", color="red", s=200)
  ax.plot(y_coords, x_coords, color="black")

  plt.show()
