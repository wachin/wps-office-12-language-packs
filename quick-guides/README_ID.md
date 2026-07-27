# Panduan singkat: pemeriksa ejaan bahasa Indonesia di WPS Office 12 untuk Linux

Panduan singkat ini memasang antarmuka dan pemeriksa ejaan bahasa Indonesia untuk WPS Office 12 di Linux.

## Persyaratan

- WPS Office 12.x sudah terpasang.
- Koneksi internet untuk mengunduh berkas Release.
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

## Mengunduh berkas Release

Buka bagian Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

Unduh dua berkas ini:

- `wps-office-12-mui.tar.xz`
- `wps-office-12-dicts-active.tar.xz`

![](../vx_images/09-release-wps-12.1.2-language-packs-v1.png)

## Memasang MUI

Ekstrak `wps-office-12-mui.tar.xz` dengan klik kanan di pengelola berkas pilihan Anda. Anda akan mendapatkan folder:

```text
wps-office-12-mui
```

Buka terminal di dalam folder tersebut. Pada sistem Linux modern, klik kanan di dalam folder biasanya menyediakan opsi seperti `Open terminal here`.

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

## Memasang kamus

Ekstrak `wps-office-12-dicts-active.tar.xz` dengan klik kanan di pengelola berkas pilihan Anda. Anda akan mendapatkan folder:

```text
wps-office-12-dicts-active
```

Buka terminal di dalam folder tersebut dan jalankan:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
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
