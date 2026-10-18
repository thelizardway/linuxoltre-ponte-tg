# Messaggi del gruppo Telegram di #LinuxOltre col nome di chi scrive invece di ULIAK
#
# Le righe che ULIAK porta dal gruppo Telegram ("<ULIAK> [TG] <Mario> ciao")
# compaiono come "<Mario> ciao", solo in questo WeeChat.
# Installazione: copiare il file in ~/.local/share/weechat/python/autoload/
# (o ~/.weechat/python/autoload/ nelle installazioni vecchie) e scrivere
# /python load ponte_tg.py (ai riavvii successivi si carica da solo).
# Serve WeeChat 2.3 o successivo con il supporto Python.

import re

import weechat

SCRIPT_NAME = "ponte_tg"
BOT = "uliak"
CANALI = {"#linuxoltre", "#distro-test"}
# Testa della riga, cercata sul testo senza colori: da ULIAK arriva anche
# con grassetto e colore ("[TG]" in blu)
TESTA_TG = re.compile(r"^\[TG\] (📢 )?<([^>]+)> ")


def colore_nick(nome):
    # "nick_color" da WeeChat 3.5, prima "irc_nick_color"
    return weechat.info_get("nick_color", nome) or weechat.info_get("irc_nick_color", nome) or ""


def riscrivi(data, line):
    tags = line.get("tags", "").split(",")
    if "nick_" + BOT not in (t.lower() for t in tags):
        return {}
    canale = line.get("buffer_name", "").rsplit(".", 1)[-1].lower()
    if canale not in CANALI:
        return {}
    messaggio = line.get("message", "")
    trovato = TESTA_TG.match(weechat.string_remove_color(messaggio, ""))
    if not trovato:
        return {}
    emoji, nome = trovato.groups()
    # Il resto del messaggio con la sua formattazione: si taglia dove finisce
    # la testa visibile (che termina con lo spazio, dopo i codici di chiusura)
    for fine in range(len(trovato.group(0)), len(messaggio) + 1):
        if weechat.string_remove_color(messaggio[:fine], "") == trovato.group(0):
            break
    return {"prefix": (emoji or "") + colore_nick(nome) + nome, "message": messaggio[fine:]}


if weechat.register(SCRIPT_NAME, "LinuxOltre", "1.1", "MIT",
                    "Messaggi del gruppo Telegram di #LinuxOltre col nome di chi scrive invece di ULIAK", "", ""):
    weechat.hook_line("formatted", "*", "irc_privmsg", "riscrivi", "")
