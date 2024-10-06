---
aliases: []
author: Maneesh Sutar
created: 2024-05-16
modified: 2024-09-28
tags:
- todo
- toread
- linux
title: Terminals
---

# Terminals

<https://gpanders.com/blog/state-of-the-terminal/>  
Also go through "further reading" section in the above article, they are good

## Escape Sequences

Escape sequences are varied and numerous, but the vast majority used in practice fall into one of three categories:

**Control Sequence Introducer (CSI) :**  
prefix `\e[` (`0x1b 0x5b`).  
For altering text inside the terminal  
reposition the cursor, change the cursor style, clear the screen, set foreground and background colors, and more.

**Device Control String (DCS)**  
No info available

**Operating System Command (OSC).**  
OSC sequences are those which begin with the prefix `\e]`  
For doing things outside of the terminal  
reading from or writing to the system clipboard, changing the title of the terminal emulator’s window, or sending desktop notifications.

Typical escape sequences are of the form `ES <parameters> m` where `ES` is either CSI/OSC/DCS escape sequence prefix.  
e.g.

````bash
printf '\e[1;32mHello \e[0;4;31mworld!\n\e[0m'
````

The first escape sequence in the example `\e[1;32m` enables the **bold** attribute (`1`) and sets the foreground color to green (`32`). The second escape sequence `\e[0;4;31m` first clears any existing styles (`0`), then enables the underline attribute (`4`), and finally sets the foreground text color to red (`31`). Finally, the last escape sequence `\e[0m` resets all styles back to their defaults.

Another use case for simple CSI sequences is redrawing text on the screen on an already existing line (e.g. for a progress bar or text that updates itself over time). Hint: look at `\r`, `CSI A`, and `CSI K`.
