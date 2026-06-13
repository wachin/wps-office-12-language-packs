# ROADMAP

Este archivo resume el estado actual del proyecto y separa lo que ya se completó de lo que todavía falta por hacer.

## Diccionarios WPS

- [x] Identificar el formato de diccionario que usa WPS Office: `dict.conf`, `main.aff` y `main.dic`.
- [x] Confirmar que `dict.conf` puede reutilizarse desde los diccionarios antiguos de WPS Office.
- [x] Confirmar que los archivos `.aff` y `.dic` de LibreOffice pueden renombrarse a `main.aff` y `main.dic` para WPS.
- [x] Crear la carpeta de salida `build/wps-libreoffice-dicts`.
- [x] Generar una colección funcional de diccionarios WPS en `build/wps-libreoffice-dicts`.
- [x] Incluir 71 carpetas de idiomas listas para instalar.
- [x] Mantener los casos especiales de nombres de LibreOffice, por ejemplo `de_DE_frami`, `fr`, `ca`, `gl_ES`, `lt`.
- [x] Mantener respaldo desde WPS antiguo para idiomas sin equivalente claro en LibreOffice.
- [x] Documentar el origen de cada diccionario en `build/wps-libreoffice-dicts/BUILD_SOURCE_MAP.txt`.
- [ ] Verificar en WPS Linux, idioma por idioma, que todos los 71 diccionarios aparezcan correctamente en la interfaz.
- [ ] Probar si algunos diccionarios requieren ajustes adicionales por compatibilidad Hunspell específica de WPS.

## Cobertura de idiomas

- [x] Convertir las variantes principales disponibles en los submódulos de LibreOffice y WPS antiguo.
- [x] Añadir nuevas carpetas de idioma que no existían en el paquete WPS antiguo, por ejemplo `de_AT`, `de_CH`, `en_CA`, `en_ZA` y varias variantes de `es_*`.
- [x] Añadir manualmente los diccionarios `hr_HR`, `km_KH` y `qu_EC` desde otras fuentes.
- [x] Enriquecer los `dict.conf` nuevos con nombres localizados adicionales: `zh_CN`, `en_US`, `es_ES`, `zh_TW`, `zh_HK`, `zh_MO`, `zh_Hant_CN`.
- [x] Enriquecer también los `dict.conf` manuales de `hr_HR`, `km_KH` y `qu_EC`.
- [ ] Revisar si faltan más idiomas útiles en LibreOffice que todavía no estén empaquetados en `build/wps-libreoffice-dicts`.
- [ ] Revisar si conviene añadir más diccionarios manuales desde otras fuentes externas.
- [ ] Corregir nombres dudosos heredados en la documentación, por ejemplo descripciones que parezcan mal traducidas o inconsistentes.

## Herramienta de conversión

- [x] Crear la herramienta gráfica PyQt6 `tools/wps_libreoffice_dict_converter.py`.
- [x] Hacer que la herramienta lea los diccionarios desde `third-party/libreoffice-dictionaries-collection/dicts`.
- [x] Hacer que la herramienta genere la salida WPS en `build/wps-libreoffice-dicts`.
- [x] Implementar análisis previo antes de convertir.
- [x] Mostrar en la interfaz las fuentes de LibreOffice y los destinos WPS en dos paneles.
- [x] Bloquear la conversión cuando existan errores previos.
- [x] Soportar mapeos especiales y respaldos desde WPS antiguo.
- [x] Hacer que la herramienta regenere `BUILD_SOURCE_MAP.txt`.
- [x] Hacer que la herramienta respete `dict.conf` ya existentes en `build`.
- [x] Hacer que la herramienta genere `dict.conf` enriquecidos para los idiomas nuevos.
- [ ] Añadir una vista más detallada de diferencias por archivo antes de convertir.
- [ ] Añadir exportación de reporte desde la interfaz.
- [ ] Añadir un resumen visual separado para errores bloqueantes, advertencias y casos manuales.
- [ ] Probar la herramienta abriendo la GUI de forma interactiva en el entorno real de escritorio.

## Documentación

- [x] Actualizar `README.md` para que la instalación de diccionarios use `build/wps-libreoffice-dicts`.
- [x] Documentar el contenido disponible de diccionarios en una tabla dentro del README.
- [x] Documentar por separado los tres diccionarios añadidos desde otras fuentes.
- [x] Documentar cómo usar la herramienta PyQt6.
- [x] Crear `.gitignore` para cachés, temporales y salidas no deseadas.
- [ ] Añadir una sección de validación real en Linux con capturas o pasos comprobados en WPS.
- [ ] Documentar mejor los idiomas que usan fallback desde WPS antiguo.
- [ ] Documentar una política clara para añadir diccionarios externos no provenientes de LibreOffice.

## MUI de Windows para Linux

- [x] Identificar que la versión Windows contiene más idiomas MUI que la versión Linux.
- [x] Identificar las rutas Windows relevantes para `mui` y para paquetes `klang*`.
- [x] Confirmar que los paquetes `klang*` contienen una carpeta principal de idioma, por ejemplo `es_ES`.
- [x] Identificar que los paquetes `klang*` también contienen una carpeta `addons`.
- [x] Verificar que la instalación Linux tiene `/opt/kingsoft/wps-office/office6/addons`.
- [x] Verificar que muchos addons de Windows coinciden por nombre con addons existentes en Linux.
- [x] Concluir que la carpeta `addons` no debe descartarse todavía porque puede servir para traducir módulos secundarios.
- [ ] Diseñar una estructura de salida para empaquetar MUI principales de Windows adaptados a Linux.
- [ ] Diseñar una estructura separada para empaquetar traducciones de `addons` compatibles con Linux.
- [ ] Determinar exactamente qué archivos MUI principales de Windows funcionan sin cambios en Linux.
- [ ] Determinar exactamente qué archivos de `addons` funcionan sin cambios en Linux.
- [ ] Identificar qué partes son específicas de Windows y deben excluirse del proyecto.
- [ ] Crear un procedimiento reproducible para copiar MUI de Windows a una estructura instalable en Linux.
- [ ] Probar al menos un idioma nuevo de Windows en WPS Linux y documentar el resultado.
- [ ] Crear una herramienta o script para automatizar el filtrado de `addons` compatibles.

## Validación del proyecto

- [x] Confirmar que cada carpeta de `build/wps-libreoffice-dicts` contiene `dict.conf`, `main.aff` y `main.dic`.
- [x] Verificar que el script Python compila con `python3 -m py_compile`.
- [ ] Ejecutar pruebas funcionales completas dentro de WPS Office Linux con varios idiomas reales.
- [ ] Validar que el README refleje exactamente el flujo final del proyecto cuando la parte MUI esté lista.
- [ ] Definir una versión inicial publicable del proyecto cuando estén cubiertos diccionarios y MUI.

