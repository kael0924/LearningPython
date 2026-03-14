import camelot


# For pdf extraction related libraries there is 2 best ( camelot-py and pdfplumber)
# user camelot if we need just the table and pdf plumber if we need table and text

# for camelot there is flavor parameter for type of extraction ( lattice, and stream) if lattice doesnt work use stream.  Lattice is default
tables = camelot.read_pdf('./resources/sample-tables.pdf', pages='1', line_scale=40) 
# line scale is to tune the scanner to detect even thin lines of tables.

print(tables)

tables.export('sample_tables.csv', f="csv", compress=False) 
# only make compress True if you need to lessen the data it export