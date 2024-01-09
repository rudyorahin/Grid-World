from __future__ import print_function
from heapq import * #Hint: Use heappop and heappush

ACTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

class AI:
    def __init__(self, grid, type):
        self.grid = grid
        self.set_type(type)
        self.set_search()

    def set_type(self, type):
        self.final_cost = 0
        self.type = type

    def set_search(self):
        self.final_cost = 0
        self.grid.reset()
        self.finished = False
        self.failed = False
        self.previous = {}

        # Initialization of algorithms goes here
        if self.type == "dfs":
            self.frontier = [self.grid.start]
            self.explored = []
        elif self.type == "bfs":
            self.frontier = [self.grid.start]
            self.explored = []
        elif self.type == "ucs":
            self.grid.nodes[self.grid.start].cost_total = 0
            self.frontier = [(self.grid.nodes[self.grid.start].cost_total , self.grid.start)]
            self.explored = []
        elif self.type == "astar":
            self.grid.nodes[self.grid.start].cost_total = 0
            self.frontier = [(self.grid.nodes[self.grid.start].cost_total + abs(self.grid.start[0]-self.grid.goal[0]) + abs(self.grid.start[1]-self.grid.goal[1]), self.grid.start)]
            self.explored = []
            
             # self.manhattan_distance = abs(self.grid.start[0] - self.grid.goal[0]) + abs(self.grid.start[1] - self.grid.goal[1])


    def get_result(self):
        total_cost = 0
        current = self.grid.goal
        while not current == self.grid.start:
            total_cost += self.grid.nodes[current].cost()
            current = self.previous[current]
            self.grid.nodes[current].color_in_path = True #This turns the color of the node to red
        total_cost += self.grid.nodes[current].cost()
        self.final_cost = total_cost

    def make_step(self):
        if self.type == "dfs":
            self.dfs_step()
        elif self.type == "bfs":
            self.bfs_step()
        elif self.type == "ucs":
            self.ucs_step()
        elif self.type == "astar":
            self.astar_step()

    #DFS: BUGGY, fix it first
    def dfs_step(self):
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return
        current = self.frontier.pop()

        # Finishes search if we've found the goal.
        if current == self.grid.goal:
            self.finished = True
            return

        children = [(current[0]+a[0], current[1]+a[1]) for a in ACTIONS]
        self.grid.nodes[current].color_checked = True
        self.grid.nodes[current].color_frontier = False

        # explored after pop from frontier
        self.explored.append(current)

        for n in children:
            if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                if not self.grid.nodes[n].puddle and n not in self.explored and n not in self.frontier:
                    self.previous[n] = current
                    self.frontier.append(n)
                    self.grid.nodes[n].color_frontier = True


    # BFS implementation BFS here (Don't forget to implement initialization at line 23)
    def bfs_step(self):
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return
        current = self.frontier.pop(0)

        # Finishes search if we've found the goal.
        if current == self.grid.goal:
            self.finished = True
            return

        children = [(current[0]+a[0], current[1]+a[1]) for a in ACTIONS]
        self.grid.nodes[current].color_checked = True
        self.grid.nodes[current].color_frontier = False

        # explored after pop from frontier
        self.explored.append(current)

        for n in children:
            if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                if not self.grid.nodes[n].puddle and n not in self.explored and n not in self.frontier:
                    self.previous[n] = current
                    self.frontier.append(n)
                    self.grid.nodes[n].color_frontier = True

    #Implement UCS here (Don't forget to implement initialization at line 23)
    def ucs_step(self):
        # print(self.frontier)
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return

        current = heappop(self.frontier)
        # print(current_cost)
        if current[1] == self.grid.goal:
            self.finished = True
            return

        children = [(current[1][0]+a[0], current[1][1]+a[1]) for a in ACTIONS]
        self.grid.nodes[current[1]].color_checked = True
        self.grid.nodes[current[1]].color_frontier = False

        self.explored.append(current[1])

        for n in children:
            if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                new_cost = self.grid.nodes[n].cost() + current[0]
                frontier = [candidate for candidate in self.frontier if candidate[1] == n]

                if not self.grid.nodes[n].puddle and not n in self.explored and not frontier:
                    # print(self.grid.nodes[n].cost())
                    self.previous[n] = current[1]
                    heappush(self.frontier, (new_cost, n))
                    self.grid.nodes[n].color_frontier = True

                elif not self.grid.nodes[n].puddle and frontier:
                    index = self.frontier[self.frontier.index((frontier[0][0], n))]
                    if index[0] > new_cost:
                        self.frontier.remove(index)
                        heappush(self.frontier, (new_cost, n))
                        self.previous[n] = current[1]

                    # if n not in self.explored:
                    #     self.previous[n] = current
                    #     self.grid.nodes[n].cost_total = new_cost
                    #     heappush(self.frontier, (self.grid.nodes[n].cost(), n))
                    #     self.grid.nodes[n].color_frontier = True
                    # elif new_cost > self.grid.nodes[n].cost_total:
                    #     self.previous[n] = current
                    #     # self.grid.nodes[n].cost_total = new_cost
                    #     # index = self.frontier.index((self.grid.nodes[n].cost_total, n))
                    #     # self.frontier[index] = (self.grid.nodes[n].cost_total, n)
                    #     # heapify(self.frontier)
                    #     heappush(self.frontier, (self.grid.nodes[n].cost(), n))
                    #     self.grid.nodes[n].color_frontier = True
                    #     print("Rudyyyyyy", self.grid.nodes[n].cost_total)
        
        # if not self.frontier:
        #     self.failed = True
        #     self.finished = True
        #     print("no path")
        #     return

        # cost, current = heappop(self.frontier)

        # if current == self.grid.goal:
        #     self.finished = True
        #     return

        # self.grid.nodes[current].color_checked = True
        # self.grid.nodes[current].color_frontier = False

        # # explored after pop from frontier
        # self.explored.append(current)

        # children = [(current[0]+a[0], current[1]+a[1]) for a in ACTIONS]
        # for n in children:
        #     if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
        #         if not self.grid.nodes[n].puddle:
        #             new_cost = self.grid.nodes[current].cost_total + self.grid.nodes[n].cost()
        #             if n not in self.explored or n not in self.frontier:
        #                 self.previous[n] = current
        #                 self.grid.nodes[n].cost_total = new_cost
        #                 heappush(self.frontier, (new_cost, n))
        #                 self.grid.nodes[n].color_frontier = True
        #             elif new_cost < self.grid.nodes[n].cost_total:
        #                 self.previous[n] = current
        #                 self.grid.nodes[n].cost_total = new_cost
        #                 self.frontier.remove((self.grid.nodes[n].cost_total, n))
        #                 heappush(self.frontier, (new_cost, n))
        #                 self.grid.nodes[n].color_frontier = True
        #                 print("rudyy")

    
    #Implement Astar here (Don't forget to implement initialization at line 23)
    def astar_step(self):
        if not self.frontier:
            self.failed = True
            self.finished = True
            print("no path")
            return

        current = heappop(self.frontier)

        if current[1] == self.grid.goal:
            self.finished = True
            return

        children = [(current[1][0] + a[0], current[1][1] + a[1]) for a in ACTIONS]
        self.grid.nodes[current[1]].color_checked = True
        self.grid.nodes[current[1]].color_frontier = False

        self.explored.append(current[1])

        
        for n in children:
            if n[0] in range(self.grid.row_range) and n[1] in range(self.grid.col_range):
                if not self.grid.nodes[n].puddle and not n in self.explored:
                    new_cost = self.grid.nodes[current[1]].cost_total + self.grid.nodes[n].cost()
                    heuristic_cost = abs(n[0] - self.grid.goal[0]) + abs(n[1] - self.grid.goal[1])
                    f_cost = new_cost + heuristic_cost
                    frontier = [candidate for candidate in self.frontier if candidate[1] == n]

                    if not frontier:
                        self.previous[n] = current[1]
                        self.grid.nodes[n].cost_total = new_cost
                        heappush(self.frontier, (f_cost, n))
                        self.grid.nodes[n].color_frontier = True

                    elif frontier[0][0] > f_cost:
                        self.frontier.remove(frontier[0])
                        self.previous[n] = current[1]
                        self.grid.nodes[n].cost_total = new_cost
                        heappush(self.frontier, (f_cost, n))
                        self.grid.nodes[n].color_frontier = True

