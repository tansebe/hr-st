
import glob
import os.path
import shutil

from PIL import Image

HTML_HEADER = """<!DOCTYPE html>
<html>
  <head>
    <title>hr-st</title>
    <link rel="stylesheet" href="index.css" />
  </head>
  <body>
    <div class="container">
    """
HTML_FOOTER = """
    </div>
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
    
    print('Generating page %i' % currentPage)
    
    html += '\n\n    <a id="page%02i"><h2 class="page-number">Manuscript Page %i</h2></a>\n' % (currentPage, currentPage)
    
    # Use the number of hieratic images to decide the number of lines for the page
    lineList = sorted(glob.glob('../hieratic_lines/page%02i/*.png' % currentPage))
    numLines = len(lineList)
    
    for j in range(numLines):
        currentLine = j+1 # Easy life
        
        print('Generating page %i, line %i' % (currentPage,currentLine))
        
        current_png_ref = 'page%02i_line%03i.png' % (currentPage, currentLine)

        # Save copies of all images in /docs for the webpage to use
        hieratic_src = '../hieratic_lines/page%02i/%s' % (currentPage, current_png_ref)
        hieroglyphic_src = '../png_lines/%s' % current_png_ref
        # Go to the next page if we've run out of images
        if not os.path.exists(hieratic_src) or not os.path.exists(hieroglyphic_src):
            break
        hieratic_dst = '../docs/images/hieratic_%s' % current_png_ref
        shutil.copyfile(hieratic_src, hieratic_dst)
        # Get the width of the hieratic line image to make the glyphs match later
        im = Image.open(hieratic_dst)
        width = im.size[0]
        hieroglyphic_dst = '../docs/images/hieroglyphic_%s' % current_png_ref
        shutil.copyfile(hieratic_src, hieratic_dst)

        html += '\n\n'
        html += '\n    <div class="line">'
        html += '\n    <a id="page%02i_line%03i">' % (currentPage, currentLine)
        html += '\n      <h3 class="line-number">Page %i, Line %i</h3>' % (currentPage, currentLine)
        html += '\n    </a>'
        html += '\n      <div class="hieratic">'
        html += '\n        <img src="./images/hieratic_%s" />' % current_png_ref
        html += '\n      </div>'
        html += '\n      <div class="hieroglyphic">'
        html += '\n        <img src="./images/hieroglyphic_%s" width="%ipx" class="flip" />' % (current_png_ref, width)
        html += '\n      </div>'
        html += '\n    </div>'



html = HTML_HEADER + html + HTML_FOOTER
f = open('../docs/hr-st.html', 'w')
f.write(html)
f.close()
