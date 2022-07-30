import random
from colorama import Fore, Style

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep


class Loader:
    def __init__(self, desc="Loading...", end="", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()



DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "
def generate_dice_faces_diagram(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`.

    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ RESULTS ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram



# Dictionary {starting pos: ending postion}
action = {#ladders
3:18, 14:32, 12:20, 34:46, 77:88, 53:64, 37:49, 7:48, 42:59, 69:70, #chute 
22:16, 36:21, 31:11, 66:1, 99:64, 67:66, 72:71, 86:63, 43:27, 33:18}

#Dictionary {Player: POS}
pos = {1:0, 2:0, 3:0, 4:0}


 #1-Liner For loop going through all values of pos and making sure that all values are below 100  


#a leaderbord has:
#standings (1st, 2nd, 3rd, 4th)
#pos of players sort() - list
def leaderboard(pos):
 pos = {k: v for k, v in sorted(pos.items(), key=lambda x: x[1], reverse=True)}
 counter = 0
 for k in pos:
  counter += 1
  print('Place:', counter, ', player:', k, 'position:', pos[k])
 print('\n\n')
  #Sorted Dictionary - Only for printing 

  


while all(x<100 for x in pos.values()):
  for player in pos:
    print("Player", player)
    print()
    temp = input("Press enter to roll:")
    num = (random.randint(1,6))
    numlist = list()
    numlist.append(num)
    loader = Loader("Rolling dice...").start()
    for i in range(4):
        sleep(0.25)
    loader.stop()
    dice_face_diagram = generate_dice_faces_diagram(numlist)

    # 4. Display the diagram
    
    print(f"\n{dice_face_diagram}")

    pos[player] += num
    if pos[player] in action:
      if pos[player] - action[pos[player]] > 0:
        print(Fore.RED +'You landed on a chute.')
      else:
        print(Fore.GREEN + 'You landed on a ladder!')
      print(Style.RESET_ALL)
      pos[player] = action[pos[player]]
    leaderboard(pos)

    if pos[player] > 100:
      print("Player", player, "wins!")
      break
      