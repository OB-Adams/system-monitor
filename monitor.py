#python 3
import psutil
import smtplib
import logging
from email.mime.text import MIMEText
from datetime import datetime
import os

import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Configuring loggin
logging.basicConfig(filename='/var/log/system_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


CPU_THRESHOLD = float(config['Monitoring']['cpu_threshold'])
MEM_THRESHOLD = float(config['Monitoring']['memory_threshold'])
DISK_THRESHOLD = float(config['Monitoring']['disk_threshold'])

SMPT_SERVER = config['Email']['smtp_server']
SMTP_PORT = int(config['Email']['smtp_port'])
SENDER = config['Email']['sender']
RECEIVER = config['Email']['receiver']
PASSWORD = config['Email']['password']

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_and_alert(f"High CPU usage: {cpu_usage}%")
        return cpu_usage


def check_memory():
    memory = psutil.virtual_memory()
    mem_usage = memory.percent
    if mem_usage > MEM_THRESHOLD:
        log_and_alert(f"High memory usage: {mem_usage}%")
        return mem_usage

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_and_alert(f"High disk usage: {disk_usage}%")
        return disk_usage

def log_and_alert(message):
    logging.warning(message)
    send_email_alert(message)

def send_email_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'System Monitor Alert'
    msg['From']  = SENDER
    msg['To'] = RECEIVER

    try:
        with smtplib.SMTP('smtp.gmail.com', SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, RECEIVER, msg.as_string())
            logging.info("Alert email sent successfully")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def main():
    metrics = {
            "timestamp":
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cpu_usage": check_cpu(),
            "memory_usage": check_memory(),
            "disk_usage": check_disk()
            }
    logging.info(f"Metrics: {metrics}")

if __name__ == "__main__":
    main()
