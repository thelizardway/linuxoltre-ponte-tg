__module_name__ = "ponte_tg"
__module_version__ = "1.0"
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
RIGA_TG = re.compile(r"^\[TG\] (📢 )?<([^>]+)> (.*)$", re.S)
EVENTI = ("Channel Message", "Channel Msg Hilight")


def riscrivi(word, word_eol, evento):
    if len(word) < 2 or hexchat.strip(word[0]).lower() != BOT:
        return hexchat.EAT_NONE
    if (hexchat.get_info("channel") or "").lower() not in CANALI:
        return hexchat.EAT_NONE
    trovato = RIGA_TG.match(word[1])
    if not trovato:
        return hexchat.EAT_NONE
    nome = (trovato.group(1) or "") + trovato.group(2)
    hexchat.emit_print(evento, nome, trovato.group(3))
    return hexchat.EAT_ALL


for _evento in EVENTI:
    hexchat.hook_print(_evento, riscrivi, _evento)
