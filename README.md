# Pomodoro (Terminal App)

A simple Pomodoro timer app for the terminal, with support for custom timer durations and pre-defined work/break sessions.

## Features

- Start a default 25-minute timer
- Set custom minutes and seconds
- Pause, resume, and reset the timer
- Run saved sessions (alternating Pomodoro and Break intervals)
- Keyboard-driven terminal UI

## Requirements

- Python 3.10+
- Windows terminal (the app uses `msvcrt` and `cls`)

## Installation

1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run

```powershell
python main.py
```

## Main Menu Controls

- 1: Set timer time
- 2: Start timer
- 3: Sessions
- 4: Exit

## Timer Controls

- s: Stop timer
- h: Start or resume timer
- r: Reset timer
- x: Exit timer view

## Session Files

Session files are stored in `data/sessions`.

Each file uses this format:

```txt
name=Session Name
times=25:0,5:0,25:0,15:0
```

Notes:
- You can use `mm:ss` or plain seconds (example: `300`).
- Intervals alternate automatically: Pomodoro, Break, Pomodoro, Break, ...

## Example Sessions

- `data/sessions/session.txt`
- `data/sessions/simple_session.txt`
