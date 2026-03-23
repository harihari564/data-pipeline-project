#!/bin/bash

# 1. Setup Variables
LOG_FILE="pipeline.log"
# Public dataset of Titanic passengers
DATA_URL="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
RAW_DATA="raw_data.csv"

# Function to write messages to our log file
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - BASH - $1" | tee -a $LOG_FILE
}

log "--- Starting automated pipeline ---"

# 2. Check dependencies
if ! command -v python3 &> /dev/null; then
    log "ERROR: python3 is not installed. Stopping."
    exit 1
fi

# 3. Setup and activate Python virtual environment (venv)
if [ ! -d "venv" ]; then
    log "Creating Python virtual environment..."
    python3 -m venv venv
fi

log "Activating virtual environment..."
source venv/bin/activate

# 4. Data Acquisition: Download with curl and check for errors
log "Downloading CSV dataset..."
# -s hides progress bar, -f fails silently on server errors, -o outputs to file
if curl -s -f -o $RAW_DATA $DATA_URL; then
    log "Download successful."
else
    log "ERROR: Failed to download data from $DATA_URL"
    exit 1
fi

# 5. Run Python Processor
log "Running Python data processor..."
if python3 process_data.py; then
    log "Python script finished successfully."
else
    log "ERROR: Python script encountered an error. Check logs."
    exit 1
fi

log "--- Pipeline completed successfully! ---"
