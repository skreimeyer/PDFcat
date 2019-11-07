import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from typing import List, BinaryIO

def concatenate(files: List[str], output: BinaryIO) -> ():
    """
    Concatenate will take a list of pdf filenames and write them all
    to a single file-object. Returns nothing on completion.
    """
    try:
        writer = PdfFileWriter()
        for infile in files:
            with open(infile,'rb') as file_data:
                reader = PdfFileReader(file_data)
                for n in range(reader.getNumPages()):
                    writer.addPage(reader.getPage(n))
                writer.write(output)
    except Exception as e:
        print("Failed to write files:",e)

def main() -> ():
    """main manages command line arguments and walks the directory for all
    filenames. Prints ``usage`` if incorrect number of arguments given.

    With the example file structure:
    
        mydir:

            | pdf1
            | pdf2
            | pdf3
    
    The command ``pdfcat mydir merged.pdf`` will create merged.pdf which has
    the contents of the three pdf files in the ``mydir`` folder.
    """
    if len(sys.argv) != 3:
        print(
"""Usage: pdfcat DIRECTORY NEWFILENAME

pdfcat will take all pdfs within a folder and combine them into a single
new file."""
        )
        quit()
    for root,_,names in os.walk(sys.argv[1]):
        files = [os.path.join(root,name) for name in names]
    target = sys.argv[2]
    with open(target, 'wb') as target_file:
        concatenate(files, target_file)

if __name__ ==  "__main__":
    main()