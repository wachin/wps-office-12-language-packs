# Pruebas rápidas del corrector ortográfico en WPS Office 12

Este archivo contiene pruebas en formato corto para marcar desde el celular.

## Pruebas pendientes recomendadas

Estas pruebas tienen los tres elementos necesarios:

- locale disponible en el Login Manager de MX Linux 23
- MUI instalado en WPS Office 12
- diccionario instalado en WPS Office 12

### Polaco

MX Linux 23 con locale pl_PL

```bash
wachin@mx23:~
$ echo $LANG
pl_PL.UTF-8
```

y WPS Office 12 con MUI pl_PL

```
/opt/kingsoft/wps-office/office6/mui/pl_PL/
```

y corrección ortográfica del idioma polaco

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pl_PL/
```

entonces la corrección ortográfica para palabras mal escritas en Polaco

```
[ ] Funciona
[ ] No funciona
```

### Portugués de Brasil

MX Linux 23 con locale pt_BR

```bash
wachin@mx23:~
$ echo $LANG
pt_BR.UTF-8
```

y WPS Office 12 con MUI pt_BR

```
/opt/kingsoft/wps-office/office6/mui/pt_BR/
```

y corrección ortográfica del idioma portugués de Brasil

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

entonces la corrección ortográfica para palabras mal escritas en Portugués de Brasil

```
[ ] Funciona
[ ] No funciona
```

### Portugués de Portugal

MX Linux 23 con locale pt_PT

```bash
wachin@mx23:~
$ echo $LANG
pt_PT.UTF-8
```

y WPS Office 12 con MUI pt_PT

```
/opt/kingsoft/wps-office/office6/mui/pt_PT/
```

y corrección ortográfica del idioma portugués de Portugal

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/
```

entonces la corrección ortográfica para palabras mal escritas en Portugués de Portugal

```
[ ] Funciona
[x] No funciona
```

Nota de prueba: con el mismo MUI `pt_PT` y locale `pt_PT.UTF-8`, WPS Office 12 sí corrige si se usa el diccionario `pt_BR` en:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

### Ruso

MX Linux 23 con locale ru_RU

```bash
wachin@mx23:~
$ echo $LANG
ru_RU.UTF-8
```

y WPS Office 12 con MUI ru_RU

```
/opt/kingsoft/wps-office/office6/mui/ru_RU/
```

y corrección ortográfica del idioma ruso

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

entonces la corrección ortográfica para palabras mal escritas en Ruso

```
[x] Funciona
[ ] No funciona
```

### Turco

MX Linux 23 con locale tr_TR

```bash
wachin@mx23:~
$ echo $LANG
tr_TR.UTF-8
```

y WPS Office 12 con MUI tr_TR

```
/opt/kingsoft/wps-office/office6/mui/tr_TR/
```

y corrección ortográfica del idioma turco

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/tr_TR/
```

entonces la corrección ortográfica para palabras mal escritas en Turco

```
[ ] Funciona
[ ] No funciona
```

## Pruebas especiales

Estas pruebas sirven para confirmar si WPS acepta un diccionario principal desde una variante regional.

### Alemán de Austria usando diccionario de Alemania

MX Linux 23 con locale de_AT

```bash
wachin@mx23:~
$ echo $LANG
de_AT.UTF-8
```

y WPS Office 12 con MUI de_DE

```
/opt/kingsoft/wps-office/office6/mui/de_DE/
```

y solo hay corrección ortográfica del idioma alemán de Alemania

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

entonces la corrección ortográfica para palabras mal escritas en Alemán

```
[ ] Funciona
[ ] No funciona
```

### Alemán de Suiza usando diccionario de Alemania

MX Linux 23 con locale de_CH

```bash
wachin@mx23:~
$ echo $LANG
de_CH.UTF-8
```

y WPS Office 12 con MUI de_DE

```
/opt/kingsoft/wps-office/office6/mui/de_DE/
```

y solo hay corrección ortográfica del idioma alemán de Alemania

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

entonces la corrección ortográfica para palabras mal escritas en Alemán

```
[ ] Funciona
[ ] No funciona
```

### Portugués de Brasil usando fallback pt_PT del MUI

MX Linux 23 con locale pt_BR

```bash
wachin@mx23:~
$ echo $LANG
pt_BR.UTF-8
```

y WPS Office 12 con MUI pt_BR

```
/opt/kingsoft/wps-office/office6/mui/pt_BR/
```

Nota: el archivo `lang.conf` de este MUI contiene:

```ini
FallBack=pt_PT
```

y hay corrección ortográfica para pt_BR y pt_PT

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/
```

entonces revisar si WPS usa correctamente el diccionario pt_BR

```
[ ] Funciona con pt_BR
[ ] Solo funciona si se elige pt_PT
[ ] No funciona
```

## Pruebas no recomendadas por ahora

Estas tienen MUI instalado, pero falta el diccionario de corrección ortográfica correspondiente en:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

| MUI instalado |                     Locale del Login Manager                     | Diccionario faltante |
| ------------- | ---------------------------------------------------------------- | -------------------- |
| `ja_JP`       | `ja_JP`                                                          | `ja_JP`              |
| `zh_CN`       | `zh_CN`                                                          | `zh_CN`              |
| `zh_HK`       | no aparece como locale directo; el Login Manager muestra `zh_TW` | `zh_HK` o `zh_TW`    |
| `th_TH`       | no aparece en `locales-mx-linux-23.md`                           | `th_TH`              |

También está instalado el MUI y diccionario `id_ID`, pero `id_ID` no aparece en la lista actual del Login Manager de MX Linux 23. Si logras iniciar una sesión con `id_ID.UTF-8`, sí conviene probarlo.
