# Краткое руководство: русская проверка орфографии в WPS Office 12 для Linux

Это краткое руководство настраивает русский интерфейс и устанавливает русскую проверку орфографии для WPS Office 12 в Linux.

## Требования

- WPS Office 12.x установлен.
- Есть подключение к интернету для скачивания файлов Release.
- Есть права администратора через `sudo`.
- WPS Office был открыт хотя бы один раз, чтобы существовал файл `~/.config/Kingsoft/Office.conf`.

## Установить WPS Office

Скачайте WPS Office 12 для Linux с официального китайского сайта:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Пакет `.deb` можно установить через установщик пакетов:

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

или из терминала:

```bash
sudo dpkg -i wps-office*.deb
```

## Скачать файл Release

Перейдите в раздел Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

Скачайте файл:

```text
wps-office-12-dicts-active.tar.xz
```

![](../vx_images/09-release-wps-12.1.2-language-packs-v1.png)

## Установить словарь

WPS Office 12 уже включает русский MUI по умолчанию:

```text
/opt/kingsoft/wps-office/office6/mui/ru_RU
```

Поэтому для русского языка нужно установить только словарь проверки орфографии.

Распакуйте `wps-office-12-dicts-active.tar.xz` правым щелчком мыши в вашем предпочитаемом файловом менеджере. Вы получите папку:

```text
wps-office-12-dicts-active
```

Откройте терминал внутри этой папки. В современных системах Linux при правом щелчке внутри папки обычно есть пункт вроде `Open terminal here`.

Выполните:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Для русского языка WPS Office 12 будет использовать:

```text
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

## Настроить WPS Office

Если Gedit не установлен, сначала установите его:

```bash
sudo apt install gedit
```

Отредактируйте:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Используйте это содержимое:

```ini
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Полностью закройте WPS Office и откройте его снова.

## Включить проверку орфографии

В WPS Writer выберите `Русский (Россия)` как язык проверки орфографии и сделайте его языком по умолчанию, если нужно.

![](../vx_images/Quotes-tests/Frase_ru_RU_RichardS-ezgif.com.gif)
