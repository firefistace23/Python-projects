import score_calc

p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0, 'balls':119, 'field':0}
p2={'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2, 'balls':112, 'field':0}
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1}
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0}
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0}

players=[p1,p2,p3,p4,p5]
result=[]

for i in range(5):
    if players[i].get('role')=='bat':
        batpoints=score_calc.batscore(players[i].get('runs'),players[i].get('4'),players[i].get('6'),players[i].get('balls'),players[i].get('field'))
        print (batpoints)
        result.append({'name':players[i].get('name'),'batscore':batpoints})
        
    if players[i].get('role')=='bowl':
        bowlpoints=score_calc.bowlscore(players[i].get('wkts'),players[i].get('overs'),players[i].get('runs'),players[i].get('field'))
        print (bowlpoints)
        print (players[i].get('name'))
        result.append({'name':players[i].get('name'),'bowlscore':bowlpoints})

for i in range(5):
    print (result[i])
