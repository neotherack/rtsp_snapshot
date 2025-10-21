# RTSP Snapshot Service

Servicio Python para capturar imágenes y video stream desde una cámara RTSP.

## Endpoints

- `GET /snapshot` - Captura una imagen fija JPEG
- `GET /video` - Stream de video MJPEG en tiempo real

## URLs

- `http://server-ip:8087/snapshot`
- `http://server-ip:8087/video`

## Configuración RTSP

- Cámara: `192.168.1.12:554`
- Servidor: `192.168.1.2`
- Puerto: `8087`

## Instalación

```bash
# Crear directorio y entorno virtual
sudo mkdir -p /opt/rtsp_snapshot
cd /opt/rtsp_snapshot
sudo python3 -m venv .venv
sudo .venv/bin/pip install flask opencv-python

# Configurar servicio systemd
sudo cp rtsp-snapshot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rtsp-snapshot.service
sudo systemctl start rtsp-snapshot.service

# Servicio Systemd

Archivo: /etc/systemd/system/rtsp-snapshot.service
ini

[Unit]
Description=RTSP Snapshot Service
After=network.target

[Service]
Type=simple
User=octoprint
Group=octoprint
ExecStart=/opt/rtsp_snapshot/.venv/bin/python /opt/rtsp_snapshot/service.py
WorkingDirectory=/opt/rtsp_snapshot
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target

#Uso con OctoPrint

Configurar en OctoPrint:

    URL de snapshot: http://server-ip:8087/snapshot
    URL de stream: http://server-ip:8087/video

# Firewall

El servicio requiere el puerto 8087/tcp abierto:
bash

sudo firewall-cmd --add-service=camara --permanent
sudo firewall-cmd --reload

# Estructura de Archivos
text

/opt/rtsp_snapshot/
├── service.py
├── rtsp-snapshot.service
└── .venv/

#Comandos Útiles
bash

## Ver estado del servicio
sudo systemctl status rtsp-snapshot.service

## Ver logs
sudo journalctl -u rtsp-snapshot.service -f

## Reiniciar servicio
sudo systemctl restart rtsp-snapshot.service
