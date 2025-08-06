import curses
import time

ASCII_RAPTOR = [
    "          ____      ________",
    "        ,^.__.>--\"~~'_.--~_)~^.",
    "       _L^~   ~    (~ _.-~ \\. |\\",
    "    ,-~    __    __,^\"/\\_A_/ /' \\",
    "  _/    ,-'  \"~~\" __) \\  ~_,^   /\\",
    " //    /  ,-~\\ x~\"  \\._\"-~     ~ _Y",
    " Y'   Y. (__.//     /  \" , \"\\_r ' ]",
    " J-.__l_>---r{      ~    \\__/ \\_ _/",
    "(_ (   (~  (  ~\"---   _.-~ `\\ / \\ !",
    " (_\"~--^----^--------\"  _.-c Y  /Y'",
    "  l~---v----.,______.--\"  /  !_/ |",
    "   \\.__!.____./~-.      _/  /  \\ !",
    "    `x._\\_____\\__,>---\"~___Y\\__/Y'",
    "        ~     ~(_~~(_)\",~___)/ /\\|",
    "               (_~~   ~~___)  \\_t",
    "               (_~~   ~~___)\\_/ |",
    "               (_~~   ~~___)\\_/ |",
    "               { ~~   ~~   }/ \\ l"
]


def animate_raptor(stdscr):
    max_y, max_x = stdscr.getmaxyx()
    r_height = len(ASCII_RAPTOR)
    r_width = max(len(line) for line in ASCII_RAPTOR)

    x = max_x
    y = max_y - r_height - 1

    while x > -r_width:
        stdscr.clear()
        for idx, line in enumerate(ASCII_RAPTOR):
            # Handle partial drawing when raptor is partially off-screen
            if 0 <= y + idx < max_y:
                slice_start = max(0, -x)
                slice_end = max_x - x if (x + len(line)) > max_x else len(line)
                visible = line[slice_start:slice_end]
                draw_x = max(0, x)
                if visible:
                    try:
                        stdscr.addstr(y + idx, draw_x, visible)
                    except curses.error:
                        pass
        stdscr.refresh()
        time.sleep(0.03)
        x -= 2

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.addstr(0, 0, "Press SPACE to unleash the velociraptor! Press 'q' to quit.")
    stdscr.refresh()

    while True:
        ch = stdscr.getch()
        if ch == ord(' '):
            animate_raptor(stdscr)
            stdscr.clear()
            stdscr.addstr(0, 0, "Press SPACE to summon again, or 'q' to quit.")
            stdscr.refresh()
        elif ch == ord('q'):
            break
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)

