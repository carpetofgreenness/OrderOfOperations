import itertools
import operator

#for i in chain([1,2,3],['a','b','c']):
#	print i

#print ([x for x in itertools.permutations('1234',4)])
#print ([x for x in itertools.product('+-*',repeat=3)])

nums = tuple(itertools.permutations('1234',4))
op_char = tuple(itertools.product('+-*',repeat=3))

ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.div
       }

items = []

for z in op_char:
	op_func0 = ops[z[0]]
	op_func1 = ops[z[1]]
	op_func2 = ops[z[2]]
	for x in nums:
		#print "operators are "
		#print z
		#print "numbers are "
		#print x
		first  = op_func0(int(x[0]),int(x[1]))
		second = op_func1(int(first),int(x[2]))
		third = op_func2(int(second),int(x[3]))
		items.append(third)
		#second = op_func1(first,int(x[2]))
		#print "sum is"
		#print third
		first0 = op_func0(int(x[0]),int(x[1]))
		second0 = op_func2(int(x[2]),int(x[3]))
		third0 = op_func1(int(first0),int(second0))
		items.append(third0)

final_items = set(items)
print final_items


#op_func0 = ops[op_char[0][0]]
#print op_func0(int(nums[0][2]),int(nums[0][3]))