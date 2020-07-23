def points(runs,balls,four,six,wkts,overs,runs2,field):
    points=0
    points=points+(runs//2)
    if runs>=100:
        points=points+10
    elif runs>=50:
        points=points+5
    else:
        points=points
    if 80<=(runs/balls)*100<=100:
        points=points+2
    elif (runs/balls)*100>100:
        points=points+6
    else:
         points=points
    points=points+four
    points=points+six*2
    points=points+10*wkts
    if 5>wkts>=3:
        points=points+5
    elif wkts>=5:
        points=points+10
    else:
        points=points
    if overs != 0:
        if 3.5<(runs2/overs)<=4.5:
            points=points+4
        elif 2<=(runs2/overs)<=3.5:
            points=points+7
        elif (runs2/overs)<2:
            points=points+10
        else:
            points=points
    points=points+10*field
    return points
                

