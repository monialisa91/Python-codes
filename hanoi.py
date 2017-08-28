# n- number of disks
# A, B, C - three roads
# We move disks from A to B, C is an auxiliary disk

# RECURSIVE ALGORITHM

def HanoiRE(n,A,B,C):
	if n > 0:
		HanoiRE(n-1,A,C,B)  # We move n-1 disks from A to C, B is an auxiliary disk
		B.append(A.pop())   # We move the n-th disk from A to B
		HanoiRE(n-1,C,B,A)  # We move n-1 disks from C to B, A is an axuliary disk

# ITERATIVE ALGORITHM

# auxiliary function verifying which move is possible in a given iteration

def LegalMove(A,B):
	if(len(A)!=0 and len(B)==0):
		B.append(A.pop())
	elif(len(A)==0 and len(B)!=0):
		A.append(B.pop())
	else:
		lastA=A[len(A)-1]
		lastB=B[len(B)-1]
		if(lastA>lastB):
			A.append(B.pop())
		else:
			B.append(A.pop())


def HanoiIT(n,A,B,C):
	moves= 2**n-1  # number of moves required
	for i in range(1, moves+1):
		if(i%3 == 1):
			LegalMove(A,B)
		elif(i%3 == 2):
			LegalMove(A,C)
		else:
			LegalMove(B,C)

# Verification of the algorithm

n=4
A=range(n,0,-1)
B=[]
C=[]

print "Before: \nA=" ,A, "B=", B, "C=", C

# a) recursive algorithm

print "RECURSIVE ALGORITHM"

HanoiRE(len(A),A,B,C)
print "After: \nA=",A,"B=",B,"C=",C

# b) iterative algorithm

print "ITERATIVE ALGORITHM"
if(n%2==0):
	HanoiIT(n,A,B,C)
else:
	HanoiIT(n,A,C,B)

print "After: \nA=",A,"B=",B,"C=",C