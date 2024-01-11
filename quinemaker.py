import sys

if len(sys.argv) != 2:
    print("Enter a Python program's file name")
    exit(1)

file_contents = open(sys.argv[1]).read()
repr_contents = file_contents.replace("\\", "\\\\").replace('"""', '""\\"')
print(file_contents)
print(f"b=\"\"\"{repr_contents}\"\"\";print(b);j='b=y';a='print(b);j=z;a=x;print(j.replace(chr(121),chr(34)*3+b.replace(chr(92),chr(92)*2).replace(chr(34)*3,chr(34)*2+chr(92)+chr(34))+chr(34)*3)+chr(59)+a.replace(chr(122),chr(39)+j+chr(39)).replace(chr(120),chr(39)+a+chr(39)))';print(j.replace(chr(121),chr(34)*3+b.replace(chr(92),chr(92)*2).replace(chr(34)*3,chr(34)*2+chr(92)+chr(34))+chr(34)*3)+chr(59)+a.replace(chr(122),chr(39)+j+chr(39)).replace(chr(120),chr(39)+a+chr(39)))")
