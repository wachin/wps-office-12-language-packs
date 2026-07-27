# About the zh-CN Test Document

The file:

```text
Quotes zh-CN (chino simplificado de China)- Richard Stallman.docx.docx
```

is used to test the Chinese spellchecking behavior in WPS Office 12 for Linux.

The name includes `zh-CN` because the Linux session used for this test is:

```bash
zh_CN.UTF-8
```

In locale names, `zh` means Chinese and `CN` means China. For this reason, the text was translated using **Chinese (Simplified)**, not Chinese (Traditional).

The phrase `chino simplificado de China` was added to the filename to make the purpose clear for Spanish-speaking users: this is the Simplified Chinese test document for China.

This test is intended for this WPS Office 12 setup:

```text
MUI:  /opt/kingsoft/wps-office/office6/mui/zh_CN
Dict: /opt/kingsoft/wps-office/office6/dicts/spellcheck/en_CH
```

WPS Office 12 Chinese version includes both of those folders by default.

## Spellcheck Test Result

In the WPS Office 12 spellcheck language window, the installed dictionary appears as:

```text
中文 + English (United States)
```

This corresponds to:

```text
/opt/kingsoft/wps-office/office6/dicts/spellcheck/en_CH
```

However, in the current test it does **not** work as a pure Simplified Chinese spellchecker. After enabling spellcheck and selecting `中文 + English (United States)`, intentionally incorrect Chinese text was not marked as misspelled.

Result:

```text
[ ] Works
[x] Does not work
```

The current conclusion is that `en_CH` seems to be a mixed Chinese + English dictionary entry included by WPS Office 12, but it does not behave like a full Simplified Chinese spellchecker for Chinese text.
