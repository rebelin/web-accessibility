# Making Files More Accessible
A "cleaning" helper for accessibility - this program expects the input to be an htm or html file

This is a work in progress. Eventually, there will be a way to interact with the terminal to make changes, rather than making changes in the code.

## Setup
This program uses the BeautifulSoup library ([view Beautiful Soup documentation here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)):

<code> pip install beautifulsoup4 </code>

## Files

* [`doc.md`](doc.md) - Progress documentation
* [`cleaner.py`](cleaner.py) - Main interactive program
* [`web_access.py`](web_access.py) - Main testing file
* [`soup.py`](soup.py) - Creates a soup instance with BeautifulSoup
* [`replace_list.txt`](replace_list.txt) - List of common (inaccessible) tags and their accessible counterparts

## Usage
Run <code> python3 web_access.py </code>
