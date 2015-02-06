import os, sys
import xml.dom.minidom

head = r"""

%\input{/Users/lucamartini/Documents/Documenti/Latex/preambles/article_preamble.tex}
\documentclass[9pt,twocolumn]{article}
\usepackage{extsizes}
\usepackage{fullpage}

\title{Affinity sides}

\author{Luca}
\date{\today}

\begin{document}

"""

tail = r"""

\end{document}

"""

pars = ""

dom1 = xml.dom.minidom.parse("affinity_side.xml")
matches = dom1.getElementsByTagName("match")

for match in matches:
    name = match.attributes.item(0).value
    par = r'\paragraph{\textbf{' + name + "}}\n"

    ins = r'\emph{in:} '
    outs = r'\emph{out:} '
    for inout in match.childNodes:
        if inout.localName == "in":
            for cardin in inout.childNodes :
                if cardin.localName == "card":
                    n = cardin.attributes.item(0).value
                    cardname = cardin.attributes.item(1).value
                    ins = ins + n + " " + cardname + "; "

        if inout.localName == "out":
            for cardin in inout.childNodes :
                if cardin.localName == "card":
                    n = cardin.attributes.item(0).value
                    cardname = cardin.attributes.item(1).value
                    outs = outs + n + " " + cardname + "; "

    pars = pars + par + ins + "\n" + outs + "\n\n"

latex = head + pars + tail

out_file = open("affinity_sides.tex","w")
out_file.write(latex)
out_file.close()
