def batscore(runs,four,six,balls,field):
    score=int(runs/2)
    if runs>50:
        score=score+5
    if runs>100:
        score=score+10
    strike_rate=runs*100/balls
    if strike_rate>100:
        score=score+4
    elif strike_rate>80:
        score=score+2
    score=score+four+2*six+10*field
    return score
def bowlscore(wkts,overs,runs,field):
    score=wkts*10
    if wkts>=3:
        score=score+5
    if wkts>=5:
        score=score+10
    economy=runs/overs
    if economy<2:
        score=score+10
    elif economy<3.5:
        score=score+7
    elif economy<4.5:
        score=score+4
    score=score+10*field
    return score
    
