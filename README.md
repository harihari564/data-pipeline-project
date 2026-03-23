# Automated Data Processing Pipeline

## Overview
This project is a fully automated data extraction and processing pipeline deployed on a Linux server. It fetches a public dataset (Titanic passengers), processes and cleans the data to find specific metrics, and securely logs all activities. The entire workflow is orchestrated using Bash and scheduled to run completely hands-free using Cron.

## Tech Stack
* **Orchestration:** Bash Scripting
* **Data Processing:** Python 3 (Virtual Environment)
* **Automation:** Linux Cron Jobs
* **Version Control:** Git & GitHub

## Project Structure
* `pipeline.sh`: The main Bash orchestrator. It manages the Python virtual environment, safely downloads the dataset via `curl`, handles error checking, and triggers the Python script.
* `process_data.py`: The Python processor. It reads the raw CSV, filters out non-survivors, and generates both a clean CSV and a JSON statistical summary.
* `summary.json`: The final output report containing calculated metrics (total evaluated, total survivors, survival rate).
* `pipeline.log`: A continuous, time-stamped log file tracking the pipeline's background execution and catching any errors.

## How to Run

### Manual Execution
To run the pipeline manually and observe the logging, execute the bash script:
\`\`\`bash
./pipeline.sh
\`\`\`

### Automated Background Execution
This pipeline is currently automated on the server to run at the top of every hour using the following crontab configuration:
\`\`\`bash
0 * * * * cd /home/harisankar/data-pipeline-project && ./pipeline.sh >> cron.log 2>&1
\`\`\`
