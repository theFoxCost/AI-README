# completely unnecessary

def choose_lang():
    
    lang = int(input("Choose Language: 1.English 2.francais 3.italiano 4.中文 5.日本語 6.한국어 7.русский 8.ภาษาไทย 9.हिंदी 10.বাংলা 11.Arabic 12. Português 13. Espanol 14. Deutsch"))
    
    match lang:
        case 1:
            lang = "English"
        case 2:
            lang = "francais"
        case 3:
            lang = "italiano"
        case 4:
            lang = "中文"
        case 5:
            lang = "日本語"
        case 6:
            lang = "한국어"
        case 7:
            lang = "русский"
        case 8:
            lang = "ภาษาไทย"
        case 9:
            lang = "हिंदी"
        case 10:
            lang = "বাংলা"
        case 11:
            lang = "Arabic"
        case 12:
            lang = "Português"
        case 13:
            lang = "Espanol"
        case 14:
            lang = "Deutsch"
        case _: # default lang
            lang = "English"
    print(f"Selected Language: {lang}")
    return lang