#7.1 Write a program that prompts for a file name, then opens that file
#and reads through the file, and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
#fhand = input("Enter file name: ")
#fh = open(fhand)
#for space in fh:
 #   space=space.rstrip()

#FH=fh.read()
#FH2 =FH.upper()
#print(FH2)
# esto sirve para la consola de coursera pero no para aca


fh = open('words.txt') # open lo abre pero no lo lee
for lines in fh:
    lines=lines.rstrip()
    print(lines.upper())
    
#FH=fh.read()
#FH2 =FH.upper()
#print(FH2)
