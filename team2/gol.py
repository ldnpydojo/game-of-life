import time

class Board(object):
     def __init__(self, cells):
         self.cells = cells

     def next_step(self):
         next_state = set([])
         interesting_cells = set([])
         for cell in self.cells:
             interesting_cells.add(cell)
             interesting_cells |= self.neighbours(cell)
         
         for cell in interesting_cells:
             is_alive = cell in self.cells
             fate = self.rules(is_alive, self.neighbours_alive(cell))
             if fate:
                next_state.add(cell)
         self.cells = next_state    
         return next_state
     
     def rules(self, is_alive, neighbours):
         if is_alive and neighbours in (2,3):
             return True
         elif not is_alive and neighbours == 3:
             return True
         return False
         
     def neighbours_alive(self, coord):
         return len(self.neighbours(coord) & self.cells)

     @staticmethod
     def neighbours(cell):
         deltas = [
                (0, 1),
                (0, -1),
                (1, 1),
                (1, -1),
                (1, 0),
                (-1, 0),
                (-1, 1),
                (-1, -1)
            ]
         neighbours = set([])
         for dx, dy in deltas:
             x, y = cell
             neighbours.add((x+dx, y+dy))
         return neighbours

     def __str__(self):
         size_x = max([x for x, y in self.cells]) + 2
         size_y = max([y for x, y in self.cells]) + 3
         size = (size_x, size_y)
         rows = []
         for y in range(size[0]):
             row = ''
             for x in range(size[1]):
                 if (x, y) in self.cells:
                      row += 'x'
                 else:
                      row += '.'
             rows.append(row)
         return u'\n'.join(rows) + '\n'

if __name__ == "__main__":
    seed1 = set([(1, 1), (1, 2), (1, 3)])
    seed2 = set([(2, 0), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)])
    seed3 = set([(2, 0), (3, 1), (1, 2), (2, 2), (3, 2)])
    b = Board(seed3)
    print b
    for step in range(1000):
        time.sleep(0.25)
        b.next_step()
        print b

