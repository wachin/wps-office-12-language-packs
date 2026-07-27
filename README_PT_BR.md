# Pacotes de idioma do WPS Office 12.x para Linux

Traduções disponíveis:

- [Inglês](README.md), disponível para usuários de inglês.
- [Español](README_ES.md), disponível para usuários de espanhol.
- [Deutsch](README_DE.md), disponível para usuários de alemão.
- [Français](README_FR.md), disponível para usuários de francês.
- [Bahasa Indonesia](README_ID.md), disponível para usuários de indonésio.

## Baixar o WPS Office 12 Linux versão chinesa

Baixe o instalador do WPS Office para sua distribuição Linux, seja ela baseada em DEB ou RPM.

Site oficial chinês:

- [https://www.wps.cn](https://www.wps.cn)

ao clicar ali, você será redirecionado para:

[https://www.wps.cn/product/wpslinux](https://www.wps.cn/product/wpslinux)

Depois instale o pacote.

**Download espelho (Mirror)**
No entanto, ele pode não ter as versões mais recentes, ou pode demorar um pouco até que elas sejam enviadas para lá:

[https://mirrors.163.com/ubuntukylin/pool/partner/](https://mirrors.163.com/ubuntukylin/pool/partner/)

### Instalar o pacote DEB com um instalador de pacotes DEB

Instale-o com um gerenciador de pacotes DEB. Em sistemas Linux, algum deles já deve estar instalado; clique com o botão direito no arquivo no gerenciador de arquivos e instale com essa ferramenta:

![](vx_images/08-Instalando-wps-office-12.1.2.25882-amd-deb.png)

### Instalar pelo terminal (Opcional)

Se você usa Debian, Ubuntu, Linux Mint ou distribuições semelhantes, também pode fazer isso pelo terminal:

```bash
sudo dpkg -i wps-office*.deb
```

Se você usa Fedora, Red Hat ou distribuições semelhantes:

```bash
sudo dnf install wps-office*.rpm
```

## Requisitos

Para continuar com este tutorial, você precisa:

- Ter o **WPS Office 12.x** instalado no Linux conforme descrito acima.
- Ter permissões de administrador com `sudo` ou ferramenta equivalente.
- Ter aberto o WPS Office pelo menos uma vez. O WPS Office cria sua configuração de usuário depois de ser aberto pela primeira vez. Se `~/.config/Kingsoft/Office.conf` não existir, abra o WPS Office, feche-o e continue a instalação.
- Ter conexão com a internet para baixar os arquivos do Release.

## Instalar as interfaces de usuário multilíngues MUI

Baixe o pacote MUI. Vá para a seção Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

baixe o arquivo:

wps-office-12-mui.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Extraia-o com o botão direito **no seu gerenciador de arquivos preferido**. Depois disso você obterá a pasta:

`wps-office-12-mui`

Então clique com o botão direito nessa pasta e escolha `Open terminal here` ou uma opção parecida. Em sistemas Linux modernos, o clique com o botão direito geralmente oferece essa opção. A partir dali,

instale os arquivos MUI com este comando:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/
```

Este comando instala os arquivos MUI (interfaces de usuário multilíngues).

## Verificar a instalação

Esse comando `sudo cp -r ./* /opt/kingsoft/wps-office/office6/mui/` copia as pastas de idioma disponíveis para a pasta real do WPS Office no Linux: `/opt/kingsoft/wps-office/office6/mui/`.

A versão chinesa do WPS Office 12 que acabamos de instalar inclui estas pastas MUI por padrão:

```
/opt/kingsoft/wps-office/office6/mui/en_US
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/mui/zh_CN
```

Estas são:

- `en_US` idioma inglês (Estados Unidos)
- `ru_RU` idioma russo (Federação Russa)
- `zh_CN` idioma chinês (China)

e também inclui estes dois dicionários de correção ortográfica por padrão:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_CH
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US
```

Estes são:

- `en_CH` dicionário chinês e inglês (Estados Unidos)
- `en_US` dicionário inglês (Estados Unidos)

No seu gerenciador de arquivos, verifique este caminho:

/opt/kingsoft/wps-office/office6/mui/

Além dos idiomas incluídos na versão chinesa, você deve ter o seguinte:

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

Isto também é copiado:

```
lang_list
```

É uma lista de seleção.


## Dicionários disponíveis e dicionários testados

Este repositório também prepara dicionários Hunspell para que o **WPS Office 12.x** possa usá-los no Linux.

Por enquanto, é preciso distinguir duas pastas:

```
build/wps-office-12-dicts-active/
wps-libreoffice-dicts/
```

A pasta `build/wps-office-12-dicts-active/` contém os dicionários selecionados para instalação agora. São os que estão sendo usados nos testes do WPS Office 12.

A pasta `wps-libreoffice-dicts/` contém todos os dicionários convertidos do LibreOffice. Ela é mantida na raiz do repositório porque, na versão chinesa do WPS Office 12, nem todas as variantes funcionam mesmo quando têm o formato correto. Talvez em uma versão futura o WPS volte a oferecer suporte a todos esses dicionários, como acontecia em versões antigas do WPS Office para Linux.

Cada pasta de dicionário tem o formato que o WPS espera:

```
dict.conf
main.aff
main.dic
```

Os arquivos `main.aff` e `main.dic` vêm principalmente da coleção de dicionários do LibreOffice:

```
third-party/libreoffice-dictionaries-collection/dicts/
```

Repositório de origem:

[https://github.com/wachin/libreoffice-dictionaries-collection](https://github.com/wachin/libreoffice-dictionaries-collection)

Os arquivos `dict.conf` são reutilizados de dicionários antigos do WPS Office quando existem, e gerados para as novas variantes.

Exceção importante: o dicionário ativo `pl_PL` vem dos dicionários antigos do WPS Office 11.2.0.9255:

```
third-party/wps-office-11.2.0.9255-dicts/dicts/pl_PL/
```

Repositório de origem:

[https://github.com/wachin/wps-office-11.2.0.9255-dicts](https://github.com/wachin/wps-office-11.2.0.9255-dicts)

Esse `pl_PL` é usado porque o dicionário polonês convertido do LibreOffice não funcionou bem no WPS Office 12. Seu arquivo `main.aff` contém:

```
SET ISO8859-2
```

Em contraste, o dicionário polonês antigo do WPS está em UTF-8 e seu `main.aff` contém:

```
SET UTF-8
```

Os dicionários atualmente ativos são:

| Código  | Dicionário            |
| ------- | --------------------- |
| `de_DE` | Alemão (Alemanha)     |
| `es_ES` | Espanhol (Espanha)    |
| `fr_FR` | Francês (França)      |
| `id_ID` | Indonésio             |
| `pl_PL` | Polonês               |
| `pt_BR` | Português (Brasil)    |
| `pt_PT` | Português             |
| `ru_RU` | Russo (Rússia)        |
| `tr_TR` | Turco (Turquia)       |

Nota sobre `pt_PT`: no MX Linux 23 com locale `pt_PT.UTF-8`, MUI `pt_PT` e o dicionário instalado como `/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/`, o WPS Office 12 não ativa a correção ortográfica para português de Portugal nos testes atuais. Na mesma instalação, a correção funciona usando o dicionário `pt_BR`.


## Instalar os dicionários

Vá para a seção Releases:

[https://github.com/wachin/wps-office-12-language-packs/releases](https://github.com/wachin/wps-office-12-language-packs/releases)

baixe o arquivo:

wps-office-12-dicts-active.tar.xz

![](vx_images/09-release-wps-12.1.2-language-packs-v1.png)

Extraia-o com o botão direito no seu gerenciador de arquivos preferido. Depois disso você obterá a pasta:

`wps-office-12-dicts-active`

Então clique com o botão direito nessa pasta e escolha `Open terminal here` ou uma opção parecida. Em sistemas Linux modernos, o clique com o botão direito geralmente oferece essa opção. A partir dali,

instale os arquivos de dicionário com este comando:

```bash
sudo cp -r ./* /opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Isso copia os dicionários ativos para a pasta que o WPS usa para a correção ortográfica.

Depois de copiar, o caminho do WPS deve conter pastas como estas:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

E dentro de cada uma:

```
dict.conf
main.aff
main.dic
```

## Ativar um idioma de interface na configuração do WPS

Se você é desenvolvedor, edite o arquivo de configuração com nano:

```bash
nano ~/.config/Kingsoft/Office.conf
```

Se você é um usuário comum, use Gedit ou outro editor de texto. Se não tiver o Gedit instalado, instale assim:

```bash
sudo apt install gedit
```

e digite isto no terminal:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

Depois que esse arquivo estiver aberto, selecione todo o texto com `Ctrl + A`, apague e substitua pelo conteúdo correspondente ao idioma que você quer usar.

A estrutura é sempre a mesma:

```
[General]
languages=CODIGO_DO_IDIOMA

[6.0]
common\DefaultLanguage=NUMERO_DO_IDIOMA
common\Local\UILanguage=NUMERO_DO_IDIOMA
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Use esta tabela para escolher o código e o número corretos:

| Idioma                           | `languages=` | `DefaultLanguage` e `UILanguage`   |
| -------------------------------- | ------------ | ---------------------------------- |
| Inglês (Estados Unidos)          | `en_US`      | `1033`                             |
| Alemão (Alemanha)                | `de_DE`      | `1031`                             |
| Espanhol (Espanha)               | `es_ES`      | `3082`                             |
| Espanhol (México)                | `es_MX`      | `2058`                             |
| Francês (Canadá)                 | `fr_CA`      | `3084`                             |
| Francês (França)                 | `fr_FR`      | `1036`                             |
| Indonésio                        | `id_ID`      | `1057`                             |
| Japonês                          | `ja_JP`      | `1041`                             |
| Polonês                          | `pl_PL`      | `1045`                             |
| Português (Brasil)               | `pt_BR`      | `1046`                             |
| Português (Portugal)             | `pt_PT`      | `2070`                             |
| Russo                            | `ru_RU`      | `1049`                             |
| Tailandês                        | `th_TH`      | `1054`                             |
| Turco                            | `tr_TR`      | `1055`                             |
| Chinês (simplificado, China)     | `zh_CN`      | `2052`                             |
| Chinês (tradicional, Hong Kong)  | `zh_HK`      | `3076`                             |

### Tabela rápida: locale, MUI e dicionário com o mesmo código

Esta tabela mostra os idiomas em que é possível comparar diretamente se o `Locale`, o MUI e o dicionário usam o mesmo código. O `x` significa que não há um dicionário ativo incluído com esse mesmo código. O símbolo `✅` marca os casos testados em que essa combinação exata funciona.

| Idioma mostrado no Login Manager    | `Locale` | `MUI`    | `Dict`  | Testado |
| ----------------------------------- | -------- | -------- | ------- | ------- |
| Inglês (Estados Unidos)             | `en_US`  | `en_US`  | `en_US` | ✅      |
| Alemão (Alemanha)                   | `de_DE`  | `de_DE`  | `de_DE` | ✅      |
| Espanhol (Espanha)                  | `es_ES`  | `es_ES`  | `es_ES` | ✅      |
| Espanhol (México)                   | `es_MX`  | `es_MX`  | x       |         |
| Francês (Canadá)                    | `fr_CA`  | `fr_CA`  | x       |         |
| Francês (França)                    | `fr_FR`  | `fr_FR`  | `fr_FR` | ✅      |
| Indonésio                           | `id_ID`  | `id_ID`  | `id_ID` | ✅      |
| Japonês                             | `ja_JP`  | `ja_JP`  | x       |         |
| Polonês                             | `pl_PL`  | `pl_PL`  | `pl_PL` | ✅      |
| Português (Brasil)                  | `pt_BR`  | `pt_BR`  | `pt_BR` | ✅      |
| Português (Portugal)                | `pt_PT`  | `pt_PT`  | `pt_PT` |         |
| Russo                               | `ru_RU`  | `ru_RU`* | `ru_RU` | ✅      |
| Tailandês                           | `th_TH`  | `th_TH`  | x       |         |
| Turco                               | `tr_TR`  | `tr_TR`  | `tr_TR` | ✅      |
| Chinês (simplificado, China)        | `zh_CN`  | `zh_CN`  | x       |         |
| Chinês (tradicional, Hong Kong)     | `zh_HK`  | `zh_HK`  | x       |         |

* A versão chinesa do WPS Office 12 já inclui o MUI `ru_RU` por padrão, por isso o arquivo MUI do Release não precisa incluir essa pasta. O dicionário de correção ortográfica `ru_RU` continua sendo instalado pelo arquivo de dicionários.

### Para inglês dos Estados Unidos:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para espanhol da Espanha:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para alemão da Alemanha:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


### Para espanhol do México:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para francês do Canadá:

```
[General]
languages=fr_CA

[6.0]
common\DefaultLanguage=3084
common\Local\UILanguage=3084
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para francês da França:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para indonésio:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para japonês:

```
[General]
languages=ja_JP

[6.0]
common\DefaultLanguage=1041
common\Local\UILanguage=1041
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para polonês:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para português do Brasil:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para português de Portugal:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para russo:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para tailandês:

```
[General]
languages=th_TH

[6.0]
common\DefaultLanguage=1054
common\Local\UILanguage=1054
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para turco:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para chinês simplificado da China:

```
[General]
languages=zh_CN

[6.0]
common\DefaultLanguage=2052
common\Local\UILanguage=2052
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

### Para chinês tradicional de Hong Kong:

```
[General]
languages=zh_HK

[6.0]
common\DefaultLanguage=3076
common\Local\UILanguage=3076
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```


Salve o arquivo, feche completamente o WPS Office e abra-o novamente. Se o idioma foi configurado corretamente, a interface abrirá no idioma escolhido.

## Solução para fazer os corretores ortográficos funcionarem no WPS Office 12

Na versão chinesa do WPS Office 12, não basta copiar um dicionário para esta pasta:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/
```

Também influenciam a configuração regional usada ao entrar na sessão Linux pelo Login Manager, o idioma MUI instalado no WPS Office e o idioma configurado neste arquivo:

```
~/.config/Kingsoft/Office.conf
```

Por isso alguns dicionários aparecem na janela `"Set language"`, mas não corrigem a ortografia. O caso mais claro é o espanhol do México: o MUI `es_MX` e o dicionário `es_MX` podem aparecer instalados, mas nos testes a correção ortográfica só funcionou com o dicionário `es_ES`.

### Testes confirmados

Estes são os testes realizados até agora:

| Corretor        | Configuração regional escolhida no Login Manager   | Locale  | MUI usado no WPS | Dicionário instalado  | Estado        |
| --------------- | -------------------------------------------------- | ------- | ---------------- | --------------------- | ------------- |
| Inglês          | `Inglês americano - Estados Unidos`                | `en_US` | `en_US`          | `en_US` UTF-8         | Funciona      |
| Inglês          | `Inglês - Irlanda`                                 | `en_IE` | `en_US`          | `en_US` UTF-8         | Funciona      |
| Inglês          | `Inglês australiano - Austrália`                   | `en_AU` | `en_US`          | `en_US` UTF-8         | Funciona      |
| Inglês          | `Inglês britânico - Reino Unido`                   | `en_GB` | `en_US`          | `en_US` UTF-8         | Funciona      |
| Inglês          | `Inglês - Nova Zelândia`                           | `en_NZ` | `en_US`          | `en_US` UTF-8         | Não funciona  |
| Espanhol        | `Espanhol - Equador`                               | `es_EC` | `es_ES`          | `es_ES` UTF-8         | Funciona      |
| Espanhol        | `Espanhol europeu - Espanha`                       | `es_ES` | `es_ES`          | `es_ES` UTF-8         | Funciona      |
| Espanhol        | `Espanhol - Estados Unidos`                        | `es_US` | `es_ES`          | `es_ES` UTF-8         | Funciona      |
| Espanhol        | `Espanhol - Venezuela`                             | `es_VE` | `es_ES`          | `es_ES` UTF-8         | Funciona      |
| Espanhol        | `Espanhol mexicano - México`                       | `es_MX` | `es_ES`          | `es_ES` UTF-8         | Funciona      |
| Espanhol        | `Espanhol - Peru`                                  | `es_PE` | `es_ES`          | `es_ES` UTF-8         | Funciona      |
| Espanhol        | `Espanhol - Uruguai`                               | `es_UY` | `es_ES`          | `es_ES` UTF-8         | Funciona      |
| Espanhol México | `Espanhol mexicano - México`                       | `es_MX` | `es_MX`          | `es_MX` UTF-8         | Não funciona  |
| Alemão          | `Alemão austríaco - Áustria`                       | `de_AT` | `de_DE`          | `de_DE` ISO8859-1     | Funciona      |
| Alemão          | `Alemão - Alemanha`                                | `de_DE` | `de_DE`          | `de_DE` ISO8859-1     | Funciona      |
| Alemão          | `Alto alemão suíço - Suíça`                        | `de_CH` | `de_DE`          | `de_DE` ISO8859-1     | Funciona      |
| Francês         | `Francês - França`                                 | `fr_FR` | `fr_FR`          | `fr_FR` UTF-8         | Funciona      |
| Francês         | `Francês canadense - Canadá`                       | `fr_CA` | `fr_CA`          | `fr_FR` UTF-8         | Funciona      |
| Indonésio       | `Indonésio - Indonesia`                            | `id_ID` | `id_ID`          | `id_ID` ISO8859-1     | Funciona      |
| Polonês         | `Polonês - Polônia`                                | `pl_PL` | `pl_PL`          | `pl_PL` UTF-8         | Funciona      |
| Português BR    | `Português brasileiro - Brasil`                    | `pt_BR` | `pt_BR`          | `pt_BR` UTF-8         | Funciona      |
| Português PT    | `Português europeu - Portugal`                     | `pt_PT` | `pt_PT`          | `pt_PT` UTF-8         | Não funciona  |
| Português PT    | `Português europeu - Portugal`                     | `pt_PT` | `pt_PT`          | `pt_BR` UTF-8         | Funciona      |
| Russo           | `Russo - Rússia`                                   | `ru_RU` | `ru_RU`          | `ru_RU` UTF-8         | Funciona      |
| Turco           | `Turco - Turquia`                                  | `tr_TR` | `tr_TR`          | `tr_TR` UTF-8         | Funciona      |

A codificação mostrada na coluna `Dicionário instalado` é obtida da linha `SET` do arquivo `main.aff` de cada dicionário.

**Nota sobre `pl_PL`**: depois de substituir o dicionário pela versão UTF-8 obtida dos dicionários antigos do WPS Office 11.2.0.9255, foi necessário selecioná-lo manualmente em `"Review"` > `"Spell Check ⌵"` > `"Set language"` > `"Polski"`. Depois de selecioná-lo, a correção ortográfica funcionou. O dicionário polonês convertido do LibreOffice não funcionou bem porque estava em `ISO8859-2`, como visto no arquivo `main.aff`.

**Nota sobre `pt_PT`**: com locale `pt_PT.UTF-8`, MUI `pt_PT` e dicionário `pt_PT`, o WPS Office 12 não ativou a correção ortográfica. Nessa mesma configuração, funcionou usando o dicionário `pt_BR`.

**Nota sobre `ru_RU`**: o corretor funcionou em um documento novo criado do zero. Em um documento originalmente criado em inglês, mesmo depois de colar texto russo traduzido, o WPS não aplicou corretamente a correção ortográfica ao texto existente.

No MX Linux 23, o locale pode ser visto no Login Manager: ao selecionar um idioma na lista, o Login Manager mostra o código do locale. Por exemplo, se você clicar em:

```
Espanhol mexicano - México
```

aparecerá:

```
es_MX
```

Se você já entrou na sessão e quer ver qual locale o sistema está usando, abra um terminal e execute:

```bash
echo $LANG
```

Exemplo:

```bash
$ echo $LANG
es_MX.UTF-8
```

### Lista de idiomas disponíveis no Login Manager do MX Linux 23

Esta é a lista observada no Login Manager do MX Linux 23:

![](vx_images/20260717.1-MX-Linux-23_Login-Manager-lnguages-ezgif.com.gif)

Disponível como tabela com locales:

| Language in the Login Manager        | Locale  |
| ------------------------------------ | ------- |
| Árabe - Egito                        | `ar_EG` |
| Bielorrusso - Bielorrússia           | `be_BY` |
| Búlgaro - Bulgária                   | `bg_BG` |
| Catalão - Espanha                    | `ca_ES` |
| Tcheco - República Tcheca            | `cs_CZ` |
| Dinamarquês - Dinamarca              | `da_DK` |
| Alemão austríaco - Áustria           | `de_AT` |
| Alto alemão suíço - Suíça            | `de_CH` |
| Alemão - Alemanha                    | `de_DE` |
| Grego - Grécia                       | `el_GR` |
| Inglês australiano - Austrália       | `en_AU` |
| Inglês canadense - Canadá            | `en_CA` |
| Inglês britânico - Reino Unido       | `en_GB` |
| Inglês - Irlanda                     | `en_IE` |
| Inglês - Nova Zelândia               | `en_NZ` |
| Inglês americano - Estados Unidos    | `en_US` |
| Espanhol - Argentina                 | `es_AR` |
| Espanhol - Bolívia                   | `es_BO` |
| Espanhol - Colômbia                  | `es_CO` |
| Espanhol - Equador                   | `es_EC` |
| Espanhol europeu - Espanha           | `es_ES` |
| Espanhol mexicano - México           | `es_MX` |
| Espanhol - Nicarágua                 | `es_NI` |
| Espanhol - Panamá                    | `es_PA` |
| Espanhol - Peru                      | `es_PE` |
| Espanhol - Estados Unidos            | `es_US` |
| Espanhol - Uruguai                   | `es_UY` |
| Espanhol - Venezuela                 | `es_VE` |
| Estoniano - Estônia                  | `et_EE` |
| Basco - Espanha                      | `eu_ES` |
| Persa - Irã                          | `fa_IR` |
| Finlandês - Finlândia                | `fi_FI` |
| Francês - Bélgica                    | `fr_BE` |
| Francês canadense - Canadá           | `fr_CA` |
| Francês suíço - Suíça                | `fr_CH` |
| Francês - França                     | `fr_FR` |
| Irlandês - Irlanda                   | `ga_IE` |
| Hebraico - Israel                    | `he_IL` |
| Croata - Croácia                     | `hr_HR` |
| Húngaro - Hungria                    | `hu_HU` |
| Islandês - Islândia                  | `is_IS` |
| Italiano - Itália                    | `it_IT` |
| Japonês - Japão                      | `ja_JP` |
| Georgiano - Geórgia                  | `ka_GE` |
| Cazaque - Cazaquistão                | `kk_KZ` |
| Coreano - Coreia do Sul              | `ko_KR` |
| Lituano - Lituânia                   | `lt_LT` |
| Letão - Letônia                      | `lv_LV` |
| Macedônio - Macedônia                | `mk_MK` |
| Norueguês Bokmål - Noruega           | `nb_NO` |
| Flamengo - Bélgica                   | `nl_BE` |
| Neerlandês - Países Baixos           | `nl_NL` |
| Norueguês Nynorsk - Noruega          | `nn_NO` |
| Polonês - Polônia                    | `pl_PL` |
| Português brasileiro - Brasil        | `pt_BR` |
| Português europeu - Portugal         | `pt_PT` |
| Romeno - Romênia                     | `ro_RO` |
| Russo - Rússia                       | `ru_RU` |
| Eslovaco - Eslováquia                | `sk_SK` |
| Esloveno - Eslovênia                 | `sl_SI` |
| Albanês - Albânia                    | `sq_AL` |
| Sérvio - Sérvia                      | `sr_RS` |
| Sueco - Suécia                       | `sv_SE` |
| Turco - Turquia                      | `tr_TR` |
| Ucraniano - Ucrânia                  | `uk_UA` |
| Chinês - China                       | `zh_CN` |
| Chinês - Taiwan                      | `zh_TW` |


## Como fazer o corretor ortográfico em inglês funcionar

Para fazer o corretor ortográfico em inglês funcionar, saia da sessão do MX Linux 23 e escolha isto no Login Manager:

```
Inglês americano - Estados Unidos
```

Depois edite:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

e deixe este conteúdo:

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

O WPS Office 12 já inclui este MUI por padrão:

```
/opt/kingsoft/wps-office/office6/mui/en_US
```

e também o dicionário:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_US/
```

### Ativar a correção ortográfica em inglês

Agora abra o WPS Writer. Vá para a guia da faixa de opções chamada:

`"Review"`

e ali em

`"Spell Check ⌵"`

clique nesse ícone `"⌵"` e clique no submenu:

`"Set Spell Check language"`

![](vx_images/20260721.2-WPS_en-US_Home-Review-SpellCheck-SetLanguage-ezgif.com.gif)

na janela que abrir, `"Inglês (Estados Unidos)"` estará entre os dicionários disponíveis por padrão.

![](vx_images/dicts-tests/01-Set-Spell-Check-Language-English-United-States.png)


se quiser, você pode clicar em `"Change Default"` embora ele já estivesse selecionado por padrão porque o MUI `en_US` já estava instalado.

Agora, no canto inferior esquerdo da janela, observe a barra de status; aparecerá um indicador semelhante a este:

`Spell Check: Disabled ⌵`

Clique nesse indicador e ele mudará para `"Enabled"`.

Além disso, se você clicar no ícone `"⌵"`, esta e outras opções estarão disponíveis em um menu suspenso.

Depois de ativado, o WPS Office começará automaticamente a verificar a ortografia do documento. A partir desse momento, palavras com erro aparecerão sublinhadas; ao clicar com o botão direito sobre uma palavra sublinhada, serão mostradas sugestões de correção. O corretor permanecerá ativo até que o usuário desative essa opção novamente:


![](vx_images/20260721.1-Quotes-MUI-en-US-Richard-Stallman-ezgif.com.gif)

---

## Como fazer o corretor ortográfico em espanhol funcionar

Para fazer o corretor ortográfico em espanhol funcionar, saia da sessão do MX Linux 23 (se estiver em outro idioma) e escolha, por exemplo, isto no Login Manager:

```
Espanhol - Equador
```

Depois edite:

```bash
gedit ~/.config/Kingsoft/Office.conf
```

e deixe este conteúdo de espanhol da Espanha:

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Nesta configuração, este MUI deve estar instalado:

```
/opt/kingsoft/wps-office/office6/mui/es_ES
```

e o dicionário:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_ES/
```


### Ativar a correção ortográfica em espanhol

Abra o WPS Writer. Vá para a guia da faixa de opções chamada:

`"Revisar"`

e ali em

`"Revisión ortográfica ⌵"`

clique nesse ícone `"⌵"` e clique no submenu:

`"Establecer idioma"`

e na janela que abrir, `"Español (España)"` estará entre os dicionários disponíveis por padrão.

e clique em `"Establecer predeterminado"` embora ele já estivesse selecionado por padrão porque o MUI `es_ES` já estava instalado.

Agora, no canto inferior esquerdo da janela, observe a barra de status; aparecerá um indicador semelhante a este:

`Revisión ortográfica: Desactivado ⌵`

Clique nesse indicador e ele mudará para `"Activado"`.

![](vx_images/20260716.1-Frases-MUI-es-ES-Richard-Stallman-ezgif.com.gif)

Além disso, se você clicar no ícone `"⌵"`, esta e outras opções estarão disponíveis em um menu suspenso.

Depois que a correção ortográfica estiver ativada, o WPS Office começará automaticamente a verificar a ortografia do documento. A partir desse momento, palavras com erro aparecerão sublinhadas; ao clicar com o botão direito sobre uma palavra sublinhada, serão mostradas sugestões de correção. O corretor permanecerá ativo até que o usuário desative essa opção novamente:

Por enquanto, nesta versão chinesa do WPS Office 12, a correção ortográfica em espanhol só funciona com o dicionário `es_ES` deste repositório:

/build/wps-office-12-dicts-active/es_ES/

No entanto, os seguintes dicionários na pasta `wps-libreoffice-dicts` não funcionam como funcionavam no WPS Office 11:

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

### Configurações regionais de espanhol ainda por testar

Estas configurações regionais do Login Manager ainda precisam ser testadas com o corretor espanhol:

```
Espanhol - Argentina
Espanhol - Bolívia
Espanhol - Colômbia
Espanhol - Nicarágua
Espanhol - Panamá
```

As outras que funcionaram estão listadas acima na tabela.

## Teste do dicionário espanhol do México que não funcionou

Realizei o seguinte teste porque tanto o MUI `es_MX` quanto o dicionário de correção ortográfica `es_MX` estão disponíveis.

O teste foi feito entrando pelo Login Manager com:

```
Espanhol mexicano - México
```

e configurando o WPS com:

```
[General]
languages=es_MX

[6.0]
common\DefaultLanguage=2058
common\Local\UILanguage=2058
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Com o MUI:

```
/opt/kingsoft/wps-office/office6/mui/es_MX
```

e o dicionário em:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/es_MX/
```

O WPS mostra `"Español (México)"` na janela de idioma, mas a correção ortográfica não funciona. Porém, se o dicionário `"Español (España)"` for selecionado nessa mesma janela, funciona.

## Como fazer o corretor ortográfico em alemão funcionar

Para alemão, saia da sessão e escolha isto no Login Manager:

```
Alemão - Alemanha
```

Depois configure `Office.conf` assim:

```
[General]
languages=de_DE

[6.0]
common\DefaultLanguage=1031
common\Local\UILanguage=1031
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

A ativação é semelhante à do dicionário em inglês:

![](vx_images/Quotes-tests/Deutsch-de_DE-Richard-S-ezgif.com.gif)

Neste teste, isto funcionou:

```
/opt/kingsoft/wps-office/office6/mui/de_DE
/opt/kingsoft/wps-office/office6/dicts/spellcheck/de_DE/
```

## Como fazer o corretor ortográfico em francês funcionar

Para francês, saia da sessão e escolha isto no Login Manager:

```
Francês - França
```

A ativação é semelhante à do dicionário em inglês.


![](vx_images/Quotes-tests/citation_fr-FR_Richard_S-ezgif.com.gif)

Depois configure `Office.conf` assim:

```
[General]
languages=fr_FR

[6.0]
common\DefaultLanguage=1036
common\Local\UILanguage=1036
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Neste teste, funcionou com:

```
/opt/kingsoft/wps-office/office6/mui/fr_FR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/fr_FR/
```



## Como fazer o corretor ortográfico em indonésio funcionar

Para indonésio, primeiro gere o locale se ele ainda não aparecer no Login Manager:

```bash
sudo dpkg-reconfigure locales
```

Na lista, marque:

```
id_ID.UTF-8 UTF-8
```

Depois saia da sessão e escolha isto no Login Manager:

```
Indonésio - Indonesia
```

Depois configure `Office.conf` assim:

```
[General]
languages=id_ID

[6.0]
common\DefaultLanguage=1057
common\Local\UILanguage=1057
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

A ativação é semelhante à do dicionário em inglês. `"Indonésio"` deve aparecer na janela de idioma da correção ortográfica.

![](vx_images/Quotes-tests/Kutipan-id_ID-Richard-S-ezgif.com.gif)

Neste teste, funcionou com:

```
/opt/kingsoft/wps-office/office6/mui/id_ID
/opt/kingsoft/wps-office/office6/dicts/spellcheck/id_ID/
```

Nota: embora a sessão Linux use `id_ID.UTF-8`, o dicionário `id_ID` instalado usa `SET ISO8859-1` em `main.aff` e funcionou corretamente no WPS Office 12.

## Como fazer o corretor ortográfico em polonês funcionar

Para polonês, saia da sessão e escolha isto no Login Manager:

```
Polonês - Polônia
```

Depois configure `Office.conf` assim:

```
[General]
languages=pl_PL

[6.0]
common\DefaultLanguage=1045
common\Local\UILanguage=1045
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

A ativação é semelhante à do dicionário em inglês. `"Polski"` deve aparecer na janela de idioma da correção ortográfica.

![](vx_images/Quotes-tests/Cytaty_pl-PL_RichardS-ezgif.com.gif)


Neste teste, funcionou com:

```
/opt/kingsoft/wps-office/office6/mui/pl_PL
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pl_PL/
```

Nota: para este teste, funcionou o dicionário `pl_PL` em UTF-8 obtido dos dicionários antigos do WPS Office 11.2.0.9255. O dicionário convertido do LibreOffice estava em `ISO8859-2` e não funcionou bem no WPS Office 12.

## Como fazer o corretor ortográfico em português do Brasil funcionar

Para português do Brasil, saia da sessão e escolha isto no Login Manager:

```
Português brasileiro - Brasil
```

Depois configure `Office.conf` assim:

```
[General]
languages=pt_BR

[6.0]
common\DefaultLanguage=1046
common\Local\UILanguage=1046
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

A ativação é semelhante à do dicionário em inglês. `"Português do Brasil"` deve aparecer na janela de idioma da correção ortográfica.

![](vx_images/Quotes-tests/Citacoes_pt-BR_Richard_S-ezgif.com.gif)

Neste teste, funcionou com:

```
/opt/kingsoft/wps-office/office6/mui/pt_BR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

Nota: embora o MUI `pt_BR` contenha `FallBack=pt_PT` em `lang.conf`, o WPS corrigiu corretamente ao selecionar `"Português do Brasil"` na janela de idioma da correção ortográfica. Se `"Português (Portugal)"` for selecionado nessa mesma sessão, o corretor não funciona.

## Teste do dicionário português de Portugal que não funcionou

Realizei o seguinte teste porque tanto o MUI `pt_PT` quanto o dicionário de correção ortográfica `pt_PT` estão disponíveis.

O teste foi feito entrando pelo Login Manager com:

```
Português europeu - Portugal
```

e configurando o WPS com:

```
[General]
languages=pt_PT

[6.0]
common\DefaultLanguage=2070
common\Local\UILanguage=2070
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

Com o MUI:

```
/opt/kingsoft/wps-office/office6/mui/pt_PT
```

e o dicionário em:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_PT/
```

O WPS mostrava `"Portuguê"` antes da correção do nome do dicionário, e agora deve mostrar `"Português (Portugal)"`; em ambos os casos, a correção ortográfica não funcionou com o dicionário `pt_PT`.

Nessa mesma configuração com locale `pt_PT.UTF-8` e MUI `pt_PT`, a correção funcionou usando o dicionário de português do Brasil:

```
/opt/kingsoft/wps-office/office6/dicts/spellcheck/pt_BR/
```

## Como fazer o corretor ortográfico em russo funcionar

Para russo, saia da sessão e escolha isto no Login Manager:

```
Russo - Rússia
```

Depois configure `Office.conf` assim:

```
[General]
languages=ru_RU

[6.0]
common\DefaultLanguage=1049
common\Local\UILanguage=1049
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

A ativação é semelhante à do dicionário em inglês. `"Русский (Россия)"` deve aparecer na janela de idioma da correção ortográfica.

![](vx_images/Quotes-tests/Frase_ru_RU_RichardS-ezgif.com.gif)


Neste teste, funcionou com:

```
/opt/kingsoft/wps-office/office6/mui/ru_RU
/opt/kingsoft/wps-office/office6/dicts/spellcheck/ru_RU/
```

Nota: o corretor russo funcionou corretamente em um documento novo criado do zero. Em um documento criado originalmente em inglês, mesmo depois de colar texto russo traduzido, o WPS não aplicou corretamente a revisão ortográfica ao texto existente.

## Como fazer o corretor ortográfico em turco funcionar

Para turco, saia da sessão e escolha isto no Login Manager:

```
Turco - Turquia
```

Depois configure `Office.conf` assim:

```
[General]
languages=tr_TR

[6.0]
common\DefaultLanguage=1055
common\Local\UILanguage=1055
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
```

A ativação é semelhante à do dicionário em inglês. `"Türkçe (Türkiye)"` deve aparecer na janela de idioma da correção ortográfica.

![](vx_images/Quotes-tests/Alntlar-tr_TR-Richard-S-ezgif.com.gif)

Neste teste, funcionou com:

```
/opt/kingsoft/wps-office/office6/mui/tr_TR
/opt/kingsoft/wps-office/office6/dicts/spellcheck/tr_TR/
```

## Referência: pacotes MUI baixados pelo WPS no Windows

Se você tem curiosidade e se pergunta de onde vieram os arquivos MUI da interface gráfica, eu os obtive no Microsoft Windows 10. O WPS Office baixa pacotes de idioma em caminhos de usuário; esta informação serve como referência para investigar arquivos de idioma da interface.

Primeiro baixe e instale o WPS Office 12 para Windows:

[https://wps.com/office/windows/](https://wps.com/office/windows/)

Exemplo no Windows 10:

![](vx_images/02-WPS-Office-global-config-menu.png)

Depois baixe os idiomas:

![](vx_images/03-Click-on-a-language-and-then-click-Apply.png)

Os idiomas baixados podem aparecer em:

```
C:\Users\youruser\AppData\Roaming\kingsoft\wps_intl\addons\pool\win-x64
```

![](vx_images/04-downloaded-languages.png)

A lista de idiomas pode aparecer em:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui\lang_list\lang_list.json
```

![20260416-000808](vx_images/507184629680596.png)

Alguns pacotes incluídos pela versão em espanhol do Windows podem aparecer em:

```
C:\Users\youruser\AppData\Local\Kingsoft\WPS Office\12.1.0.25830\office6\mui
```

![](vx_images/05-languages-downloaded-by-the-Spanish-version.png)

Se este projeto ajudou você, pode deixar uma estrela no repositório.

---

# Agradecimentos

Ao usuário [mmvill](https://github.com/mmvill), que me escreveu e disse que encontrou uma maneira de fazer o dicionário de correção ortográfica em espanhol funcionar no WPS Office 12.
