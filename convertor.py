from pylatexenc.latex2text import LatexNodes2Text

def parse_latex(latex_code):
    return LatexNodes2Text().latex_to_text(latex_code)

print(parse_latex("\begin{align} 2x + 3y &= 7 \ 4x - 5y &= 1 \end{align}"))