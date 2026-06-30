
# Stone, Paper, Scissor — Multi-Round Score Tracker (Python)

A command-line Stone-Paper-Scissor game where you choose how many rounds to play against the computer, and the program keeps score across all of them.

This is a step up from a single-round version: instead of just printing "you win" once, it tracks how many rounds you won, how many the computer won, and how many were draws, then tells you who won overall.

## Game Rules

| Choice | Beats | Loses to |
|---|---|---|
| Stone (`s`) | Scissor | Paper |
| Paper (`p`) | Stone | Scissor |
| Scissor (`sc`) | Paper | Stone |

Internally, each choice is stored as a number: `stone = 1`, `paper = 0`, `scissor = -1`. Using numbers instead of text makes it possible to compare choices with simple math instead of writing out every case by hand.

## How to Run

```bash
python pss.py
```

You'll first be asked how many rounds you want to play. Then, for each round, you'll be asked to enter your choice: `s` for stone, `p` for paper, or `sc` for scissor. After all rounds are done, your final score, the computer's score, and the draw count are printed, along with the overall winner.

## How It Works

The game logic lives inside a function called `game()`, which plays exactly one round: it picks a random choice for the computer, asks you for your choice, decides the result, and returns a number representing what happened (a win, a loss, or a draw). The main part of the program calls `game()` once per round inside a loop, and uses the number it gets back to update the running score.

The win/loss check doesn't compare every possible pair by hand. Instead, it looks at the *difference* between your choice and the computer's choice (`you - com`). Because of how the numbers are assigned, a win always produces a difference of either `2` or `-1`, and a loss produces something else. This is a more compact way of expressing the same rules as a long list of if/elif statements.

One deliberate design choice: the result of `game()` is saved into a variable (`result`) before checking it, instead of calling `game()` directly inside the if/elif chain. Calling it multiple times would re-run the whole round — including picking a new random computer choice — every time it's checked, which would break the scoring. Saving the result once avoids that.

## Sample Output

```
Enter the number of times you want to play the game 3
Enter your choice s/sc/p= s
your choice = s 
 computer's choice = sc 

Enter your choice s/sc/p= p
your choice = p 
 computer's choice = s 

Enter your choice s/sc/p= sc
your choice = sc 
 computer's choice = sc 

your score = 2
computer score  = 0
Match drawn = 1
You won  by  2 
```

## Concepts Practiced

- Writing a function that returns a value, and using that value to control program flow (instead of calling the function repeatedly)
- Dictionaries for two-way lookups between letters and numbers
- Looping a fixed number of times and accumulating a running total (score tracking)
- Replacing a long if/elif chain with a single arithmetic comparison

## Known Limitations / Next Steps

- No input validation yet — entering anything other than `s`, `p`, or `sc` will crash the program with a `KeyError`. A future version should check the input before looking it up, the same way it's handled in the Snake-Water-Gun project's later iteration.
- The comment block at the top of the file sketches a more modular design (separate functions for `get_player_choice()`, `generate_computer_choice()`, `check_winner()`, `update_score()`, and `display_result()`). The current version works correctly but hasn't been split up that way yet — that refactor is the planned next step.

## Author

Shabd Gupta
