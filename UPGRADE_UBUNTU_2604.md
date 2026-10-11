# Upgrade de arrakis a Ubuntu 26.04.1 LTS — impacto en `rtsp_snapshot`

Fecha: 2026-10-10/11. Documento general: `/opt/servicios_locales/upgrade_2604/README.md`.

## Qué cambió

Ubuntu 26.04 sustituye Python 3.12 por **Python 3.14** (`python3.12` ya no existe). El venv de este
proyecto apuntaba a `/usr/bin/python3.12` y dejó de funcionar con el upgrade. **No hubo cambios de código.**

## Venv reconstruido

| | |
|---|---|
| Ruta | `/opt/rtsp_snapshot/.venv` (misma ruta, mismo dueño y permisos) |
| Python | 3.12.3 -> **3.14** |
| Paquetes instalados | 12 |
| Versiones distintas al manifiesto 3.12 | ninguno: todas las versiones idénticas al manifiesto |
| Venv anterior (se conserva unos días) | `/opt/rtsp_snapshot/.venv.py312` |
| Manifiesto previo | `/opt/servicios_locales/upgrade_2604/manifests/venvs/opt_rtsp_snapshot_.venv.req` |
| Log | `/opt/servicios_locales/upgrade_2604/venv_logs/opt_rtsp_snapshot_.venv.log` |
| Script | `/opt/servicios_locales/upgrade_2604/rebuild_venv.sh` |

## Uso del venv

`rtsp-snapshot.service` (actualmente `disabled`).

## Verificación

Venv reconstruido (numpy/opencv con wheels 3.14); no se ejecutó.

## Rehacer el venv desde cero

```bash
/opt/servicios_locales/upgrade_2604/rebuild_venv.sh /opt/rtsp_snapshot/.venv \
  /opt/servicios_locales/upgrade_2604/manifests/venvs/opt_rtsp_snapshot_.venv.req
```
