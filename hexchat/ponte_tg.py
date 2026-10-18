__module_name__ = "ponte_tg"
__module_version__ = "1.1"
__module_description__ = "Messaggi del gruppo Telegram di #LinuxOltre col nome di chi scrive invece di ULIAK"

# Le righe che ULIAK porta dal gruppo Telegram ("<ULIAK> [TG] <Mario> ciao")
# compaiono come "<Mario> ciao", solo in questa finestra di HexChat.
# Installazione: copiare il file in ~/.config/hexchat/addons/ (Linux) o in
# %APPDATA%\HexChat\addons\ (Windows), poi riavviare HexChat oppure
# Finestra > Plugin e script > Carica. Serve il supporto Python di HexChat.

import re

import hexchat

BOT = "uliak"
CANALI = {"#linuxoltre", "#distro-test"}
# Testa della riga, cercata sul testo senza colori: da ULIAK arriva anche
# con grassetto e colore ("[TG]" in blu)
TESTA_TG = re.compile(r"^\[TG\] (📢 )?<([^>]+)> ")
EVENTI = ("Channel Message", "Channel Msg Hilight")


def riscrivi(word, word_eol, evento):
    if len(word) < 2 or hexchat.strip(word[0]).lower() != BOT:
        return hexchat.EAT_NONE
    if (hexchat.get_info("channel") or "").lower() not in CANALI:
        return hexchat.EAT_NONE
    messaggio = word[1]
    trovato = TESTA_TG.match(hexchat.strip(messaggio))
    if not trovato:
        return hexchat.EAT_NONE
    # Il resto del messaggio con la sua formattazione: si taglia dove finisce
    # la testa visibile (che termina con lo spazio, dopo i codici di chiusura)
    for fine in range(len(trovato.group(0)), len(messaggio) + 1):
        if hexchat.strip(messaggio[:fine]) == trovato.group(0):
            break
    nome = (trovato.group(1) or "") + trovato.group(2)
    hexchat.emit_print(evento, nome, messaggio[fine:])
    return hexchat.EAT_ALL


for _evento in EVENTI:
    hexchat.hook_print(_evento, riscrivi, _evento)
