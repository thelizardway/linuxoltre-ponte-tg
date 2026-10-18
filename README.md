# Ponte Telegram di #LinuxOltre: nome di chi scrive al posto di ULIAK

ULIAK porta su IRC i messaggi del gruppo Telegram [t.me/linuxoltre](https://t.me/linuxoltre) così:

```
<ULIAK> [TG] <Mario> ciao a tutti
```

Con uno di questi script, **solo nel tuo client**, la stessa riga diventa:

```
<Mario> ciao a tutti
```

I post del canale Telegram compaiono come `<📢 LinuxOltre> ...`. Vale su **#linuxoltre** e **#distro-test** (rete Azzurra) e solo per le righe scritte davvero da ULIAK: chi scrive `[TG] <qualcuno>` a mano resta col proprio nick.

## WeeChat

Serve WeeChat 2.3 o successivo con il supporto Python.

```
mkdir -p ~/.local/share/weechat/python/autoload
curl -o ~/.local/share/weechat/python/autoload/ponte_tg.py https://raw.githubusercontent.com/thelizardway/linuxoltre-ponte-tg/main/weechat/ponte_tg.py
```

Nelle installazioni vecchie la cartella è `~/.weechat/python/autoload/`. Poi in WeeChat:

```
/python load ponte_tg.py
```

Ai riavvii successivi si carica da solo. Per toglierlo: `/python unload ponte_tg` e cancellare il file.

## HexChat

Serve il supporto Python di HexChat (su Windows: opzione "Python" durante l'installazione).

Scarica [`hexchat/ponte_tg.py`](hexchat/ponte_tg.py) e copialo in:

- Linux: `~/.config/hexchat/addons/`
- Windows: `%APPDATA%\HexChat\addons\`

Poi riavvia HexChat, oppure *Finestra → Plugin e script → Carica*. Per toglierlo: scaricalo da *Plugin e script* e cancella il file.

## Da sapere

- Cambia solo quello che vedi tu: anche i log del tuo client registrano il nome di chi ha scritto da Telegram.
- Chi scrive da Telegram non è su IRC: per rispondergli scrivi in canale, non in privato.
- Le evidenziazioni restano: se qualcuno dal gruppo scrive il tuo nick, il client ti avvisa come sempre.

Licenza MIT.
