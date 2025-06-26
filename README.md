# Bump Sound Helper for Visually Impaired Pokémon Players

This is a Python tool that plays a bump sound when the player is pushing into a wall or obstacle for more than 1.5 seconds. Designed for blind and visually impaired Pokémon fans.

🎮 **Supports Nintendo Switch Joy-Con**

🦯 **Lets you feel obstacles through sound**

## How It Works

- Detects if you push the stick into a wall
- After 1.5 seconds, it plays a bump sound
- Prevents repeat sounds for 1 second
- Works with `se_wall_bump.wav` (included)

## Requirements

- Python 3
- pygame (`pip install pygame`)
- Joy-Con or compatible controller
- Yuzu emulator or any similar setup

## Run

```bash
python bump_with_joycon.py
```

MIT License