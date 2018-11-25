import pafy
import re 
url = 'https://www.youtube.com/watch?v=DWaoq0714cM'
fetch = re.search(r'.{11}$', url).group()
v = pafy.new(fetch)
print('Available Streams:')
print('*'*22)
for i,j in enumerate(v.streams,1):
 print(str(i)+'.',j)
inp = int(input('\nEnter Stream Number: '))
d = v.streams[inp-1]
d.download()
