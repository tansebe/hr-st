
import glob

from PIL import Image

HTML_HEADER = """<!DOCTYPE html>
<html>
  <head>
    <title>hr-st</title>
    <link rel="stylesheet" href="index.css" />
  </head>
  <body>
    """
HTML_FOOTER = """
  </body>
</html>
"""


# Our main bucket to be filled
html = ''

# Use the number of MdC pages to decide the total number of pages for the webpage
# Note that this may not be correct, but any errors 
# (say, an empty MdC file that adds one to this number)
# have only minor consquences
pageList = sorted(glob.glob("../mdc_pages/page*.gly"))
numPages = len(pageList)

# We don't assume that the numbers in the filenames are valid
# We simply make the appropriate spaces and fix errors after
for i in range(numPages):
    currentPage = i+1 # Let's just make life easier whenever we can
    
    html += '\n\n    <h2>Manuscript Page %i</h2>\n' % currentPage
    
    # Use the number of hieratic images to decide the number of lines for the page
    lineList = sorted(glob.glob('../hieratic_lines/page%02i/*.png' % currentPage))
    numLines = len(lineList)
    
    for j in range(numLines):
        currentLine = j+1 # Easy life
        
        
        im = Image.open('../hieratic_lines/page%02i/page%02i_line%03i.png' % (currentPage, currentPage, currentLine))
        width = im.size[0]
        
        html += '\n\n'
        html += '\n    <div class="line">'
        html += '\n    <h3>Line %i</h3>' % currentLine
        html += '\n      <div class="hieratic">'
        html += '\n        <img src="../hieratic_lines/page%02i/page%02i_line%03i.png" />' % (currentPage, currentPage, currentLine)
        html += '\n      </div>'
        html += '\n      <div class="hieroglyphic">'
        html += '\n        <img src="../png_lines/page%02i_line%03i.png" width="%ipx" class="hieroglyphic" />' % (currentPage, currentLine, width)
        html += '\n      </div>'
        html += '\n    </div>'



html = HTML_HEADER + html + HTML_FOOTER
f = open('../docs/hr-st.html', 'w')
f.write(html)
f.close()