# Hızlı kılavuz: WPS Office 12 Linux’ta Türkçe yazım denetimi

Bu kısa kılavuz, Linux üzerinde WPS Office 12 için Türkçe arayüzü ve Türkçe yazım denetimini kurar.

## Gereksinimler

- WPS Office 12.x kurulu.
- Bu depo indirilmiş veya klonlanmış.
- `sudo` ile yönetici izni.
- `~/.config/Kingsoft/Office.conf` dosyasının oluşması için WPS Office en az bir kez açılmış.

## WPS Office’i kurma

WPS Office 12 Linux sürümünü resmi Çin sitesinden indirin:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

`.deb` paketini paket yükleyicinizle kurabilirsiniz:

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

veya terminalden:

```bash
sudo dpkg -i wps-office*.deb
```

## MUI ve sözlükleri kurma

Bu deponun kök dizininden şunu çalıştırın:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
sudo cp -r build/dicts-active/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Türkçe için şunları kullanın:

```text
/opt/kingsoft/wps-office/office6/mui/tr_TR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/tr_TR/
```

## WPS Office’i yapılandırma

Düzenleyin:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Şu içeriği kullanın:

```ini
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

WPS Office’i tamamen kapatın ve tekrar açın.

## Yazım denetimini etkinleştirme

WPS Writer’da yazım denetimi dili olarak `Türkçe (Türkiye)` seçin ve gerekirse varsayılan yapın.

![](../vx_images/Quotes-tests/Alntlar-tr_TR-Richard-S-ezgif.com.gif)
