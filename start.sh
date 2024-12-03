function auto() {
    python3 Script.py &
    PID=$!
    echo "running with PID: $PID"
}

function stop() {
    if [ ! -z "$PID" ]; then
        echo "Stopping with PID: $PID"
        kill -9 $PID
    else
        echo "No process found to stop."
    fi
}

while true; do
    echo "Starting auto process..."
    auto
    sleep 30
    stop
done
