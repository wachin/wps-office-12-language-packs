# Panduan singkat: pemeriksa ejaan bahasa Indonesia di WPS Office 12 untuk Linux

Panduan singkat ini memasang antarmuka dan pemeriksa ejaan bahasa Indonesia untuk WPS Office 12 di Linux.

## Persyaratan

- WPS Office 12.x sudah terpasang.
- Repositori ini sudah diunduh atau dikloning.
- Izin administrator dengan `sudo`.
- WPS Office sudah pernah dibuka sekali agar `~/.config/Kingsoft/Office.conf` ada.

## Memasang WPS Office

Unduh WPS Office 12 untuk Linux dari situs resmi Tiongkok:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Anda dapat memasang paket `.deb` dengan pemasang paket:

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

atau dari terminal:

```bash
sudo dpkg -i wps-office*.deb
```

## Memasang MUI dan kamus

Dari root repositori ini, jalankan:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
sudo cp -r build/dicts-active/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Jika `id_ID` belum muncul di Login Manager, buat locale terlebih dahulu:

```bash
sudo dpkg-reconfigure locales
```

Tandai:

```text
id_ID.UTF-8 UTF-8
```

Untuk bahasa Indonesia, WPS Office 12 akan menggunakan:

```text
/opt/kingsoft/wps-office/office6/mui/id_ID
/opt/kingsoft/wps-office/office6/dicts/spellcheck/id_ID/
```

## Mengonfigurasi WPS Office

Jika Gedit belum terpasang, pasang terlebih dahulu:

```bash
sudo apt install gedit
```

Edit:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Gunakan isi berikut:

```ini
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Tutup WPS Office sepenuhnya lalu buka lagi.

## Mengaktifkan pemeriksaan ejaan

Di WPS Writer, pilih `Indonesian` sebagai bahasa pemeriksaan ejaan dan jadikan default jika perlu.

![](../vx_images/Quotes-tests/Kutipan-id_ID-Richard-S-ezgif.com.gif)
