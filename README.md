# Py Books

Py books is a python based CLI application that utilizes the Googlebooks api.

## Installation

Start by installing the current version of Python on your computer. This can be done either by command prompt or by windows installer. 

Click [Here](https://docs.python.org/3/using/windows.html) for instructions to download Python on Windows

Most current Mac OS comes with Python pre-installed. Click [Here](https://docs.python-guide.org/starting/install3/osx/) for Mac OS documentation.


Python Package manager pip should be installed with these two methods. You will need pip to download Python Packages and modules
```bash
pip install {insert dependency package here}
```
For this project the only dependencies I downloaded were:
request (to have access to the [Google Books API](https://developers.google.com/books/docs/overview) and pdb (for debugging).

```bash
$ python -m pip install requests}
```
```bash
python3 -m pdb myscript.py}
```
 
## Usage

```python
import request
```
 This app can be used to search a term, and it will recover 5 titles with Author and publishing company. If there is no author or publishing company listed, this is noted in in the Output.

This can be used to create a favorites list of books that are reloadable even after terminating the program. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.