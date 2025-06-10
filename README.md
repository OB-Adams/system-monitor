# System Monitoring Tool
A Python-based tool to monitor Linux system resources (CPU, memory, disk) with logging and email alerts.

## Features
- Monitors CPU, memory and disk usage using 'psutil'.
- Logs metrics to '/var/log/system_monitor'.
- Sends email alerts for high resource usage.
- Configurable threshold and SMTP settings via 'config.ini'

## Prerequisites
- Linux (e.g. Ubuntu 22.04, CentOS 9)
- Python 3.8+
- 'psutil' ('pip install psutil')

## Installation 
1. Cone the repository:
