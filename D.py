
import sys
def ominousOmino(input_, T):
	
	a = "GABRIEL"
	b = "RICHARD"
	for t in range(0, T):
		X, R, C = input_[t].split()
		X = int(X)
		R = int(R)
		C = int(C)

		'''---------'''
		y = X
		status = ""
		for x in range(1,X+1):
			if (R>=y and C>=x) or (R>=x and C>=y):
				status = "pass"
			else:
				status = "fail"
				break
			y -= 1
		'''--------------'''

		if min(R,C)**2 <= X and (R*C)/X <= 2:
			status = "fail"


		if (R*C)%X==0 and status=="pass":
			r = "Case #%d: %s"%(t+1, a)
		else:
			r = "Case #%d: %s"%(t+1, b)
		print r

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    inp = []
    for _t in xrange(t):
        line =  f.readline().strip()
        inp.append(line)

    ominousOmino(input_=inp, T=t)