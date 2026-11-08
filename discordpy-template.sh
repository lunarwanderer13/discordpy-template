#!/usr/bin/env bash

cd "$(dirname "$0")" || exit 1

touch app.log
LOG="app.log"

while true; do
    echo "[$(date)] Starting app..." >> "$LOG"
    source .venv/bin/activate
    python main.py >> "$LOG" 2>&1
    echo -e "\n\n---\n\n[$(date)] App Crashed.\n\n---\n\n" >> "$LOG"
    sleep 1
done

