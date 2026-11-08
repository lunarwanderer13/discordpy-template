#!/usr/bin/env bash

PID=$(pgrep -fo "discordpy-template.sh")

if [[ -z "$PID" ]]; then
    echo "App not found."
    exit 1
fi

PGID=$(ps -o pgid= -p "$PID" | xargs)

if [[ -z "$PGID" ]]; then
    echo "Process group not found."
    exit 1
fi

echo "Stopping app (PID: $PID, PGID: $PGID)"

kill -- "-$PGID"

