# WPS Office 12.x language packs for Linux

## Descarga WPS Office 12 Linux versión China

Descarga el instalador de WPS Office para tu distribucion Linux basada en paqueteía deb o RPM.

Sitio oficial de la página china:

- [https://www.wps.cn](https://www.wps.cn)

allí al dar clic, redirije a:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Luego instala el paquete.

### Instalar deb con gestor de instalacion de paquetes deb

Instalación con algún gestor de paquetes deb, das clic derecho en el administrador de archivos:

![](vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

### Instalar desde la terminal (Opcional)

Si usas Debian, Ubuntu, Linux Mint o similares si desea lo puede hacer también desde la terminal:

```bash
sudo dpkg -i wps-office*.deb
```

Si usas Fedora, Red Hat o similares:

```bash
sudo dnf install wps-office*.rpm
```

## Requisitos

Para continuar con este tutorial necesitas

- Tener **WPS Office 12.x** instalado en Linux según se describe arriba.
- Tener permisos de administrador con `sudo`.
- Haber abierto WPS Office al menos una vez.
- Tener este repositorio descargado o clonado en tu computadora.
- WPS Office crea su configuración de usuario después de abrirlo por primera vez. Si no existe este archivo `~/.config/Kingsoft/Office.conf` abre WPS Office, ciérralo y continúa con la instalación.

## Descargar o clonar este repositorio

Para instalar las MUI (Interfaz de usuario multilingüe), primero necesitas tener este proyecto en tu equipo. A continuación dos maneras de hacerlo, elija sólo una de ellas:

### Opción 1: descargar el ZIP e instalar las MUI

1. Abre esta página:

   [https://github.com/wachin/wps-office-12-language-packs](https://github.com/wachin/wps-office-12-language-packs)

2. Haz clic en el botón verde:

```
<> Code
```

3. Haz clic en:

```
Download ZIP
```

4. Cuando termine la descarga, descomprime el archivo ZIP con clic dereho "Extraer aquí"
5. Abre una terminal allí y ejecuta:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
```

con este comando quedarán instaladas las MUI (Interfaz de usuario multilingüe)

### Opción 2: clonar con Git e instalar las MUI

Si no tienes `git` instalado, instálalo:

```bash
sudo apt install git
```

Luego clona el repositorio:

```bash
git clone https://github.com/wachin/wps-office-12-language-packs
```

Entra a la carpeta:

```bash
cd wps-office-12-language-packs
```

ejecuta:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
```

con este comando quedarán instaladas las MUI (Interfaz de usuario multilingüe)

## Verificar la instalación

Ese comando copia las carpetas de idioma disponibles en `sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/` a la carpeta real de WPS Office en Linux. En `/opt/kingsoft/wps-office/office6/mui/` deberías tener, además de los idiomas originales de Linux, carpetas como estas, revisa desde tu administrador de archivos:

```
de_DE
es_ES
es_MX
fr_CA
fr_FR
id_ID
ja_JP
pl_PL
pt_BR
pt_PT
th_TH
tr_TR
zh_HK
```

También se copia:

```
lang_list
```

Es una lista de selección. 


## Diccionarios disponibles

Este repositorio además prepara diccionarios Hunspell para que **WPS Office 12.x** pueda usarlos en Linux.

Los diccionarios listos para instalar están en:

```
build/wps-libreoffice-dicts
```

Cada carpeta de idioma tiene el formato que WPS espera:

```
dict.conf
main.aff
main.dic
```

Los archivos `main.aff` y `main.dic` vienen de la colección de diccionarios de LibreOffice. Los `dict.conf` se reutilizan desde los diccionarios antiguos de WPS Office cuando existen, y se generan para las variantes nuevas.

Actualmente `build/wps-libreoffice-dicts` contiene 71 diccionarios listos para WPS Office. Cada entrada corresponde a una carpeta que puede copiarse directamente a `/opt/kingsoft/wps-office/office6/dicts/spellcheck/`.

| Código  |           Diccionario            |
| ------- | -------------------------------- |
| `af_ZA` | African (South Africa)           |
| `be_BY` | Belarusian (Belarus)             |
| `bg_BG` | Bulgarian (Bulgaria)             |
| `bn_BD` | Bengali (Bangladesh)             |
| `bs_BA` | Bosnian (Bosnia and Herzegovina) |
| `ca_ES` | Catalan (Catalonia)              |
| `cs_CZ` | Czech (Czech)                    |
| `da_DK` | Danish (Denmark)                 |
| `de_AT` | German (Austria)                 |
| `de_CH` | German (Switzerland)             |
| `de_DE` | German (Germany)                 |
| `el_GR` | Greek (Greece)                   |
| `en_AU` | English (Australia)              |
| `en_CA` | English (Canada)                 |
| `en_GB` | English (United Kingdom)         |
| `en_US` | English (United States)          |
| `en_ZA` | English (South Africa)           |
| `es_AR` | Spanish (Argentina)              |
| `es_BO` | Spanish (Bolivia)                |
| `es_CL` | Spanish (Chile)                  |
| `es_CO` | Spanish (Colombia)               |
| `es_CR` | Spanish (Costa Rica)             |
| `es_CU` | Spanish (Cuba)                   |
| `es_DO` | Spanish (Dominican Republic)     |
| `es_EC` | Spanish (Ecuador)                |
| `es_ES` | Spanish (Spain)                  |
| `es_GQ` | Spanish (Equatorial Guinea)      |
| `es_GT` | Spanish (Guatemala)              |
| `es_HN` | Spanish (Honduras)               |
| `es_MX` | Spanish (Mexico)                 |
| `es_NI` | Spanish (Nicaragua)              |
| `es_PA` | Spanish (Panama)                 |
| `es_PE` | Spanish (Peru)                   |
| `es_PH` | Spanish (Philippines)            |
| `es_PR` | Spanish (Puerto Rico)            |
| `es_PY` | Spanish (Paraguay)               |
| `es_SV` | Spanish (El Salvador)            |
| `es_US` | Spanish (United States)          |
| `es_UY` | Spanish (Uruguay)                |
| `es_VE` | Spanish (Venezuela)              |
| `fr_FR` | French (France)                  |
| `gd_GB` | Scots Gaelic (Great Britain)     |
| `gl`    | Galician (strict Volga)          |
| `gu_IN` | Gujarati (India)                 |
| `hi_IN` | Hindi (India)                    |
| `hr_HR` | Croatian (Croatia)               |
| `hu_HU` | Hungarian (Hungary)              |
| `id_ID` | Indonesian                       |
| `is`    | Icelandic                        |
| `it_IT` | Italian (Italy)                  |
| `km_KH` | Khmer (Cambodia)                 |
| `lt_LT` | Lithuanian (Lithuania)           |
| `ms_MY` | Malay (Malaysia)                 |
| `nb_NO` | Norwegian (Norway)               |
| `ne_NP` | Nepali (Nepal)                   |
| `nl_NL` | Dutch                            |
| `pl_PL` | Polish                           |
| `pt_BR` | Portuguese (Brazil)              |
| `pt_PT` | Portuguese                       |
| `qu_EC` | Kichwa (Ecuador)                 |
| `ro_RO` | Romanian (Romania)               |
| `ru_RU` | Russian (Russia)                 |
| `sk_SK` | Slovak (Slovakia)                |
| `sl_SI` | Slovenian (Slovenia)             |
| `sq_AL` | Albanian (Albania)               |
| `sr`    | Serbio                           |
| `sv_SE` | Swedish (Sweden)                 |
| `sw_TZ` | Swahili (Tanzania)               |
| `tr_TR` | Turkish (Turkey)                 |
| `uk_UA` | Ukrainian (Ukraine)              |
| `vi_VN` | Vietnamese (Vietnam)             |

### Diccionarios añadidos desde otras fuentes

Además de los diccionarios convertidos desde LibreOffice y los heredados de WPS Office, este paquete incluye los siguientes diccionarios añadidos manualmente desde otras fuentes:

| Código  |    Diccionario     |                              Nota                              |
| ------- | ------------------ | -------------------------------------------------------------- |
| `hr_HR` | Croatian (Croatia) | Añadido desde otra fuente y empaquetado con el formato de WPS. |
| `km_KH` | Khmer (Cambodia)   | Añadido desde otra fuente y empaquetado con el formato de WPS. |
| `qu_EC` | Kichwa (Ecuador)   | Añadido desde otra fuente y empaquetado con el formato de WPS. |

Los tres usan el mismo formato final que los demás diccionarios: `dict.conf`, `main.aff` y `main.dic`. Sus `dict.conf` también incluyen nombres localizados para que WPS pueda mostrarlos mejor en distintos idiomas de interfaz.

## Instalar los diccionarios

Desde la raíz de este repositorio, ejecuta:

```bash
sudo cp -r build/wps-libreoffice-dicts/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Esto copia todos los diccionarios convertidos a la carpeta que WPS usa para la corrección ortográfica.

Después de copiar, la ruta de WPS debe quedar con carpetas como estas:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_MX/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_EC/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

Y dentro de cada una:

```
dict.conf
main.aff
main.dic
```

## Activar un idioma de la interfaz en la configuración de WPS

Si eres un desarrollador edita el archivo de configuración con nano:

```bash
nano ~/.config/Kingsoft/Office.conf
```

Si eres un usuario normal usa Gedit u otro editor de texto. Para Gedit sino lo tienes instalado instalalo así:

```bash
sudo apt install gedit
```

y pon en la terminal:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Una vez abierto ese archivo selecciona todo el texto que haya allí con `Ctrl + A`, bórralo, y coloca en su lugar el contenido correspondiente al idioma que quieres usar.

La estructura siempre es la misma:

```
[General]
languages=CODIGO_DEL_IDIOMA

[6.0]
common\DefaultLanguage=NUMERO_IDIOMA
common\Local\UILanguage=NUMERO_IDIOMA
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Usa esta tabla para elegir el código y el número correcto:

|             Idioma               | `languages=` | `DefaultLanguage` y `UILanguage` |
| -------------------------------- | ------------ | -------------------------------- |
| English (United States)          | `en_US`      | `1033`                           |
| German (Germany)                 | `de_DE`      | `1031`                           |
| Spanish (Spain)                  | `es_ES`      | `3082`                           |
| Spanish (Mexico)                 | `es_MX`      | `2058`                           |
| French (Canada)                  | `fr_CA`      | `3084`                           |
| French (France)                  | `fr_FR`      | `1036`                           |
| Indonesian                       | `id_ID`      | `1057`                           |
| Japanese                         | `ja_JP`      | `1041`                           |
| Polish                           | `pl_PL`      | `1045`                           |
| Portuguese (Brazil)              | `pt_BR`      | `1046`                           |
| Portuguese (Portugal)            | `pt_PT`      | `2070`                           |
| Russian                          | `ru_RU`      | `1049`                           |
| Thai                             | `th_TH`      | `1054`                           |
| Turkish                          | `tr_TR`      | `1055`                           |
| Chinese (Simplified, China)      | `zh_CN`      | `2052`                           |
| Chinese (Traditional, Hong Kong) | `zh_HK`      | `3076`                           |

### Para inglés de Estados Unidos:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para el Español de España:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para el Alemán de Alemania:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


### Para español de México:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para francés de Canadá:

```
[General]
languages=fr_CA

[6.0]
common\DefaultLanguage=3084
common\Local\UILanguage=3084
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para francés de Francia:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para indonesio:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para japonés:

```
[General]
languages=ja_JP

[6.0]
common\DefaultLanguage=1041
common\Local\UILanguage=1041
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para polaco:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para portugués de Brasil:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para portugués de Portugal:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para ruso:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para tailandés:

```
[General]
languages=th_TH

[6.0]
common\DefaultLanguage=1054
common\Local\UILanguage=1054
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para turco:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para chino simplificado de China:

```
[General]
languages=zh_CN

[6.0]
common\DefaultLanguage=2052
common\Local\UILanguage=2052
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para chino tradicional de Hong Kong:

```
[General]
languages=zh_HK

[6.0]
common\DefaultLanguage=3076
common\Local\UILanguage=3076
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


Guarda el archivo, cierra WPS Office por completo y vuelve a abrirlo. Si el idioma quedó bien configurado, la interfaz abrirá en el idioma elegido.

## Activar la corrección ortográfica

Después de instalar los diccionarios:

1. Abre WPS Writer.
2. Ve en la cinta a la que tiene el nombre "Revisar" y allí da clic en el selector "▼" que está a la derecha en "Revisión ortográfica" y da clic en "Establecer idioma".
3. Selecciona el idioma deseado, por ejemplo `Español (España)`, `Español (Ecuado)` u otro.
4. Da clic en "Establecer como predeterminado" y prueba escribiendo una palabra con error.

Si el idioma aparece en la lista, WPS está leyendo correctamente la carpeta instalada.


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

## Referencia: idiomas descargados por WPS en Windows

En Windows, WPS Office descarga paquetes de idioma en rutas de usuario. Esta información sirve como referencia para investigar archivos de idioma de la interfaz.

Primero descarga e instala WPS Office 12 para Windows:

[https://wps.com/office/windows/](https://wps.com/office/windows/)

Ejemplo en Windows 10:

![](vx_images/02-WPS-Office-global-config-menu.png)

Luego descarga los idiomas:

![](vx_images/03-Click-on-a-language-and-then-click-Apply.png)

Los idiomas descargados pueden aparecer en:

```
C:\Users\youruser\AppData\Roaming\kingsoft\wps_intl\addons\pool\win-x64
```

![](vx_images/04-downloaded-languages.png)

La lista de idiomas puede aparecer en:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui\lang_list\lang_list.json
```

![20260416-000808](vx_images/507184629680596.png)

Algunos paquetes incluidos por la versión de Windows en español pueden aparecer en:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui
```

![](vx_images/05-languages-downloaded-by-the-Spanish-version.png)

Si este proyecto te ayudó, puedes dejar una estrella en el repositorio.
