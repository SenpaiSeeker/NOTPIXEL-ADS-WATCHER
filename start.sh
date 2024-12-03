#!/bin/bash

PID=""
LOG_FILE="script_output.log"  # Log file to monitor for the "Delay" message.

function auto() {
    python3 Script.py &> $LOG_FILE &  # Redirecting output to log file.
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
    # Check if the "Delay" message exists in the log file.
    if grep -q "Delay" $LOG_FILE; then
        echo "Delay detected. Restarting..."
        return 0  # Delay detected
    else
        return 1  # No Delay detected
    fi
}

while true; do
    echo "Starting auto process..."
    auto

    # Monitor for "Delay" message and restart if found.
    while true; do
        sleep 5  # Check every 5 seconds.
        
        if check_delay; then
            stop
            break  # Exit the inner loop and restart the process.
        fi
    done
done
