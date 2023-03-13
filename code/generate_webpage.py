
import glob
import os.path
import shutil
import time

from PIL import Image

HTML_HEADER = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>hr-st</title>
    <link rel="stylesheet" href="index.css" />
  </head>
  <body>
    """
HTML_MAIN = """
    <div class="container">
    <div class="right">
    <h1>Contendings of Horus and Seth</h1>
    <p>Transcription from Papyrus Chester Beatty</p>
    </div>
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
        hieroglyphic_dst = '../docs/images/hieroglyphic_%s' % current_png_ref
        shutil.copyfile(hieroglyphic_src, hieroglyphic_dst)

        # Get the width of the hieratic line image to make the glyphs match later
        im = Image.open(hieratic_dst)
        width = im.size[0]
        # Older rendered text needs to be flipped to RTL.
        flip_boundary = (2022, 3, 14, 0, 0, 0, 0, 0, -1)
        hieroglyphic_mtime = os.path.getmtime(hieroglyphic_src)
        should_flip = (hieroglyphic_mtime - time.mktime(flip_boundary)) < 0
        maybe_flip = 'class="flip" ' if should_flip else ''

        html += '\n\n'
        html += '\n    <div class="line">'
        html += '\n    <a id="page%02i_line%03i">' % (currentPage, currentLine)
        html += '\n      <h3 class="line-number">Page %i, Line %i</h3>' % (currentPage, currentLine)
        html += '\n    </a>'
        html += '\n      <div class="hieratic">'
        html += '\n        <img src="./images/hieratic_%s" />' % current_png_ref
        html += '\n      </div>'
        html += '\n      <div class="hieroglyphic">'
        html += '\n        <img src="./images/hieroglyphic_%s" width="%ipx" %s/>' % (current_png_ref, width, maybe_flip)
        html += '\n      </div>'
        html += '\n    </div>'


# Build a navigation header for faster access than scrolling.
nav = """<div class="navbar">
    <button class="flip big"
        aria-role="open and close navigation menu"
      >𓊛</button>
    <nav class="hidden">
      <ol>
"""
for i in range(numPages):
    currentPage = i + 1
    nav += ' ' * 8
    nav += '<li><a href="#page%02d">Page %d</a></li>\n' % (currentPage, currentPage)
nav += """      </ol>
    </nav>
    </div>
"""

script = """
<script>
document.addEventListener('DOMContentLoaded', (e) => {
  navbutton = document.querySelector('button');
  navbutton.addEventListener('mousedown', (click) => {
    toggle_nav();
  });
});

function toggle_nav() {
  nav = document.querySelector('nav');
  if (nav.classList.contains('hidden')) {
      nav.classList.remove('hidden');
  } else {
      nav.classList.add('hidden');
  }
}
</script>
"""

html = HTML_HEADER + nav + HTML_MAIN + html + HTML_FOOTER + script

f = open('../docs/hr-st.html', 'w')
f.write(html)
f.close()
