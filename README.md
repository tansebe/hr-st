# Contendings of Horus and Seth

This a collaboration space for [a transcription of this ancient
Egyptian story](https://tansebe.github.io/hr-st/hr-st.html). Produced by the Hieratic Reading Group from
the [ⲧⲁⲛⲥⲏⲃⲉ ⲛ̄ⲧⲙⲛ̄ⲧⲛⲣⲙ̄ⲛ̄ⲕⲏⲙⲉ](https://discord.gg/eWuykwPnxt) discord server.

![Chester Beatty Papyrus image](https://viewer.cbl.ie/viewer/api/v1/records/Pap_1_1/files/images/D0003317.jpg/2314,1293,1017,224/max/0/default.jpg)
![N41:z-Xrd-m-D53-nb:r-Dr:r-G7](hr-st-sample.svg)

## Usage

### General File Generation and Editing (The Easy Stuff)

#### The Hieroglyphic Transcription

Manuel de Codage (MdC) files to be edited are in the `mdc_pages` directory. 
They are named according to page number.
Feel free to edit the hieroglyphs there as needed.
Note that if you edit any MdC text in any folder *other than* `mdc_pages`, 
your work will probably be overwritten when the site gets updated.
Just stick to `mdc_pages` and you'll be fine.

#### The Hieratic Manuscript

As you can probably tell, the hieratic text we're using is taken from a large image and cropped into individual lines.
This is a slightly tedious process, but it must be done, and it does offer some benefit in terms of getting a better sense of the manuscript.
All of the materials for this are in the `hieratic_lines` folder.
It should be clear enough how it works.
First we have to cut out the page, then the lines, then the cropped lines have to be further refined to look nice and show only the line we want. 
You can work on any part of that. You can't break anything that we can't fix, so be bold and get to work. Worst case, you learn some hieratic.

#### An Important Warning!

You really can't break anything in this, so you should feel free to fork and tinker.
If you do end up messing something up, we can always roll back your changes. 
Seriously, go nuts.

## Building Output (The Difficult Stuff)

### Quick Workflow 

1. `python code/split_mdc_lines.py`
1.  `../jsesh_sample` -> make images (follow instructions in that readme) -> copy images to `hr-st`
1. `code/generate_webpage`
1. upload changes


### Detailed Process

1. Generating MdC Lines

Do not edit lines in the `mdc_lines` directory. If you do, they will be overwritten.
Instead, edit the line in the relevant page in `mdc_pages`.
Then, run `python code/split_mdc_lines.py` to update all the line MdC.
Note that you will also need to regenerate the images afterward.

2. Generating bitmapped images

This project relies on a separate project [JSesh sample](https://github.com/jare/jsesh_sample) to generate a list of png images. Because that project is rather difficult to use without following its instructions to the letter, I've been generating these images by simply copying the MdC lines from this project into that one (change the `.gly` extension to `.txt` if necessary), generating the images there, and copying the finished images back to the relevant folder in this project. Obviously there exists a much more elegant method for doing this automatically, but so far this cludge is fast and reliable enough to preclude developing another workflow.

3. Generate webpage

The script at `python code/generate_webpage.py` will create a webpage in the `docs` folder (already configured to appear online on [github pages](https://tansebe.github.io/hr-st/hr-st.html)). In the process, it will also copy all images from their respective directories into docs for inclusion on the page. This makes the script somewhat slow, but it also means that `docs` contains a clean webpage with no external dependencies.

## Academic Sources

The source for this is [Papyrus Chester Beatty I](https://viewer.cbl.ie/viewer/image/Pap_1_1/1/) written during the New Kingdom period around 1160 BCE,
probably in Thebes. Images are [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/).

- Alan Gardiner *The Library of A. Chester Beatty* Oxford, 1931.
  (hieroglyphic transcription, background description)

- Enzo Chuirco [transcription and transliteration](http://www.enzochiurco.it/HS%20gero%20+%20t%20+%20t.htm) retrieved 2021 October 17.

- Simpson "The Contendings of Horus and Seth" in *The Literature of Ancient Egypt* 2003, pp. 91-103.
  (translation)

- Lichtheim *Ancient Egyptian Literature* vol. 2, 1973, 2006.
  (translation)
