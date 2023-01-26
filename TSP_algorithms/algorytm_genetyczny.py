from math import sqrt
from random import randint, sample
import matplotlib.pyplot as plt
import time
from genetic_library import GeneticAlgorithm, Element
from genetic_library.selection_models import elite_selection_model

START_POINT = []
POINTS = []
# START_POINT = [(200, 600)]
# POINTS = [(1000, 200), (1750, 800), (100, 50), (1750, 50), (900, 850), (1000, 1000), (500, 500), (700, 100), (650, 1000),
#           (900, 100), (1800, 250), (700, 500), (900, 1000), (100, 200), (300, 400), (400, 300), (100, 1000), (200, 1000),
#           (1000, 100), (5, 312), (437, 987), (1381, 517), (620, 300), (722, 112), (1015, 1000), (108, 108),
#           (17, 403), (403, 515), (703, 3), (1700, 215), (1133, 408), (815, 100), (1250, 50), (314, 77),
#           (785, 250), (230, 480), (1355, 57), (60, 80), (1900, 150), (300, 800), (750, 600), (1215, 550), (480, 320),
#           (612, 50), (1800, 20), (1750, 30), (1325, 515), (100, 900), (1750, 15)]
STOP = int(input("Podaj ilość pokoleń do sprawdzenia: "))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 2000])
ax.set_ylim([0, 1000])

def onclick(event):
    global START_POINT, POINTS, fig, ax
    # print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #       (event.button, event.x, event.y, event.xdata, event.ydata))

    if START_POINT:
        ax.scatter(event.xdata, event.ydata, color='black', s=10)
        fig.canvas.draw()
        tup = (int(event.xdata), int(event.ydata))
        POINTS.append(tup)
        print("Lista punktów:", POINTS)
    else:
        ax.scatter(event.xdata, event.ydata, color='red', s=30)
        fig.canvas.draw()
        tup = (int(event.xdata), int(event.ydata))
        START_POINT.append(tup)
        print("Pierwszy punkt:", START_POINT)

def plotting():
    global START_POINT, POINTS, fig, ax
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.get_current_fig_manager().full_screen_toggle()
    plt.title(f"Kliknij na mapie, aby dodać punkty. Naciśnij 'Q', by wyznaczyć najkrótszą trasy dla {STOP} pokoleń.", fontsize=10)
    plt.show()

def genetic_shortest_path():
    global START_POINT, POINTS
    END_POINT = START_POINT

    class Route(Element):
        def __init__(self, points):
            self.points = points
            super().__init__()

        def _perform_mutation(self):
            first = randint(1, len(self.points) - 2)
            second = randint(1, len(self.points) - 2)

            self.points[first], self.points[second] = self.points[second], self.points[first]

        def crossover(self, element2: 'Element') -> 'Element':
            child_points = self.points[1:int(len(self.points) / 2)]
            for point in element2.points:
                if point not in child_points and point not in END_POINT + START_POINT:
                    child_points.append(point)

                if len(child_points) == len(element2.points):
                    break
            return Route(START_POINT + child_points + END_POINT)

        def evaluate_function(self):
            def _calculate_distance(x1, x2, y1, y2):
                return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            sum = 0
            for i, p in enumerate(self.points):
                if i + 1 > len(self.points) - 1:
                    break
                next_point = self.points[i + 1]
                sum += _calculate_distance(p[0], next_point[0], p[1], next_point[1])

            return sum

        def __repr__(self):
            return str(self.points)

    def first_generation_generator():
        return [Route(START_POINT + sample(POINTS, len(POINTS)) + END_POINT) for _ in range(100)]

    plt.ion()
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def stop_condition(string, current_fitness, i):
        global STOP
        ax1.clear()
        ax1.scatter(*zip(*string.points))
        ax1.plot(*zip(*string.points))
        fig.canvas.draw()
        fig.canvas.flush_events()

        return i == STOP

    ga = GeneticAlgorithm(first_generation_generator, elite_selection_model, stop_condition)
    ga.run()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Czas wykonania całkowitej pracy algorytmu: ", elapsed_time)
    plt.title("Naciśnij 'Q', by wrócić do okna wyboru trybu. Wyniki znajdują się w terminalu.", fontsize=8)
    plt.show(block=True)

plotting()
start_time = time.time()
genetic_shortest_path()
