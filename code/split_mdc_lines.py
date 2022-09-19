JSESH_HEADER = """++JSesh_Info 1.0 +s
++JSesh_use_lines_for_shading true +s
++JSesh_max_quadrant_width 22.0 +s
++JSesh_line_skip 6.0 +s
++JSesh_small_skip 2.0 +s
++JSesh_column_skip 10.0 +s
++JSesh_standard_sign_height 18.0 +s
++JSesh_small_body_scale_limit 12.0 +s
++JSesh_cartouche_line_width 1.0 +s
++JSesh_small_sign_centered false +s
++JSesh_page_direction RIGHT_TO_LEFT +s
++JSesh_max_quadrantHeight 18.0 +s
++JSesh_page_orientation HORIZONTAL +s"""

OUTPUT_DIR = '../mdc_lines/'

import glob
import os

pageList = glob.glob("../mdc_pages/page*.gly")

# Create the output directory if necessary
os.makedirs(OUTPUT_DIR, exist_ok = True)

for pageName in pageList:
    pageNumber = int(pageName[-6:-4])
    print('Spliting lines in page number %i' % pageNumber)
    f = open(pageName, 'r')
    page = f.read()
    f.close()
    
    lines = page.split('\n')
    
    lineNumber = 1
    for line in lines:
        
        if len(line) < 2:
            continue
        
        if line[0:2] == "++":
            # print('header line')
            continue
        
        newFilename = '%spage%02i_line%03i.txt' % (OUTPUT_DIR, pageNumber, lineNumber)
        f = open(newFilename, 'w')
        f.write(JSESH_HEADER + '\n' + line)
        f.close()
        
        lineNumber += 1
    
