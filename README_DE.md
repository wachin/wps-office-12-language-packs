# WPS Office 12.x-Sprachpakete für Linux

Verfügbare Übersetzungen:

- [English](README.md), verfügbar für englischsprachige Benutzer.
- [Español](README_ES.md), verfügbar für spanischsprachige Benutzer.

## WPS Office 12 Linux, chinesische Version, herunterladen

Lade das WPS-Office-Installationspaket für deine Linux-Distribution herunter, entweder für DEB-basierte oder RPM-basierte Systeme.

Offizielle chinesische Website:

- [https://www.wps.cn](https://www.wps.cn)

Ein Klick dort leitet weiter zu:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Installiere anschließend das Paket.

**Mirror-Download**
Dort sind jedoch möglicherweise nicht die neuesten Versionen vorhanden, oder es kann etwas dauern, bis sie dort hochgeladen werden:

[https://mirrors.163.com/ubuntukylin/pool/partner/](https://mirrors.163.com/ubuntukylin/pool/partner/)

### DEB-Paket mit einem DEB-Paketinstaller installieren

Installiere es mit einem DEB-Paketmanager. Auf Linux-Systemen sollte bereits einer installiert sein; klicke im Dateimanager mit der rechten Maustaste auf die Datei und installiere sie mit diesem Werkzeug:

![](vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

### Über das Terminal installieren (optional)

Wenn du Debian, Ubuntu, Linux Mint oder ähnliche Distributionen verwendest, kannst du es auch über das Terminal installieren:

```bash
sudo dpkg -i wps-office*.deb
```

Wenn du Fedora, Red Hat oder ähnliche Distributionen verwendest:

```bash
sudo dnf install wps-office*.rpm
```

## Voraussetzungen

Um mit dieser Anleitung fortzufahren, brauchst du:

- **WPS Office 12.x** unter Linux installiert, wie oben beschrieben.
- Administratorrechte mit `sudo` oder einem gleichwertigen Werkzeug.
- WPS Office mindestens einmal geöffnet haben. WPS Office erstellt seine Benutzerkonfiguration nach dem ersten Start. Wenn `~/.config/Kingsoft/Office.conf` nicht existiert, öffne WPS Office, schließe es wieder und fahre dann mit der Installation fort.
- Eine Internetverbindung haben, um die Release-Dateien herunterzuladen.

## Die mehrsprachigen MUI-Benutzeroberflächen installieren

Lade das MUI-Paket herunter. Gehe zum Bereich Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

lade die Datei herunter:

wps-office-12-mui.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Entpacke sie per Rechtsklick **in deinem bevorzugten Dateimanager**. Danach erhältst du den Ordner:

`wps-office-12-mui`

Klicke dann mit der rechten Maustaste auf diesen Ordner und wähle `Open terminal here` oder einen ähnlichen Eintrag. In modernen Linux-Systemen bietet der Rechtsklick normalerweise diese Option. Von dort aus

installierst du die MUI-Dateien mit diesem Befehl:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

Dieser Befehl installiert die MUI-Dateien (mehrsprachige Benutzeroberflächen).

## Installation überprüfen

Der Befehl `sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/` kopiert die verfügbaren Sprachordner in den echten WPS-Office-Ordner unter Linux: `/opt/kingsoft/wps-office/office6/mui/`.

Die chinesische Version von WPS Office 12, die wir gerade installiert haben, enthält standardmäßig diese MUI-Ordner:

```
/opt/kingsoft/wps-office/office6/mui/en_US
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/mui/zh_CN
```

Das sind:

- `en_US` Englisch (Vereinigte Staaten)
- `ru_RU` Russisch (Russische Föderation)
- `zh_CN` Chinesisch (China)

und sie enthält standardmäßig auch diese zwei Wörterbücher für die Rechtschreibprüfung:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_CH
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US
```

Das sind:

- `en_CH` Chinesisch und Englisch (Vereinigte Staaten)
- `en_US` Englisch (Vereinigte Staaten)

Prüfe in deinem Dateimanager diesen Pfad:

/opt/kingsoft/wps-office/office6/mui/

Zusätzlich zu den Sprachen, die in der chinesischen Version enthalten sind, solltest du Folgendes haben:

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

Außerdem wird kopiert:

```
lang_list
```

Das ist eine Auswahlliste.


## Verfügbare und getestete Wörterbücher

Dieses Repository bereitet außerdem Hunspell-Wörterbücher so vor, dass **WPS Office 12.x** sie unter Linux verwenden kann.

Derzeit muss zwischen zwei Ordnern unterschieden werden:

```
build/wps-office-12-dicts-active/
wps-libreoffice-dicts/
```

Der Ordner `build/wps-office-12-dicts-active/` enthält die Wörterbücher, die derzeit zur Installation ausgewählt sind. Diese werden für die Tests mit WPS Office 12 verwendet.

Der Ordner `wps-libreoffice-dicts/` enthält alle aus LibreOffice konvertierten Wörterbücher. Er bleibt im Wurzelverzeichnis des Repositorys, weil in der chinesischen Version von WPS Office 12 nicht alle Varianten funktionieren, auch wenn sie das richtige Format haben. Vielleicht unterstützt WPS in einer zukünftigen Version wieder alle diese Wörterbücher, so wie es ältere WPS-Office-Versionen für Linux getan haben.

Jeder Wörterbuchordner hat das von WPS erwartete Format:

```
dict.conf
main.aff
main.dic
```

Die Dateien `main.aff` und `main.dic` stammen hauptsächlich aus der LibreOffice-Wörterbuchsammlung:

```
third-party/libreoffice-dictionaries-collection/dicts/
```

Quell-Repository:

[https://github.com/wachin/libreoffice-dictionaries-collection](https://github.com/wachin/libreoffice-dictionaries-collection)

Die `dict.conf`-Dateien werden aus alten WPS-Office-Wörterbüchern wiederverwendet, wenn sie vorhanden sind, und für neue Varianten erzeugt.

Wichtige Ausnahme: Das aktive Wörterbuch `pl_PL` stammt aus den alten Wörterbüchern von WPS Office 11.2.0.9255:

```
third-party/wps-office-11.2.0.9255-dicts/dicts/pl_PL/
```

Quell-Repository:

[https://github.com/wachin/wps-office-11.2.0.9255-dicts](https://github.com/wachin/wps-office-11.2.0.9255-dicts)

Dieses `pl_PL` wird verwendet, weil das aus LibreOffice konvertierte polnische Wörterbuch in WPS Office 12 nicht gut funktionierte. Seine Datei `main.aff` enthält:

```
SET ISO8859-2
```

Im Gegensatz dazu ist das alte polnische WPS-Wörterbuch in UTF-8 und seine `main.aff` enthält:

```
SET UTF-8
```

Die derzeit aktiven Wörterbücher sind:

| Code    | Wörterbuch                |
| ------- | ------------------------- |
| `de_DE` | Deutsch (Deutschland)     |
| `es_ES` | Spanisch (Spanien)        |
| `fr_FR` | Französisch (Frankreich)  |
| `id_ID` | Indonesisch               |
| `pl_PL` | Polnisch                  |
| `pt_BR` | Portugiesisch (Brasilien) |
| `pt_PT` | Portugiesisch             |
| `ru_RU` | Russisch (Russland)       |
| `tr_TR` | Türkisch (Türkei)         |

Hinweis zu `pt_PT`: Unter MX Linux 23 mit Locale `pt_PT.UTF-8`, MUI `pt_PT` und dem Wörterbuch unter `/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/` aktiviert WPS Office 12 in den aktuellen Tests die Rechtschreibprüfung für Portugiesisch aus Portugal nicht. In derselben Installation funktioniert die Rechtschreibprüfung jedoch mit dem Wörterbuch `pt_BR`.


## Wörterbücher installieren

Gehe zum Bereich Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

lade die Datei herunter:

wps-office-12-dicts-active.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Entpacke sie per Rechtsklick in deinem bevorzugten Dateimanager. Danach erhältst du den Ordner:

`wps-office-12-dicts-active`

Klicke dann mit der rechten Maustaste auf diesen Ordner und wähle `Open terminal here` oder einen ähnlichen Eintrag. In modernen Linux-Systemen bietet der Rechtsklick normalerweise diese Option. Von dort aus

installierst du die Wörterbuchdateien mit diesem Befehl:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Dadurch werden die aktiven Wörterbücher in den Ordner kopiert, den WPS für die Rechtschreibprüfung verwendet.

Nach dem Kopieren sollte der WPS-Pfad Ordner wie diese enthalten:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Und in jedem davon:

```
dict.conf
main.aff
main.dic
```

## Eine Oberflächensprache in der WPS-Konfiguration aktivieren

Wenn du Entwickler bist, bearbeite die Konfigurationsdatei mit nano:

```bash
nano ~/.config/Kingsoft/Office.conf
```

Wenn du ein normaler Benutzer bist, verwende Gedit oder einen anderen Texteditor. Falls Gedit nicht installiert ist, installiere es so:

```bash
sudo apt install gedit
```

und gib dies im Terminal ein:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Sobald diese Datei geöffnet ist, wähle den gesamten Text darin mit `Ctrl + A` aus, lösche ihn und ersetze ihn durch den Inhalt für die Sprache, die du verwenden möchtest.

Die Struktur ist immer gleich:

```
[General]
languages=SPRACHCODE

[6.0]
common\DefaultLanguage=SPRACHNUMMER
common\Local\UILanguage=SPRACHNUMMER
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Verwende diese Tabelle, um den richtigen Code und die richtige Nummer auszuwählen:

| Sprache                             | `languages=` | `DefaultLanguage` und `UILanguage` |
| ----------------------------------- | ------------ | ---------------------------------- |
| Englisch (Vereinigte Staaten)       | `en_US`      | `1033`                             |
| Deutsch (Deutschland)               | `de_DE`      | `1031`                             |
| Spanisch (Spanien)                  | `es_ES`      | `3082`                             |
| Spanisch (Mexiko)                   | `es_MX`      | `2058`                             |
| Französisch (Kanada)                | `fr_CA`      | `3084`                             |
| Französisch (Frankreich)            | `fr_FR`      | `1036`                             |
| Indonesisch                         | `id_ID`      | `1057`                             |
| Japanisch                           | `ja_JP`      | `1041`                             |
| Polnisch                            | `pl_PL`      | `1045`                             |
| Portugiesisch (Brasilien)           | `pt_BR`      | `1046`                             |
| Portugiesisch (Portugal)            | `pt_PT`      | `2070`                             |
| Russisch                            | `ru_RU`      | `1049`                             |
| Thailändisch                        | `th_TH`      | `1054`                             |
| Türkisch                            | `tr_TR`      | `1055`                             |
| Chinesisch (vereinfacht, China)     | `zh_CN`      | `2052`                             |
| Chinesisch (traditionell, Hongkong) | `zh_HK`      | `3076`                             |

### Kurztabelle: Locale, MUI und Wörterbuch mit demselben Code

Diese Tabelle zeigt die Sprachen, bei denen direkt verglichen werden kann, ob `Locale`, MUI und Wörterbuch denselben Code verwenden. Das `x` bedeutet, dass kein aktives Wörterbuch mit demselben Code enthalten ist. Das Symbol `✅` markiert getestete Fälle, in denen genau diese Kombination funktioniert.

| Im Login Manager angezeigte Sprache | `Locale` | `MUI`    | `Dict`  | Getestet |
| ----------------------------------- | -------- | -------- | ------- | -------- |
| Englisch (Vereinigte Staaten)       | `en_US`  | `en_US`  | `en_US` | ✅        |
| Deutsch (Deutschland)               | `de_DE`  | `de_DE`  | `de_DE` | ✅        |
| Spanisch (Spanien)                  | `es_ES`  | `es_ES`  | `es_ES` | ✅        |
| Spanisch (Mexiko)                   | `es_MX`  | `es_MX`  | x       |          |
| Französisch (Kanada)                | `fr_CA`  | `fr_CA`  | x       |          |
| Französisch (Frankreich)            | `fr_FR`  | `fr_FR`  | `fr_FR` | ✅        |
| Indonesisch                         | `id_ID`  | `id_ID`  | `id_ID` | ✅        |
| Japanisch                           | `ja_JP`  | `ja_JP`  | x       |          |
| Polnisch                            | `pl_PL`  | `pl_PL`  | `pl_PL` | ✅        |
| Portugiesisch (Brasilien)           | `pt_BR`  | `pt_BR`  | `pt_BR` | ✅        |
| Portugiesisch (Portugal)            | `pt_PT`  | `pt_PT`  | `pt_PT` |          |
| Russisch                            | `ru_RU`  | `ru_RU`* | `ru_RU` | ✅        |
| Thailändisch                        | `th_TH`  | `th_TH`  | x       |          |
| Türkisch                            | `tr_TR`  | `tr_TR`  | `tr_TR` | ✅        |
| Chinesisch (vereinfacht, China)     | `zh_CN`  | `zh_CN`  | x       |          |
| Chinesisch (traditionell, Hongkong) | `zh_HK`  | `zh_HK`  | x       |          |

* Die chinesische Version von WPS Office 12 enthält das MUI `ru_RU` bereits standardmäßig. Deshalb muss das MUI-Archiv aus dem Release diesen Ordner nicht enthalten. Das Rechtschreibwörterbuch `ru_RU` wird weiterhin aus dem Wörterbucharchiv installiert.

### Für Englisch Vereinigte Staaten:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Spanisch aus Spanien:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Deutsch aus Deutschland:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


### Für Spanisch aus Mexiko:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Französisch aus Kanada:

```
[General]
languages=fr_CA

[6.0]
common\DefaultLanguage=3084
common\Local\UILanguage=3084
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Französisch aus Frankreich:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Indonesisch:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Japanisch:

```
[General]
languages=ja_JP

[6.0]
common\DefaultLanguage=1041
common\Local\UILanguage=1041
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Polnisch:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für brasilianisches Portugiesisch:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Portugiesisch aus Portugal:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Russisch:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Thailändischländisch:

```
[General]
languages=th_TH

[6.0]
common\DefaultLanguage=1054
common\Local\UILanguage=1054
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für Türkisch:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für vereinfachtes Chinesisch aus China:

```
[General]
languages=zh_CN

[6.0]
common\DefaultLanguage=2052
common\Local\UILanguage=2052
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Für traditionelles Chinesisch aus Hongkong:

```
[General]
languages=zh_HK

[6.0]
common\DefaultLanguage=3076
common\Local\UILanguage=3076
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


Speichere die Datei, schließe WPS Office vollständig und öffne es erneut. Wenn die Sprache richtig konfiguriert wurde, öffnet sich die Oberfläche in der gewählten Sprache.

## Lösung, damit die Rechtschreibprüfungen in WPS Office 12 funktionieren

In der chinesischen Version von WPS Office 12 reicht es nicht aus, ein Wörterbuch in diesen Ordner zu kopieren:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Auch die regionale Einstellung, mit der du dich über den Login Manager in der Linux-Sitzung angemeldet hast, die in WPS Office installierte MUI-Sprache und die in dieser Datei konfigurierte Sprache spielen eine Rolle:

```
~/.config/Kingsoft/Office.conf
```

Deshalb erscheinen manche Wörterbücher im Fenster `"Set language"`, führen aber keine Rechtschreibprüfung durch. Der deutlichste Fall ist Spanisch aus Mexiko: Die MUI `es_MX` und das Wörterbuch `es_MX` können als installiert erscheinen, aber in den Tests funktionierte die Rechtschreibprüfung nur mit dem Wörterbuch `es_ES`.

### Bestätigte Tests

Dies sind die bisher durchgeführten Tests:

| Rechtschreibprüfung | Im Login Manager gewählte Regionaleinstellung      | Locale  | In WPS verwendete MUI | Installiertes Wörterbuch | Status             |
| ------------------- | -------------------------------------------------- | ------- | --------------------- | ------------------------ | ------------------ |
| Englisch            | `Amerikanisches Englisch - Vereinigte Staaten`     | `en_US` | `en_US`               | `en_US` UTF-8            | Funktioniert       |
| Englisch            | `Englisch - Irland`                                | `en_IE` | `en_US`               | `en_US` UTF-8            | Funktioniert       |
| Englisch            | `Australisches Englisch - Australien`              | `en_AU` | `en_US`               | `en_US` UTF-8            | Funktioniert       |
| Englisch            | `Britisches Englisch - Vereinigtes Königreich`     | `en_GB` | `en_US`               | `en_US` UTF-8            | Funktioniert       |
| Englisch            | `Englisch - Neuseeland`                            | `en_NZ` | `en_US`               | `en_US` UTF-8            | Funktioniert nicht |
| Spanisch            | `Spanisch - Ecuador`                               | `es_EC` | `es_ES`               | `es_ES` UTF-8            | Funktioniert       |
| Spanisch            | `Europäisches Spanisch - Spanien`                  | `es_ES` | `es_ES`               | `es_ES` UTF-8            | Funktioniert       |
| Spanisch            | `Spanisch - Vereinigte Staaten`                    | `es_US` | `es_ES`               | `es_ES` UTF-8            | Funktioniert       |
| Spanisch            | `Spanisch - Venezuela`                             | `es_VE` | `es_ES`               | `es_ES` UTF-8            | Funktioniert       |
| Spanisch            | `Mexikanisches Spanisch - Mexiko`                  | `es_MX` | `es_ES`               | `es_ES` UTF-8            | Funktioniert       |
| Spanisch            | `Spanisch - Peru`                                  | `es_PE` | `es_ES`               | `es_ES` UTF-8            | Funktioniert       |
| Spanisch            | `Spanisch - Uruguay`                               | `es_UY` | `es_ES`               | `es_ES` UTF-8            | Funktioniert       |
| Spanisch Mexiko     | `Mexikanisches Spanisch - Mexiko`                  | `es_MX` | `es_MX`               | `es_MX` UTF-8            | Funktioniert nicht |
| Deutsch             | `Österreichisches Deutsch - Österreich`            | `de_AT` | `de_DE`               | `de_DE` ISO8859-1        | Funktioniert       |
| Deutsch             | `Deutsch - Deutschland`                            | `de_DE` | `de_DE`               | `de_DE` ISO8859-1        | Funktioniert       |
| Deutsch             | `Schweizer Hochdeutsch - Schweiz`                  | `de_CH` | `de_DE`               | `de_DE` ISO8859-1        | Funktioniert       |
| Französisch         | `Französisch - Frankreich`                         | `fr_FR` | `fr_FR`               | `fr_FR` UTF-8            | Funktioniert       |
| Französisch         | `Kanadisches Französisch - Kanada`                 | `fr_CA` | `fr_CA`               | `fr_FR` UTF-8            | Funktioniert       |
| Indonesisch         | `Indonesisch - Indonesia`                          | `id_ID` | `id_ID`               | `id_ID` ISO8859-1        | Funktioniert       |
| Polnisch            | `Polnisch - Polen`                                 | `pl_PL` | `pl_PL`               | `pl_PL` UTF-8            | Funktioniert       |
| Portugiesisch BR    | `Brasilianisches Portugiesisch - Brasilien`        | `pt_BR` | `pt_BR`               | `pt_BR` UTF-8            | Funktioniert       |
| Portugiesisch PT    | `Europäisches Portugiesisch - Portugal`            | `pt_PT` | `pt_PT`               | `pt_PT` UTF-8            | Funktioniert nicht |
| Portugiesisch PT    | `Europäisches Portugiesisch - Portugal`            | `pt_PT` | `pt_PT`               | `pt_BR` UTF-8            | Funktioniert       |
| Russisch            | `Russisch - Russland`                              | `ru_RU` | `ru_RU`               | `ru_RU` UTF-8            | Funktioniert       |
| Türkisch            | `Türkisch - Türkei`                                | `tr_TR` | `tr_TR`               | `tr_TR` UTF-8            | Funktioniert       |

Die in der Spalte `Installiertes Wörterbuch` angezeigte Kodierung stammt aus der Zeile `SET` der Datei `main.aff` des jeweiligen Wörterbuchs.

**Hinweis zu `pl_PL`**: Nach dem Ersetzen des Wörterbuchs durch die UTF-8-Version aus den alten Wörterbüchern von WPS Office 11.2.0.9255 musste es manuell unter `"Review"` > `"Spell Check ⌵"` > `"Set language"` > `"Polski"` ausgewählt werden. Nach der Auswahl funktionierte die Rechtschreibprüfung. Das aus LibreOffice konvertierte polnische Wörterbuch funktionierte nicht gut, weil es in `ISO8859-2` kodiert war, wie in seiner Datei `main.aff` zu sehen ist.

**Hinweis zu `pt_PT`**: Mit Locale `pt_PT.UTF-8`, MUI `pt_PT` und Wörterbuch `pt_PT` aktivierte WPS Office 12 die Rechtschreibprüfung nicht. In derselben Konfiguration funktionierte sie mit dem Wörterbuch `pt_BR`.

**Hinweis zu `ru_RU`**: Die Rechtschreibprüfung funktionierte in einem neu erstellten Dokument. In einem ursprünglich auf Englisch erstellten Dokument wendete WPS die Rechtschreibprüfung auf den vorhandenen Text nicht korrekt an, obwohl übersetzter russischer Text eingefügt wurde.

Unter MX Linux 23 kann die Locale im Login Manager angezeigt werden: Wenn du eine Sprache aus der Liste auswählst, zeigt der Login Manager den Locale-Code an. Wenn du zum Beispiel klickst:

```
Mexikanisches Spanisch - Mexiko
```

erscheint Folgendes:

```
es_MX
```

Wenn du bereits angemeldet bist und sehen möchtest, welche Locale dein System verwendet, öffne ein Terminal und führe aus:

```bash
echo $LANG
```

Beispiel:

```bash
$ echo $LANG
es_MX.UTF-8
```

### Liste der im MX Linux 23 Login Manager verfügbaren Sprachen

Dies ist die im MX Linux 23 Login Manager beobachtete Liste:

![](vx_images/20260717.1-MX-Linux-23_Login-Manager-lnguages-ezgif.com.gif)

Als Tabelle mit Locales:

| Language in the Login Manager                | Locale  |
| -------------------------------------------- | ------- |
| Arabisch - Ägypten                           | `ar_EG` |
| Belarussisch - Belarus                       | `be_BY` |
| Bulgarisch - Bulgarien                       | `bg_BG` |
| Katalanisch - Spanien                        | `ca_ES` |
| Tschechisch - Tschechische Republik          | `cs_CZ` |
| Dänisch - Dänemark                           | `da_DK` |
| Österreichisches Deutsch - Österreich        | `de_AT` |
| Schweizer Hochdeutsch - Schweiz              | `de_CH` |
| Deutsch - Deutschland                        | `de_DE` |
| Griechisch - Griechenland                    | `el_GR` |
| Australisches Englisch - Australien          | `en_AU` |
| Kanadisches Englisch - Kanada                | `en_CA` |
| Britisches Englisch - Vereinigtes Königreich | `en_GB` |
| Englisch - Irland                            | `en_IE` |
| Englisch - Neuseeland                        | `en_NZ` |
| Amerikanisches Englisch - Vereinigte Staaten | `en_US` |
| Spanisch - Argentinien                       | `es_AR` |
| Spanisch - Bolivien                          | `es_BO` |
| Spanisch - Kolumbien                         | `es_CO` |
| Spanisch - Ecuador                           | `es_EC` |
| Europäisches Spanisch - Spanien              | `es_ES` |
| Mexikanisches Spanisch - Mexiko              | `es_MX` |
| Spanisch - Nicaragua                         | `es_NI` |
| Spanisch - Panama                            | `es_PA` |
| Spanisch - Peru                              | `es_PE` |
| Spanisch - Vereinigte Staaten                | `es_US` |
| Spanisch - Uruguay                           | `es_UY` |
| Spanisch - Venezuela                         | `es_VE` |
| Estnisch - Estland                           | `et_EE` |
| Baskisch - Spanien                           | `eu_ES` |
| Persisch - Iran                              | `fa_IR` |
| Finnisch - Finnland                          | `fi_FI` |
| Französisch - Belgien                        | `fr_BE` |
| Kanadisches Französisch - Kanada             | `fr_CA` |
| Schweizer Französisch - Schweiz              | `fr_CH` |
| Französisch - Frankreich                     | `fr_FR` |
| Irisch - Irland                              | `ga_IE` |
| Hebräisch - Israel                           | `he_IL` |
| Kroatisch - Kroatien                         | `hr_HR` |
| Ungarisch - Ungarn                           | `hu_HU` |
| Isländisch - Island                          | `is_IS` |
| Italienisch - Italien                        | `it_IT` |
| Japanisch - Japan                            | `ja_JP` |
| Georgisch - Georgien                         | `ka_GE` |
| Kasachisch - Kasachstan                      | `kk_KZ` |
| Koreanisch - Südkorea                        | `ko_KR` |
| Litauisch - Litauen                          | `lt_LT` |
| Lettisch - Lettland                          | `lv_LV` |
| Mazedonisch - Mazedonien                     | `mk_MK` |
| Norwegisch Bokmål - Norwegen                 | `nb_NO` |
| Flämisch - Belgien                           | `nl_BE` |
| Niederländisch - Niederlande                 | `nl_NL` |
| Norwegisch Nynorsk - Norwegen                | `nn_NO` |
| Polnisch - Polen                             | `pl_PL` |
| Brasilianisches Portugiesisch - Brasilien    | `pt_BR` |
| Europäisches Portugiesisch - Portugal        | `pt_PT` |
| Rumänisch - Rumänien                         | `ro_RO` |
| Russisch - Russland                          | `ru_RU` |
| Slowakisch - Slowakei                        | `sk_SK` |
| Slowenisch - Slowenien                       | `sl_SI` |
| Albanisch - Albanien                         | `sq_AL` |
| Serbisch - Serbien                           | `sr_RS` |
| Schwedisch - Schweden                        | `sv_SE` |
| Türkisch - Türkei                            | `tr_TR` |
| Ukrainisch - Ukraine                         | `uk_UA` |
| Chinesisch - China                           | `zh_CN` |
| Chinesisch - Taiwan                          | `zh_TW` |


## So funktioniert die englische Rechtschreibprüfung

Damit die englische Rechtschreibprüfung funktioniert, melde dich von MX Linux 23 ab und wähle im Login Manager:

```
Amerikanisches Englisch - Vereinigte Staaten
```

Bearbeite anschließend:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

und lasse diesen Inhalt stehen:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

WPS Office 12 enthält diese MUI bereits standardmäßig:

```
/opt/kingsoft/wps-office/office6/mui/en_US
```

und auch das Wörterbuch:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

### Englische Rechtschreibprüfung aktivieren

Öffne nun WPS Writer. Gehe zum Ribbon-Tab mit dem Namen:

`"Review"`

und dort zu

`"Spell Check ⌵"`

klicke auf dieses Symbol `"⌵"` und dann auf das Untermenü:

`"Set Spell Check language"`

![](vx_images/20260721.2-WPS_en-US_Home-Review-SpellCheck-SetLanguage-ezgif.com.gif)

Im geöffneten Fenster befindet sich `"Englisch (Vereinigte Staaten)"` standardmäßig unter den verfügbaren Wörterbüchern.

![](vx_images/dicts-tests/01-Set-Spell-Check-Language-English-United-States.png)


Wenn du möchtest, kannst du auf `"Change Default"` klicken, obwohl es bereits standardmäßig ausgewählt war, weil die MUI `en_US` bereits installiert war.

Sieh nun in der unteren linken Ecke des Fensters auf die Statusleiste; dort erscheint ein ähnlicher Hinweis:

`Spell Check: Disabled ⌵`

Klicke auf diesen Hinweis, und er wechselt zu `"Enabled"`.

Wenn du außerdem auf das Symbol `"⌵"` klickst, stehen diese und weitere Optionen in einem Dropdown-Menü zur Verfügung.

Nach der Aktivierung beginnt WPS Office automatisch mit der Rechtschreibprüfung des Dokuments. Ab diesem Moment werden falsch geschriebene Wörter unterstrichen; ein Rechtsklick auf ein unterstrichenes Wort zeigt Korrekturvorschläge. Die Rechtschreibprüfung bleibt aktiviert, bis der Benutzer diese Option wieder deaktiviert:


![](vx_images/20260721.1-Quotes-MUI-en-US-Richard-Stallman-ezgif.com.gif)

---

## So funktioniert die spanische Rechtschreibprüfung

Damit die spanische Rechtschreibprüfung funktioniert, melde dich von MX Linux 23 ab (falls du in einer anderen Sprache angemeldet bist) und wähle im Login Manager zum Beispiel:

```
Spanisch - Ecuador
```

Bearbeite anschließend:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

und lasse diesen Inhalt für Spanisch aus Spanien stehen:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

In dieser Konfiguration muss diese MUI installiert sein:

```
/opt/kingsoft/wps-office/office6/mui/es_ES
```

und das Wörterbuch:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
```


### Spanische Rechtschreibprüfung aktivieren

Öffne WPS Writer. Gehe zum Ribbon-Tab mit dem Namen:

`"Revisar"`

und dort zu

`"Revisión ortográfica ⌵"`

klicke auf dieses Symbol `"⌵"` und dann auf das Untermenü:

`"Establecer idioma"`

Im geöffneten Fenster befindet sich `"Español (España)"` standardmäßig unter den verfügbaren Wörterbüchern.

und klicke auf `"Establecer predeterminado"`, obwohl es bereits standardmäßig ausgewählt war, weil die MUI `es_ES` bereits installiert war.

Sieh nun in der unteren linken Ecke des Fensters auf die Statusleiste; dort erscheint ein ähnlicher Hinweis:

`Revisión ortográfica: Desactivado ⌵`

Klicke auf diesen Hinweis, und er wechselt zu `"Activado"`.

![](vx_images/20260716.1-Frases-MUI-es-ES-Richard-Stallman-ezgif.com.gif)

Wenn du außerdem auf das Symbol `"⌵"` klickst, stehen diese und weitere Optionen in einem Dropdown-Menü zur Verfügung.

Sobald die Rechtschreibprüfung aktiviert ist, beginnt WPS Office automatisch mit der Prüfung des Dokuments. Ab diesem Moment werden falsch geschriebene Wörter unterstrichen; ein Rechtsklick auf ein unterstrichenes Wort zeigt Korrekturvorschläge. Die Rechtschreibprüfung bleibt aktiviert, bis der Benutzer diese Option wieder deaktiviert:

Derzeit funktioniert in dieser chinesischen Version von WPS Office 12 die spanische Rechtschreibprüfung nur mit dem Wörterbuch `es_ES` aus diesem Repository:

/build/dicts-active/es_ES/

Die folgenden Wörterbücher im Ordner `wps-libreoffice-dicts` funktionieren jedoch nicht so, wie sie in WPS Office 11 funktionierten:

```
/wps-libreoffice-dicts/es_AR
/wps-libreoffice-dicts/es_BO
/wps-libreoffice-dicts/es_CL
/wps-libreoffice-dicts/es_CO
/wps-libreoffice-dicts/es_CR
/wps-libreoffice-dicts/es_CU
/wps-libreoffice-dicts/es_DO
/wps-libreoffice-dicts/es_EC
/wps-libreoffice-dicts/es_ES
/wps-libreoffice-dicts/es_GQ
/wps-libreoffice-dicts/es_GT
/wps-libreoffice-dicts/es_HN
/wps-libreoffice-dicts/es_MX
/wps-libreoffice-dicts/es_NI
/wps-libreoffice-dicts/es_PA
/wps-libreoffice-dicts/es_PE
/wps-libreoffice-dicts/es_PH
/wps-libreoffice-dicts/es_PR
/wps-libreoffice-dicts/es_PY
/wps-libreoffice-dicts/es_SV
/wps-libreoffice-dicts/es_US
/wps-libreoffice-dicts/es_UY
/wps-libreoffice-dicts/es_VE
```

### Noch zu testende spanische Regionaleinstellungen

Diese Regionaleinstellungen des Login Managers müssen noch mit der spanischen Rechtschreibprüfung getestet werden:

```
Spanisch - Argentinien
Spanisch - Bolivien
Spanisch - Kolumbien
Spanisch - Nicaragua
Spanisch - Panama
```

Die anderen, die funktionierten, stehen oben in der Tabelle.

## Test des Wörterbuchs Spanisch Mexiko, das nicht funktionierte

Ich habe den folgenden Test durchgeführt, weil sowohl die MUI `es_MX` als auch das Rechtschreibwörterbuch `es_MX` verfügbar sind.

Für den Test wurde über den Login Manager angemeldet mit:

```
Mexikanisches Spanisch - Mexiko
```

und WPS wurde konfiguriert mit:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Mit der MUI:

```
/opt/kingsoft/wps-office/office6/mui/es_MX
```

und dem Wörterbuch unter:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_MX/
```

WPS zeigt `"Español (México)"` im Sprachfenster an, aber die Rechtschreibprüfung funktioniert nicht. Wenn in demselben Fenster jedoch das Wörterbuch `"Español (España)"` ausgewählt wird, funktioniert sie.

## So funktioniert die deutsche Rechtschreibprüfung

Für Deutsch melde dich ab und wähle im Login Manager:

```
Deutsch - Deutschland
```

Konfiguriere `Office.conf` anschließend so:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Die Aktivierung erfolgt ähnlich wie beim englischen Wörterbuch:

![](vx_images/Quotes-tests/Deutsch-de_DE-Richard-S-ezgif.com.gif)

In diesem Test funktionierte Folgendes:

```
/opt/kingsoft/wps-office/office6/mui/de_DE
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

## So funktioniert die französische Rechtschreibprüfung

Für Französisch melde dich ab und wähle im Login Manager:

```
Französisch - Frankreich
```

Die Aktivierung erfolgt ähnlich wie beim englischen Wörterbuch.


![](vx_images/Quotes-tests/citation_fr-FR_Richard_S-ezgif.com.gif)

Konfiguriere `Office.conf` anschließend so:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

In diesem Test funktionierte es mit:

```
/opt/kingsoft/wps-office/office6/mui/fr_FR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
```



## So funktioniert die indonesische Rechtschreibprüfung

Für Indonesisch erzeuge zuerst die Locale, falls sie noch nicht im Login Manager erscheint:

```bash
sudo dpkg-reconfigure locales
```

Markiere in der Liste:

```
id_ID.UTF-8 UTF-8
```

Melde dich anschließend ab und wähle im Login Manager:

```
Indonesisch - Indonesia
```

Konfiguriere `Office.conf` anschließend so:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Die Aktivierung erfolgt ähnlich wie beim englischen Wörterbuch. `"Indonesisch"` sollte im Fenster für die Sprache der Rechtschreibprüfung erscheinen.

![](vx_images/Quotes-tests/Kutipan-id_ID-Richard-S-ezgif.com.gif)

In diesem Test funktionierte es mit:

```
/opt/kingsoft/wps-office/office6/mui/id_ID
/opt/kingsoft/wps-office/office6/dicts/spellcheck/id_ID/
```

Hinweis: Obwohl die Linux-Sitzung `id_ID.UTF-8` verwendet, nutzt das installierte Wörterbuch `id_ID` in `main.aff` den Eintrag `SET ISO8859-1` und funktionierte korrekt in WPS Office 12.

## So funktioniert die polnische Rechtschreibprüfung

Für Polnisch melde dich ab und wähle im Login Manager:

```
Polnisch - Polen
```

Konfiguriere `Office.conf` anschließend so:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Die Aktivierung erfolgt ähnlich wie beim englischen Wörterbuch. `"Polski"` sollte im Fenster für die Sprache der Rechtschreibprüfung erscheinen.

![](vx_images/Quotes-tests/Cytaty_pl-PL_RichardS-ezgif.com.gif)


In diesem Test funktionierte es mit:

```
/opt/kingsoft/wps-office/office6/mui/pl_PL
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pl_PL/
```

Hinweis: Für diesen Test funktionierte das UTF-8-Wörterbuch `pl_PL` aus den alten Wörterbüchern von WPS Office 11.2.0.9255. Das aus LibreOffice konvertierte Wörterbuch war in `ISO8859-2` kodiert und funktionierte in WPS Office 12 nicht gut.

## So funktioniert die brasilianisch-portugiesische Rechtschreibprüfung

Für brasilianisches Portugiesisch melde dich ab und wähle im Login Manager:

```
Brasilianisches Portugiesisch - Brasilien
```

Konfiguriere `Office.conf` anschließend so:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Die Aktivierung erfolgt ähnlich wie beim englischen Wörterbuch. `"Português do Brasil"` sollte im Fenster für die Sprache der Rechtschreibprüfung erscheinen.

![](vx_images/Quotes-tests/Citacoes_pt-BR_Richard_S-ezgif.com.gif)

In diesem Test funktionierte es mit:

```
/opt/kingsoft/wps-office/office6/mui/pt_BR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Hinweis: Obwohl die MUI `pt_BR` in `lang.conf` den Eintrag `FallBack=pt_PT` enthält, prüfte WPS korrekt, wenn `"Português do Brasil"` im Fenster für die Sprache der Rechtschreibprüfung ausgewählt wurde. Wenn in derselben Sitzung `"Português (Portugal)"` ausgewählt wird, funktioniert die Rechtschreibprüfung nicht.

## Test des Wörterbuchs Portugiesisch Portugal, das nicht funktionierte

Ich habe den folgenden Test durchgeführt, weil sowohl die MUI `pt_PT` als auch das Rechtschreibwörterbuch `pt_PT` verfügbar sind.

Für den Test wurde über den Login Manager angemeldet mit:

```
Europäisches Portugiesisch - Portugal
```

und WPS wurde konfiguriert mit:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Mit der MUI:

```
/opt/kingsoft/wps-office/office6/mui/pt_PT
```

und dem Wörterbuch unter:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/
```

WPS zeigte vor der Korrektur des Wörterbuchnamens `"Portuguê"`; jetzt sollte `"Português (Portugal)"` angezeigt werden. In beiden Fällen funktionierte die Rechtschreibprüfung mit dem Wörterbuch `pt_PT` nicht.

In derselben Konfiguration mit Locale `pt_PT.UTF-8` und MUI `pt_PT` funktionierte die Rechtschreibprüfung mit dem brasilianisch-portugiesischen Wörterbuch:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

## So funktioniert die russische Rechtschreibprüfung

Für Russisch melde dich ab und wähle im Login Manager:

```
Russisch - Russland
```

Konfiguriere `Office.conf` anschließend so:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Die Aktivierung erfolgt ähnlich wie beim englischen Wörterbuch. `"Русский (Россия)"` sollte im Fenster für die Sprache der Rechtschreibprüfung erscheinen.

![](vx_images/Quotes-tests/Frase_ru_RU_RichardS-ezgif.com.gif)


In diesem Test funktionierte es mit:

```
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

Hinweis: Die russische Rechtschreibprüfung funktionierte korrekt in einem neu erstellten Dokument. In einem ursprünglich auf Englisch erstellten Dokument wendete WPS die Rechtschreibprüfung auf den vorhandenen Text nicht korrekt an, obwohl übersetzter russischer Text eingefügt wurde.

## So funktioniert die türkische Rechtschreibprüfung

Für Türkisch melde dich ab und wähle im Login Manager:

```
Türkisch - Türkei
```

Konfiguriere `Office.conf` anschließend so:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Die Aktivierung erfolgt ähnlich wie beim englischen Wörterbuch. `"Türkçe (Türkiye)"` sollte im Fenster für die Sprache der Rechtschreibprüfung erscheinen.

![](vx_images/Quotes-tests/Alntlar-tr_TR-Richard-S-ezgif.com.gif)

In diesem Test funktionierte es mit:

```
/opt/kingsoft/wps-office/office6/mui/tr_TR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/tr_TR/
```

## Referenz: von WPS unter Windows heruntergeladene MUI-Pakete

Wenn du neugierig bist und dich fragst, woher die MUI-Dateien für die grafische Oberfläche stammen: Ich habe sie unter Microsoft Windows 10 erhalten. WPS Office lädt Sprachpakete in Benutzerpfade herunter; diese Information ist als Referenz für die Untersuchung von Oberflächensprachdateien nützlich.

Lade zuerst WPS Office 12 für Windows herunter und installiere es:

[https://wps.com/office/windows/](https://wps.com/office/windows/)

Beispiel unter Windows 10:

![](vx_images/02-WPS-Office-global-config-menu.png)

Lade anschließend die Sprachen herunter:

![](vx_images/03-Click-on-a-language-and-then-click-Apply.png)

Die heruntergeladenen Sprachen können hier erscheinen:

```
C:\Users\youruser\AppData\Roaming\kingsoft\wps_intl\addons\pool\win-x64
```

![](vx_images/04-downloaded-languages.png)

Die Sprachliste kann hier erscheinen:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui\lang_list\lang_list.json
```

![20260416-000808](vx_images/507184629680596.png)

Einige Pakete, die von der spanischen Windows-Version mitgeliefert werden, können hier erscheinen:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui
```

![](vx_images/05-languages-downloaded-by-the-Spanish-version.png)

Wenn dir dieses Projekt geholfen hat, kannst du dem Repository einen Stern geben.

---

# Danksagungen

An den Benutzer [mmvill](https://github.com/mmvill), der mir schrieb und mir mitteilte, dass er einen Weg gefunden hat, das spanische Rechtschreibwörterbuch in WPS Office 12 zum Laufen zu bringen.
