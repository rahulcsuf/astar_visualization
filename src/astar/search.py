import numpy as np
import heapq
from typing import Callable

def __astar(
  grid: np.array,
  start: tuple,
  goal: tuple,
  heuristic: Callable[[tuple, tuple], np.array]
) -> list[list[int]]:
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
  close_set = set()
  came_from = {}
  gscore = {start: 0}
  fscore = {start: heuristic(start, goal)}
  oheap = []

  heapq.heappush(oheap, (fscore[start], start))

  while oheap:
    current = heapq.heappop(oheap)[1]
    if current == goal:
      data = []

      while current in came_from:
        data.append(current)
        current = came_from[current]

      return data
    close_set.add(current)

    for i, j in neighbors:
      neighbor = current[0] + i, current[1] + j
      tentative_g_score = gscore[current] + heuristic(current, neighbor)
      if 0 <= neighbor[0] < grid.shape[0]:
        if 0 <= neighbor[1] < grid.shape[1]:
          if grid[neighbor[0]][neighbor[1]] == 1:
            continue
        else:
          continue
      else:
        continue

      if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
        continue

      if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
        came_from[neighbor] = current
        gscore[neighbor] = tentative_g_score
        fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
        heapq.heappush(oheap, (fscore[neighbor], neighbor))

def search(
  grid: np.array,
  start: tuple,
  goal: tuple,
  heuristic: Callable[[tuple, tuple], np.array]
) -> list:
  route = __astar(grid, start, goal, heuristic)
  if route:
    route = route + [start]
    route = route[::-1]
    return route
