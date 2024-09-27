#!/bin/bash


cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')

mem_usage=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')

disk_usage=$(df -h | awk '$NF=="/"{printf "%s", $5}')

echo "$(date +"%Y-%m-%d %H:%M:%S"), CPU: $cpu_usage%, RAM: $mem_usage%, Disk: $disk_usage" >> /var/log/sys_monitor.log
