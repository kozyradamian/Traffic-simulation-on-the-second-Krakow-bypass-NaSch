#0-wolna komorka 1-zajeta komorka 2-czerwone swiatlo 3-koniec drogi(koniecznosc zmiany pasa)

class Road(object):
    def __init__(self,lane,l_road=None,r_road=None,other_roads=None):
        self.lane=lane
        self.l_road=l_road
        self.r_road=r_road
        self.other_roads=other_roads #roads that cross this road
               
    def print_road(self,reverse=False):
        if(not reverse):
            for i in range(len(self.lane)):
                if(self.lane[i].crossing_id!=None):
                    print(max(self.lane[i].vehicle,self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
                else:
                    print(self.lane[i].vehicle,end=' ')
            print('')
        else: #droga z prawej do lewej
            for i in range(len(self.lane)-1,-1,-1):
                if(self.lane[i].crossing_id!=None):
                    print(max(self.lane[i].vehicle,self.other_roads[self.lane[i].crossing_id-1].lane[self.lane[i].index].vehicle),end=' ')                
                else:
                    print(self.lane[i].vehicle,end=' ')
            print('')


class Cell(object):
    def __init__(self,vehicle,crossroads=False,crossing_id=None,index=None,speed_limit=4):
        self.vehicle=vehicle
        self.crossroads=crossroads
        self.crossing_id=crossing_id
        self.index=index
        self.speed_limit=speed_limit 
    
    
def traffic_lights_management(traffic_lights_timer):
    if(traffic_lights_timer==80):
        traffic_lights_timer=0
    
    if(traffic_lights_timer==0):
        traffic_ligths1(1)
     
    if(traffic_lights_timer==17):
        traffic_ligths1(2)    
        
    elif(traffic_lights_timer==20):
        traffic_ligths1(3)
        
    elif(traffic_lights_timer==60):
        traffic_ligths1(4)
        
    elif(traffic_lights_timer==70):
        traffic_ligths1(5)
        
    traffic_lights_timer+=1
        
        
def traffic_ligths1(x): #sekwencja swiatel
    if(x==1):
        main_road1.lane[23].vehicle=0
        main_road2.lane[23].vehicle=0
        main_road3.lane[23].vehicle=0
        main_road4.lane[28].vehicle=0
        main_road5.lane[28].vehicle=0
        main_road6.lane[28].vehicle=0
        r1.lane[14].vehicle=2
        r2.lane[14].vehicle=2
        r1.lane[7].vehicle=2
        r2.lane[7].vehicle=2
    elif(x==2):
        main_road1.lane[23].vehicle=2
        main_road2.lane[23].vehicle=2
        main_road3.lane[23].vehicle=2
        main_road4.lane[28].vehicle=2
        main_road5.lane[28].vehicle=2
        main_road6.lane[28].vehicle=2
    elif(x==3):
        r1.lane[14].vehicle=0
        r2.lane[14].vehicle=0
    elif(x==4):
        r1.lane[7].vehicle=0
        r2.lane[7].vehicle=0
    elif(x==5):
        r1.lane[7].vehicle=2
        r2.lane[7].vehicle=2
        
    
###representing roads###
########################## roads init with empty cells ################################       
main_road4 = [Cell(0) for i in range(55)]
main_road5 = [Cell(0) for i in range(55)]
main_road6 = [Cell(0) for i in range(55)]
main_road1 = [Cell(0) for i in range(78)]
main_road2 = [Cell(0) for i in range(78)]
main_road3 = [Cell(0) for i in range(78)]
r1 = [Cell(0) for i in range(26)]
r2 = [Cell(0) for i in range(26)]
r3 = [Cell(0) for i in range(10)]
r4 = [Cell(0) for i in range(26)]
r5 = [Cell(0) for i in range(26)]


########################## special cells and init roads obj ###########################
#main_road1
main_road1[24]=Cell(0,True,1,15) #r1
main_road1[25]=Cell(0,True,2,15) #r2
main_road1[59]=Cell(0,True,4,15) #r4
main_road1[60]=Cell(0,True,5,15) #r5
main_road1 = Road(main_road1)
#---

#main_road2
main_road2[24]=Cell(0,True,1,16) #r1
main_road2[25]=Cell(0,True,2,16) #r2
main_road2[59]=Cell(0,True,4,16) #r4
main_road2[60]=Cell(0,True,5,16) #r5
main_road2 = Road(main_road2)
#---

#main_road3
main_road3[24]=Cell(0,True,1,17) #r1
main_road3[25]=Cell(0,True,2,17) #r2
main_road3[59]=Cell(0,True,4,17) #r4
main_road3[60]=Cell(0,True,5,17) #r5
main_road3[42]=Cell(0,True,3,8)  #r3
main_road3 = Road(main_road3)
#---

#main_road4
main_road4[29]=Cell(0,True,1,8) #r2
main_road4[30]=Cell(0,True,2,8) #r1
main_road4 = Road(main_road4)
#---

#main_road5
main_road5[29]=Cell(0,True,1,9) #r2
main_road5[30]=Cell(0,True,2,9) #r1
main_road5 = Road(main_road5)
#---

#main_road6
main_road6[29]=Cell(0,True,1,10) #r2
main_road6[30]=Cell(0,True,2,10) #r1
main_road6 = Road(main_road6)
#---

#r1 \/
r1[8]=Cell(0,True,1,30)  #mr4
r1[9]=Cell(0,True,2,30)  #mr5
r1[10]=Cell(0,True,3,30) #mr6
r1[15]=Cell(0,True,4,24) #mr1
r1[16]=Cell(0,True,5,24) #mr2
r1[17]=Cell(0,True,6,24) #mr3
r1 = Road(r1)
#---

#r2 /\
r2[8]=Cell(0,True,1,25)  #mr3
r2[9]=Cell(0,True,2,25)  #mr2
r2[10]=Cell(0,True,3,25) #mr1
r2[15]=Cell(0,True,4,29) #mr6
r2[16]=Cell(0,True,5,29) #mr5
r2[17]=Cell(0,True,6,29) #mr4
r2 = Road(r2)
#---

#r3 /\
r3[8]=Cell(0,True,1,42)  #mr3
r3[9]=Cell(3) #end of road
r3 = Road(r3)
#---

#r4 \/
#r4[8]=Cell(0,True,1,30)  #mr4
#r4[9]=Cell(0,True,2,30)  #mr5
#r4[10]=Cell(0,True,3,30) #mr6
r4[15]=Cell(0,True,4,59) #mr1
r4[16]=Cell(0,True,5,59) #mr2
r4[17]=Cell(0,True,6,59) #mr3
r4 = Road(r4)
#---

#r5 /\
r5[8]=Cell(0,True,1,60)  #mr3
r5[9]=Cell(0,True,2,60)  #mr2
r5[10]=Cell(0,True,3,60) #mr1
#r5[15]=Cell(0,True,4,29) #mr6
#r5[16]=Cell(0,True,5,29) #mr5
#r5[17]=Cell(0,True,6,29) #mr4
r5 = Road(r5)
#---


########################## setting neighbors and other roads ##########################
#main_road1
main_road1.r_road=main_road2
main_road1.other_roads=[r1,r2,None,r4,r5]
#---

#main_road2
main_road2.l_road=main_road1
main_road2.r_road=main_road3
main_road2.other_roads=[r1,r2,None,r4,r5]
#---

#main_road3
main_road3.l_road=main_road2
main_road3.other_roads=[r1,r2,r3,r4,r5]
#---

#main_road4
main_road4.l_road=main_road5
main_road4.other_roads=[r2,r1]
#---

#main_road5
main_road5.r_road=main_road4
main_road5.l_road=main_road6
main_road5.other_roads=[r2,r1]
#---

#main_road6
main_road6.r_road=main_road5
main_road6.other_roads=[r2,r1]
#---

#r1
r1.other_roads=[main_road4,main_road5,main_road6,main_road1,main_road2,main_road3] 
#---

#r2
r2.other_roads=[main_road3,main_road2,main_road1,main_road6,main_road5,main_road4]
#---

#r3
r3.other_roads=[main_road3]
#---

#r4
r4.other_roads=[None,None,None,main_road1,main_road2,main_road3] #TODO: gora droga
#---

#r5
r5.other_roads=[main_road3,main_road2,main_road1,None,None,None]
#---