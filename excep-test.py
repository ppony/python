try:
     try:
         raise EOFError('XD')
     except EOFError as e:
         print(e.args)
         raise IndexError('Orz')
except IndexError as e:
     print(e.args)
     #print(e.__cause__.args)
     print(e.__context__.args)
