
# Sistema de Monitoreo de Recursos del Sistema (Bash y Python) 

## Visión General

Este proyecto es una herramienta sencilla y efectiva para monitorear el uso de recursos del sistema (CPU, RAM, Disco) en servidores o estaciones de trabajo. Incluye un script en Bash para recopilar datos y otro en Python para generar informes visuales.

## Características

- **Monitorización periódica**: Registra el uso de CPU, RAM y Disco en intervalos definidos.
- **Generación de informes**: Crea gráficos que muestran las tendencias de uso a lo largo del tiempo.
- **Configuración flexible**: Fácil de configurar para monitorear en intervalos específicos.
- **Uso de Cron**: Automatiza la ejecución del script de monitoreo usando cron.

## Requisitos

- **Sistema operativo**: Linux o macOS
- **Dependencias de Python**: `matplotlib`, `pandas`
  
  ```bash
  pip install matplotlib pandas
  ```

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/franjimenxz/System-monitor.git
   cd System-monitor
   ```

2. **Hacer ejecutable el script de monitoreo**:
   ```bash
   chmod +x monitor.sh
   ```

## Uso

1. **Ejecutar el Script de Monitoreo**:
   ```bash
   ./monitor.sh
   ```

   El script registrará el uso de CPU, RAM y Disco en el archivo `/var/log/sys_monitor.log`.

2. **Generar un Informe Gráfico**:
   ```bash
   python3 generate_report.py
   ```

   Este comando generará un gráfico llamado `system_usage_report.png` que mostrará las tendencias de uso de los recursos.

3. **Automatización con Cron**:
   Para ejecutar el script de monitoreo automáticamente cada 5 minutos, añade la siguiente línea a tu crontab:
   
   ```bash
   */5 * * * * /ruta/al/script/monitor.sh
   ```

## Ejemplo de Salida del Log

```
2024-09-27 14:00:01, CPU: 12.5%, RAM: 45.32%, Disk: 30%
2024-09-27 14:05:01, CPU: 18.7%, RAM: 47.21%, Disk: 30%
2024-09-27 14:10:01, CPU: 20.1%, RAM: 48.33%, Disk: 30%
2024-09-27 14:15:01, CPU: 15.9%, RAM: 46.87%, Disk: 31%
2024-09-27 14:20:01, CPU: 25.3%, RAM: 49.05%, Disk: 31%
```

## Ejemplo de Salida del Informe

Una vez que ejecutes `generate_report.py`, se generará un archivo de imagen que visualizará las métricas de uso de recursos del sistema a lo largo del tiempo. 

---

# System Resource Monitor (Bash and Python) (EN)

## Overview

This project is a simple and effective tool for monitoring system resource usage (CPU, RAM, Disk) on servers or workstations. It includes a Bash script for data collection and a Python script for generating visual reports.

## Features

- **Periodic Monitoring**: Logs CPU, RAM, and Disk usage at defined intervals.
- **Report Generation**: Creates graphs showing usage trends over time.
- **Flexible Configuration**: Easy to configure for specific monitoring intervals.
- **Cron Usage**: Automates script execution using cron.

## Requirements

- **Operating System**: Linux or macOS
- **Python Dependencies**: `matplotlib`, `pandas`

  ```bash
  pip install matplotlib pandas
  ```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/franjimenxz/System-monitor.git
   cd System-monitor
   ```

2. **Make the Monitoring Script Executable**:
   ```bash
   chmod +x monitor.sh
   ```

## Usage

1. **Run the Monitoring Script**:
   ```bash
   ./monitor.sh
   ```

   The script will log CPU, RAM, and Disk usage to the file `/var/log/sys_monitor.log`.

2. **Generate a Report**:
   ```bash
   python3 generate_report.py
   ```

   This command will generate a graph called `system_usage_report.png` showing the resource usage trends.

3. **Automation with Cron**:
   To automatically run the monitoring script every 5 minutes, add the following line to your crontab:
   
   ```bash
   */5 * * * * /path/to/script/monitor.sh
   ```

## Example Log Output

```
2024-09-27 14:00:01, CPU: 12.5%, RAM: 45.32%, Disk: 30%
2024-09-27 14:05:01, CPU: 18.7%, RAM: 47.21%, Disk: 30%
2024-09-27 14:10:01, CPU: 20.1%, RAM: 48.33%, Disk: 30%
2024-09-27 14:15:01, CPU: 15.9%, RAM: 46.87%, Disk: 31%
2024-09-27 14:20:01, CPU: 25.3%, RAM: 49.05%, Disk: 31%
```

## Example Report Output

After running `generate_report.py`, a PNG image file will be created that visualizes system resource usage metrics over time.
