# Old-printer-extension

## Description
If you happen to have an old printer and need to print pages on both sides of the paper in Adobe Reader just like me, this script may be helpful to you. It will calculate number of pages, so you don't need to do it by yourself and you can just paste it to the "pages" box in Adobe. It provides two modes: single-page and double-page mode. In single mode, you'll get two pages on one sheet paper, while in double mode you'll get four pages - two on each side.

## Getting started

To run this script just type following command in project directory in your terminal:
```
python .\src\print_pages.py start end mode
```
 where `start` is number representing first page from the range, `stop` is number representing last page from the range and `mode`:
 > 1 -> single-page mode\
 > 2 -> double-page mode.

## Usage
In case of wrong range or missing one of the range arguments, you will see:
```
no range specified!
```

In case of wrong or no mode specified, you'll be guided how to do it properly:
```
incorrect mode! you need to choose single page mode - 1, or double page - 2
```
