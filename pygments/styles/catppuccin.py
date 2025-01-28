from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, Error, Generic, Number, Operator, Text

__all__ = ['CatppuccinMochaStyle']

base = "#1e1e2e"
mauve = "#cba6f7"
red = "#f38ba8"
peach = "#fab387"
yellow = "#f9e2af"
green = "#a6e3a1"
sky = "#89dceb"
blue = "#89b4fa"
text = "#cdd6f4"
overlay0 = "#6c7086"

class CatppuccinMochaStyle(Style):


    name='catppuccin-mocha'
    styles = {
        Token:                  sky,
        Comment:                overlay0,
        Keyword:                mauve,
        
        Name:                   peach,
        Name.Class:             yellow,
        Name.Function:          blue,

        Error:                  red,                  

        String:                 green + "italic",

        Number:                 peach,

        Operator:               sky,

        Text:                   text
    }