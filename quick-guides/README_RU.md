# Краткое руководство: русская проверка орфографии в WPS Office 12 для Linux

Это краткое руководство устанавливает русский интерфейс и русскую проверку орфографии для WPS Office 12 в Linux.

## Требования

- WPS Office 12.x установлен.
- Этот репозиторий скачан или клонирован.
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

## Установить MUI и словари

Из корня этого репозитория выполните:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
sudo cp -r build/dicts-active/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Для русского языка используйте:

```text
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

## Настроить WPS Office

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
