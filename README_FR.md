# Paquets de langue WPS Office 12.x pour Linux

Traductions disponibles :

- [Anglais](README.md), disponible pour les utilisateurs anglophones.
- [Español](README_ES.md), disponible pour les utilisateurs hispanophones.
- [Deutsch](README_DE.md), disponible pour les utilisateurs germanophones.

Guide rapide en français : [quick-guides/README_FR.md](quick-guides/README_FR.md).

## Télécharger la version chinoise de WPS Office 12 pour Linux

Téléchargez le programme d’installation de WPS Office pour votre distribution Linux, qu’elle soit basée sur DEB ou sur RPM.

Site officiel chinois :

- [https://www.wps.cn](https://www.wps.cn)

un clic redirige vers :

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Installez ensuite le paquet.

**Téléchargement miroir**
Cependant, il se peut qu’il ne contienne pas les dernières versions, ou qu’elles mettent un certain temps à y être publiées :

[https://mirrors.163.com/ubuntukylin/pool/partner/](https://mirrors.163.com/ubuntukylin/pool/partner/)

### Installer le paquet DEB avec un installateur de paquets DEB

Installez-le avec un gestionnaire de paquets DEB. Sur les systèmes Linux, l’un d’eux devrait déjà être installé ; faites un clic droit sur le fichier dans votre gestionnaire de fichiers et installez-le avec cet outil :

![](vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

### Installer depuis le terminal (facultatif)

Si vous utilisez Debian, Ubuntu, Linux Mint ou une distribution similaire, vous pouvez aussi le faire depuis le terminal :

```bash
sudo dpkg -i wps-office*.deb
```

Si vous utilisez Fedora, Red Hat ou une distribution similaire :

```bash
sudo dnf install wps-office*.rpm
```

## Prérequis

Pour suivre ce tutoriel, vous avez besoin de :

- Avoir **WPS Office 12.x** installé sous Linux comme décrit ci-dessus.
- Avoir des droits d’administration avec `sudo` ou un outil équivalent.
- Avoir ouvert WPS Office au moins une fois. WPS Office crée sa configuration utilisateur après le premier lancement. Si `~/.config/Kingsoft/Office.conf` n’existe pas, ouvrez WPS Office, fermez-le, puis continuez l’installation.
- Avoir une connexion Internet pour télécharger les fichiers du Release.

## Installer les interfaces utilisateur multilingues MUI

Téléchargez le paquet MUI. Allez dans la section Releases :

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

téléchargez le fichier :

wps-office-12-mui.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Extrayez-le avec un clic droit **dans votre gestionnaire de fichiers préféré**. Vous obtiendrez alors le dossier :

`wps-office-12-mui`

Ensuite, faites un clic droit sur ce dossier et choisissez `Open terminal here` ou une option similaire. Dans les systèmes Linux modernes, le clic droit propose généralement cette option. À partir de ce terminal,

installez les fichiers MUI avec cette commande :

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

Cette commande installe les fichiers MUI (interfaces utilisateur multilingues).

## Vérifier l’installation

La commande `sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/` copie les dossiers de langue disponibles dans le véritable dossier de WPS Office sous Linux : `/opt/kingsoft/wps-office/office6/mui/`.

La version chinoise de WPS Office 12 que nous venons d’installer inclut par défaut ces dossiers MUI :

```
/opt/kingsoft/wps-office/office6/mui/en_US
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/mui/zh_CN
```

Ce sont :

- `en_US` langue anglaise (États-Unis)
- `ru_RU` langue russe (Fédération de Russie)
- `zh_CN` langue chinoise (Chine)

et elle inclut aussi par défaut ces deux dictionnaires de correction orthographique :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_CH
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US
```

Ce sont :

- `en_CH` dictionnaire chinois et anglais (États-Unis)
- `en_US` dictionnaire anglais (États-Unis)

Depuis votre gestionnaire de fichiers, vérifiez ce chemin :

/opt/kingsoft/wps-office/office6/mui/

En plus des langues incluses dans la version chinoise, vous devriez avoir les éléments suivants :

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

Ceci est aussi copié :

```
lang_list
```

Il s’agit d’une liste de sélection.


## Dictionnaires disponibles et dictionnaires testés

Ce dépôt prépare aussi des dictionnaires Hunspell afin que **WPS Office 12.x** puisse les utiliser sous Linux.

Pour l’instant, il faut distinguer deux dossiers :

```
build/wps-office-12-dicts-active/
wps-libreoffice-dicts/
```

Le dossier `build/wps-office-12-dicts-active/` contient les dictionnaires sélectionnés pour l’installation actuelle. Ce sont ceux qui sont utilisés pour les tests avec WPS Office 12.

Le dossier `wps-libreoffice-dicts/` contient tous les dictionnaires convertis depuis LibreOffice. Il est conservé à la racine du dépôt parce que, dans la version chinoise de WPS Office 12, toutes les variantes ne fonctionnent pas même lorsqu’elles ont le bon format. Peut-être qu’une future version de WPS prendra de nouveau en charge tous ces dictionnaires, comme le faisaient les anciennes versions de WPS Office pour Linux.

Chaque dossier de dictionnaire a le format attendu par WPS :

```
dict.conf
main.aff
main.dic
```

Les fichiers `main.aff` et `main.dic` proviennent principalement de la collection de dictionnaires LibreOffice :

```
third-party/libreoffice-dictionaries-collection/dicts/
```

Dépôt source :

[https://github.com/wachin/libreoffice-dictionaries-collection](https://github.com/wachin/libreoffice-dictionaries-collection)

Les fichiers `dict.conf` sont réutilisés à partir d’anciens dictionnaires WPS Office lorsqu’ils existent, et générés pour les nouvelles variantes.

Exception importante : le dictionnaire actif `pl_PL` provient des anciens dictionnaires de WPS Office 11.2.0.9255 :

```
third-party/wps-office-11.2.0.9255-dicts/dicts/pl_PL/
```

Dépôt source :

[https://github.com/wachin/wps-office-11.2.0.9255-dicts](https://github.com/wachin/wps-office-11.2.0.9255-dicts)

Ce `pl_PL` est utilisé parce que le dictionnaire polonais converti depuis LibreOffice n’a pas bien fonctionné dans WPS Office 12. Son fichier `main.aff` contient :

```
SET ISO8859-2
```

En revanche, l’ancien dictionnaire polonais de WPS est en UTF-8 et son fichier `main.aff` contient :

```
SET UTF-8
```

Les dictionnaires actuellement actifs sont :

| Code    | Dictionnaire         |
| ------- | -------------------- |
| `de_DE` | Allemand (Allemagne) |
| `es_ES` | Espagnol (Espagne)   |
| `fr_FR` | Français (France)    |
| `id_ID` | Indonésien           |
| `pl_PL` | Polonais             |
| `pt_BR` | Portugais (Brésil)   |
| `pt_PT` | Portugais            |
| `ru_RU` | Russe (Russie)       |
| `tr_TR` | Turc (Turquie)       |

Remarque sur `pt_PT` : sous MX Linux 23 avec la locale `pt_PT.UTF-8`, la MUI `pt_PT` et le dictionnaire installé dans `/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/`, WPS Office 12 n’active pas la correction orthographique pour le portugais du Portugal dans les tests actuels. Dans la même installation, la correction fonctionne avec le dictionnaire `pt_BR`.


## Installer les dictionnaires

Allez dans la section Releases :

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

téléchargez le fichier :

wps-office-12-dicts-active.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Extrayez-le avec un clic droit dans votre gestionnaire de fichiers préféré. Vous obtiendrez alors le dossier :

`wps-office-12-dicts-active`

Ensuite, faites un clic droit sur ce dossier et choisissez `Open terminal here` ou une option similaire. Dans les systèmes Linux modernes, le clic droit propose généralement cette option. À partir de ce terminal,

installez les fichiers de dictionnaire avec cette commande :

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Cela copie les dictionnaires actifs dans le dossier que WPS utilise pour la correction orthographique.

Après la copie, le chemin de WPS doit contenir des dossiers comme ceux-ci :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Et dans chacun d’eux :

```
dict.conf
main.aff
main.dic
```

## Activer une langue d’interface dans la configuration de WPS

Si vous êtes développeur, modifiez le fichier de configuration avec nano :

```bash
nano ~/.config/Kingsoft/Office.conf
```

Si vous êtes un utilisateur normal, utilisez Gedit ou un autre éditeur de texte. Si Gedit n’est pas installé, installez-le ainsi :

```bash
sudo apt install gedit
```

et saisissez ceci dans le terminal :

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Une fois ce fichier ouvert, sélectionnez tout son contenu avec `Ctrl + A`, supprimez-le, puis remplacez-le par le contenu correspondant à la langue que vous voulez utiliser.

La structure est toujours la même :

```
[General]
languages=CODE_LANGUE

[6.0]
common\DefaultLanguage=NUMERO_LANGUE
common\Local\UILanguage=NUMERO_LANGUE
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Utilisez ce tableau pour choisir le code et le numéro corrects :

| Langue                            | `languages=` | `DefaultLanguage` et `UILanguage`  |
| --------------------------------- | ------------ | ---------------------------------- |
| Anglais (États-Unis)              | `en_US`      | `1033`                             |
| Allemand (Allemagne)              | `de_DE`      | `1031`                             |
| Espagnol (Espagne)                | `es_ES`      | `3082`                             |
| Espagnol (Mexique)                | `es_MX`      | `2058`                             |
| Français (Canada)                 | `fr_CA`      | `3084`                             |
| Français (France)                 | `fr_FR`      | `1036`                             |
| Indonésien                        | `id_ID`      | `1057`                             |
| Japonais                          | `ja_JP`      | `1041`                             |
| Polonais                          | `pl_PL`      | `1045`                             |
| Portugais (Brésil)                | `pt_BR`      | `1046`                             |
| Portugais (Portugal)              | `pt_PT`      | `2070`                             |
| Russe                             | `ru_RU`      | `1049`                             |
| Thaï                              | `th_TH`      | `1054`                             |
| Turc                              | `tr_TR`      | `1055`                             |
| Chinois (simplifié, Chine)        | `zh_CN`      | `2052`                             |
| Chinois (traditionnel, Hong Kong) | `zh_HK`      | `3076`                             |

### Tableau rapide : locale, MUI et dictionnaire avec le même code

Ce tableau montre les langues pour lesquelles on peut comparer directement si la `Locale`, la MUI et le dictionnaire utilisent le même code. Le `x` signifie qu’aucun dictionnaire actif avec ce même code n’est inclus. Le symbole `✅` marque les cas testés où cette combinaison exacte fonctionne.

| Langue affichée dans le Login Manager | `Locale` | `MUI`    | `Dict`  | Testé |
| ------------------------------------- | -------- | -------- | ------- | ----- |
| Anglais (États-Unis)                  | `en_US`  | `en_US`  | `en_US` | ✅     |
| Allemand (Allemagne)                  | `de_DE`  | `de_DE`  | `de_DE` | ✅     |
| Espagnol (Espagne)                    | `es_ES`  | `es_ES`  | `es_ES` | ✅     |
| Espagnol (Mexique)                    | `es_MX`  | `es_MX`  | x       |       |
| Français (Canada)                     | `fr_CA`  | `fr_CA`  | x       |       |
| Français (France)                     | `fr_FR`  | `fr_FR`  | `fr_FR` | ✅     |
| Indonésien                            | `id_ID`  | `id_ID`  | `id_ID` | ✅     |
| Japonais                              | `ja_JP`  | `ja_JP`  | x       |       |
| Polonais                              | `pl_PL`  | `pl_PL`  | `pl_PL` | ✅     |
| Portugais (Brésil)                    | `pt_BR`  | `pt_BR`  | `pt_BR` | ✅     |
| Portugais (Portugal)                  | `pt_PT`  | `pt_PT`  | `pt_PT` |       |
| Russe                                 | `ru_RU`  | `ru_RU`* | `ru_RU` | ✅     |
| Thaï                                  | `th_TH`  | `th_TH`  | x       |       |
| Turc                                  | `tr_TR`  | `tr_TR`  | `tr_TR` | ✅     |
| Chinois (simplifié, Chine)            | `zh_CN`  | `zh_CN`  | x       |       |
| Chinois (traditionnel, Hong Kong)     | `zh_HK`  | `zh_HK`  | x       |       |

* La version chinoise de WPS Office 12 inclut déjà la MUI `ru_RU` par défaut. L’archive MUI du Release n’a donc pas besoin d’inclure ce dossier. Le dictionnaire de correction orthographique `ru_RU` est toujours installé depuis l’archive des dictionnaires.

### Pour l’anglais des États-Unis :

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour l’espagnol d’Espagne :

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour l’allemand d’Allemagne :

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


### Pour l’espagnol du Mexique :

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le français du Canada :

```
[General]
languages=fr_CA

[6.0]
common\DefaultLanguage=3084
common\Local\UILanguage=3084
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le français de France :

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour l’indonésien :

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le japonais :

```
[General]
languages=ja_JP

[6.0]
common\DefaultLanguage=1041
common\Local\UILanguage=1041
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le polonais :

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le portugais brésilien :

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le portugais du Portugal :

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le russe :

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le thaï :

```
[General]
languages=th_TH

[6.0]
common\DefaultLanguage=1054
common\Local\UILanguage=1054
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le turc :

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le chinois simplifié de Chine :

```
[General]
languages=zh_CN

[6.0]
common\DefaultLanguage=2052
common\Local\UILanguage=2052
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Pour le chinois traditionnel de Hong Kong :

```
[General]
languages=zh_HK

[6.0]
common\DefaultLanguage=3076
common\Local\UILanguage=3076
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


Enregistrez le fichier, fermez complètement WPS Office, puis rouvrez-le. Si la langue a été correctement configurée, l’interface s’ouvrira dans la langue choisie.

## Solution pour faire fonctionner les correcteurs orthographiques dans WPS Office 12

Dans la version chinoise de WPS Office 12, copier un dictionnaire dans ce dossier ne suffit pas :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Le paramètre régional utilisé lors de la connexion à la session Linux depuis le Login Manager, la langue MUI installée dans WPS Office et la langue configurée dans ce fichier comptent aussi :

```
~/.config/Kingsoft/Office.conf
```

C’est pourquoi certains dictionnaires apparaissent dans la fenêtre `"Set language"`, mais ne corrigent pas l’orthographe. Le cas le plus clair est l’espagnol du Mexique : la MUI `es_MX` et le dictionnaire `es_MX` peuvent apparaître comme installés, mais lors des tests la correction orthographique n’a fonctionné qu’avec le dictionnaire `es_ES`.

### Tests confirmés

Voici les tests effectués jusqu’à présent :

| Correcteur       | Paramètre régional choisi dans le Login Manager    | Locale  | MUI utilisée dans WPS | Dictionnaire installé | État              |
| ---------------- | -------------------------------------------------- | ------- | --------------------- | --------------------- | ----------------- |
| Anglais          | `Anglais américain - États-Unis`                   | `en_US` | `en_US`               | `en_US` UTF-8         | Fonctionne        |
| Anglais          | `Anglais - Irlande`                                | `en_IE` | `en_US`               | `en_US` UTF-8         | Fonctionne        |
| Anglais          | `Anglais australien - Australie`                   | `en_AU` | `en_US`               | `en_US` UTF-8         | Fonctionne        |
| Anglais          | `Anglais britannique - Royaume-Uni`                | `en_GB` | `en_US`               | `en_US` UTF-8         | Fonctionne        |
| Anglais          | `Anglais - Nouvelle-Zélande`                       | `en_NZ` | `en_US`               | `en_US` UTF-8         | Ne fonctionne pas |
| Espagnol         | `Espagnol - Équateur`                              | `es_EC` | `es_ES`               | `es_ES` UTF-8         | Fonctionne        |
| Espagnol         | `Espagnol européen - Espagne`                      | `es_ES` | `es_ES`               | `es_ES` UTF-8         | Fonctionne        |
| Espagnol         | `Espagnol - États-Unis`                            | `es_US` | `es_ES`               | `es_ES` UTF-8         | Fonctionne        |
| Espagnol         | `Espagnol - Venezuela`                             | `es_VE` | `es_ES`               | `es_ES` UTF-8         | Fonctionne        |
| Espagnol         | `Espagnol mexicain - Mexique`                      | `es_MX` | `es_ES`               | `es_ES` UTF-8         | Fonctionne        |
| Espagnol         | `Espagnol - Pérou`                                 | `es_PE` | `es_ES`               | `es_ES` UTF-8         | Fonctionne        |
| Espagnol         | `Espagnol - Uruguay`                               | `es_UY` | `es_ES`               | `es_ES` UTF-8         | Fonctionne        |
| Espagnol Mexique | `Espagnol mexicain - Mexique`                      | `es_MX` | `es_MX`               | `es_MX` UTF-8         | Ne fonctionne pas |
| Allemand         | `Allemand autrichien - Autriche`                   | `de_AT` | `de_DE`               | `de_DE` ISO8859-1     | Fonctionne        |
| Allemand         | `Allemand - Allemagne`                             | `de_DE` | `de_DE`               | `de_DE` ISO8859-1     | Fonctionne        |
| Allemand         | `Allemand suisse - Suisse`                         | `de_CH` | `de_DE`               | `de_DE` ISO8859-1     | Fonctionne        |
| Français         | `Français - France`                                | `fr_FR` | `fr_FR`               | `fr_FR` UTF-8         | Fonctionne        |
| Français         | `Français canadien - Canada`                       | `fr_CA` | `fr_CA`               | `fr_FR` UTF-8         | Fonctionne        |
| Indonésien       | `Indonésien - Indonesia`                           | `id_ID` | `id_ID`               | `id_ID` ISO8859-1     | Fonctionne        |
| Polonais         | `Polonais - Pologne`                               | `pl_PL` | `pl_PL`               | `pl_PL` UTF-8         | Fonctionne        |
| Portugais BR     | `Portugais brésilien - Brésil`                     | `pt_BR` | `pt_BR`               | `pt_BR` UTF-8         | Fonctionne        |
| Portugais PT     | `Portugais européen - Portugal`                    | `pt_PT` | `pt_PT`               | `pt_PT` UTF-8         | Ne fonctionne pas |
| Portugais PT     | `Portugais européen - Portugal`                    | `pt_PT` | `pt_PT`               | `pt_BR` UTF-8         | Fonctionne        |
| Russe            | `Russe - Russie`                                   | `ru_RU` | `ru_RU`               | `ru_RU` UTF-8         | Fonctionne        |
| Turc             | `Turc - Turquie`                                   | `tr_TR` | `tr_TR`               | `tr_TR` UTF-8         | Fonctionne        |

L’encodage indiqué dans la colonne `Dictionnaire installé` provient de la ligne `SET` du fichier `main.aff` de chaque dictionnaire.

**Remarque sur `pl_PL`** : après avoir remplacé le dictionnaire par la version UTF-8 issue des anciens dictionnaires de WPS Office 11.2.0.9255, il a fallu le sélectionner manuellement dans `"Review"` > `"Spell Check ⌵"` > `"Set language"` > `"Polski"`. Après l’avoir sélectionné, la correction orthographique a fonctionné. Le dictionnaire polonais converti depuis LibreOffice n’a pas bien fonctionné parce qu’il était en `ISO8859-2`, comme on peut le voir dans son fichier `main.aff`.

**Remarque sur `pt_PT`** : avec la locale `pt_PT.UTF-8`, la MUI `pt_PT` et le dictionnaire `pt_PT`, WPS Office 12 n’a pas activé la correction orthographique. Dans cette même configuration, elle a fonctionné avec le dictionnaire `pt_BR`.

**Remarque sur `ru_RU`** : le correcteur a fonctionné dans un nouveau document créé depuis zéro. Dans un document créé à l’origine en anglais, même après avoir collé du texte russe traduit, WPS n’a pas appliqué correctement la correction orthographique au texte existant.

Sous MX Linux 23, la locale peut être vue dans le Login Manager : lorsque vous sélectionnez une langue dans la liste, le Login Manager affiche le code de locale. Par exemple, si vous cliquez sur :

```
Espagnol mexicain - Mexique
```

ceci apparaîtra :

```
es_MX
```

Si vous êtes déjà connecté et que vous voulez voir quelle locale votre système utilise, ouvrez un terminal et exécutez :

```bash
echo $LANG
```

Exemple :

```bash
$ echo $LANG
es_MX.UTF-8
```

### Liste des langues disponibles dans le Login Manager de MX Linux 23

Voici la liste observée dans le Login Manager de MX Linux 23 :

![](vx_images/20260717.1-MX-Linux-23_Login-Manager-lnguages-ezgif.com.gif)

Disponible sous forme de tableau avec les locales :

| Language in the Login Manager        | Locale  |
| ------------------------------------ | ------- |
| Arabe - Égypte                       | `ar_EG` |
| Biélorusse - Biélorussie             | `be_BY` |
| Bulgare - Bulgarie                   | `bg_BG` |
| Catalan - Espagne                    | `ca_ES` |
| Tchèque - République tchèque         | `cs_CZ` |
| Danois - Danemark                    | `da_DK` |
| Allemand autrichien - Autriche       | `de_AT` |
| Allemand suisse - Suisse             | `de_CH` |
| Allemand - Allemagne                 | `de_DE` |
| Grec - Grèce                         | `el_GR` |
| Anglais australien - Australie       | `en_AU` |
| Anglais canadien - Canada            | `en_CA` |
| Anglais britannique - Royaume-Uni    | `en_GB` |
| Anglais - Irlande                    | `en_IE` |
| Anglais - Nouvelle-Zélande           | `en_NZ` |
| Anglais américain - États-Unis       | `en_US` |
| Espagnol - Argentine                 | `es_AR` |
| Espagnol - Bolivie                   | `es_BO` |
| Espagnol - Colombie                  | `es_CO` |
| Espagnol - Équateur                  | `es_EC` |
| Espagnol européen - Espagne          | `es_ES` |
| Espagnol mexicain - Mexique          | `es_MX` |
| Espagnol - Nicaragua                 | `es_NI` |
| Espagnol - Panama                    | `es_PA` |
| Espagnol - Pérou                     | `es_PE` |
| Espagnol - États-Unis                | `es_US` |
| Espagnol - Uruguay                   | `es_UY` |
| Espagnol - Venezuela                 | `es_VE` |
| Estonien - Estonie                   | `et_EE` |
| Basque - Espagne                     | `eu_ES` |
| Persan - Iran                        | `fa_IR` |
| Finnois - Finlande                   | `fi_FI` |
| Français - Belgique                  | `fr_BE` |
| Français canadien - Canada           | `fr_CA` |
| Français suisse - Suisse             | `fr_CH` |
| Français - France                    | `fr_FR` |
| Irlandais - Irlande                  | `ga_IE` |
| Hébreu - Israël                      | `he_IL` |
| Croate - Croatie                     | `hr_HR` |
| Hongrois - Hongrie                   | `hu_HU` |
| Islandais - Islande                  | `is_IS` |
| Italien - Italie                     | `it_IT` |
| Japonais - Japon                     | `ja_JP` |
| Géorgien - Géorgie                   | `ka_GE` |
| Kazakh - Kazakhstan                  | `kk_KZ` |
| Coréen - Corée du Sud                | `ko_KR` |
| Lituanien - Lituanie                 | `lt_LT` |
| Letton - Lettonie                    | `lv_LV` |
| Macédonien - Macédoine               | `mk_MK` |
| Norvégien Bokmål - Norvège           | `nb_NO` |
| Flamand - Belgique                   | `nl_BE` |
| Néerlandais - Pays-Bas               | `nl_NL` |
| Norvégien Nynorsk - Norvège          | `nn_NO` |
| Polonais - Pologne                   | `pl_PL` |
| Portugais brésilien - Brésil         | `pt_BR` |
| Portugais européen - Portugal        | `pt_PT` |
| Roumain - Roumanie                   | `ro_RO` |
| Russe - Russie                       | `ru_RU` |
| Slovaque - Slovaquie                 | `sk_SK` |
| Slovène - Slovénie                   | `sl_SI` |
| Albanais - Albanie                   | `sq_AL` |
| Serbe - Serbie                       | `sr_RS` |
| Suédois - Suède                      | `sv_SE` |
| Turc - Turquie                       | `tr_TR` |
| Ukrainien - Ukraine                  | `uk_UA` |
| Chinois - Chine                      | `zh_CN` |
| Chinois - Taïwan                     | `zh_TW` |


## Faire fonctionner le correcteur orthographique anglais

Pour faire fonctionner le correcteur orthographique anglais, déconnectez-vous de MX Linux 23 et choisissez ceci dans le Login Manager :

```
Anglais américain - États-Unis
```

Modifiez ensuite :

```bash
gedit ~/.config/Kingsoft/Office.conf
```

et laissez ce contenu :

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

WPS Office 12 inclut déjà cette MUI par défaut :

```
/opt/kingsoft/wps-office/office6/mui/en_US
```

ainsi que le dictionnaire :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

### Activer la correction orthographique anglaise

Ouvrez maintenant WPS Writer. Allez dans l’onglet du ruban nommé :

`"Review"`

et là, dans

`"Spell Check ⌵"`

cliquez sur cette icône `"⌵"`, puis cliquez sur le sous-menu :

`"Set Spell Check language"`

![](vx_images/20260721.2-WPS_en-US_Home-Review-SpellCheck-SetLanguage-ezgif.com.gif)

dans la fenêtre qui s’ouvre, `"Anglais (États-Unis)"` fera partie des dictionnaires disponibles par défaut.

![](vx_images/dicts-tests/01-Set-Spell-Check-Language-English-United-States.png)


si vous le souhaitez, vous pouvez cliquer sur `"Change Default"`, bien qu’il soit déjà sélectionné par défaut parce que la MUI `en_US` était déjà installée.

Maintenant, dans le coin inférieur gauche de la fenêtre, regardez la barre d’état ; un indicateur similaire à celui-ci apparaîtra :

`Spell Check: Disabled ⌵`

Cliquez sur cet indicateur et il passera à `"Enabled"`.

De plus, si vous cliquez sur l’icône `"⌵"`, cette option et d’autres seront disponibles dans un menu déroulant.

Une fois activé, WPS Office commencera automatiquement à vérifier l’orthographe du document. À partir de ce moment, les mots mal orthographiés seront soulignés ; un clic droit sur un mot souligné affichera des suggestions de correction. Le correcteur restera activé jusqu’à ce que l’utilisateur désactive de nouveau cette option :


![](vx_images/20260721.1-Quotes-MUI-en-US-Richard-Stallman-ezgif.com.gif)

---

## Faire fonctionner le correcteur orthographique espagnol

Pour faire fonctionner le correcteur orthographique espagnol, déconnectez-vous de MX Linux 23 (si vous êtes dans une autre langue) et choisissez, par exemple, ceci dans le Login Manager :

```
Espagnol - Équateur
```

Modifiez ensuite :

```bash
gedit ~/.config/Kingsoft/Office.conf
```

et laissez ce contenu pour l’espagnol d’Espagne :

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Dans cette configuration, cette MUI doit être installée :

```
/opt/kingsoft/wps-office/office6/mui/es_ES
```

et le dictionnaire :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
```


### Activer la correction orthographique espagnole

Ouvrez WPS Writer. Allez dans l’onglet du ruban nommé :

`"Revisar"`

et là, dans

`"Revisión ortográfica ⌵"`

cliquez sur cette icône `"⌵"`, puis cliquez sur le sous-menu :

`"Establecer idioma"`

et dans la fenêtre qui s’ouvre, `"Español (España)"` fera partie des dictionnaires disponibles par défaut.

et cliquez sur `"Establecer predeterminado"`, bien qu’il soit déjà sélectionné par défaut parce que la MUI `es_ES` était déjà installée.

Maintenant, dans le coin inférieur gauche de la fenêtre, regardez la barre d’état ; un indicateur similaire à celui-ci apparaîtra :

`Revisión ortográfica: Desactivado ⌵`

Cliquez sur cet indicateur et il passera à `"Activado"`.

![](vx_images/20260716.1-Frases-MUI-es-ES-Richard-Stallman-ezgif.com.gif)

De plus, si vous cliquez sur l’icône `"⌵"`, cette option et d’autres seront disponibles dans un menu déroulant.

Une fois la correction orthographique activée, WPS Office commencera automatiquement à vérifier l’orthographe du document. À partir de ce moment, les mots mal orthographiés seront soulignés ; un clic droit sur un mot souligné affichera des suggestions de correction. Le correcteur restera activé jusqu’à ce que l’utilisateur désactive de nouveau cette option :

Pour l’instant, dans cette version chinoise de WPS Office 12, la correction orthographique espagnole ne fonctionne qu’avec le dictionnaire `es_ES` de ce dépôt :

/build/wps-office-12-dicts-active/es_ES/

Cependant, les dictionnaires suivants du dossier `wps-libreoffice-dicts` ne fonctionnent pas comme ils fonctionnaient dans WPS Office 11 :

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

### Paramètres régionaux espagnols restant à tester

Ces paramètres régionaux du Login Manager doivent encore être testés avec le correcteur espagnol :

```
Espagnol - Argentine
Espagnol - Bolivie
Espagnol - Colombie
Espagnol - Nicaragua
Espagnol - Panama
```

Les autres qui ont fonctionné sont indiqués plus haut dans le tableau.

## Test du dictionnaire espagnol du Mexique qui n’a pas fonctionné

J’ai effectué le test suivant parce que la MUI `es_MX` et le dictionnaire de correction orthographique `es_MX` sont tous deux disponibles.

Le test a consisté à se connecter depuis le Login Manager avec :

```
Espagnol mexicain - Mexique
```

et à configurer WPS avec :

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Avec la MUI :

```
/opt/kingsoft/wps-office/office6/mui/es_MX
```

et le dictionnaire dans :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_MX/
```

WPS affiche `"Español (México)"` dans la fenêtre de langue, mais la correction orthographique ne fonctionne pas. En revanche, si le dictionnaire `"Español (España)"` est sélectionné dans cette même fenêtre, elle fonctionne.

## Faire fonctionner le correcteur orthographique allemand

Pour l’allemand, déconnectez-vous et choisissez ceci dans le Login Manager :

```
Allemand - Allemagne
```

Configurez ensuite `Office.conf` ainsi :

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

L’activation est similaire à celle du dictionnaire anglais :

![](vx_images/Quotes-tests/Deutsch-de_DE-Richard-S-ezgif.com.gif)

Dans ce test, ceci a fonctionné :

```
/opt/kingsoft/wps-office/office6/mui/de_DE
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

## Faire fonctionner le correcteur orthographique français

Pour le français, déconnectez-vous et choisissez ceci dans le Login Manager :

```
Français - France
```

L’activation est similaire à celle du dictionnaire anglais.


![](vx_images/Quotes-tests/citation_fr-FR_Richard_S-ezgif.com.gif)

Configurez ensuite `Office.conf` ainsi :

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Dans ce test, cela a fonctionné avec :

```
/opt/kingsoft/wps-office/office6/mui/fr_FR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
```



## Faire fonctionner le correcteur orthographique indonésien

Pour l’indonésien, générez d’abord la locale si elle n’apparaît pas encore dans le Login Manager :

```bash
sudo dpkg-reconfigure locales
```

Dans la liste, cochez :

```
id_ID.UTF-8 UTF-8
```

Déconnectez-vous ensuite et choisissez ceci dans le Login Manager :

```
Indonésien - Indonesia
```

Configurez ensuite `Office.conf` ainsi :

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

L’activation est similaire à celle du dictionnaire anglais. `"Indonésien"` doit apparaître dans la fenêtre de langue de correction orthographique.

![](vx_images/Quotes-tests/Kutipan-id_ID-Richard-S-ezgif.com.gif)

Dans ce test, cela a fonctionné avec :

```
/opt/kingsoft/wps-office/office6/mui/id_ID
/opt/kingsoft/wps-office/office6/dicts/spellcheck/id_ID/
```

Remarque : bien que la session Linux utilise `id_ID.UTF-8`, le dictionnaire `id_ID` installé utilise `SET ISO8859-1` dans `main.aff` et a fonctionné correctement dans WPS Office 12.

## Faire fonctionner le correcteur orthographique polonais

Pour le polonais, déconnectez-vous et choisissez ceci dans le Login Manager :

```
Polonais - Pologne
```

Configurez ensuite `Office.conf` ainsi :

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

L’activation est similaire à celle du dictionnaire anglais. `"Polski"` doit apparaître dans la fenêtre de langue de correction orthographique.

![](vx_images/Quotes-tests/Cytaty_pl-PL_RichardS-ezgif.com.gif)


Dans ce test, cela a fonctionné avec :

```
/opt/kingsoft/wps-office/office6/mui/pl_PL
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pl_PL/
```

Remarque : pour ce test, le dictionnaire `pl_PL` en UTF-8 provenant des anciens dictionnaires de WPS Office 11.2.0.9255 a fonctionné. Le dictionnaire converti depuis LibreOffice était en `ISO8859-2` et n’a pas bien fonctionné dans WPS Office 12.

## Faire fonctionner le correcteur orthographique portugais brésilien

Pour le portugais brésilien, déconnectez-vous et choisissez ceci dans le Login Manager :

```
Portugais brésilien - Brésil
```

Configurez ensuite `Office.conf` ainsi :

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

L’activation est similaire à celle du dictionnaire anglais. `"Português do Brasil"` doit apparaître dans la fenêtre de langue de correction orthographique.

![](vx_images/Quotes-tests/Citacoes_pt-BR_Richard_S-ezgif.com.gif)

Dans ce test, cela a fonctionné avec :

```
/opt/kingsoft/wps-office/office6/mui/pt_BR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Remarque : bien que la MUI `pt_BR` contienne `FallBack=pt_PT` dans `lang.conf`, WPS a corrigé correctement lorsque `"Português do Brasil"` a été sélectionné dans la fenêtre de langue de correction orthographique. Si `"Português (Portugal)"` est sélectionné dans cette même session, le correcteur ne fonctionne pas.

## Test du dictionnaire portugais du Portugal qui n’a pas fonctionné

J’ai effectué le test suivant parce que la MUI `pt_PT` et le dictionnaire de correction orthographique `pt_PT` sont tous deux disponibles.

Le test a consisté à se connecter depuis le Login Manager avec :

```
Portugais européen - Portugal
```

et à configurer WPS avec :

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Avec la MUI :

```
/opt/kingsoft/wps-office/office6/mui/pt_PT
```

et le dictionnaire dans :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/
```

WPS affichait `"Portuguê"` avant la correction du nom du dictionnaire, et maintenant il devrait afficher `"Português (Portugal)"` ; dans les deux cas, la correction orthographique n’a pas fonctionné avec le dictionnaire `pt_PT`.

Dans cette même configuration avec la locale `pt_PT.UTF-8` et la MUI `pt_PT`, la correction orthographique a fonctionné avec le dictionnaire portugais brésilien :

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

## Faire fonctionner le correcteur orthographique russe

Pour le russe, déconnectez-vous et choisissez ceci dans le Login Manager :

```
Russe - Russie
```

Configurez ensuite `Office.conf` ainsi :

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

L’activation est similaire à celle du dictionnaire anglais. `"Русский (Россия)"` doit apparaître dans la fenêtre de langue de correction orthographique.

![](vx_images/Quotes-tests/Frase_ru_RU_RichardS-ezgif.com.gif)


Dans ce test, cela a fonctionné avec :

```
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

Remarque : le correcteur russe a fonctionné correctement dans un nouveau document créé depuis zéro. Dans un document créé à l’origine en anglais, même après avoir collé du texte russe traduit, WPS n’a pas appliqué correctement la correction orthographique au texte existant.

## Faire fonctionner le correcteur orthographique turc

Pour le turc, déconnectez-vous et choisissez ceci dans le Login Manager :

```
Turc - Turquie
```

Configurez ensuite `Office.conf` ainsi :

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

L’activation est similaire à celle du dictionnaire anglais. `"Türkçe (Türkiye)"` doit apparaître dans la fenêtre de langue de correction orthographique.

![](vx_images/Quotes-tests/Alntlar-tr_TR-Richard-S-ezgif.com.gif)

Dans ce test, cela a fonctionné avec :

```
/opt/kingsoft/wps-office/office6/mui/tr_TR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/tr_TR/
```

## Référence : paquets MUI téléchargés par WPS sous Windows

Si vous êtes curieux et vous demandez d’où viennent les fichiers MUI de l’interface graphique, je les ai obtenus sous Microsoft Windows 10. WPS Office télécharge les paquets de langue dans des chemins utilisateur ; cette information sert de référence pour rechercher les fichiers de langue de l’interface.

Téléchargez et installez d’abord WPS Office 12 pour Windows :

[https://wps.com/office/windows/](https://wps.com/office/windows/)

Exemple sous Windows 10 :

![](vx_images/02-WPS-Office-global-config-menu.png)

Téléchargez ensuite les langues :

![](vx_images/03-Click-on-a-language-and-then-click-Apply.png)

Les langues téléchargées peuvent apparaître dans :

```
C:\Users\youruser\AppData\Roaming\kingsoft\wps_intl\addons\pool\win-x64
```

![](vx_images/04-downloaded-languages.png)

La liste des langues peut apparaître dans :

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui\lang_list\lang_list.json
```

![20260416-000808](vx_images/507184629680596.png)

Certains paquets inclus par la version Windows en espagnol peuvent apparaître dans :

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui
```

![](vx_images/05-languages-downloaded-by-the-Spanish-version.png)

Si ce projet vous a aidé, vous pouvez laisser une étoile au dépôt.

---

# Remerciements

À l’utilisateur [mmvill](https://github.com/mmvill), qui m’a écrit et m’a dit qu’il avait trouvé une façon de faire fonctionner le dictionnaire de correction orthographique espagnol dans WPS Office 12.
