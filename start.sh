#!/bin/bash

PID=""

function auto() {
    python3 Script.py &
    PID=$!
    echo "Running with PID: $PID"
}

function stop() {
    if [ ! -z "$PID" ]; then
        echo "Stopping process with PID: $PID"
        kill -9 $PID
    else
        echo "No process found to stop."
    fi
}

function check_delay() {
    while true; do6
        if ps -p $PID -o comm= | grep -q "Script.py"; then
            if tail -n 10 /var/log/syslog | grep -q "Delay"; then
                echo "Delay detected, restarting process..."
                stop
                auto
            fi
        fi
    done
}

echo "Starting auto process..."
auto
check_delay
