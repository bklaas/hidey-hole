load("render.star", "render")

def main():
    return render.Root(
        child = render.Row(
            children = [
                render.Text("Hello, Brown Bag Participants!"),
                render.Text("We can dance if we want to, we can leave your friends behind; because if your friends don't dance and if they don't dance, well they're...no friends of mine."),
            ],
        )
    )
