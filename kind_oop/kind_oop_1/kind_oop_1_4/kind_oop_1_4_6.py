class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        min_lim, max_lim = Graph.LIMIT_Y
        max_lim += 1
        print(*(num for num in self.data if num in range(min_lim, max_lim)))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
