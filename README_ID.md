# Paket bahasa WPS Office 12.x untuk Linux

Terjemahan yang tersedia:

- [Inggris](README.md), tersedia untuk pengguna berbahasa Inggris.
- [Español](README_ES.md), tersedia untuk pengguna berbahasa Spanyol.
- [Deutsch](README_DE.md), tersedia untuk pengguna berbahasa Jerman.
- [Français](README_FR.md), tersedia untuk pengguna berbahasa Prancis.

## Mengunduh WPS Office 12 Linux versi Tiongkok

Unduh pemasang WPS Office untuk distribusi Linux Anda, baik yang berbasis DEB maupun RPM.

Situs web resmi Tiongkok:

- [https://www.wps.cn](https://www.wps.cn)

klik di sana akan mengarahkan ke:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Lalu pasang paket tersebut.

**Unduhan mirror**
Namun, mirror tersebut mungkin tidak memiliki versi terbaru, atau mungkin perlu waktu sampai versi terbaru diunggah ke sana:

[https://mirrors.163.com/ubuntukylin/pool/partner/](https://mirrors.163.com/ubuntukylin/pool/partner/)

### Memasang paket DEB dengan pemasang paket DEB

Pasang dengan pengelola paket DEB. Pada sistem Linux biasanya sudah ada salah satu alat tersebut; klik kanan berkas di pengelola berkas Anda dan pasang dengan alat itu:

![](vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

### Memasang dari terminal (Opsional)

Jika Anda menggunakan Debian, Ubuntu, Linux Mint, atau distribusi serupa, Anda juga dapat melakukannya dari terminal:

```bash
sudo dpkg -i wps-office*.deb
```

Jika Anda menggunakan Fedora, Red Hat, atau distribusi serupa:

```bash
sudo dnf install wps-office*.rpm
```

## Persyaratan

Untuk mengikuti tutorial ini, Anda memerlukan:

- **WPS Office 12.x** sudah terpasang di Linux seperti dijelaskan di atas.
- Izin administrator dengan `sudo` atau alat yang setara.
- WPS Office sudah pernah dibuka setidaknya satu kali. WPS Office membuat konfigurasi pengguna setelah pertama kali dibuka. Jika `~/.config/Kingsoft/Office.conf` belum ada, buka WPS Office, tutup kembali, lalu lanjutkan instalasi.
- Repositori ini sudah diunduh atau dikloning ke komputer Anda.

## Memasang antarmuka pengguna multibahasa MUI

Untuk memasang berkas MUI (antarmuka pengguna multibahasa), proyek ini harus ada di komputer Anda. Ada **dua** cara untuk melakukannya; pilih hanya **satu**:

### Opsi 1: unduh ZIP dan pasang berkas MUI

1. Buka halaman ini:

   [https://github.com/wachin/wps-office-12-language-packs](https://github.com/wachin/wps-office-12-language-packs)

2. Klik tombol hijau:

```
<> Code ▼
```

3. Klik:

```
Download ZIP
```

4. Setelah unduhan selesai, ekstrak berkas ZIP dengan klik kanan dan pilih "Extract here".
5. Buka terminal di lokasi tersebut dan jalankan:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
```

perintah ini memasang berkas MUI (antarmuka pengguna multibahasa).

### Opsi 2: kloning dengan Git dan pasang berkas MUI

Jika `git` belum terpasang, pasang terlebih dahulu:

```bash
sudo apt install git
```

Kemudian kloning repositori:

```bash
git clone https://github.com/wachin/wps-office-12-language-packs
```

Masuk ke folder:

```bash
cd wps-office-12-language-packs
```

jalankan:

```bash
sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/
```

perintah ini memasang berkas MUI (antarmuka pengguna multibahasa).

## Memverifikasi instalasi

Perintah `sudo cp -r build/wps-mui/* /opt/kingsoft/wps-office/office6/mui/` menyalin folder bahasa yang tersedia ke folder WPS Office yang sebenarnya di Linux: `/opt/kingsoft/wps-office/office6/mui/`.

WPS Office 12 versi Tiongkok yang baru dipasang menyertakan folder MUI berikut secara bawaan:

/opt/kingsoft/wps-office/office6/mui/en_US
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/mui/zh_CN

dan juga menyertakan dua kamus pemeriksa ejaan berikut secara bawaan:

/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_CH
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US

Dari pengelola berkas, periksa path ini:

/opt/kingsoft/wps-office/office6/mui/

Selain bahasa yang disertakan dalam versi Tiongkok, Anda seharusnya memiliki yang berikut:

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

Ini juga disalin:

```
lang_list
```

Ini adalah daftar pilihan.


## Kamus yang tersedia dan kamus yang sudah diuji

Repositori ini juga menyiapkan kamus Hunspell agar **WPS Office 12.x** dapat menggunakannya di Linux.

Untuk saat ini, dua folder perlu dibedakan:

```
build/dicts-active/
wps-libreoffice-dicts/
```

Folder `build/dicts-active/` berisi kamus yang saat ini dipilih untuk dipasang. Kamus inilah yang digunakan untuk pengujian WPS Office 12.

Folder `wps-libreoffice-dicts/` berisi semua kamus yang dikonversi dari LibreOffice. Folder ini disimpan di root repositori karena pada WPS Office 12 versi Tiongkok tidak semua varian berfungsi walaupun formatnya benar. Mungkin pada versi WPS mendatang semua kamus tersebut akan didukung kembali seperti pada versi lama WPS Office untuk Linux.

Setiap folder kamus memiliki format yang diharapkan WPS:

```
dict.conf
main.aff
main.dic
```

Berkas `main.aff` dan `main.dic` terutama berasal dari koleksi kamus LibreOffice:

```
third-party/libreoffice-dictionaries-collection/dicts/
```

Repositori sumber:

[https://github.com/wachin/libreoffice-dictionaries-collection](https://github.com/wachin/libreoffice-dictionaries-collection)

Berkas `dict.conf` digunakan kembali dari kamus WPS Office lama jika tersedia, dan dibuat untuk varian baru.

Pengecualian penting: kamus aktif `pl_PL` berasal dari kamus lama WPS Office 11.2.0.9255:

```
third-party/wps-office-11.2.0.9255-dicts/dicts/pl_PL/
```

Repositori sumber:

[https://github.com/wachin/wps-office-11.2.0.9255-dicts](https://github.com/wachin/wps-office-11.2.0.9255-dicts)

`pl_PL` tersebut digunakan karena kamus bahasa Polandia yang dikonversi dari LibreOffice tidak bekerja dengan baik di WPS Office 12. Berkas `main.aff`-nya berisi:

```
SET ISO8859-2
```

Sebaliknya, kamus Polandia lama dari WPS menggunakan UTF-8 dan `main.aff`-nya berisi:

```
SET UTF-8
```

Kamus yang saat ini aktif adalah:

| Kode    | Kamus               |
| ------- | ------------------- |
| `de_DE` | Jerman (Jerman)     |
| `es_ES` | Spanyol (Spanyol)   |
| `fr_FR` | Prancis (Prancis)   |
| `id_ID` | Indonesia           |
| `pl_PL` | Polandia            |
| `pt_BR` | Portugis (Brasil)   |
| `pt_PT` | Portugis            |
| `ru_RU` | Rusia (Rusia)       |
| `tr_TR` | Turki (Turkey)      |

Catatan tentang `pt_PT`: pada MX Linux 23 dengan locale `pt_PT.UTF-8`, MUI `pt_PT`, dan kamus terpasang sebagai `/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/`, WPS Office 12 tidak mengaktifkan pemeriksaan ejaan untuk Portugis Portugal pada pengujian saat ini. Pada instalasi yang sama, pemeriksaan ejaan berfungsi dengan kamus `pt_BR`.


## Memasang kamus

From the root of this repository, jalankan:

```bash
sudo cp -r build/dicts-active/* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Ini menyalin kamus aktif ke folder yang digunakan WPS untuk pemeriksaan ejaan.

Setelah disalin, path WPS seharusnya berisi folder seperti ini:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Dan di dalam masing-masing:

```
dict.conf
main.aff
main.dic
```

## Mengaktifkan bahasa antarmuka dalam konfigurasi WPS

Jika Anda seorang pengembang, edit berkas konfigurasi dengan nano:

```bash
nano ~/.config/Kingsoft/Office.conf
```

Jika Anda pengguna biasa, gunakan Gedit atau editor teks lain. Jika Gedit belum terpasang, pasang seperti ini:

```bash
sudo apt install gedit
```

dan masukkan ini di terminal:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Setelah berkas itu terbuka, pilih semua teks di dalamnya dengan `Ctrl + A`, hapus, lalu ganti dengan isi untuk bahasa yang ingin digunakan.

Strukturnya selalu sama:

```
[General]
languages=KODE_BAHASA

[6.0]
common\DefaultLanguage=NOMOR_BAHASA
common\Local\UILanguage=NOMOR_BAHASA
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Gunakan tabel ini untuk memilih kode dan nomor yang benar:

| Bahasa                            | `languages=` | `DefaultLanguage` dan `UILanguage` |
| --------------------------------- | ------------ | ---------------------------------- |
| Inggris (Amerika Serikat)         | `en_US`      | `1033`                             |
| Jerman (Jerman)                   | `de_DE`      | `1031`                             |
| Spanyol (Spanyol)                 | `es_ES`      | `3082`                             |
| Spanyol (Meksiko)                 | `es_MX`      | `2058`                             |
| Prancis (Kanada)                  | `fr_CA`      | `3084`                             |
| Prancis (Prancis)                 | `fr_FR`      | `1036`                             |
| Indonesia                         | `id_ID`      | `1057`                             |
| Jepang                            | `ja_JP`      | `1041`                             |
| Polandia                          | `pl_PL`      | `1045`                             |
| Portugis (Brasil)                 | `pt_BR`      | `1046`                             |
| Portugis (Portugal)               | `pt_PT`      | `2070`                             |
| Rusia                             | `ru_RU`      | `1049`                             |
| Thailand                          | `th_TH`      | `1054`                             |
| Turki                             | `tr_TR`      | `1055`                             |
| Tionghoa (Sederhana, Tiongkok)    | `zh_CN`      | `2052`                             |
| Tionghoa (Tradisional, Hong Kong) | `zh_HK`      | `3076`                             |

### Tabel cepat: locale, MUI, dan kamus dengan kode yang sama

Tabel ini menunjukkan bahasa yang dapat dibandingkan langsung apakah `Locale`, MUI, dan kamus menggunakan kode yang sama. Tanda `x` berarti tidak ada kamus aktif dengan kode yang sama. Simbol `✅` menandai kasus yang sudah diuji dan kombinasi tepat tersebut berfungsi.

| Language shown in the Login Manager | `Locale` | `MUI`   | `Dict`  | Tested  |
| ----------------------------------- | -------- | ------- | ------- | ------- |
| Inggris (Amerika Serikat)           | `en_US`  | `en_US` | `en_US` | ✅       |
| Jerman (Jerman)                     | `de_DE`  | `de_DE` | `de_DE` | ✅       |
| Spanyol (Spanyol)                   | `es_ES`  | `es_ES` | `es_ES` | ✅       |
| Spanyol (Meksiko)                   | `es_MX`  | `es_MX` | x       |         |
| Prancis (Kanada)                    | `fr_CA`  | `fr_CA` | x       |         |
| Prancis (Prancis)                   | `fr_FR`  | `fr_FR` | `fr_FR` | ✅       |
| Indonesia                           | `id_ID`  | `id_ID` | `id_ID` | ✅       |
| Jepang                              | `ja_JP`  | `ja_JP` | x       |         |
| Polandia                            | `pl_PL`  | `pl_PL` | `pl_PL` | ✅       |
| Portugis (Brasil)                   | `pt_BR`  | `pt_BR` | `pt_BR` | ✅       |
| Portugis (Portugal)                 | `pt_PT`  | `pt_PT` | `pt_PT` |         |
| Rusia                               | `ru_RU`  | `ru_RU` | `ru_RU` | ✅       |
| Thailand                            | `th_TH`  | `th_TH` | x       |         |
| Turki                               | `tr_TR`  | `tr_TR` | `tr_TR` | ✅       |
| Tionghoa (Sederhana, Tiongkok)      | `zh_CN`  | `zh_CN` | x       |         |
| Tionghoa (Tradisional, Hong Kong)   | `zh_HK`  | `zh_HK` | x       |         |

### Untuk Inggris Amerika Serikat:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Spanyol dari Spanyol:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Jerman dari Jerman:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


### Untuk Spanyol dari Meksiko:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Prancis dari Kanada:

```
[General]
languages=fr_CA

[6.0]
common\DefaultLanguage=3084
common\Local\UILanguage=3084
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Prancis dari Prancis:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Indonesia:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Jepang:

```
[General]
languages=ja_JP

[6.0]
common\DefaultLanguage=1041
common\Local\UILanguage=1041
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Polandia:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Portugis Brasil:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Portugis dari Portugal:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Rusia:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Thailandland:

```
[General]
languages=th_TH

[6.0]
common\DefaultLanguage=1054
common\Local\UILanguage=1054
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Turki:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Tionghoa sederhana dari Tiongkok:

```
[General]
languages=zh_CN

[6.0]
common\DefaultLanguage=2052
common\Local\UILanguage=2052
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Untuk Tionghoa tradisional dari Hong Kong:

```
[General]
languages=zh_HK

[6.0]
common\DefaultLanguage=3076
common\Local\UILanguage=3076
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


Simpan berkas, tutup WPS Office sepenuhnya, lalu buka lagi. Jika bahasa dikonfigurasi dengan benar, antarmuka akan terbuka dalam bahasa yang dipilih.

## Solusi agar pemeriksa ejaan berfungsi di WPS Office 12

Pada WPS Office 12 versi Tiongkok, menyalin kamus ke folder ini saja tidak cukup:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Pengaturan regional yang digunakan saat masuk ke sesi Linux dari Login Manager, bahasa MUI yang terpasang di WPS Office, dan bahasa yang dikonfigurasi di berkas ini juga berpengaruh:

```
~/.config/Kingsoft/Office.conf
```

Itulah sebabnya beberapa kamus muncul di jendela `"Set language"`, tetapi tidak melakukan pemeriksaan ejaan. Kasus paling jelas adalah Spanyol Meksiko: MUI `es_MX` dan kamus `es_MX` dapat terlihat terpasang, tetapi pada pengujian pemeriksaan ejaan hanya berfungsi dengan kamus `es_ES`.

### Pengujian yang dikonfirmasi

Berikut pengujian yang telah dilakukan sejauh ini:

| Pemeriksa ejaan | Pengaturan regional yang dipilih di Login Manager  | Locale  | MUI yang digunakan di WPS | Kamus terpasang       | Status          |
| --------------- | -------------------------------------------------- | ------- | ------------------------- | --------------------- | --------------- |
| Inggris         | `Inggris Amerika - Amerika Serikat`                | `en_US` | `en_US`                   | `en_US` UTF-8         | Berfungsi       |
| Inggris         | `Inggris - Irlandia`                               | `en_IE` | `en_US`                   | `en_US` UTF-8         | Berfungsi       |
| Inggris         | `Inggris Australia - Australia`                    | `en_AU` | `en_US`                   | `en_US` UTF-8         | Berfungsi       |
| Inggris         | `Inggris Britania - Britania Raya`                 | `en_GB` | `en_US`                   | `en_US` UTF-8         | Berfungsi       |
| Inggris         | `Inggris - Selandia Baru`                          | `en_NZ` | `en_US`                   | `en_US` UTF-8         | Tidak berfungsi |
| Spanyol         | `Spanyol - Ekuador`                                | `es_EC` | `es_ES`                   | `es_ES` UTF-8         | Berfungsi       |
| Spanyol         | `Spanyol Eropa - Spanyol`                          | `es_ES` | `es_ES`                   | `es_ES` UTF-8         | Berfungsi       |
| Spanyol         | `Spanyol - Amerika Serikat`                        | `es_US` | `es_ES`                   | `es_ES` UTF-8         | Berfungsi       |
| Spanyol         | `Spanyol - Venezuela`                              | `es_VE` | `es_ES`                   | `es_ES` UTF-8         | Berfungsi       |
| Spanyol         | `Spanyol Meksiko - Meksiko`                        | `es_MX` | `es_ES`                   | `es_ES` UTF-8         | Berfungsi       |
| Spanyol         | `Spanyol - Peru`                                   | `es_PE` | `es_ES`                   | `es_ES` UTF-8         | Berfungsi       |
| Spanyol         | `Spanyol - Uruguay`                                | `es_UY` | `es_ES`                   | `es_ES` UTF-8         | Berfungsi       |
| Spanyol Meksiko | `Spanyol Meksiko - Meksiko`                        | `es_MX` | `es_MX`                   | `es_MX` UTF-8         | Tidak berfungsi |
| Jerman          | `Jerman Austria - Austria`                         | `de_AT` | `de_DE`                   | `de_DE` ISO8859-1     | Berfungsi       |
| Jerman          | `Jerman - Jerman`                                  | `de_DE` | `de_DE`                   | `de_DE` ISO8859-1     | Berfungsi       |
| Jerman          | `Jerman Tinggi Swiss - Swiss`                      | `de_CH` | `de_DE`                   | `de_DE` ISO8859-1     | Berfungsi       |
| Prancis         | `Prancis - Prancis`                                | `fr_FR` | `fr_FR`                   | `fr_FR` UTF-8         | Berfungsi       |
| Prancis         | `Prancis Kanada - Kanada`                          | `fr_CA` | `fr_CA`                   | `fr_FR` UTF-8         | Berfungsi       |
| Indonesia       | `Indonesia - Indonesia`                            | `id_ID` | `id_ID`                   | `id_ID` ISO8859-1     | Berfungsi       |
| Polandia        | `Polandia - Polandia`                              | `pl_PL` | `pl_PL`                   | `pl_PL` UTF-8         | Berfungsi       |
| Portugis BR     | `Portugis Brasil - Brasil`                         | `pt_BR` | `pt_BR`                   | `pt_BR` UTF-8         | Berfungsi       |
| Portugis PT     | `Portugis Eropa - Portugal`                        | `pt_PT` | `pt_PT`                   | `pt_PT` UTF-8         | Tidak berfungsi |
| Portugis PT     | `Portugis Eropa - Portugal`                        | `pt_PT` | `pt_PT`                   | `pt_BR` UTF-8         | Berfungsi       |
| Rusia           | `Rusia - Rusia`                                    | `ru_RU` | `ru_RU`                   | `ru_RU` UTF-8         | Berfungsi       |
| Turki           | `Turki - Turki`                                    | `tr_TR` | `tr_TR`                   | `tr_TR` UTF-8         | Berfungsi       |

Encoding yang ditampilkan pada kolom `Kamus terpasang` diambil dari baris `SET` di berkas `main.aff` masing-masing kamus.

**Catatan tentang `pl_PL`**: setelah mengganti kamus dengan versi UTF-8 dari kamus lama WPS Office 11.2.0.9255, kamus tersebut harus dipilih secara manual di `"Review"` > `"Spell Check ⌵"` > `"Set language"` > `"Polski"`. Setelah dipilih, pemeriksaan ejaan berfungsi. Kamus Polandia yang dikonversi dari LibreOffice tidak bekerja dengan baik karena menggunakan `ISO8859-2`, seperti terlihat pada berkas `main.aff`-nya.

**Catatan tentang `pt_PT`**: dengan locale `pt_PT.UTF-8`, MUI `pt_PT`, dan kamus `pt_PT`, WPS Office 12 tidak mengaktifkan pemeriksaan ejaan. Pada konfigurasi yang sama, pemeriksaan berfungsi dengan kamus `pt_BR`.

**Catatan tentang `ru_RU`**: pemeriksa ejaan berfungsi pada dokumen baru yang dibuat dari awal. Pada dokumen yang awalnya dibuat dalam bahasa Inggris, meskipun teks Rusia terjemahan ditempelkan, WPS tidak menerapkan pemeriksaan ejaan dengan benar pada teks yang sudah ada.

Pada MX Linux 23, locale dapat dilihat di Login Manager: saat Anda memilih bahasa dari daftar, Login Manager menampilkan kode locale. Misalnya, jika Anda mengklik:

```
Spanyol Meksiko - Meksiko
```

ini akan muncul:

```
es_MX
```

Jika Anda sudah masuk sesi dan ingin melihat locale yang digunakan sistem, buka terminal dan jalankan:

```bash
echo $LANG
```

Contoh:

```bash
$ echo $LANG
es_MX.UTF-8
```

### Daftar bahasa yang tersedia di Login Manager MX Linux 23

Ini adalah daftar yang diamati di Login Manager MX Linux 23:

![](vx_images/20260717.1-MX-Linux-23_Login-Manager-lnguages-ezgif.com.gif)

Tersedia sebagai tabel dengan locale:

| Language in the Login Manager        | Locale  |
| ------------------------------------ | ------- |
| Arab - Mesir                         | `ar_EG` |
| Belarus - Belarus                    | `be_BY` |
| Bulgaria - Bulgaria                  | `bg_BG` |
| Katalan - Spanyol                    | `ca_ES` |
| Ceko - Republik Ceko                 | `cs_CZ` |
| Denmark - Denmark                    | `da_DK` |
| Jerman Austria - Austria             | `de_AT` |
| Jerman Tinggi Swiss - Swiss          | `de_CH` |
| Jerman - Jerman                      | `de_DE` |
| Yunani - Yunani                      | `el_GR` |
| Inggris Australia - Australia        | `en_AU` |
| Inggris Kanada - Kanada              | `en_CA` |
| Inggris Britania - Britania Raya     | `en_GB` |
| Inggris - Irlandia                   | `en_IE` |
| Inggris - Selandia Baru              | `en_NZ` |
| Inggris Amerika - Amerika Serikat    | `en_US` |
| Spanyol - Argentina                  | `es_AR` |
| Spanyol - Bolivia                    | `es_BO` |
| Spanyol - Kolombia                   | `es_CO` |
| Spanyol - Ekuador                    | `es_EC` |
| Spanyol Eropa - Spanyol              | `es_ES` |
| Spanyol Meksiko - Meksiko            | `es_MX` |
| Spanyol - Nikaragua                  | `es_NI` |
| Spanyol - Panama                     | `es_PA` |
| Spanyol - Peru                       | `es_PE` |
| Spanyol - Amerika Serikat            | `es_US` |
| Spanyol - Uruguay                    | `es_UY` |
| Spanyol - Venezuela                  | `es_VE` |
| Estonia - Estonia                    | `et_EE` |
| Basque - Spanyol                     | `eu_ES` |
| Persia - Iran                        | `fa_IR` |
| Finlandia - Finlandia                | `fi_FI` |
| Prancis - Belgia                     | `fr_BE` |
| Prancis Kanada - Kanada              | `fr_CA` |
| Prancis Swiss - Swiss                | `fr_CH` |
| Prancis - Prancis                    | `fr_FR` |
| Irlandia - Irlandia                  | `ga_IE` |
| Ibrani - Israel                      | `he_IL` |
| Kroasia - Kroasia                    | `hr_HR` |
| Hungaria - Hungaria                  | `hu_HU` |
| Islandia - Islandia                  | `is_IS` |
| Italia - Italia                      | `it_IT` |
| Jepang - Jepang                      | `ja_JP` |
| Georgia - Georgia                    | `ka_GE` |
| Kazakh - Kazakhstan                  | `kk_KZ` |
| Korea - Korea Selatan                | `ko_KR` |
| Lituania - Lituania                  | `lt_LT` |
| Latvia - Latvia                      | `lv_LV` |
| Makedonia - Makedonia                | `mk_MK` |
| Norwegia Bokmål - Norwegia           | `nb_NO` |
| Flemish - Belgia                     | `nl_BE` |
| Belanda - Belanda                    | `nl_NL` |
| Norwegia Nynorsk - Norwegia          | `nn_NO` |
| Polandia - Polandia                  | `pl_PL` |
| Portugis Brasil - Brasil             | `pt_BR` |
| Portugis Eropa - Portugal            | `pt_PT` |
| Rumania - Rumania                    | `ro_RO` |
| Rusia - Rusia                        | `ru_RU` |
| Slovakia - Slovakia                  | `sk_SK` |
| Slovenia - Slovenia                  | `sl_SI` |
| Albania - Albania                    | `sq_AL` |
| Serbia - Serbia                      | `sr_RS` |
| Swedia - Swedia                      | `sv_SE` |
| Turki - Turki                        | `tr_TR` |
| Ukraina - Ukraina                    | `uk_UA` |
| Tionghoa - Tiongkok                  | `zh_CN` |
| Tionghoa - Taiwan                    | `zh_TW` |


## Cara membuat pemeriksa ejaan bahasa Inggris berfungsi

Agar pemeriksa ejaan bahasa Inggris berfungsi, keluar dari sesi MX Linux 23 lalu pilih ini di Login Manager:

```
Inggris Amerika - Amerika Serikat
```

Lalu edit:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

dan biarkan isi berikut:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

WPS Office 12 sudah menyertakan MUI ini secara bawaan:

```
/opt/kingsoft/wps-office/office6/mui/en_US
```

dan juga kamusnya:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

### Mengaktifkan pemeriksaan ejaan bahasa Inggris

Sekarang buka WPS Writer. Buka tab ribbon bernama:

`"Review"`

dan di sana, pada

`"Spell Check ⌵"`

klik ikon `"⌵"` tersebut lalu klik submenu:

`"Set Spell Check language"`

![](vx_images/20260721.2-WPS_en-US_Home-Review-SpellCheck-SetLanguage-ezgif.com.gif)

di jendela yang terbuka, `"Inggris (Amerika Serikat)"` akan termasuk dalam kamus yang tersedia secara bawaan.

![](vx_images/dicts-tests/01-Set-Spell-Check-Language-English-United-States.png)


jika Anda mau, Anda dapat mengklik `"Change Default"` walaupun itu sudah dipilih secara bawaan karena MUI `en_US` sudah terpasang.

Sekarang, di sudut kiri bawah jendela, perhatikan bilah status; indikator seperti ini akan muncul:

`Spell Check: Disabled ⌵`

Klik indikator itu dan statusnya akan berubah menjadi `"Enabled"`.

Selain itu, jika Anda mengklik ikon `"⌵"`, opsi ini dan opsi lain akan tersedia dalam menu drop-down.

Setelah diaktifkan, WPS Office akan mulai memeriksa ejaan dokumen secara otomatis. Sejak saat itu, kata yang salah eja akan digarisbawahi; klik kanan pada kata yang digarisbawahi akan menampilkan saran koreksi. Pemeriksa ejaan akan tetap aktif sampai pengguna menonaktifkan opsi ini lagi:


![](vx_images/20260721.1-Quotes-MUI-en-US-Richard-Stallman-ezgif.com.gif)

---

## Cara membuat pemeriksa ejaan bahasa Spanyol berfungsi

Agar pemeriksa ejaan bahasa Spanyol berfungsi, keluar dari sesi MX Linux 23 (jika Anda sedang memakai bahasa lain) lalu pilih, misalnya, ini di Login Manager:

```
Spanyol - Ekuador
```

Lalu edit:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

dan biarkan isi untuk Spanyol dari Spanyol berikut:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Dalam konfigurasi ini, MUI berikut harus terpasang:

```
/opt/kingsoft/wps-office/office6/mui/es_ES
```

dan kamusnya:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
```


### Mengaktifkan pemeriksaan ejaan bahasa Spanyol

Buka WPS Writer. Buka tab ribbon bernama:

`"Revisar"`

dan di sana, pada

`"Revisión ortográfica ⌵"`

klik ikon `"⌵"` tersebut lalu klik submenu:

`"Establecer idioma"`

dan di jendela yang terbuka, `"Español (España)"` akan termasuk dalam kamus yang tersedia secara bawaan.

dan klik `"Establecer predeterminado"` walaupun itu sudah dipilih secara bawaan karena MUI `es_ES` sudah terpasang.

Sekarang, di sudut kiri bawah jendela, perhatikan bilah status; indikator seperti ini akan muncul:

`Revisión ortográfica: Desactivado ⌵`

Klik indikator itu dan statusnya akan berubah menjadi `"Activado"`.

![](vx_images/20260716.1-Frases-MUI-es-ES-Richard-Stallman-ezgif.com.gif)

Selain itu, jika Anda mengklik ikon `"⌵"`, opsi ini dan opsi lain akan tersedia dalam menu drop-down.

Setelah pemeriksaan ejaan diaktifkan, WPS Office akan mulai memeriksa ejaan dokumen secara otomatis. Sejak saat itu, kata yang salah eja akan digarisbawahi; klik kanan pada kata yang digarisbawahi akan menampilkan saran koreksi. Pemeriksa ejaan akan tetap aktif sampai pengguna menonaktifkan opsi ini lagi:

Untuk saat ini, pada WPS Office 12 versi Tiongkok ini, pemeriksaan ejaan bahasa Spanyol hanya berfungsi dengan kamus `es_ES` dari repositori ini:

/build/dicts-active/es_ES/

Namun, kamus berikut di folder `wps-libreoffice-dicts` tidak berfungsi seperti pada WPS Office 11:

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

### Pengaturan regional bahasa Spanyol yang masih perlu diuji

Pengaturan regional Login Manager berikut masih perlu diuji dengan pemeriksa ejaan bahasa Spanyol:

```
Spanyol - Argentina
Spanyol - Bolivia
Spanyol - Kolombia
Spanyol - Nikaragua
Spanyol - Panama
```

Yang lainnya yang berhasil sudah tercantum di tabel di atas.

## Pengujian kamus Spanyol Meksiko yang tidak berfungsi

Saya melakukan pengujian berikut karena MUI `es_MX` dan kamus pemeriksa ejaan `es_MX` tersedia.

Pengujian dilakukan dengan masuk dari Login Manager menggunakan:

```
Spanyol Meksiko - Meksiko
```

dan mengonfigurasi WPS dengan:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Dengan MUI:

```
/opt/kingsoft/wps-office/office6/mui/es_MX
```

dan kamus di:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_MX/
```

WPS menampilkan `"Español (México)"` di jendela bahasa, tetapi pemeriksaan ejaan tidak berfungsi. Namun, jika kamus `"Español (España)"` dipilih di jendela yang sama, pemeriksaan ejaan berfungsi.

## Cara membuat pemeriksa ejaan bahasa Jerman berfungsi

Untuk bahasa Jerman, keluar dari sesi lalu pilih ini di Login Manager:

```
Jerman - Jerman
```

Lalu konfigurasikan `Office.conf` seperti ini:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Aktivasinya mirip dengan kamus bahasa Inggris:

![](vx_images/Quotes-tests/Deutsch-de_DE-Richard-S-ezgif.com.gif)

Dalam pengujian ini, yang berikut berfungsi:

```
/opt/kingsoft/wps-office/office6/mui/de_DE
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

## Cara membuat pemeriksa ejaan bahasa Prancis berfungsi

Untuk bahasa Prancis, keluar dari sesi lalu pilih ini di Login Manager:

```
Prancis - Prancis
```

Aktivasinya mirip dengan kamus bahasa Inggris.


![](vx_images/Quotes-tests/citation_fr-FR_Richard_S-ezgif.com.gif)

Lalu konfigurasikan `Office.conf` seperti ini:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Dalam pengujian ini, pemeriksaan berfungsi dengan:

```
/opt/kingsoft/wps-office/office6/mui/fr_FR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
```



## Cara membuat pemeriksa ejaan bahasa Indonesia berfungsi

Untuk bahasa Indonesia, buat locale terlebih dahulu jika belum muncul di Login Manager:

```bash
sudo dpkg-reconfigure locales
```

Di daftar, tandai:

```
id_ID.UTF-8 UTF-8
```

Lalu keluar dari sesi dan pilih ini di Login Manager:

```
Indonesia - Indonesia
```

Lalu konfigurasikan `Office.conf` seperti ini:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Aktivasinya mirip dengan kamus bahasa Inggris. `"Indonesia"` seharusnya muncul di jendela bahasa pemeriksaan ejaan.

![](vx_images/Quotes-tests/Kutipan-id_ID-Richard-S-ezgif.com.gif)

Dalam pengujian ini, pemeriksaan berfungsi dengan:

```
/opt/kingsoft/wps-office/office6/mui/id_ID
/opt/kingsoft/wps-office/office6/dicts/spellcheck/id_ID/
```

Catatan: walaupun sesi Linux menggunakan `id_ID.UTF-8`, kamus `id_ID` yang terpasang menggunakan `SET ISO8859-1` di `main.aff` dan berfungsi dengan benar di WPS Office 12.

## Cara membuat pemeriksa ejaan bahasa Polandia berfungsi

Untuk bahasa Polandia, keluar dari sesi lalu pilih ini di Login Manager:

```
Polandia - Polandia
```

Lalu konfigurasikan `Office.conf` seperti ini:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Aktivasinya mirip dengan kamus bahasa Inggris. `"Polski"` seharusnya muncul di jendela bahasa pemeriksaan ejaan.

![](vx_images/Quotes-tests/Cytaty_pl-PL_RichardS-ezgif.com.gif)


Dalam pengujian ini, pemeriksaan berfungsi dengan:

```
/opt/kingsoft/wps-office/office6/mui/pl_PL
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pl_PL/
```

Catatan: untuk pengujian ini, kamus `pl_PL` UTF-8 yang diambil dari kamus lama WPS Office 11.2.0.9255 berfungsi. Kamus yang dikonversi dari LibreOffice menggunakan `ISO8859-2` dan tidak bekerja dengan baik di WPS Office 12.

## Cara membuat pemeriksa ejaan bahasa Portugis Brasil berfungsi

Untuk bahasa Portugis Brasil, keluar dari sesi lalu pilih ini di Login Manager:

```
Portugis Brasil - Brasil
```

Lalu konfigurasikan `Office.conf` seperti ini:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Aktivasinya mirip dengan kamus bahasa Inggris. `"Português do Brasil"` seharusnya muncul di jendela bahasa pemeriksaan ejaan.

![](vx_images/Quotes-tests/Citacoes_pt-BR_Richard_S-ezgif.com.gif)

Dalam pengujian ini, pemeriksaan berfungsi dengan:

```
/opt/kingsoft/wps-office/office6/mui/pt_BR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Catatan: walaupun MUI `pt_BR` berisi `FallBack=pt_PT` di `lang.conf`, WPS memeriksa ejaan dengan benar saat `"Português do Brasil"` dipilih di jendela bahasa pemeriksaan ejaan. Jika `"Português (Portugal)"` dipilih dalam sesi yang sama, pemeriksa ejaan tidak berfungsi.

## Pengujian kamus Portugis Portugal yang tidak berfungsi

Saya melakukan pengujian berikut karena MUI `pt_PT` dan kamus pemeriksa ejaan `pt_PT` tersedia.

Pengujian dilakukan dengan masuk dari Login Manager menggunakan:

```
Portugis Eropa - Portugal
```

dan mengonfigurasi WPS dengan:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Dengan MUI:

```
/opt/kingsoft/wps-office/office6/mui/pt_PT
```

dan kamus di:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/
```

WPS menampilkan `"Portuguê"` sebelum nama kamus diperbaiki, dan sekarang seharusnya menampilkan `"Português (Portugal)"`; dalam kedua kasus tersebut, pemeriksaan ejaan tidak berfungsi dengan kamus `pt_PT`.

Dalam konfigurasi locale `pt_PT.UTF-8` dan MUI `pt_PT` yang sama, pemeriksaan ejaan berfungsi menggunakan kamus Portugis Brasil:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

## Cara membuat pemeriksa ejaan bahasa Rusia berfungsi

Untuk bahasa Rusia, keluar dari sesi lalu pilih ini di Login Manager:

```
Rusia - Rusia
```

Lalu konfigurasikan `Office.conf` seperti ini:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Aktivasinya mirip dengan kamus bahasa Inggris. `"Русский (Россия)"` seharusnya muncul di jendela bahasa pemeriksaan ejaan.

![](vx_images/Quotes-tests/Frase_ru_RU_RichardS-ezgif.com.gif)


Dalam pengujian ini, pemeriksaan berfungsi dengan:

```
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

Catatan: pemeriksa ejaan bahasa Rusia berfungsi dengan benar pada dokumen baru yang dibuat dari awal. Pada dokumen yang awalnya dibuat dalam bahasa Inggris, meskipun teks Rusia terjemahan ditempelkan, WPS tidak menerapkan pemeriksaan ejaan dengan benar pada teks yang sudah ada.

## Cara membuat pemeriksa ejaan bahasa Turki berfungsi

Untuk bahasa Turki, keluar dari sesi lalu pilih ini di Login Manager:

```
Turki - Turki
```

Lalu konfigurasikan `Office.conf` seperti ini:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Aktivasinya mirip dengan kamus bahasa Inggris. `"Türkçe (Türkiye)"` seharusnya muncul di jendela bahasa pemeriksaan ejaan.

![](vx_images/Quotes-tests/Alntlar-tr_TR-Richard-S-ezgif.com.gif)

Dalam pengujian ini, pemeriksaan berfungsi dengan:

```
/opt/kingsoft/wps-office/office6/mui/tr_TR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/tr_TR/
```

## Referensi: paket MUI yang diunduh WPS di Windows

Jika Anda penasaran dari mana berkas MUI untuk antarmuka grafis berasal, saya mendapatkannya di Microsoft Windows 10. WPS Office mengunduh paket bahasa ke path pengguna; informasi ini berguna sebagai referensi untuk meneliti berkas bahasa antarmuka.

Pertama unduh dan pasang WPS Office 12 untuk Windows:

[https://wps.com/office/windows/](https://wps.com/office/windows/)

Contoh di Windows 10:

![](vx_images/02-WPS-Office-global-config-menu.png)

Kemudian unduh bahasa:

![](vx_images/03-Click-on-a-language-and-then-click-Apply.png)

Bahasa yang diunduh mungkin muncul di:

```
C:\Users\youruser\AppData\Roaming\kingsoft\wps_intl\addons\pool\win-x64
```

![](vx_images/04-downloaded-languages.png)

Daftar bahasa mungkin muncul di:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui\lang_list\lang_list.json
```

![20260416-000808](vx_images/507184629680596.png)

Beberapa paket yang disertakan oleh versi Windows bahasa Spanyol mungkin muncul di:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui
```

![](vx_images/05-languages-downloaded-by-the-Spanish-version.png)

Jika proyek ini membantu Anda, Anda dapat memberi bintang pada repositori.

---

# Ucapan terima kasih

Kepada pengguna [mmvill](https://github.com/mmvill), yang menulis kepada saya dan memberi tahu bahwa ia menemukan cara untuk membuat kamus pemeriksa ejaan bahasa Spanyol berfungsi di WPS Office 12.
