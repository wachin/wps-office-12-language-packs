# WPS Office 12.x language packs for Linux

Este repositorio prepara diccionarios Hunspell para que **WPS Office 12.x** pueda usarlos en Linux.

Los diccionarios listos para instalar están en:

```text
build/wps-libreoffice-dicts
```

Cada carpeta de idioma tiene el formato que WPS espera:

```text
dict.conf
main.aff
main.dic
```

Los archivos `main.aff` y `main.dic` vienen de la colección de diccionarios de LibreOffice. Los `dict.conf` se reutilizan desde los diccionarios antiguos de WPS Office cuando existen, y se generan para las variantes nuevas.

## Diccionarios disponibles

Actualmente `build/wps-libreoffice-dicts` contiene 71 diccionarios listos para WPS Office. Cada entrada corresponde a una carpeta que puede copiarse directamente a `/opt/kingsoft/wps-office/office6/dicts/spellcheck/`.

| Código | Diccionario |
| ------ | ----------- |
| `af_ZA` | African (South Africa) |
| `be_BY` | Belarusian (Belarus) |
| `bg_BG` | Bulgarian (Bulgaria) |
| `bn_BD` | Bengali (Bangladesh) |
| `bs_BA` | Bosnian (Bosnia and Herzegovina) |
| `ca_ES` | Catalan (Catalonia) |
| `cs_CZ` | Czech (Czech) |
| `da_DK` | Danish (Denmark) |
| `de_AT` | German (Austria) |
| `de_CH` | German (Switzerland) |
| `de_DE` | German (Germany) |
| `el_GR` | Greek (Greece) |
| `en_AU` | English (Australia) |
| `en_CA` | English (Canada) |
| `en_GB` | English (United Kingdom) |
| `en_US` | English (United States) |
| `en_ZA` | English (South Africa) |
| `es_AR` | Spanish (Argentina) |
| `es_BO` | Spanish (Bolivia) |
| `es_CL` | Spanish (Chile) |
| `es_CO` | Spanish (Colombia) |
| `es_CR` | Spanish (Costa Rica) |
| `es_CU` | Spanish (Cuba) |
| `es_DO` | Spanish (Dominican Republic) |
| `es_EC` | Spanish (Ecuador) |
| `es_ES` | Spanish (Spain) |
| `es_GQ` | Spanish (Equatorial Guinea) |
| `es_GT` | Spanish (Guatemala) |
| `es_HN` | Spanish (Honduras) |
| `es_MX` | Spanish (Mexico) |
| `es_NI` | Spanish (Nicaragua) |
| `es_PA` | Spanish (Panama) |
| `es_PE` | Spanish (Peru) |
| `es_PH` | Spanish (Philippines) |
| `es_PR` | Spanish (Puerto Rico) |
| `es_PY` | Spanish (Paraguay) |
| `es_SV` | Spanish (El Salvador) |
| `es_US` | Spanish (United States) |
| `es_UY` | Spanish (Uruguay) |
| `es_VE` | Spanish (Venezuela) |
| `fr_FR` | French (France) |
| `gd_GB` | Scots Gaelic (Great Britain) |
| `gl` | Galician (strict Volga) |
| `gu_IN` | Gujarati (India) |
| `hi_IN` | Hindi (India) |
| `hr_HR` | Croatian (Croatia) |
| `hu_HU` | Hungarian (Hungary) |
| `id_ID` | Indonesian |
| `is` | Icelandic |
| `it_IT` | Italian (Italy) |
| `km_KH` | Khmer (Cambodia) |
| `lt_LT` | Lithuanian (Lithuania) |
| `ms_MY` | Malay (Malaysia) |
| `nb_NO` | Norwegian (Norway) |
| `ne_NP` | Nepali (Nepal) |
| `nl_NL` | Dutch |
| `pl_PL` | Polish |
| `pt_BR` | Portuguese (Brazil) |
| `pt_PT` | Portuguese |
| `qu_EC` | Kichwa (Ecuador) |
| `ro_RO` | Romanian (Romania) |
| `ru_RU` | Russian (Russia) |
| `sk_SK` | Slovak (Slovakia) |
| `sl_SI` | Slovenian (Slovenia) |
| `sq_AL` | Albanian (Albania) |
| `sr` | Serbio |
| `sv_SE` | Swedish (Sweden) |
| `sw_TZ` | Swahili (Tanzania) |
| `tr_TR` | Turkish (Turkey) |
| `uk_UA` | Ukrainian (Ukraine) |
| `vi_VN` | Vietnamese (Vietnam) |

### Diccionarios añadidos desde otras fuentes

Además de los diccionarios convertidos desde LibreOffice y los heredados de WPS Office, este paquete incluye estos diccionarios añadidos manualmente desde otras fuentes:

| Código | Diccionario | Nota |
| ------ | ----------- | ---- |
| `hr_HR` | Croatian (Croatia) | Añadido desde otra fuente y empaquetado con el formato de WPS. |
| `km_KH` | Khmer (Cambodia) | Añadido desde otra fuente y empaquetado con el formato de WPS. |
| `qu_EC` | Kichwa (Ecuador) | Añadido desde otra fuente y empaquetado con el formato de WPS. |

