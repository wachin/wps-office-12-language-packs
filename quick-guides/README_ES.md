# Guía rápida: corrector ortográfico en español en WPS Office 12 para Linux

Esta guía corta instala la interfaz y el corrector ortográfico en español para WPS Office 12 en Linux.

## Requisitos

- WPS Office 12.x instalado.
- Este repositorio descargado o clonado.
- Permisos de administrador con `sudo`.
- WPS Office abierto al menos una vez para que exista `~/.config/Kingsoft/Office.conf`.

## Instalar WPS Office

Descarga WPS Office 12 para Linux desde el sitio chino oficial:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Puedes instalar el paquete `.deb` con tu instalador de paquetes:

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

o desde la terminal:

```bash
sudo dpkg -i wps-office*.deb
```

## Instalar MUI y diccionarios

Desde la raíz de este repositorio, ejecuta:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
sudo cp -r build/dicts-active/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Para español, usa:

```text
/opt/kingsoft/wps-office/office6/mui/es_ES
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
```

## Configurar WPS Office

Edita:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Usa este contenido:

```ini
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Cierra WPS Office por completo y vuelve a abrirlo.

## Activar la corrección ortográfica

En WPS Writer, ve a:

`Revisar` > `Revisión ortográfica ⌵` > `Establecer idioma`

Selecciona `Español (España)` y establécelo como predeterminado si hace falta.

Si la barra de estado muestra `Revisión ortográfica: Desactivado ⌵`, haz clic allí para cambiarlo a `Activado`.

![](../vx_images/20260716.1-Frases-MUI-es-ES-Richard-Stallman-ezgif.com.gif)
