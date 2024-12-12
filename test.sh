#!/bin/bash

# Function to handle user input
check_input() {
    while true; do
        read -r input
        if [[ "$input" == "potatoide" ]]; then
            echo "Exiting..."
            exit 0
        fi
    done
}

# Start the input check in the background
check_input &

# Infinite loop to print "patata"
while true; do
    echo "patata"
    sleep 1  # Adding a delay to avoid flooding the terminal
done
