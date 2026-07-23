# Kurzanleitung: deutsche Rechtschreibprüfung in WPS Office 12 für Linux

Diese kurze Anleitung installiert die deutsche Oberfläche und Rechtschreibprüfung für WPS Office 12 unter Linux.

## Voraussetzungen

- WPS Office 12.x ist installiert.
- Dieses Repository ist heruntergeladen oder geklont.
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

## MUI und Wörterbücher installieren

Führe im Wurzelverzeichnis dieses Repositorys aus:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
sudo cp -r build/dicts-active/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Für Deutsch verwendet WPS Office 12:

```text
/opt/kingsoft/wps-office/office6/mui/de_DE
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

## WPS Office konfigurieren

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
