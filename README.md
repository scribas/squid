# Squid
Rangle large CSV files with ease.

This project started, because many people around me work with csv files, too large to open in any text editor, but do not have the coding skills to manipulate or view these files with a stream editor.

## Installation
- Install the newest version of Python3x
- Download squid.py
- Run `python squid.py`

Squid deliberately avoids using external libraries. No additional Python packages need to be installed first.

## Features

```
  COMMANDS:
  =========
    list       (l,ls)  - List content of present working directory.
    cd         (cd)    - Change the present working directory.
    open       (o)     - Point to a new text file.
    search     (?)     - Search for column content.
    columns    (c)     - View the column headings within the file.
    rows       (r)     - Count the number of rows within the file.
    view       (v)     - View the a portion of the content of a file.
    stats      (s)     - Basic stats on a specific column.
    histo      (h)     - Histogram on a specific column.
    delimiter  (d)     - Change the csv file delimiter.
    exit/quit  (x,q)   - Quit the program.

  Open:
  =====

  Description:
    The open command points to the file that Squid should work on.
    A path should be defined with unix-like front-slashes.
    If no path is defined, the file is assumed to be in the present working directory.

    Syntax 1: o
    Syntax 2: o path/csv_filename
 
  Search:
  =======

  Description:
    Searches for the first 20 matches of a field value.

  Syntax: ? search_term

  Columns:
  ========

  Description:
    Lists all columns.

  View:
  =====

  Description:
    View displays the requested columns of the rows specified.
    By default, view lists the first 10 rows of the csv file loaded.
    If start_row is specified, 10 rows from that point onwards will be listed.
    If start_col is specified, 10 cols from that point onwards will be listed.
    By specifying end_row, less or more than 10 rows can be listed.
    By specifying end_col, less or more than 10 cols can be listed.

    Syntax 1: v
    Syntax 2: v start_row start_col end_row end_col

  Stats:
  ======

  Description:
    Provides Min, Max, Total, Count, Mean stats on provided column.

  Syntax: s col_num

  Histogram:
  ==========

  Description:
    Draw up a histogram of the values of the specified column.
    By default, max_value is set to 100, min_value to 0 and bins to 20.

  Syntax 1: h col_num
  Syntax 2: h col_num max_value min_value bins

  Delimiter:
  ==========

  Description:
    By default, the delimiter in a csv file is assumed to be a comma.
    By specifying character, the delimiter can be changed to one or more other symbols.

  Syntax: d
```
