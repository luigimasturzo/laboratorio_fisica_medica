# Open the output file in write ('w') mode.
outputFile = open('output_data.txt', 'w')
for i in range(10):
    outputFile.write('%d\t%d\n' % (i, i**2))
# Close the output file.
outputFile.close()
