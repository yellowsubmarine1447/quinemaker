a = 1
b="""a = 1""";print(b);a='b=y;print(b);a=x;print(a.replace(chr(121),chr(34)+chr(34)+chr(34)+b+chr(34)+chr(34)+chr(34)).replace(chr(120),chr(39)+a+chr(39)))';print(a.replace(chr(121),chr(34)+chr(34)+chr(34)+b+chr(34)+chr(34)+chr(34)).replace(chr(120),chr(39)+a+chr(39)))