Los tres usan el mismo formato final que los demás diccionarios: `dict.conf`, `main.aff` y `main.dic`. Sus `dict.conf` también incluyen nombres localizados para que WPS pueda mostrarlos mejor en distintos idiomas de interfaz.

## Requisitos

- Tener **WPS Office 12.x** instalado en Linux.
- Tener permisos de administrador con `sudo`.
- Haber abierto WPS Office al menos una vez.
- Tener creada la carpeta `build/wps-libreoffice-dicts` con los diccionarios convertidos.

WPS suele crear su configuración de usuario después de abrirlo por primera vez. Si no existe este archivo:

```text
~/.config/Kingsoft/Office.conf
```

abre WPS Office, ciérralo y continúa con la instalación.

## Rutas usadas por WPS Office

En la versión Linux de WPS Office instalada en `/opt`, las rutas principales son:

```text
/opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Ahí WPS guarda los diccionarios de corrección ortográfica.

```text
~/.config/Kingsoft/Office.conf
```

Ahí WPS guarda la configuración del usuario.

## Instalar los diccionarios

Desde la raíz de este repositorio, ejecuta:

```bash
sudo mkdir -p /opt/kingsoft/wps-office/office6/dicts/spellcheck
sudo cp -r build/wps-libreoffice-dicts/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Esto copia todos los diccionarios convertidos a la carpeta que WPS usa para la corrección ortográfica.

Después de copiar, la ruta de WPS debe quedar con carpetas como estas:

```text
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_MX/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_EC/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

Y dentro de cada una:

```text
dict.conf
main.aff
main.dic
```

## Activar español en la configuración de WPS

Edita el archivo de configuración:

```bash
nano ~/.config/Kingsoft/Office.conf
```

También puedes usar otro editor, por ejemplo:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Para usar español de España como idioma principal, puedes dejar este contenido:

```ini
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Para español de México, cambia `languages=es_ES` por:

```ini
languages=es_MX
```

Guarda el archivo, cierra WPS Office por completo y vuelve a abrirlo.

## Activar la corrección ortográfica

Después de instalar los diccionarios:

1. Abre WPS Writer.
2. Ve a las opciones de idioma o corrección ortográfica.
3. Selecciona el idioma deseado, por ejemplo `es_ES`, `es_MX` o `es_EC`.
4. Aplica los cambios y prueba escribiendo una palabra con error.

Si el idioma aparece en la lista, WPS está leyendo correctamente la carpeta instalada.

## Resumen rápido

Desde la raíz del repositorio:

```bash
sudo mkdir -p /opt/kingsoft/wps-office/office6/dicts/spellcheck
sudo cp -r build/wps-libreoffice-dicts/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
nano ~/.config/Kingsoft/Office.conf
```

Contenido recomendado para español de España:

```ini
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

## Si algo no funciona

Revisa estos puntos:

1. WPS Office fue abierto al menos una vez antes de editar `Office.conf`.
2. La carpeta `/opt/kingsoft/wps-office/office6/dicts/spellcheck/` existe.
3. Copiaste el contenido de `build/wps-libreoffice-dicts`, no la carpeta contenedora completa.
4. Cada idioma instalado tiene `dict.conf`, `main.aff` y `main.dic`.
5. Cerraste y volviste a abrir WPS Office después de copiar los diccionarios.
6. El idioma elegido existe en la carpeta de diccionarios instalada.

## Herramienta de conversión LibreOffice a WPS

Este repositorio incluye una herramienta gráfica en PyQt6 para regenerar los diccionarios cuando actualices el submódulo de LibreOffice:

```text
tools/wps_libreoffice_dict_converter.py
```

La herramienta toma diccionarios desde:

```text
third-party/libreoffice-dictionaries-collection/dicts
```

y genera el formato de WPS en:

```text
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

```text
build/wps-libreoffice-dicts/BUILD_SOURCE_MAP.txt
```

Ese archivo indica de dónde salió cada diccionario.

## Referencia: idiomas descargados por WPS en Windows

En Windows, WPS Office descarga paquetes de idioma en rutas de usuario. Esta información sirve como referencia para investigar archivos de idioma de la interfaz.

Primero descarga e instala WPS Office 12 para Windows:

[https://wps.com/office/windows/](https://wps.com/office/windows/)

Ejemplo en Windows 10:

![](vx_images/02-WPS-Office-global-config-menu.png)

Luego descarga los idiomas:

![](vx_images/03-Click-on-a-language-and-then-click-Apply.png)

Los idiomas descargados pueden aparecer en:

```text
C:\Users\youruser\AppData\Roaming\kingsoft\wps_intl\addons\pool\win-x64
```

![](vx_images/04-downloaded-languages.png)

La lista de idiomas puede aparecer en:

```text
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui\lang_list\lang_list.json
```

![20260416-000808](vx_images/507184629680596.png)

Algunos paquetes incluidos por la versión de Windows en español pueden aparecer en:

```text
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui
```

![](vx_images/05-languages-downloaded-by-the-Spanish-version.png)

Si este proyecto te ayudó, puedes dejar una estrella en el repositorio.
