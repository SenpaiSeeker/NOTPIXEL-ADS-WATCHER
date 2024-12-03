#!/bin/bash

function auto() {
    python3 Script.py &
    PID=$!
    echo "Running with PID: $PID"
}

function stop() {
    if [ ! -z "$PID" ]; then
        echo "Stopping with PID: $PID"
        kill -9 $PID
        PID=""
    else
        echo "No process found to stop."
    fi
}

function monitor_logs() {
    while true; do
        if tail -n 1 /var/log/syslog | grep -q "Delay 6 minutes"; then
            echo "Detected 'Delay 6 minutes' in logs. Restarting process..."
            stop
            auto
        fi
        sleep 1
    done
}

echo "Starting auto process..."
auto
monitor_logs
