# Guia rápido: corretor ortográfico em português do Brasil no WPS Office 12 para Linux

Este guia curto instala a interface e o corretor ortográfico em português do Brasil para WPS Office 12 no Linux.

## Requisitos

- WPS Office 12.x instalado.
- Conexão com a internet para baixar os arquivos do Release.
- Permissões de administrador com `sudo`.
- WPS Office aberto pelo menos uma vez para que `~/.config/Kingsoft/Office.conf` exista.

## Instalar WPS Office

Baixe WPS Office 12 para Linux pelo site chinês oficial:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Você pode instalar o pacote `.deb` com seu instalador de pacotes:

![](../vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

ou pelo terminal:

```bash
sudo dpkg -i wps-office*.deb
```

## Baixar os arquivos do Release

Vá para a seção Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

Baixe estes dois arquivos:

- `wps-office-12-mui.tar.xz`
- `wps-office-12-dicts-active.tar.xz`

![](../vx_images/09-release-wps-12.1.2-language-packs-v1.png)

## Instalar MUI

Extraia `wps-office-12-mui.tar.xz` com o botão direito no seu gerenciador de arquivos preferido. Você obterá a pasta:

```text
wps-office-12-mui
```

Abra um terminal dentro dessa pasta. Em sistemas Linux modernos, ao clicar com o botão direito dentro de uma pasta geralmente aparece uma opção como `Open terminal here`.

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

## Instalar dicionários

Extraia `wps-office-12-dicts-active.tar.xz` com o botão direito no seu gerenciador de arquivos preferido. Você obterá a pasta:

```text
wps-office-12-dicts-active
```

Abra um terminal dentro dessa pasta e execute:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Para português do Brasil, o WPS Office 12 usará:

```text
/opt/kingsoft/wps-office/office6/mui/pt_BR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

## Configurar WPS Office

Se você não tiver o Gedit instalado, instale-o primeiro:

```bash
sudo apt install gedit
```

Edite:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Use este conteúdo:

```ini
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Feche completamente o WPS Office e abra novamente.

## Ativar a correção ortográfica

No WPS Writer, selecione `Português do Brasil` como idioma da correção ortográfica e defina como padrão se necessário.

![](../vx_images/dicts-tests/08-Login-locale-pt-BR_WPS-MUI-pt-BR_Dict-pt-BR-UTF-8_WPS-select-Portugues-do-Brasil.png)

![](../vx_images/Quotes-tests/Citacoes_pt-BR_Richard_S-ezgif.com.gif)
