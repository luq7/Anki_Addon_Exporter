<p align="center">
  <img width=50% height=50% src="/src/anki_exporter_logo.png">
</p>


# Anki Addon Exporter

<p>
<a href="LICENSE" target="_blank" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-orange.svg"></a>
<a href="https://www.python.org/downloads/" target="_blank" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.8-green.svg"></a>
<a href="https://apps.ankiweb.net/" target="_blank" title="Anki version"><img src="https://img.shields.io/badge/Software-Anki%202.1-blue"></a>
<a title="Supported OS"><img src="https://img.shields.io/badge/Supports-Win%2FMac%2FLinux-green"></a>
</p>
A mini application for those people who are lazy to get their Anki's addon code manually. 


***
## Problem

If you have ever experienced an error in Anki and the only solution is reinstallation, then all your beloved add-ons would most likely disappear. It is painful to go through the add-on page to get those add-on codes. Even worse when you have to rely on your memory which add-ons you used previously.

## Solution
An application that would extract all your add-on's code (numbers), so you could have them added once you have Anki reinstalled. 

(PS: If you don't have any add-ons yet, you will get a: `No such path` message.)
***

## Objective 
Save lazy people's time.



## Install
#### Executable
 * Window executable file:[`ankiExport.exe`](/windowExe/dist/)
 * Mac runnable file: [`ankiExport.app`](/macApp/dist/)
 * Linux runnable file: [`ankiExport`](/linuxRunnable/dist/ankiExport/)

#### Manual
 * Download the `scr`, and run the source code (If your system is not supported.)
 

## Screenshot

### Using default (Only for Anki2.1.x):

#### Window executable
Clone my `windowExe/dist/ankiExport.exe` and open it. 

<p align="center">
  <img width=75% height=75% src="/gif/ankiXporterWin10.gif" alt="Windows 10 Executable Default Demo Gif" title="Win10 Default Demo Gif">
</p>

#### Mac .app runnable
Clone my `/macApp/dist/ankiExport.app` (the whole `ankiExport.app` thing), and change to the directory where you cloned the file by using terminal and then use the command 
```
open ankiExport.app
```
to run it.

<p align="center">
  <img width=75% height=75% src="/gif/ankiXporterMac.gif" alt="Mac .app Runnable Default Demo Gif" title="Mac Default Demo Gif">
</p>

#### Linux runnable
Clone my `/linuxRunnable/dist/ankiExport/`, and change to the directory where you cloned the file by using terminal and then use the command 
```
./ankiExport/ankiExport
```
to run it

<p align="center">
  <img width=75% height=75% src="/gif/ankiXporterLinux.gif" alt="Linux Runnable Default Demo Gif" title="Linux Default Demo Gif">
</p>


If you have Anki2.0, please use the __Browse__ button to look for the add-on's directory. Here is the official Anki for [*File Locations*](https://docs.ankiweb.net/#/files?id=file-locations)


## Feedback 
Feel free to [open an issue ](https://github.com/luckas72/Anki_Addon_Exporter/issues/) if you find any bugs. Also, feel free to contribute.
