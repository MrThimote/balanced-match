# balanced-match

The goal of this little project is to implement a balanced match in a string for two regular expressions. 

# Usage

To use it in your project, download the balmatch.py file and do 

from balmatch import balanced_match

To launch it, you just need to launch the function with two strings, the openning and closing sequences and then your string to test, if no match was found, it will return (-1, -1, "") but if it found one, it will send the start of the sequence with the openning, the start of the end and the string in between. For an example balanced_match("{", "}", "a{b{c{}}}d}") returns (1, 8, 'b{c{}}') with the start of the { the start of the end } and the string. It also works with regex for example balanced_match("({)|(\[)", "}", "a{b[c{}}}d}") returns (1, 8, 'b[c{}}')
