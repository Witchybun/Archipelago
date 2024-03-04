from worlds.AutoWorld import AutoWorldRegister, World
from worlds.generic import GenericWorld
from tkinter import *
from tkinter import ttk

non_hidden_banned_games = ["Archipelago", "Sudoku"]


games = {name: world for name, world in AutoWorldRegister.world_types.items()}
game_names = games.keys()
current_game = GenericWorld
root = Tk()


def set_world(game: str):
    global current_game
    if not game:
        current_game = GenericWorld
    current_game = games[game]
    return "Stinky"


wrapper_left = LabelFrame(root, text="Supported Games")
wrapper_right_high = LabelFrame(root, text="Generic Settings")
wrapper_right_low = LabelFrame(root, text="Game Settings")

canvas_left = Canvas(wrapper_left)
canvas_left.pack(side=LEFT, fill="y")
canvas_right_top = Canvas(wrapper_right_high)
canvas_right_top.pack(fill="both")

y_scroll_bar = ttk.Scrollbar(wrapper_left, orient="vertical", command=canvas_left.yview)
y_scroll_bar.pack(side=RIGHT, fill="y")
canvas_left.configure(yscrollcommand=y_scroll_bar.set)

canvas_left.bind('<Configure>', lambda e: canvas_left.configure(scrollregion=canvas_left.bbox('all')))

frame_left = Frame(canvas_left)
canvas_left.create_window((0, 0), window=frame_left, anchor="w")
frame_right_top = Frame(canvas_right_top)

wrapper_left.pack(fill="y", expand=0, padx=10, pady=10, side=LEFT)
wrapper_right_high.pack(fill="both", expand=1, padx=10, pady=10)
wrapper_right_low.pack(fill="both", expand=1, padx=10, pady=10)

for game in game_names:
    game_button = Button(frame_left, text=game, justify="center", command=set_world(game))
    game_button.pack(fill="x")

Label(frame_right_top, text="Player Name").grid(row=0, column=0)


root.geometry('1000x650')
root.wm_title("Yaml Maker")


root.mainloop()
