## Herramienta de conversión LibreOffice a WPS

Este repositorio incluye una herramienta gráfica en PyQt6 para regenerar los diccionarios cuando actualices el submódulo de LibreOffice:

```
tools/wps_libreoffice_dict_converter.py
```

La herramienta toma diccionarios desde:

```
third-party/libreoffice-dictionaries-collection/dicts
```

y genera el formato de WPS en:

```
build/wps-libreoffice-dicts
```

### Instalar PyQt6

En Debian, Ubuntu, Linux Mint o similares:

```bash
sudo apt install python3-pyqt6
```

Si prefieres usar `pip`:

```bash
python3 -m pip install PyQt6
```

### Ejecutar la herramienta

Desde la raíz del repositorio:

```bash
python3 tools/wps_libreoffice_dict_converter.py
```

La ventana muestra:

- A la izquierda: los archivos y carpetas fuente de LibreOffice.
- A la derecha: los destinos que se crearán o actualizarán en `build/wps-libreoffice-dicts`.
- Abajo: errores bloqueantes, advertencias y resumen del análisis.

Primero pulsa **Analyze**. Si no hay errores bloqueantes, el botón **Convert** queda habilitado.

La herramienta verifica antes de escribir:

- Que existan los pares `.aff` y `.dic`.
- Que cada destino tenga o pueda generar `dict.conf`.
- Que los nombres especiales estén mapeados correctamente, por ejemplo `de_DE_frami`, `fr`, `ca`, `lt`.
- Que los respaldos antiguos de WPS estén disponibles para idiomas sin equivalente en LibreOffice.
- Que no haya diccionarios nuevos de LibreOffice sin revisar.

Al convertir, también actualiza:

```
build/wps-libreoffice-dicts/BUILD_SOURCE_MAP.txt
```

Ese archivo indica de dónde salió cada diccionario.
