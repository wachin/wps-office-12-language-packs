
# Archivos de configuración para pruebas

Respaldar perfil actual (aunque también se puede eliminar):

```bash
mv ~/.config/Kingsoft ~/.config/Kingsoft.backup
mkdir -p ~/.config/Kingsoft
```

Luego crear ~/.config/Kingsoft/Office.conf con uno de estos contenidos:

### Minimal en_US

```
[General]
languages=en_US

[6.0]
common\DefaultLanguage=1033
common\Local\UILanguage=1033
common\spellcheck\locale_wps=en_US
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
wps\Application%20Settings\CheckSpellingAsYouType=1
wps\Application%20Settings\CheckGrammarAsYouType=1
wps\Application%20Settings\SplChkSuggestSpellingCorrections=1
wps\Application%20Settings\SplChkSuggestFromMainDictionaryOnly=1
wps\Application%20Settings\ShowSpellingIgnoredWords=1
wps\Application%20Settings\CheckSpellingByOnlineService=0
wps\Application%20Settings\CheckSpellingOnlySpellCheck=1
wps\Application%20Settings\CheckLanguage=1
wps\Application%20Settings\CheckGrammarWithSpelling=1
```

### Minimal es_ES

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
common\spellcheck\locale_wps=es_ES
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
wps\Application%20Settings\CheckSpellingAsYouType=1
wps\Application%20Settings\CheckGrammarAsYouType=1
wps\Application%20Settings\SplChkSuggestSpellingCorrections=1
wps\Application%20Settings\SplChkSuggestFromMainDictionaryOnly=1
wps\Application%20Settings\ShowSpellingIgnoredWords=1
wps\Application%20Settings\CheckSpellingByOnlineService=0
wps\Application%20Settings\CheckSpellingOnlySpellCheck=1
wps\Application%20Settings\CheckLanguage=1
wps\Application%20Settings\CheckGrammarWithSpelling=1
```

### Minimal es_EC

```
[General]
languages=es_ES

[6.0]
common\DefaultLanguage=3082
common\Local\UILanguage=3082
common\spellcheck\locale_wps=es_EC
wpsoffice\Application%20Settings\AppComponentMode=prome_independ
wpsoffice\Application%20Settings\AppComponentModeInstall=prome_independ
wps\Application%20Settings\CheckSpellingAsYouType=1
wps\Application%20Settings\CheckGrammarAsYouType=1
wps\Application%20Settings\SplChkSuggestSpellingCorrections=1
wps\Application%20Settings\SplChkSuggestFromMainDictionaryOnly=1
wps\Application%20Settings\ShowSpellingIgnoredWords=1
wps\Application%20Settings\CheckSpellingByOnlineService=0
wps\Application%20Settings\CheckSpellingOnlySpellCheck=1
wps\Application%20Settings\CheckLanguage=1
wps\Application%20Settings\CheckGrammarWithSpelling=1
```


Notas importantes:

- Para es_EC, dejo la interfaz en es_ES porque no tengo MUI es_EC; sólo cambiar el corrector con locale_wps=es_EC.
- Probar con un solo diccionario instalado en /opt/kingsoft/wps-office/office6/dicts/spellcheck/.
- Después de abrir WPS y probar, revisa si WPS volvió a cambiar esta clave:

wps\Application%20Settings\CheckSpellingAsYouType=1


