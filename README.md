![Asteroids Demo](asteroids.gif)

# Asteroids

A modern Python + Pygame remake of the classic arcade favorite. Navigate your ship through an ever-increasing field of drifting space rocks—blast them to pieces, but watch out: larger asteroids fragment into smaller, faster chunks!

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Gameplay Mechanics](#gameplay-mechanics)
4. [Dependencies](#dependencies)
5. [Installation & Running](#installation--running)
6. [Controls](#controls)
7. [Scoring System](#scoring-system)
8. [Directory Structure](#directory-structure)
9. [Configuration](#configuration)
10. [Future Improvements](#future-improvements)
11. [Contributing](#contributing)
12. [License](#license)

---

## Overview

You pilot a triangular ship in the middle of the screen. Asteroids drift in from the edges. Your goal is simple: **survive** as long as you can, rack up points by destroying asteroids, and watch the chaos unfold as rocks split and multiply.

---

## Features

- **Smooth controls**: inertia-based thrust and rotation
- **Asteroid splitting**: large → medium → small → gone
- **Collision detection**: precise circle-vs-circle checks
- **Weapon cooldown**: 0.3-second delay between shots
- **Dynamic difficulty**: spawn rate and speed ramp up over time
- **On-screen HUD**: current score displayed in real time

---

## Gameplay Mechanics

1. **Movement**
   - Thrust forward/back along the ship’s facing direction
   - Rotational inertia for a classic arcade feel

2. **Shooting**
   - Press **Spacebar** to fire bullets
   - Bullets have a fixed lifespan and travel at 500 px/s
   - Weapon cooldown prevents spamming

3. **Asteroid Behavior**
   - Each rock is a `CircleShape` with a `position`, `velocity`, and `radius`
   - On being shot, an asteroid’s `split()` method:
     - Calls `kill()` on itself
     - If `radius > ASTEROID_MIN_RADIUS`: spawns two smaller asteroids with random split angles (20–50°) and 20% greater speed
     - Otherwise, it simply disappears

---

## Dependencies

- **Python** 3.12 or higher
- **Pygame** 2.6.1

Install Pygame via pip:

```bash
pip install pygame
