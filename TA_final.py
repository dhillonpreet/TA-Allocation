# -*- coding: utf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('random-matching-fe28e183d850.json', scope)
gs = gspread.authorize(credentials)
bs=gs.open("TA allocation")
a = bs.get_worksheet(0)
b = bs.get_worksheet(2)
c = bs.get_worksheet(1)
d = bs.get_worksheet(3)
slots={}
preferred_rankings_prof = {}
preferred_rankings_ta = {}
for i in range(2,len(a.col_values(1))+1):
 preferred_rankings_prof[(a.cell(i,1)).value]= a.row_values(i)[1:]
for i in range(2,len(b.col_values(1))+1):
 preferred_rankings_ta[(b.cell(i,1)).value]= b.row_values(i)[1:]
for i in range(2,len(d.col_values(1))+1):
 slots[(d.cell(i,1)).value]= d.cell(i,2).value
co=0
for i in slots.values():
    co=co+int(i)
if co<len(preferred_rankings_ta.keys()):
    temp=preferred_rankings_ta
    preferred_rankings_ta=preferred_rankings_prof
    preferred_rankings_prof=temp
    slots={}
    for i in preferred_rankings_prof.keys():
        slots[i]=1
tentative_assignments 	= []
free_ta 				= []

def init_free_ta():
    for ta in preferred_rankings_ta.keys():
            free_ta.append(ta)

def begin_matching(ta):

    for prof in preferred_rankings_ta[ta]:
        taken_match = [couple for couple in tentative_assignments if prof in couple]
        if (len(taken_match) < int(slots[prof])):
            tentative_assignments.append([ta, prof])
            free_ta.remove(ta)
            break
        elif (len(taken_match) >= int(slots[prof])):
            current_ta = preferred_rankings_prof[prof].index(taken_match[0][0])
            current_pair=taken_match[0]
            for i in taken_match:
                if preferred_rankings_prof[prof].index(i[0])>current_ta:
                    current_ta=preferred_rankings_prof[prof].index(i[0])
                    current_pair=i
            potential_ta = preferred_rankings_prof[prof].index(ta)
            if (current_ta < potential_ta):
                0+0
            else: 				
                free_ta.remove(ta)
                free_ta.append(current_pair[0])
                for i in taken_match:
                    if i == current_pair:
                        i[0]=ta
                break

def stable_matching():
	while (len(free_ta) > 0):
		for ta in free_ta:
			begin_matching(ta)


def main():
    init_free_ta()
    stable_matching()
    final_assignments={}
    for i in preferred_rankings_prof.keys():
        final_assignments[i]=[]
    for i in tentative_assignments:
        final_assignments[i[1]].append(i[0])
    print(final_assignments)
    count1=0
    count2=0
    count3=0
    for i in final_assignments.keys():
        c.update_cell(count1+2, 1,i )
        count1+=1
    for j in final_assignments.values():
        for k in j:
            c.update_cell(count2+2, count3+2,k )
            count3+=1
        count3=0
        count2+=1

main()