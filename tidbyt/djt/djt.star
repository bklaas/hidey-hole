load("render.star", "render")

def main():
    return render.Root(
        child = 
            render.Plot(
              data = [
                (0, 66.22),
                (1, 49.93),
                (2, 46.74),
                (3, 33.08),
                (4, 27.20),
                (5, 18.08),
                (6, 14.79),
              ],
              width = 64,
              height = 32,
              color = "#0f0",
              color_inverted = "#f00",
              x_lim = (0, 6),
              y_lim = (0, 68),
              fill = True,
            ),
    )
