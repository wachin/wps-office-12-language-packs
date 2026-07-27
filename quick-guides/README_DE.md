# Kurzanleitung: deutsche Rechtschreibprüfung in WPS Office 12 für Linux

Diese kurze Anleitung installiert die deutsche Oberfläche und Rechtschreibprüfung für WPS Office 12 unter Linux.

## Voraussetzungen

- WPS Office 12.x ist installiert.
- Internetverbindung zum Herunterladen der Release-Dateien.
- Administratorrechte mit `sudo` sind vorhanden.
- WPS Office wurde mindestens einmal geöffnet, damit `~/.config/Kingsoft/Office.conf` existiert.

## WPS Office installieren

Lade WPS Office 12 für Linux von der offiziellen chinesischen Seite herunter:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Du kannst das `.deb`-Paket mit deinem Paketinstaller installieren:

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

oder über das Terminal:

```bash
sudo dpkg -i wps-office*.deb
```

## Release-Dateien herunterladen

Gehe zum Bereich Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

Lade diese zwei Dateien herunter:

- `wps-office-12-mui.tar.xz`
- `wps-office-12-dicts-active.tar.xz`

![](../vx_images/09-release-wps-12.1.2-language-packs-v1.png)

## MUI installieren

Entpacke `wps-office-12-mui.tar.xz` per Rechtsklick in deinem bevorzugten Dateimanager. Du erhältst den Ordner:

```text
wps-office-12-mui
```

Öffne ein Terminal in diesem Ordner. In modernen Linux-Systemen gibt es beim Rechtsklick in einen Ordner normalerweise eine Option wie `Open terminal here`.

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

## Wörterbücher installieren

Entpacke `wps-office-12-dicts-active.tar.xz` per Rechtsklick in deinem bevorzugten Dateimanager. Du erhältst den Ordner:

```text
wps-office-12-dicts-active
```

Öffne ein Terminal in diesem Ordner und führe aus:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Für Deutsch verwendet WPS Office 12:

```text
/opt/kingsoft/wps-office/office6/mui/de_DE
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

## WPS Office konfigurieren

Wenn Gedit nicht installiert ist, installiere es zuerst:

```bash
sudo apt install gedit
```

Bearbeite:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Verwende diesen Inhalt:

```ini
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Schließe WPS Office vollständig und öffne es erneut.

## Rechtschreibprüfung aktivieren

Wähle in WPS Writer die Sprache der Rechtschreibprüfung und setze Deutsch als Standard, falls nötig.

![](../vx_images/Quotes-tests/Deutsch-de_DE-Richard-S-ezgif.com.gif)
