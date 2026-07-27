# Языковые пакеты WPS Office 12.x для Linux

Доступные переводы:

- [Английский](README.md), доступно для англоязычных пользователей.
- [Español](README_ES.md), доступно для испаноязычных пользователей.
- [Deutsch](README_DE.md), доступно для немецкоязычных пользователей.
- [Français](README_FR.md), доступно для франкоязычных пользователей.
- [Bahasa Indonesia](README_ID.md), доступно для пользователей индонезийского языка.
- [Português do Brasil](README_PT_BR.md), доступно для пользователей бразильского португальского языка.

## Скачать китайскую версию WPS Office 12 для Linux

Скачайте установщик WPS Office для вашего дистрибутива Linux, основанного на DEB или RPM.

Официальный китайский сайт:

- [https://www.wps.cn](https://www.wps.cn)

при нажатии происходит перенаправление на:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Затем установите пакет.

**Загрузка с зеркала**
Однако там может не быть самых последних версий, либо их загрузка туда может занимать некоторое время:

[https://mirrors.163.com/ubuntukylin/pool/partner/](https://mirrors.163.com/ubuntukylin/pool/partner/)

### Установить DEB-пакет с помощью установщика DEB-пакетов

Установите его с помощью менеджера DEB-пакетов. В Linux-системах один из таких инструментов обычно уже установлен; щелкните файл правой кнопкой мыши в файловом менеджере и установите его этим инструментом:

![](vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

### Установить из терминала (необязательно)

Если вы используете Debian, Ubuntu, Linux Mint или похожие дистрибутивы, это также можно сделать из терминала:

```bash
sudo dpkg -i wps-office*.deb
```

Если вы используете Fedora, Red Hat или похожие дистрибутивы:

```bash
sudo dnf install wps-office*.rpm
```

## Требования

Для продолжения этого руководства вам нужно:

- Иметь установленный **WPS Office 12.x** в Linux, как описано выше.
- Иметь права администратора через `sudo` или аналогичный инструмент.
- Открыть WPS Office хотя бы один раз. WPS Office создает пользовательскую конфигурацию после первого запуска. Если `~/.config/Kingsoft/Office.conf` не существует, откройте WPS Office, закройте его и продолжайте установку.
- Иметь подключение к интернету для скачивания файлов Release.

## Установить многоязычные пользовательские интерфейсы MUI

Скачайте пакет MUI. Перейдите в раздел Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

скачайте файл:

wps-office-12-mui.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Распакуйте его правым щелчком мыши **в вашем предпочитаемом файловом менеджере**, после этого появится папка:

`wps-office-12-mui`

Затем щелкните правой кнопкой мыши по этой папке и выберите `Open terminal here` или похожий пункт. В современных системах Linux такая опция обычно появляется при правом щелчке. После этого, из этой папки

установите файлы MUI такой командой:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

Эта команда устанавливает файлы MUI (многоязычные пользовательские интерфейсы).

## Проверить установку

Команда `sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/` копирует доступные языковые папки в реальную папку WPS Office в Linux: `/opt/kingsoft/wps-office/office6/mui/`.

Китайская версия WPS Office 12, которую мы только что установили, по умолчанию включает эти папки MUI:

```
/opt/kingsoft/wps-office/office6/mui/en_US
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/mui/zh_CN
```

Это:

- `en_US` английский (США) язык
- `ru_RU` русский (Российская Федерация) язык
- `zh_CN` китайский (Китай) язык

а также по умолчанию включает эти два словаря проверки орфографии:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_CH
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US
```

Это:

- `en_CH` китайский и английский (США) словарь
- `en_US` английский (США) словарь

В файловом менеджере проверьте этот путь:

/opt/kingsoft/wps-office/office6/mui/

Кроме языков, включенных в китайскую версию, у вас должно быть следующее:

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

Также копируется:

```
lang_list
```

Это список выбора.


## Доступные и протестированные словари

Этот репозиторий также подготавливает словари Hunspell, чтобы **WPS Office 12.x** мог использовать их в Linux.

На данный момент нужно различать две папки:

```
build/wps-office-12-dicts-active/
wps-libreoffice-dicts/
```

Папка `build/wps-office-12-dicts-active/` содержит словари, выбранные для текущей установки. Именно они используются для тестирования WPS Office 12.

Папка `wps-libreoffice-dicts/` содержит все словари, преобразованные из LibreOffice. Она хранится в корне репозитория, потому что в китайской версии WPS Office 12 не все варианты работают, даже если имеют правильный формат. Возможно, в будущей версии WPS снова будет поддерживать все эти словари, как это было в старых версиях WPS Office для Linux.

Каждая папка словаря имеет формат, ожидаемый WPS:

```
dict.conf
main.aff
main.dic
```

Файлы `main.aff` и `main.dic` в основном взяты из коллекции словарей LibreOffice:

```
third-party/libreoffice-dictionaries-collection/dicts/
```

Исходный репозиторий:

[https://github.com/wachin/libreoffice-dictionaries-collection](https://github.com/wachin/libreoffice-dictionaries-collection)

Файлы `dict.conf` повторно используются из старых словарей WPS Office, если они существуют, и создаются для новых вариантов.

Важное исключение: активный словарь `pl_PL` взят из старых словарей WPS Office 11.2.0.9255:

```
third-party/wps-office-11.2.0.9255-dicts/dicts/pl_PL/
```

Исходный репозиторий:

[https://github.com/wachin/wps-office-11.2.0.9255-dicts](https://github.com/wachin/wps-office-11.2.0.9255-dicts)

Этот `pl_PL` используется потому, что польский словарь, преобразованный из LibreOffice, плохо работал в WPS Office 12. Его файл `main.aff` содержит:

```
SET ISO8859-2
```

Напротив, старый польский словарь WPS использует UTF-8, и его `main.aff` содержит:

```
SET UTF-8
```

Текущие активные словари:

| Код     | Словарь                  |
| ------- | ------------------------ |
| `de_DE` | Немецкий (Германия)      |
| `es_ES` | Испанский (Испания)      |
| `fr_FR` | Французский (Франция)    |
| `id_ID` | Индонезийский            |
| `pl_PL` | Польский                 |
| `pt_BR` | Португальский (Бразилия) |
| `pt_PT` | Португальский            |
| `ru_RU` | Русский (Россия)         |
| `tr_TR` | Турецкий (Турция)        |

Примечание о `pt_PT`: в MX Linux 23 с locale `pt_PT.UTF-8`, MUI `pt_PT` и словарем, установленным как `/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/`, WPS Office 12 в текущих тестах не включает проверку орфографии для португальского языка Португалии. В той же установке проверка орфографии работает со словарем `pt_BR`.


## Установить словари

Перейдите в раздел Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

скачайте файл:

wps-office-12-dicts-active.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Распакуйте его правым щелчком мыши в вашем предпочитаемом файловом менеджере, после этого появится папка:

`wps-office-12-dicts-active`

Затем щелкните правой кнопкой мыши по этой папке и выберите `Open terminal here` или похожий пункт. В современных системах Linux такая опция обычно появляется при правом щелчке. После этого, из этой папки

установите файлы словарей такой командой:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Это копирует активные словари в папку, которую WPS использует для проверки орфографии.

После копирования путь WPS должен содержать такие папки:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

И внутри каждой из них:

```
dict.conf
main.aff
main.dic
```

## Включить язык интерфейса в конфигурации WPS

Если вы разработчик, отредактируйте файл конфигурации с помощью nano:

```bash
nano ~/.config/Kingsoft/Office.conf
```

Если вы обычный пользователь, используйте Gedit или другой текстовый редактор. Если Gedit не установлен, установите его так:

```bash
sudo apt install gedit
```

и введите это в терминале:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Когда файл откроется, выделите весь текст в нем с помощью `Ctrl + A`, удалите его и замените содержимым для языка, который хотите использовать.

Структура всегда одинаковая:

```
[General]
languages=КОД_ЯЗЫКА

[6.0]
common\DefaultLanguage=НОМЕР_ЯЗЫКА
common\Local\UILanguage=НОМЕР_ЯЗЫКА
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Используйте эту таблицу, чтобы выбрать правильный код и номер:

| Язык                              | `languages=` | `DefaultLanguage` и `UILanguage`   |
| --------------------------------- | ------------ | ---------------------------------- |
| Английский (США)                  | `en_US`      | `1033`                             |
| Немецкий (Германия)               | `de_DE`      | `1031`                             |
| Испанский (Испания)               | `es_ES`      | `3082`                             |
| Испанский (Мексика)               | `es_MX`      | `2058`                             |
| Французский (Канада)              | `fr_CA`      | `3084`                             |
| Французский (Франция)             | `fr_FR`      | `1036`                             |
| Индонезийский                     | `id_ID`      | `1057`                             |
| Японский                          | `ja_JP`      | `1041`                             |
| Польский                          | `pl_PL`      | `1045`                             |
| Португальский (Бразилия)          | `pt_BR`      | `1046`                             |
| Португальский (Португалия)        | `pt_PT`      | `2070`                             |
| Русский                           | `ru_RU`      | `1049`                             |
| Тайский                           | `th_TH`      | `1054`                             |
| Турецкий                          | `tr_TR`      | `1055`                             |
| Китайский (упрощенный, Китай)     | `zh_CN`      | `2052`                             |
| Китайский (традиционный, Гонконг) | `zh_HK`      | `3076`                             |

### Краткая таблица: locale, MUI и словарь с одним кодом

Эта таблица показывает языки, для которых можно напрямую сравнить, используют ли `Locale`, MUI и словарь один и тот же код. `x` означает, что активный словарь с таким же кодом не включен. Символ `✅` отмечает протестированные случаи, в которых эта точная комбинация работает.

| Язык, показанный в Login Manager     | `Locale` | `MUI`    | `Dict`  | Проверено |
| ------------------------------------ | -------- | -------- | ------- | --------- |
| Английский (США)                     | `en_US`  | `en_US`  | `en_US` | ✅         |
| Немецкий (Германия)                  | `de_DE`  | `de_DE`  | `de_DE` | ✅         |
| Испанский (Испания)                  | `es_ES`  | `es_ES`  | `es_ES` | ✅         |
| Испанский (Мексика)                  | `es_MX`  | `es_MX`  | x       |           |
| Французский (Канада)                 | `fr_CA`  | `fr_CA`  | x       |           |
| Французский (Франция)                | `fr_FR`  | `fr_FR`  | `fr_FR` | ✅         |
| Индонезийский                        | `id_ID`  | `id_ID`  | `id_ID` | ✅         |
| Японский                             | `ja_JP`  | `ja_JP`  | x       |           |
| Польский                             | `pl_PL`  | `pl_PL`  | `pl_PL` | ✅         |
| Португальский (Бразилия)             | `pt_BR`  | `pt_BR`  | `pt_BR` | ✅         |
| Португальский (Португалия)           | `pt_PT`  | `pt_PT`  | `pt_PT` |           |
| Русский                              | `ru_RU`  | `ru_RU`* | `ru_RU` | ✅         |
| Тайский                              | `th_TH`  | `th_TH`  | x       |           |
| Турецкий                             | `tr_TR`  | `tr_TR`  | `tr_TR` | ✅         |
| Китайский (упрощенный, Китай)        | `zh_CN`  | `zh_CN`  | x       |           |
| Китайский (традиционный, Гонконг)    | `zh_HK`  | `zh_HK`  | x       |           |

* Китайская версия WPS Office 12 уже включает MUI `ru_RU` по умолчанию, поэтому архив MUI из Release не должен включать эту папку. Словарь проверки орфографии `ru_RU` все равно устанавливается из архива словарей.

### Для английского США:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для испанского из Испании:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для немецкого из Германии:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


### Для испанского из Мексики:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для французского из Канады:

```
[General]
languages=fr_CA

[6.0]
common\DefaultLanguage=3084
common\Local\UILanguage=3084
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для французского из Франции:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для индонезийского:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для японского:

```
[General]
languages=ja_JP

[6.0]
common\DefaultLanguage=1041
common\Local\UILanguage=1041
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для польского:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для бразильского португальского:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для португальского из Португалии:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для русского:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для тайского:

```
[General]
languages=th_TH

[6.0]
common\DefaultLanguage=1054
common\Local\UILanguage=1054
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для турецкого:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для упрощенного китайского из Китая:

```
[General]
languages=zh_CN

[6.0]
common\DefaultLanguage=2052
common\Local\UILanguage=2052
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Для традиционного китайского из Гонконга:

```
[General]
languages=zh_HK

[6.0]
common\DefaultLanguage=3076
common\Local\UILanguage=3076
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


Сохраните файл, полностью закройте WPS Office и откройте его снова. Если язык настроен правильно, интерфейс откроется на выбранном языке.

## Решение для работы средств проверки орфографии в WPS Office 12

В китайской версии WPS Office 12 недостаточно просто скопировать словарь в эту папку:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Также важны региональные настройки, выбранные при входе в сеанс Linux через Login Manager, язык MUI, установленный в WPS Office, и язык, настроенный в этом файле:

```
~/.config/Kingsoft/Office.conf
```

Поэтому некоторые словари появляются в окне `"Set language"`, но не выполняют проверку орфографии. Самый ясный пример — испанский из Мексики: MUI `es_MX` и словарь `es_MX` могут отображаться как установленные, но в тестах проверка орфографии работала только со словарем `es_ES`.

### Подтвержденные тесты

Вот тесты, выполненные на данный момент:

| Проверка орфографии | Региональная настройка, выбранная в Login Manager  | Locale  | MUI в WPS        | Установленный словарь | Статус        |
| ------------------- | -------------------------------------------------- | ------- | ---------------- | --------------------- | ------------- |
| Английский          | `Американский английский - США`                    | `en_US` | `en_US`          | `en_US` UTF-8         | Работает      |
| Английский          | `Английский - Ирландия`                            | `en_IE` | `en_US`          | `en_US` UTF-8         | Работает      |
| Английский          | `Австралийский английский - Австралия`             | `en_AU` | `en_US`          | `en_US` UTF-8         | Работает      |
| Английский          | `Британский английский - Великобритания`           | `en_GB` | `en_US`          | `en_US` UTF-8         | Работает      |
| Английский          | `Английский - Новая Зеландия`                      | `en_NZ` | `en_US`          | `en_US` UTF-8         | Не работает   |
| Испанский           | `Испанский - Эквадор`                              | `es_EC` | `es_ES`          | `es_ES` UTF-8         | Работает      |
| Испанский           | `Европейский испанский - Испания`                  | `es_ES` | `es_ES`          | `es_ES` UTF-8         | Работает      |
| Испанский           | `Испанский - США`                                  | `es_US` | `es_ES`          | `es_ES` UTF-8         | Работает      |
| Испанский           | `Испанский - Венесуэла`                            | `es_VE` | `es_ES`          | `es_ES` UTF-8         | Работает      |
| Испанский           | `Мексиканский испанский - Мексика`                 | `es_MX` | `es_ES`          | `es_ES` UTF-8         | Работает      |
| Испанский           | `Испанский - Перу`                                 | `es_PE` | `es_ES`          | `es_ES` UTF-8         | Работает      |
| Испанский           | `Испанский - Уругвай`                              | `es_UY` | `es_ES`          | `es_ES` UTF-8         | Работает      |
| Испанский Мексики   | `Мексиканский испанский - Мексика`                 | `es_MX` | `es_MX`          | `es_MX` UTF-8         | Не работает   |
| Немецкий            | `Австрийский немецкий - Австрия`                   | `de_AT` | `de_DE`          | `de_DE` ISO8859-1     | Работает      |
| Немецкий            | `Немецкий - Германия`                              | `de_DE` | `de_DE`          | `de_DE` ISO8859-1     | Работает      |
| Немецкий            | `Швейцарский верхненемецкий - Швейцария`           | `de_CH` | `de_DE`          | `de_DE` ISO8859-1     | Работает      |
| Французский         | `Французский - Франция`                            | `fr_FR` | `fr_FR`          | `fr_FR` UTF-8         | Работает      |
| Французский         | `Канадский французский - Канада`                   | `fr_CA` | `fr_CA`          | `fr_FR` UTF-8         | Работает      |
| Индонезийский       | `Индонезийский - Indonesia`                        | `id_ID` | `id_ID`          | `id_ID` ISO8859-1     | Работает      |
| Польский            | `Польский - Польша`                                | `pl_PL` | `pl_PL`          | `pl_PL` UTF-8         | Работает      |
| Португальский BR    | `Бразильский португальский - Бразилия`             | `pt_BR` | `pt_BR`          | `pt_BR` UTF-8         | Работает      |
| Португальский PT    | `Европейский португальский - Португалия`           | `pt_PT` | `pt_PT`          | `pt_PT` UTF-8         | Не работает   |
| Португальский PT    | `Европейский португальский - Португалия`           | `pt_PT` | `pt_PT`          | `pt_BR` UTF-8         | Работает      |
| Русский             | `Русский - Россия`                                 | `ru_RU` | `ru_RU`          | `ru_RU` UTF-8         | Работает      |
| Турецкий            | `Турецкий - Турция`                                | `tr_TR` | `tr_TR`          | `tr_TR` UTF-8         | Работает      |

Кодировка, указанная в столбце `Установленный словарь`, берется из строки `SET` файла `main.aff` каждого словаря.

**Примечание о `pl_PL`**: после замены словаря на UTF-8-версию из старых словарей WPS Office 11.2.0.9255 его пришлось выбрать вручную в `"Review"` > `"Spell Check ⌵"` > `"Set language"` > `"Polski"`. После выбора проверка орфографии заработала. Польский словарь, преобразованный из LibreOffice, работал плохо, потому что был в `ISO8859-2`, как видно в его файле `main.aff`.

**Примечание о `pt_PT`**: с locale `pt_PT.UTF-8`, MUI `pt_PT` и словарем `pt_PT` WPS Office 12 не включил проверку орфографии. В той же конфигурации она работала со словарем `pt_BR`.

**Примечание о `ru_RU`**: проверка орфографии работала в новом документе, созданном с нуля. В документе, изначально созданном на английском, даже после вставки переведенного русского текста WPS не применил проверку орфографии к существующему тексту корректно.

В MX Linux 23 locale можно увидеть в Login Manager: когда вы выбираете язык из списка, Login Manager показывает код locale. Например, если нажать:

```
Мексиканский испанский - Мексика
```

появится:

```
es_MX
```

Если вы уже вошли в сеанс и хотите узнать, какую locale использует система, откройте терминал и выполните:

```bash
echo $LANG
```

Пример:

```bash
$ echo $LANG
es_MX.UTF-8
```

### Список языков, доступных в Login Manager MX Linux 23

Это список, наблюдавшийся в Login Manager MX Linux 23:

![](vx_images/20260717.1-MX-Linux-23_Login-Manager-lnguages-ezgif.com.gif)

Доступно как таблица с locale:

| Language in the Login Manager          | Locale  |
| -------------------------------------- | ------- |
| Арабский - Египет                      | `ar_EG` |
| Белорусский - Беларусь                 | `be_BY` |
| Болгарский - Болгария                  | `bg_BG` |
| Каталанский - Испания                  | `ca_ES` |
| Чешский - Чехия                        | `cs_CZ` |
| Датский - Дания                        | `da_DK` |
| Австрийский немецкий - Австрия         | `de_AT` |
| Швейцарский верхненемецкий - Швейцария | `de_CH` |
| Немецкий - Германия                    | `de_DE` |
| Греческий - Греция                     | `el_GR` |
| Австралийский английский - Австралия   | `en_AU` |
| Канадский английский - Канада          | `en_CA` |
| Британский английский - Великобритания | `en_GB` |
| Английский - Ирландия                  | `en_IE` |
| Английский - Новая Зеландия            | `en_NZ` |
| Американский английский - США          | `en_US` |
| Испанский - Аргентина                  | `es_AR` |
| Испанский - Боливия                    | `es_BO` |
| Испанский - Колумбия                   | `es_CO` |
| Испанский - Эквадор                    | `es_EC` |
| Европейский испанский - Испания        | `es_ES` |
| Мексиканский испанский - Мексика       | `es_MX` |
| Испанский - Никарагуа                  | `es_NI` |
| Испанский - Панама                     | `es_PA` |
| Испанский - Перу                       | `es_PE` |
| Испанский - США                        | `es_US` |
| Испанский - Уругвай                    | `es_UY` |
| Испанский - Венесуэла                  | `es_VE` |
| Эстонский - Эстония                    | `et_EE` |
| Баскский - Испания                     | `eu_ES` |
| Персидский - Иран                      | `fa_IR` |
| Финский - Финляндия                    | `fi_FI` |
| Французский - Бельгия                  | `fr_BE` |
| Канадский французский - Канада         | `fr_CA` |
| Швейцарский французский - Швейцария    | `fr_CH` |
| Французский - Франция                  | `fr_FR` |
| Ирландский - Ирландия                  | `ga_IE` |
| Иврит - Израиль                        | `he_IL` |
| Хорватский - Хорватия                  | `hr_HR` |
| Венгерский - Венгрия                   | `hu_HU` |
| Исландский - Исландия                  | `is_IS` |
| Итальянский - Италия                   | `it_IT` |
| Японский - Япония                      | `ja_JP` |
| Грузинский - Грузия                    | `ka_GE` |
| Казахский - Казахстан                  | `kk_KZ` |
| Корейский - Южная Корея                | `ko_KR` |
| Литовский - Литва                      | `lt_LT` |
| Латышский - Латвия                     | `lv_LV` |
| Македонский - Македония                | `mk_MK` |
| Норвежский Bokmål - Норвегия           | `nb_NO` |
| Фламандский - Бельгия                  | `nl_BE` |
| Нидерландский - Нидерланды             | `nl_NL` |
| Норвежский Nynorsk - Норвегия          | `nn_NO` |
| Польский - Польша                      | `pl_PL` |
| Бразильский португальский - Бразилия   | `pt_BR` |
| Европейский португальский - Португалия | `pt_PT` |
| Румынский - Румыния                    | `ro_RO` |
| Русский - Россия                       | `ru_RU` |
| Словацкий - Словакия                   | `sk_SK` |
| Словенский - Словения                  | `sl_SI` |
| Албанский - Албания                    | `sq_AL` |
| Сербский - Сербия                      | `sr_RS` |
| Шведский - Швеция                      | `sv_SE` |
| Турецкий - Турция                      | `tr_TR` |
| Украинский - Украина                   | `uk_UA` |
| Китайский - Китай                      | `zh_CN` |
| Китайский - Тайвань                    | `zh_TW` |


## Как заставить работать английскую проверку орфографии

Чтобы английская проверка орфографии работала, выйдите из сеанса MX Linux 23 и выберите в Login Manager:

```
Американский английский - США
```

Затем отредактируйте:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

и оставьте такое содержимое:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

WPS Office 12 уже включает эту MUI по умолчанию:

```
/opt/kingsoft/wps-office/office6/mui/en_US
```

а также словарь:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

### Включить английскую проверку орфографии

Теперь откройте WPS Writer. Перейдите на вкладку ленты с названием:

`"Review"`

и там в

`"Spell Check ⌵"`

нажмите значок `"⌵"` и выберите подменю:

`"Set Spell Check language"`

![](vx_images/20260721.2-WPS_en-US_Home-Review-SpellCheck-SetLanguage-ezgif.com.gif)

в открывшемся окне `"Английский (США)"` будет среди доступных словарей по умолчанию.

![](vx_images/dicts-tests/01-Set-Spell-Check-Language-English-United-States.png)


при желании можно нажать `"Change Default"`, хотя он уже был выбран по умолчанию, потому что MUI `en_US` уже была установлена.

Теперь в нижнем левом углу окна посмотрите на строку состояния; появится индикатор, похожий на этот:

`Spell Check: Disabled ⌵`

Нажмите этот индикатор, и он изменится на `"Enabled"`.

Кроме того, если нажать значок `"⌵"`, эта и другие опции будут доступны в выпадающем меню.

После включения WPS Office автоматически начнет проверять орфографию документа. С этого момента слова с ошибками будут подчеркиваться; щелчок правой кнопкой мыши по подчеркнутому слову покажет предложения исправления. Проверка орфографии останется включенной, пока пользователь снова не отключит эту опцию:


![](vx_images/20260721.1-Quotes-MUI-en-US-Richard-Stallman-ezgif.com.gif)

---

## Как заставить работать испанскую проверку орфографии

Чтобы испанская проверка орфографии работала, выйдите из сеанса MX Linux 23 (если вы сейчас в другом языке) и выберите, например, это в Login Manager:

```
Испанский - Эквадор
```

Затем отредактируйте:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

и оставьте это содержимое для испанского из Испании:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

В этой конфигурации должна быть установлена эта MUI:

```
/opt/kingsoft/wps-office/office6/mui/es_ES
```

и словарь:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
```


### Включить испанскую проверку орфографии

Откройте WPS Writer. Перейдите на вкладку ленты с названием:

`"Revisar"`

и там в

`"Revisión ortográfica ⌵"`

нажмите значок `"⌵"` и выберите подменю:

`"Establecer idioma"`

и в открывшемся окне `"Español (España)"` будет среди доступных словарей по умолчанию.

и нажмите `"Establecer predeterminado"`, хотя он уже был выбран по умолчанию, потому что MUI `es_ES` уже была установлена.

Теперь в нижнем левом углу окна посмотрите на строку состояния; появится индикатор, похожий на этот:

`Revisión ortográfica: Desactivado ⌵`

Нажмите этот индикатор, и он изменится на `"Activado"`.

![](vx_images/20260716.1-Frases-MUI-es-ES-Richard-Stallman-ezgif.com.gif)

Кроме того, если нажать значок `"⌵"`, эта и другие опции будут доступны в выпадающем меню.

Когда проверка орфографии включена, WPS Office автоматически начнет проверять орфографию документа. С этого момента слова с ошибками будут подчеркиваться; щелчок правой кнопкой мыши по подчеркнутому слову покажет предложения исправления. Проверка орфографии останется включенной, пока пользователь снова не отключит эту опцию:

На данный момент в этой китайской версии WPS Office 12 испанская проверка орфографии работает только со словарем `es_ES` из этого репозитория:

/build/dicts-active/es_ES/

Однако следующие словари в папке `wps-libreoffice-dicts` не работают так, как работали в WPS Office 11:

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

### Испанские региональные настройки, которые еще нужно протестировать

Эти региональные настройки Login Manager еще нужно протестировать с испанской проверкой орфографии:

```
Испанский - Аргентина
Испанский - Боливия
Испанский - Колумбия
Испанский - Никарагуа
Испанский - Панама
```

Остальные, которые работали, перечислены выше в таблице.

## Тест словаря испанского Мексики, который не сработал

Я выполнил следующий тест, потому что доступны и MUI `es_MX`, и словарь проверки орфографии `es_MX`.

В тесте вход через Login Manager выполнялся с:

```
Мексиканский испанский - Мексика
```

и WPS был настроен так:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

С MUI:

```
/opt/kingsoft/wps-office/office6/mui/es_MX
```

и со словарем в:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_MX/
```

WPS показывает `"Español (México)"` в языковом окне, но проверка орфографии не работает. Однако если в том же окне выбрать словарь `"Español (España)"`, она работает.

## Как заставить работать немецкую проверку орфографии

Для немецкого выйдите из сеанса и выберите в Login Manager:

```
Немецкий - Германия
```

Затем настройте `Office.conf` так:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Активация похожа на активацию английского словаря:

![](vx_images/Quotes-tests/Deutsch-de_DE-Richard-S-ezgif.com.gif)

В этом тесте сработало следующее:

```
/opt/kingsoft/wps-office/office6/mui/de_DE
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

## Как заставить работать французскую проверку орфографии

Для французского выйдите из сеанса и выберите в Login Manager:

```
Французский - Франция
```

Активация похожа на активацию английского словаря.


![](vx_images/Quotes-tests/citation_fr-FR_Richard_S-ezgif.com.gif)

Затем настройте `Office.conf` так:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

В этом тесте работало с:

```
/opt/kingsoft/wps-office/office6/mui/fr_FR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
```



## Как заставить работать индонезийскую проверку орфографии

Для индонезийского сначала создайте locale, если она еще не появляется в Login Manager:

```bash
sudo dpkg-reconfigure locales
```

В списке отметьте:

```
id_ID.UTF-8 UTF-8
```

Затем выйдите из сеанса и выберите в Login Manager:

```
Индонезийский - Indonesia
```

Затем настройте `Office.conf` так:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Активация похожа на активацию английского словаря. `"Индонезийский"` должен появиться в окне языка проверки орфографии.

![](vx_images/Quotes-tests/Kutipan-id_ID-Richard-S-ezgif.com.gif)

В этом тесте работало с:

```
/opt/kingsoft/wps-office/office6/mui/id_ID
/opt/kingsoft/wps-office/office6/dicts/spellcheck/id_ID/
```

Примечание: хотя сеанс Linux использует `id_ID.UTF-8`, установленный словарь `id_ID` использует `SET ISO8859-1` в `main.aff` и корректно работал в WPS Office 12.

## Как заставить работать польскую проверку орфографии

Для польского выйдите из сеанса и выберите в Login Manager:

```
Польский - Польша
```

Затем настройте `Office.conf` так:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Активация похожа на активацию английского словаря. `"Polski"` должен появиться в окне языка проверки орфографии.

![](vx_images/Quotes-tests/Cytaty_pl-PL_RichardS-ezgif.com.gif)


В этом тесте работало с:

```
/opt/kingsoft/wps-office/office6/mui/pl_PL
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pl_PL/
```

Примечание: для этого теста сработал словарь `pl_PL` в UTF-8, взятый из старых словарей WPS Office 11.2.0.9255. Словарь, преобразованный из LibreOffice, был в `ISO8859-2` и плохо работал в WPS Office 12.

## Как заставить работать проверку орфографии бразильского португальского

Для бразильского португальского выйдите из сеанса и выберите в Login Manager:

```
Бразильский португальский - Бразилия
```

Затем настройте `Office.conf` так:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Активация похожа на активацию английского словаря. `"Português do Brasil"` должен появиться в окне языка проверки орфографии.

![](vx_images/Quotes-tests/Citacoes_pt-BR_Richard_S-ezgif.com.gif)

В этом тесте работало с:

```
/opt/kingsoft/wps-office/office6/mui/pt_BR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Примечание: хотя MUI `pt_BR` содержит `FallBack=pt_PT` в `lang.conf`, WPS корректно проверял орфографию, когда в окне языка проверки орфографии был выбран `"Português do Brasil"`. Если в том же сеансе выбрать `"Português (Portugal)"`, проверка орфографии не работает.

## Тест словаря португальского Португалии, который не сработал

Я выполнил следующий тест, потому что доступны и MUI `pt_PT`, и словарь проверки орфографии `pt_PT`.

В тесте вход через Login Manager выполнялся с:

```
Европейский португальский - Португалия
```

и WPS был настроен так:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

С MUI:

```
/opt/kingsoft/wps-office/office6/mui/pt_PT
```

и со словарем в:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/
```

WPS показывал `"Portuguê"` до исправления имени словаря, а теперь должен показывать `"Português (Portugal)"`; в обоих случаях проверка орфографии со словарем `pt_PT` не работала.

В той же конфигурации locale `pt_PT.UTF-8` и MUI `pt_PT` проверка орфографии работала с бразильским португальским словарем:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

## Как заставить работать русскую проверку орфографии

Для русского выйдите из сеанса и выберите в Login Manager:

```
Русский - Россия
```

Затем настройте `Office.conf` так:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Активация похожа на активацию английского словаря. `"Русский (Россия)"` должен появиться в окне языка проверки орфографии.

![](vx_images/Quotes-tests/Frase_ru_RU_RichardS-ezgif.com.gif)


В этом тесте работало с:

```
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

Примечание: русская проверка орфографии корректно работала в новом документе, созданном с нуля. В документе, изначально созданном на английском, даже после вставки переведенного русского текста WPS не применил проверку орфографии к существующему тексту корректно.

## Как заставить работать турецкую проверку орфографии

Для турецкого выйдите из сеанса и выберите в Login Manager:

```
Турецкий - Турция
```

Затем настройте `Office.conf` так:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Активация похожа на активацию английского словаря. `"Türkçe (Türkiye)"` должен появиться в окне языка проверки орфографии.

![](vx_images/Quotes-tests/Alntlar-tr_TR-Richard-S-ezgif.com.gif)

В этом тесте работало с:

```
/opt/kingsoft/wps-office/office6/mui/tr_TR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/tr_TR/
```

## Справка: пакеты MUI, загруженные WPS в Windows

Если вам интересно, откуда взялись файлы MUI для графического интерфейса, я получил их в Microsoft Windows 10. WPS Office загружает языковые пакеты в пользовательские пути; эта информация полезна как справка для изучения файлов языка интерфейса.

Сначала скачайте и установите WPS Office 12 для Windows:

[https://wps.com/office/windows/](https://wps.com/office/windows/)

Пример в Windows 10:

![](vx_images/02-WPS-Office-global-config-menu.png)

Затем скачайте языки:

![](vx_images/03-Click-on-a-language-and-then-click-Apply.png)

Скачанные языки могут находиться в:

```
C:\Users\youruser\AppData\Roaming\kingsoft\wps_intl\addons\pool\win-x64
```

![](vx_images/04-downloaded-languages.png)

Список языков может находиться в:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui\lang_list\lang_list.json
```

![20260416-000808](vx_images/507184629680596.png)

Некоторые пакеты, включенные в испанскую версию Windows, могут находиться в:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui
```

![](vx_images/05-languages-downloaded-by-the-Spanish-version.png)

Если этот проект помог вам, можно поставить звезду репозиторию.

---

# Благодарности

Пользователю [mmvill](https://github.com/mmvill), который написал мне и сообщил, что нашел способ заставить испанский словарь проверки орфографии работать в WPS Office 12.
