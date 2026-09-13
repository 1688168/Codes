# Robot Room Cleaner DFS Animation

This folder contains a replayable visualization of LeetCode 489, using the exact Example 1 room:

```text
room = [[1,1,1,1,1,0,1,1],
        [1,1,1,1,1,0,1,1],
        [1,0,1,1,1,1,1,1],
        [0,0,0,1,0,0,0,0],
        [1,1,1,1,1,1,1,1]]

start = (1, 3)
initial direction = north/up
```

The animation follows the same turn-first DFS logic as the original C++ solution.

## Files

- `index.html` — the complete standalone animation, including all HTML, CSS, JavaScript, room
  data, and DFS simulation code.
- `robot-room-cleaner-dfs.fragment.html` — the unwrapped, human-readable source used to build the
  standalone page.
- `README.md` — these instructions.

No installation, package manager, build step, or internet connection is required.

## Run the animation

### Option 1: Finder

1. Open this folder in Finder.
2. Double-click `index.html`.
3. It will open in your default web browser and begin playing automatically.

### Option 2: macOS Terminal

Run:

```bash
open "/Users/yeuchinglee/Documents/ylee/ylee_repo/Codes/LC/0489_animation/index.html"
```

### Option 3: Any browser

Drag `index.html` into a Chrome, Safari, Firefox, or Edge window.

## Controls

- **Pause / Play** — stop or continue automatic playback.
- **← Step / Step →** — inspect one robot operation at a time.
- **Restart** — return to the initial state and replay from the beginning.
- **Speed** — adjust playback from `0.5×` to `4×`.

## Visual meanings

- Red brick-patterned cell: blocked cell (`0`).
- Plain accessible cell: open but not yet discovered (`1`).
- Blue cell: discovered by DFS but not yet cleaned.
- Green cell: cleaned.
- Purple robot: normal DFS exploration.
- Orange robot: physical `goBack()` operation.
- Solid purple cell border: the robot's current cell.
- Bright red wall border: `move()` just tested that wall and returned `false`.
- Dashed yellow border: DFS considered an already visited neighbor and did not move.

The text below the grid explains the current API operation. The `DFS stack` line shows the active
recursive calls. Notice that returning from a recursive function does not itself move the robot;
the orange `goBack()` sequence physically returns it to the parent and restores its direction.

## Modify the room

The complete source is embedded in `index.html`. For easier reading, open
`robot-room-cleaner-dfs.fragment.html` in a text editor and search for:

```javascript
const rows = [0, 1, 2, 3, 4];
const cols = [0, 1, 2, 3, 4, 5, 6, 7];
const openCells = new Set([
```

The keys in `openCells` are the accessible `(row, column)` coordinates. Any grid coordinate not in
that set is rendered as blocked. Also update the initial `state.row`, `state.col`, the starting
visited key, and the arguments to `dfs(...)` if you want to move the starting position.
