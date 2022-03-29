# obsidian-math-document

Reuse latex math formula support in obsidian vault.

## How to use

1. Write basic latex document
1. Use package command to apply color on text(?)
1. Use pandoc to convert from latex to markdown
1. Use converter to complete markdown document(?)
1. Embed converted document in Obsidian document

### 2 - 4

pandoc did reconize `\textcolor` and convert them,  
however, Visual Studio Code or Obsidian doesn't support this flavor of syntax.

The standard markdown way to color text is using CSS,  
however, pandoc actively escape HTML tags from `<font...> </font>` to `\<font...\> \</font\>`  
make such thing impossible even if you write HTML in latex document.  
There is no way to turn off escape currently by my research.

So `<font` will written as `fontOpen`, `</font>` will written as `fontEnd`, etc,  
then use python script replace them to bypass pandoc escape.

By doing this, use command provided in `Color_*.tex`,  
for example: Bold and Blue text: `\blub{blue text here}`

When latex to pdf as usual, use `Color_Latex.tex`, when latex to markdown, use `Color_Markdown.tex`.  
The two package will generate different markup.

### 3

`pandoc "input file.tex" -f latex -t markdown -s -o "output file.md" --wrap=none`

`--wrap=none` tell pandoc left everything as is, don't break lines if too long.

### 4

`python Converter.py "output file.md"`

The file will be override. Backup all document related files before doing this!
