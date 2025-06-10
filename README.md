# System Monitor
A simple Python tool to monitor CPU, disk, and memory usage on an Ubuntu server, with alerts for high usage.
Features

Monitors CPU, disk, and memory in real-time using the psutil library.
Alerts when usage exceeds thresholds (e.g., CPU > 80%, disk > 90%, memory > 85%).
Runs as a cron job for continuous monitoring.

## Prerequisites

Operating System: Ubuntu (or other Linux distributions with Python support).
Python: Version 3.6 or higher.
Dependencies: psutil library for system monitoring.
Git: For cloning the repository.
GitHub SSH Key: For pushing/pulling changes (configured via SSH).

## Setup

Clone the Repository:
git clone git@github.com:ob-adams/system-monitor.git
cd system-monitor

Install psutil:
```
pip install psutil
```

## Usage

Run the Script:Test the script manually:
python3 system_monitor.py

The script checks CPU, disk, and memory usage and logs or sends alerts based on thresholds.

Set Up Cron Job:Schedule the script to run every 5 minutes:
crontab -e

Add:
*/5 * * * * /usr/bin/python3 /path/to/repo/system_monitor.py >> /path/to/repo/logfile.log 2>&1

Replace /path/to/repo/ with the actual path to your repository.

Configure Thresholds:Edit system_monitor.py to adjust alert thresholds:
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 90

Test Alerts:Simulate high usage to test alerts:
sudo apt install stress
stress --cpu 4 --timeout 60  # CPU stress
stress --vm 2 --vm-bytes 1G --timeout 60  # Memory stress

## Files

system_monitor.py: Main monitoring script.
README.md: This documentation.
.gitignore: Ignores sensitive files (e.g., logs).
logfile.log: Cron job output (optional).

## Contributing

Fork the repository on GitHub.
Clone your fork and create a branch:git checkout -b feature-branch


Commit and push changes:git commit -m "Add feature"
git push origin feature-branch


Open a pull request on GitHub.

License
MIT License (see LICENSE).
Contact
Email: obobadams@gmail.com or open a GitHub issue.
