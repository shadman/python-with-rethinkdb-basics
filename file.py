
import common
from partial import mine

print('testing')

print('declearing function')

def my_func(type = True, str = 'noo'):
 if type == 1:
  return 'true' + str
 else:
  return 'false' + str


print(my_func(str='yess', type=False))

common.me('shan')

mine('shadman')

#raise ValueError('number must be non-negative')

try:
	import shan
except ImportError:
	#print('error')
	chardet = None
	#raise ValueError('Test')

if chardet:
	print(chardet)
else:
	print(None)

has_chardet = chardet if chardet else 2
print(has_chardet)

array = [11,22,33]
print(array[0])
print(array[-1])
array.append(22)
print('Length:' + str(len(array)))

array = range(11)
print(array[2])
print('Length:' + str(len(array)))

for i in array:
	print('Index Value: ' + str(i))

count = 0
while (count < 10):
	print('This is:' + str(count))
	count = count + 1 


print('ba bye')

