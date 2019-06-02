# PyGraphics-Four-in-a-Row

Naive implementation of the popular game to get four of the same color in a row including graphics and sound effects.

This code was written naively, intentionally omitting the use of classes and objects, as a learning exercise with my kids.

If you just want to play the game on Windows, download PyGraphics-Four-in-a-Row.exe. It's a Windows standalone game; no need to install. Just download and run. Created with:

```
$ pyinstaller.exe --add-data="intro.wav;." --add-dat="clickbounce.wav;." --add-data="tie.wav;." --add-data="win.wav;." --add-data="LICENSE;." --noconsole --onefile .\fourinarow.py
```
