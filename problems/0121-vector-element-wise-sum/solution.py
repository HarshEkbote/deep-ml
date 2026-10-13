def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if not a or not b:
		return -1
	elif len(a)!=len(b):
		return -1
	else:
		result=[]
		if len(a)==len(b):
			for i in range(len(a)):
				result.append(a[i]+b[i])
		return result