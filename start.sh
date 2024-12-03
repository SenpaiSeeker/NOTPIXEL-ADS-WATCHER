#!/bin/bash

# Fungsi untuk memulai proses
function auto() {
    python3 Script.py &  # Menjalankan Script.py di latar belakang
    PID=$!               # Menyimpan PID proses
    echo "Running with PID: $PID"
}

# Fungsi untuk menghentikan proses
function stop() {
    if [ ! -z "$PID" ]; then
        echo "Stopping process with PID: $PID"
        kill -9 $PID 2>/dev/null  # Mematikan proses dengan PID yang tersimpan
        PID=""
    else
        echo "No process found to stop."
    fi
}

# Memulai loop untuk memonitor log
while true; do
    echo "Starting auto process..."
    auto

    # Memeriksa log untuk pesan "Delay 6 minutes"
    tail -f /var/log/syslog | while read LINE; do
        echo "$LINE" | grep -q "Delay 6 minutes"
        if [ $? -eq 0 ]; then
            echo "Detected 'Delay 6 minutes' in logs. Restarting process..."
            stop
            break
        fi
    done

    sleep 1  # Opsional, tambahkan jeda untuk menghindari iterasi yang terlalu cepat
done
