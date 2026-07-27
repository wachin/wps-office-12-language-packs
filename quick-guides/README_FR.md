# Guide rapide : correcteur orthographique français dans WPS Office 12 pour Linux

Ce petit guide installe l’interface et le correcteur orthographique français pour WPS Office 12 sous Linux.

## Prérequis

- WPS Office 12.x installé.
- Connexion Internet pour télécharger les fichiers du Release.
- Droits d’administration avec `sudo`.
- WPS Office ouvert au moins une fois pour que `~/.config/Kingsoft/Office.conf` existe.

## Installer WPS Office

Téléchargez WPS Office 12 pour Linux depuis le site chinois officiel :

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Vous pouvez installer le paquet `.deb` avec votre installateur de paquets :

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

ou depuis le terminal :

```bash
sudo dpkg -i wps-office*.deb
```

## Télécharger les fichiers du Release

Allez dans la section Releases :

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

Téléchargez ces deux fichiers :

- `wps-office-12-mui.tar.xz`
- `wps-office-12-dicts-active.tar.xz`

![](../vx_images/09-release-wps-12.1.2-language-packs-v1.png)

## Installer la MUI

Extrayez `wps-office-12-mui.tar.xz` avec un clic droit dans votre gestionnaire de fichiers préféré. Vous obtiendrez le dossier :

```text
wps-office-12-mui
```

Ouvrez un terminal dans ce dossier. Dans les systèmes Linux modernes, un clic droit dans un dossier propose généralement une option comme `Open terminal here`.

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

## Installer les dictionnaires

Extrayez `wps-office-12-dicts-active.tar.xz` avec un clic droit dans votre gestionnaire de fichiers préféré. Vous obtiendrez le dossier :

```text
wps-office-12-dicts-active
```

Ouvrez un terminal dans ce dossier et exécutez :

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Pour le français, WPS Office 12 utilisera :

```text
/opt/kingsoft/wps-office/office6/mui/fr_FR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
```

## Configurer WPS Office

Si Gedit n’est pas installé, installez-le d’abord :

```bash
sudo apt install gedit
```

Modifiez :

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Utilisez ce contenu :

```ini
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Fermez complètement WPS Office puis rouvrez-le.

## Activer la correction orthographique

Dans WPS Writer, sélectionnez le dictionnaire français comme langue de correction orthographique et définissez-le par défaut si nécessaire.

![](../vx_images/Quotes-tests/citation_fr-FR_Richard_S-ezgif.com.gif)
