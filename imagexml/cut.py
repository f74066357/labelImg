# coding=Big5
n=input('num：')
total=input('total：')
k=1
while(k<=int(total)):
  if (k<10):
    t='0'+str(k)
  else:
    t=str(k)
    
  filename='fb'+n+'_'+t+'.xml'
  print(filename)
  try:
    f = open(filename, 'r')
    l = open("list.txt", 'a')
    fb = open("fb.txt", 'a')
    l.write(filename+"\n")
    lines_n = [lines.rstrip('\r\n') for lines in f.readlines() if lines.strip()]
    for i, line in enumerate(lines_n):
      if(len(line)>10):
        test=line[4]+line[5]+line[6]+line[7]
        if(test=='lena'):
          #print("ok")
          front=line.split('>')[1]
          back=front.split('<')[0]
          #print(back)
          fb.write(back+" ")
        if(test=='xmin'):
          front=line.split('>')[1]
          back=front.split('<')[0]
          #print(back)
          fb.write(back+" ")
        if(test=='ymin'):
          front=line.split('>')[1]
          back=front.split('<')[0]
          #print(back)
          fb.write(back+" ")
        if(test=='xmax'):
          front=line.split('>')[1]
          back=front.split('<')[0]
          #print(back)
          fb.write(back+" ")
        if(test=='ymax'):
          front=line.split('>')[1]
          back=front.split('<')[0]
          #print(back)
          fb.write(back)
          fb.write('\n')
  except:
    error = open("error.txt", 'a')
    error.write(filename+'\n')
  k=k+1
f.close()
fb.close()
error.close()
  