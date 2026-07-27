# Quick guide: English spellchecker in WPS Office 12 for Linux

This short guide installs the English interface and spellchecker for WPS Office 12 on Linux.

## Requirements

- WPS Office 12.x installed.
- Internet connection to download the release files.
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

## Download the release files

Go to the Release section:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

Download these two files:

- `wps-office-12-mui.tar.xz`
- `wps-office-12-dicts-active.tar.xz`

![](../vx_images/09-release-wps-12.1.2-language-packs-v1.png)

## Install the MUI

Extract `wps-office-12-mui.tar.xz` with right-click in your preferred file manager. You will get the folder:

```text
wps-office-12-mui
```

Open a terminal inside that folder. In modern Linux systems, right-clicking inside a folder usually provides an option such as `Open terminal here`.

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

## Install the dictionaries

Extract `wps-office-12-dicts-active.tar.xz` with right-click in your preferred file manager. You will get the folder:

```text
wps-office-12-dicts-active
```

Open a terminal inside that folder and run:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

For English, WPS Office 12 will use:

```text
/opt/kingsoft/wps-office/office6/mui/en_US
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

## Configure WPS Office

If you do not have Gedit installed, install it first:

```bash
sudo apt install gedit
```

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
