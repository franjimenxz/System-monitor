
# Sistema de Monitoreo de Recursos del Sistema

Este proyecto es una herramienta sencilla diseñada para ayudar a los administradores de sistemas a monitorear el uso de los recursos del sistema (CPU, RAM, Disco). Incluye un script en Bash para recopilar y registrar estas métricas, y un script en Python para generar gráficos a partir de los datos recogidos.

## Archivos

- **`monitor.sh`**: Este es el script principal en Bash. Su función es capturar el uso actual de CPU, RAM y Disco en el sistema y registrar estos datos en un archivo de log. Este archivo de log es donde podrás revisar el estado de los recursos del sistema en diferentes momentos del tiempo.

- **`generate_report.py`**: Este script en Python toma los datos que ha recopilado el script de monitoreo y genera un gráfico que muestra cómo han variado los recursos del sistema a lo largo del tiempo. Es perfecto para una visión más visual y fácil de entender.

- **`crontab_example.txt`**: Aquí te damos un ejemplo de cómo puedes configurar una tarea programada (`cron`) para que el script de monitoreo se ejecute automáticamente cada 5 minutos, sin que tengas que preocuparte por ejecutarlo manualmente.

## ¿Cómo Usar Este Proyecto?

### Paso 1: Ejecutar el Script de Monitoreo

Primero, asegúrate de que el script `monitor.sh` tenga permisos de ejecución:

\`\`\`bash
chmod +x monitor.sh
\`\`\`

Luego, puedes ejecutarlo manualmente para comenzar a recopilar datos:

\`\`\`bash
./monitor.sh
\`\`\`

Cada vez que ejecutes este script, se agregará una nueva línea en el archivo de log (`/var/log/sys_monitor.log`) con la fecha, la hora, y los porcentajes de uso de CPU, RAM y Disco.

#### Ejemplo de Salida en el Log:

Después de ejecutar `monitor.sh` varias veces, el archivo de log podría verse así:

\`\`\`plaintext
2024-09-27 14:00:01, CPU: 12.5%, RAM: 45.32%, Disk: 30%
2024-09-27 14:05:01, CPU: 18.7%, RAM: 47.21%, Disk: 30%
2024-09-27 14:10:01, CPU: 20.1%, RAM: 48.33%, Disk: 30%
2024-09-27 14:15:01, CPU: 15.9%, RAM: 46.87%, Disk: 31%
2024-09-27 14:20:01, CPU: 25.3%, RAM: 49.05%, Disk: 31%
\`\`\`


### Paso 2: Generar un Informe Gráfico

Una vez que hayas recopilado suficientes datos, puedes generar un gráfico para visualizar cómo han variado los recursos del sistema:

\`\`\`bash
python3 generate_report.py
\`\`\`

Este comando creará un archivo llamado `system_usage_report.png`, que mostrará un gráfico con las siguientes líneas:

- **CPU Usage (%)**: El porcentaje de uso de CPU a lo largo del tiempo.
- **RAM Usage (%)**: El porcentaje de uso de RAM a lo largo del tiempo.
- **Disk Usage (%)**: El porcentaje de uso de Disco a lo largo del tiempo.

### Dependencias

Para que todo funcione, necesitarás tener instalados los siguientes paquetes de Python:

- **`matplotlib`**: Para generar gráficos. Puedes instalarlo con `pip`:
  \`\`\`bash
  pip install matplotlib
  \`\`\`

- **`pandas`**: Para manejar los datos en formato tabular. Puedes instalarlo con `pip`:
  \`\`\`bash
  pip install pandas
  \`\`\`

## Resumen

Este proyecto es una solución simple y efectiva para monitorear los recursos del sistema. Es ideal si necesitas una forma rápida y fácil de saber cómo está funcionando tu servidor o computadora a lo largo del tiempo. ¡Esperamos que te sea útil!
