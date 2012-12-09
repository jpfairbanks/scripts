from pyPdf import PdfFileWriter, PdfFileReader
from os import listdir
#if the execution fails, then you must manually remove the file that it created.
CENTRAL_PRINTING_LIMIT = 200
PREFIX_STR = "output-doc"
def prefix_sum(l):
    return [sum(l[0:i]) for i in range(len(l))]

def merge_pages(out_obj, files):
    num_pages = 0
    for filei in files:
        for pageNum in range(filei.getNumPages()):
            out_obj.addPage(filei.getPage(pageNum))
    return out_obj, remaining_files
def merge_pages_better(out_obj, files):
    num_pages = 0
    while (len(files)!=0 and num_pages+ files[0].getNumPages() < CENTRAL_PRINTING_LIMIT):
        next_file = files.pop(0)
        for pageNum in range(next_file.getNumPages()):
            out_obj.addPage(next_file.getPage(pageNum))
        num_pages = out_obj.getNumPages()
    return 1

def consume_files(filelist):
    i = 0
    while (len(filelist) > 0):
        output = PdfFileWriter()
        merge_pages_better(output, filelist)
        outputstream = file(PREFIX_STR+str(i)+'.pdf', 'wb')
        print "%s%d.pdf has %d pages" % (PREFIX_STR, i, output.getNumPages())
        i = i + 1
        output.write(outputstream)
        outputstream.close()
    return 1

filenames = []
__manual__ = False
if (__manual__ == True):
    filenames = ["doc1.pdf", 'doc2.pdf']
else:
    filenames = listdir('.')
#hope that we only operate on pdf's 
filenames = filter(lambda k: k.endswith('pdf'), filenames)
print filenames
infiles = [ PdfFileReader(file(f, 'rb')) for f in filenames ]
filesizes = [ f.getNumPages() for f in infiles ]

#print the file stats
for i in range(len(infiles)):
    print "file %d: %s, len= %d" % (i, filenames[i], filesizes[i])

indicator = consume_files(infiles)
print indicator

'''# print how many pages input1 has:
print "document-output.pdf has %s pages." % output.getNumPages()'''

'''# finally, write "output" to document-output.pdf
outputStream = file("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
'''
'''
# add page 1 from input1 to output document, unchanged
output.addPage(input1.getPage(0))
'''

'''# print the title of document1.pdf
print "title = %s" % (input1.getDocumentInfo().title)'''
