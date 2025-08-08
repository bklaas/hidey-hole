load("render.star", "render")

def main():
    return render.Root(
        child = render.Column(
            children = [
                render.Marquee(
                    width=128,
                    child=render.Text("Hello, Brown Bag Participants!"),
                    offset_start=0,
                    offset_end=0,
                ),
                render.Box(width=128, height=8, color = "#0a0"),
                render.Marquee(
                    width=128,
                    child=render.Text("We can dance if we want to, we can leave your friends behind; because if your friends don't dance and if they don't dance, well they're...no friends of mine."),
                    offset_start=0,
                    offset_end=0,
                ),
                render.Box(width=128, height=8, color = "#00a"),
            ],
        )
    )
