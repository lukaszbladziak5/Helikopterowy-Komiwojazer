import matplotlib.pyplot as plt
from itertools import permutations
import time

points = []
# points = [(200, 600), (1000, 200), (1750, 800), (100, 50), (1750, 50), (900, 850), (1000, 1000), (500, 500), (700, 100), (650, 1200)]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
best_route = None

def onclick(event):
    global points, ax, fig
    if points:
        points.append((event.xdata, event.ydata))
        ax.scatter(event.xdata, event.ydata, color='black', s=10)
        fig.canvas.draw()
    else:
        points.append((event.xdata, event.ydata))
        ax.scatter(event.xdata, event.ydata, color='red', s=30)
        fig.canvas.draw()

def draw_first_plot():
    global fig, ax
    plt.get_current_fig_manager().full_screen_toggle()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    ax.set_xlim([0, 2000])
    ax.set_ylim([0, 1000])
    plt.title("Kliknij na mapie, aby dodać punkty. Naciśnij 'Q', by wyznaczyć najkrótszą trasę.", fontsize=10)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def plot_route(route):
    # Rysowanie najkrótszej trasy
    x = [point[0] for point in route]
    x.append(route[0][0])
    y = [point[1] for point in route]
    y.append(route[0][1])
    plt.title("Naciśnij 'Q', by wrócić do okna wyboru trybu. Wyniki znajdują się w terminalu.", fontsize=8)
    plt.plot(x, y, '-o')
    plt.show()

def calculate_route():
    # Obliczanie wszystkich możliwych tras
    global points, best_route
    start_time = time.time()
    routes = list(permutations(points))

    # Obliczanie najkrótszej trasy
    min_distance = float("inf")
    for route in routes:
        distance = 0
        for i in range(len(route) - 1):
            distance += ((route[i][0] - route[i+1][0]) ** 2 + (route[i][1] - route[i+1][1]) ** 2) ** 0.5
        distance += ((route[len(route) -1][0] - route[0][0]) ** 2 + (route[len(route) -1][1] - route[0][1]) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            best_route = route
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Wyniki:\n")
    print("Czas wykonania: ", elapsed_time)
    print("Długość najlepszej trasy dla",len(best_route), "miast to:", min_distance)



draw_first_plot()
calculate_route()
plot_route(best_route)
