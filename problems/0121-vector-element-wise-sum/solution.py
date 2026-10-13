def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if not a or not b or len(a)!=len(b):
		return -1
	
	return [x+y for x, y in zip(a,b)]