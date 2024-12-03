#!/bin/bash

function auto() {
    python3 Script.py &
    PID=$!
    echo "Running with PID: $PID"
}

function stop() {
    if [ ! -z "$PID" ]; then
        echo "Stopping process with PID: $PID"
        kill -9 $PID
        PID=""
    else
        echo "No process found to stop."
    fi
}

while true; do
    echo "Starting auto process..."
    auto

    while kill -0 $PID 2>/dev/null; do
        if grep -q "Delay 6 minutes" <(tail -f /var/log/syslog 2>/dev/null); then
            echo "Detected 'Delay 6 minutes' in logs. Restarting process..."
            stop
            break
        fi
        sleep 1
    done

    echo "Restarting auto process..."
    sleep 1
done
