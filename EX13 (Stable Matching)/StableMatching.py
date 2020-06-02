
# -- Variables used -- #

temp_read = []

pref_list_men = dict()
pref_list_women = dict()
men = dict()
women = dict()
pref_rank_list = dict()
propose_flag = dict()

unmatched = "-"

# -------------------- #

# -- Functions Used -- #

def isFree(w):
	if(women[w]=="-"):
		return True
	else:
		return False

def Unstable(m,w):
	m1 = women[w]
	if(pref_rank_list[w][m1] > pref_rank_list[w][m]):
		return True
	else:
		return False
	
def proposal(m):
	indx = propose_flag[m]
	w = pref_list_men[m][indx]
	men[m] = w
	return w

def undo_proposal(m):
	men[m] = "-"

def accept_proposal(m,w):
	women[w] = m

def reject_proposal(w):
	men[women[w]] = "-"
	women[w] = "-"

def find_unmatched_male():
	for i in men:
		if(men[i] == "-"):
			return i
	return "-"

def cur_iteration(itr_count):
	print("Itr %-2d : { "%(itr_count),end="")
	for i in men:
		if(men[i]!="-"):
			print(i+men[i],end=" ")
	print("} ",end="")

def input_and_precalc_from_file():
	f = open("input.txt","r")
	
	temp_read = f.readline().split()

	count = len(temp_read) - 1

	pref_list_men[temp_read[0]] = temp_read[1:]
	men[temp_read[0]] = unmatched
	propose_flag[temp_read[0]] = 0;

	for i in range(1,count):
		temp_read = f.readline().split()
		pref_list_men[temp_read[0]] = temp_read[1:]
		men[temp_read[0]] = unmatched
		propose_flag[temp_read[0]] = 0;

	empty_line = f.readline()

	for i in range(count):
		temp_read = f.readline().split()
		pref_list_women[temp_read[0]] = temp_read[1:]
		women[temp_read[0]] = unmatched

		cou = 1
		temp_d = dict()

		for val in pref_list_women[temp_read[0]]:
			temp_d[val] = cou
			cou+=1

		pref_rank_list[temp_read[0]] = temp_d
	
	f.close()

def input_and_precalc_from_console():
	temp_read = input().split()

	count = len(temp_read) - 1

	pref_list_men[temp_read[0]] = temp_read[1:]
	men[temp_read[0]] = unmatched
	propose_flag[temp_read[0]] = 0;

	for i in range(1,count):
		temp_read = input().split()
		pref_list_men[temp_read[0]] = temp_read[1:]
		men[temp_read[0]] = unmatched
		propose_flag[temp_read[0]] = 0;

	empty_line = input()

	for i in range(count):
		temp_read = input().split()
		pref_list_women[temp_read[0]] = temp_read[1:]
		women[temp_read[0]] = unmatched

		cou = 1
		temp_d = dict()

		for val in pref_list_women[temp_read[0]]:
			temp_d[val] = cou
			cou+=1

		pref_rank_list[temp_read[0]] = temp_d

def stable_Matching():
	itr_count = 0
	while(find_unmatched_male()!="-"):
		
		if(itr_count!=0): 
			print()
		cur_iteration(itr_count)
		
		m = find_unmatched_male()
		w = proposal(m)

		if(isFree(w)):
			accept_proposal(m,w)
		else:
			if(Unstable(m,w)):
				reject_proposal(w)
				accept_proposal(m,w)
			else:
				undo_proposal(m)

		propose_flag[m] += 1
		itr_count+=1
	print()
	cur_iteration(itr_count)
	print("  <--- Stable Match")
		
# --------------------- #

# ------- Main ------- #

def main():
	input_and_precalc_from_console()
	#input_and_precalc_from_file()
	stable_Matching()

if __name__=="__main__":
	main()

# --------------------- #


'''
TESTCASES : - 

IP:
a  u  r  t  s
b  r  t  u  s
c  t  u  s  r
d  u  r  t  s

r  a  c  d  b
s  d  a  b  c
t  c  b  d  a 
u  b  d  c  a

OP:
Itr 0  : { } 
Itr 1  : { au } 
Itr 2  : { au br } 
Itr 3  : { au br ct } 
Itr 4  : { br ct du } 
Itr 5  : { ar ct du } 
Itr 6  : { ar ct du } 
Itr 7  : { ar bu ct } 
Itr 8  : { ar bu ct } 
Itr 9  : { ar bu ct } 
Itr 10 : { ar bu ct ds }   <--- Stable Match

IP:
a r q s
b s q r
c q r s

OP:
q a c b
r c a b
s a b c

Itr 0  : { } 
Itr 1  : { ar } 
Itr 2  : { ar bs } 
Itr 3  : { ar bs cq }   <--- Stable Match 

'''

