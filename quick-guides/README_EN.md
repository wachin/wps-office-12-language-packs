# Quick guide: English spellchecker in WPS Office 12 for Linux

This short guide installs the English interface and spellchecker for WPS Office 12 on Linux.

## Requirements

- WPS Office 12.x installed.
- This repository downloaded or cloned.
- Administrator permissions with `sudo`.
- WPS Office opened at least once so `~/.config/Kingsoft/Office.conf` exists.

## Install WPS Office

Download WPS Office 12 for Linux from the official Chinese site:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

You can install the `.deb` package with your package installer:

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

or from the terminal:

```bash
sudo dpkg -i wps-office*.deb
```

## Install the MUI and dictionaries

From the root of this repository, run:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
sudo cp -r build/dicts-active/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

For English, WPS Office 12 already includes:

```text
/opt/kingsoft/wps-office/office6/mui/en_US
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

## Configure WPS Office

Edit:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Use this content:

```ini
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Close WPS Office completely and open it again.

## Enable spellchecking

In WPS Writer, go to:

`Review` > `Spell Check ⌵` > `Set Spell Check language`

Select `English (United States)` and set it as default if needed.

![](../vx_images/20260721.2-WPS_en-US_Home-Review-SpellCheck-SetLanguage-ezgif.com.gif)

If the status bar shows `Spell Check: Disabled ⌵`, click it so it changes to `Enabled`.

![](../vx_images/20260721.1-Quotes-MUI-en-US-Richard-Stallman-ezgif.com.gif)
