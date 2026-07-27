Actualmente `wps-libreoffice-dicts-experimental` contiene 71 diccionarios convertidos para WPS Office. Esta carpeta queda como material experimental en la raíz del repositorio, porque en WPS Office 12 versión China no todos estos diccionarios funcionan aunque tengan el formato correcto. Para la instalación recomendada usa `build/wps-office-12-dicts-active/`.

| Código  |           Diccionario            |
| ------- | -------------------------------- |
| `af_ZA` | African (South Africa)           |
| `be_BY` | Belarusian (Belarus)             |
| `bg_BG` | Bulgarian (Bulgaria)             |
| `bn_BD` | Bengali (Bangladesh)             |
| `bs_BA` | Bosnian (Bosnia and Herzegovina) |
| `ca_ES` | Catalan (Catalonia)              |
| `cs_CZ` | Czech (Czech)                    |
| `da_DK` | Danish (Denmark)                 |
| `de_AT` | German (Austria)                 |
| `de_CH` | German (Switzerland)             |
| `de_DE` | German (Germany)                 |
| `el_GR` | Greek (Greece)                   |
| `en_AU` | English (Australia)              |
| `en_CA` | English (Canada)                 |
| `en_GB` | English (United Kingdom)         |
| `en_US` | English (United States)          |
| `en_ZA` | English (South Africa)           |
| `es_AR` | Spanish (Argentina)              |
| `es_BO` | Spanish (Bolivia)                |
| `es_CL` | Spanish (Chile)                  |
| `es_CO` | Spanish (Colombia)               |
| `es_CR` | Spanish (Costa Rica)             |
| `es_CU` | Spanish (Cuba)                   |
| `es_DO` | Spanish (Dominican Republic)     |
| `es_EC` | Spanish (Ecuador)                |
| `es_ES` | Spanish (Spain)                  |
| `es_GQ` | Spanish (Equatorial Guinea)      |
| `es_GT` | Spanish (Guatemala)              |
| `es_HN` | Spanish (Honduras)               |
| `es_MX` | Spanish (Mexico)                 |
| `es_NI` | Spanish (Nicaragua)              |
| `es_PA` | Spanish (Panama)                 |
| `es_PE` | Spanish (Peru)                   |
| `es_PH` | Spanish (Philippines)            |
| `es_PR` | Spanish (Puerto Rico)            |
| `es_PY` | Spanish (Paraguay)               |
| `es_SV` | Spanish (El Salvador)            |
| `es_US` | Spanish (United States)          |
| `es_UY` | Spanish (Uruguay)                |
| `es_VE` | Spanish (Venezuela)              |
| `fr_FR` | French (France)                  |
| `gd_GB` | Scots Gaelic (Great Britain)     |
| `gl`    | Galician (strict Volga)          |
| `gu_IN` | Gujarati (India)                 |
| `hi_IN` | Hindi (India)                    |
| `hr_HR` | Croatian (Croatia)               |
| `hu_HU` | Hungarian (Hungary)              |
| `id_ID` | Indonesian                       |
| `is`    | Icelandic                        |
| `it_IT` | Italian (Italy)                  |
| `km_KH` | Khmer (Cambodia)                 |
| `lt_LT` | Lithuanian (Lithuania)           |
| `ms_MY` | Malay (Malaysia)                 |
| `nb_NO` | Norwegian (Norway)               |
| `ne_NP` | Nepali (Nepal)                   |
| `nl_NL` | Dutch                            |
| `pl_PL` | Polish                           |
| `pt_BR` | Portuguese (Brazil)              |
| `pt_PT` | Portuguese                       |
| `qu_EC` | Kichwa (Ecuador)                 |
| `ro_RO` | Romanian (Romania)               |
| `ru_RU` | Russian (Russia)                 |
| `sk_SK` | Slovak (Slovakia)                |
| `sl_SI` | Slovenian (Slovenia)             |
| `sq_AL` | Albanian (Albania)               |
| `sr`    | Serbio                           |
| `sv_SE` | Swedish (Sweden)                 |
| `sw_TZ` | Swahili (Tanzania)               |
| `tr_TR` | Turkish (Turkey)                 |
| `uk_UA` | Ukrainian (Ukraine)              |
| `vi_VN` | Vietnamese (Vietnam)             |

### Diccionarios añadidos desde otras fuentes

Además de los diccionarios convertidos desde LibreOffice y los heredados de WPS Office, este paquete incluye los siguientes diccionarios añadidos manualmente desde otras fuentes:

| Código  |    Diccionario     |                              Nota                              |
| ------- | ------------------ | -------------------------------------------------------------- |
| `hr_HR` | Croatian (Croatia) | Añadido desde otra fuente y empaquetado con el formato de WPS. |
| `km_KH` | Khmer (Cambodia)   | Añadido desde otra fuente y empaquetado con el formato de WPS. |
| `qu_EC` | Kichwa (Ecuador)   | Añadido desde otra fuente y empaquetado con el formato de WPS. |

Los tres usan el mismo formato final que los demás diccionarios: `dict.conf`, `main.aff` y `main.dic`. Sus `dict.conf` también incluyen nombres localizados para que WPS pueda mostrarlos mejor en distintos idiomas de interfaz.
