# Tesla's 3 6 9 obsession began with his fixation on the number three — and suggests that three, six, and nine could hold the key to the universe. 
#The theory has been co-opted and expanded upon even today by people who hope to improve their lives by “manifesting” their desires by repeatedly writing them out.
# so in this project I'm going to write a prove code using the geometry circle to show the power of those three digits mathematically
def TeslaThroty():
  new_list = []
  num = 15
  # generate 360° circle values
  for i in range(1, 25):
    d = num*i  
  
    x = [int(a) for a in str(d)]
    s = sum(x)
    stri = len(str(s))
    if stri >= 2:
      x = [int(a) for a in str(s)]
      s = sum(x)
      new_list.append(s)
    else:
      new_list.append(s)
    
    r = sum(new_list)
    x = [int(a) for a in str(r)]
    z = sum(x)
    k = [int(a) for a in str(z)]
    t = sum(k)
    print(d, '°')
    print(new_list,'=',r,'=' ,x, '=', t)


TeslaThroty()
