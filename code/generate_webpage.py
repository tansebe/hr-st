
HTML_HEADER = """<!DOCTYPE html>
<html>
  <head>
    <title>hr-st</title>
  </head>
  <body>
    """
HTML_FOOTER = """
  </body>
</html>
"""

html = ''

import glob
pageList = glob.glob("../mdc_pages/page*.gly")
numPages = len(pageList)

for i in range(numPages):
    
    html += '<h1>Manuscript Page %i</h1>' % i
    
# for pageName in pageList:
#     pageNumber = int(pageName[-6:-4])
#     print('Spliting lines in page number %i' % pageNumber)
#     f = open(pageName, 'r')
#     page = f.read()
#     f.close()
# 
#     lines = page.split('\n')
# 
#     lineNumber = 1
#     for line in lines:
# 
#         if len(line) < 2:
#             continue
# 
#         if line[0:2] == "++":
#             # print('header line')
#             continue
# 
#         newFilename = '%spage%02i_line%03i.txt' % (OUTPUT_DIR, pageNumber, lineNumber)
#         f = open(newFilename, 'w')
#         f.write(JSESH_HEADER + '\n' + line)
#         f.close()
# 
#         lineNumber += 1

html = HTML_HEADER + html + HTML_FOOTER
f = open('../docs/hr-st.html', 'w')
f.write(html)
f.close()