

def FINAL(Type,Duration,Budget,TYPE,Ques):
  print(Type,Duration,Budget,TYPE,Ques)

  import pandas as pd
  import numpy as np
  from  itertools import chain
  import numpy as np
  import re
  import math
  from math import cos, sin, atan2, sqrt
  import folium
  from folium import plugins
  #from IPython.display import Image
  import plotly.express as px
  import datetime
  from datetime import timedelta
  from datetime import datetime
  from plotly.express import timeline
  import pickle
  def dict_index_key(val_to_find,DICT):
    for k,v in DICT.items():
      if (v==val_to_find):
        return k
  def next_min(lis):
    m = [x*(-1) for x in lis]
  def get_pid_from_index(no):
    return 'POI'+str(no+1)
  def get_place(POI):
    c = jaipur_poi_df.loc[POI,'POIs']
    return c


  jaipur_poi_df = pd.read_csv('data/jaipur-poi.csv')
  dist_only_matrix_df = pd.read_csv('data/dist_only_matrix.csv')


  jaipur_poi_df.set_index('PID',inplace=True)
  jaipur_poi_df.head()
  dist_only_matrix_df.set_index('PID',inplace=True)
  dist_only_matrix_df.head(10)
  def extract(st):
    if (len(st)==8):
      return (st[2:6])
    else:
      return (st[2:7])
  def poi_finddist(poi1,poi2): 

    # extracting indices
    POI1=poi1.upper()
    POI2=poi2.upper()
    for i in jaipur_poi_df.iloc[:,0]:

      # to get name of place from pid (Ex: 'POI70')
      P1 = extract(np.array_str(jaipur_poi_df[jaipur_poi_df['POIs']==POI1].index.values))
      P2 = extract(np.array_str(jaipur_poi_df[jaipur_poi_df['POIs']==POI2].index.values))

      # indices
      x=int(P1[3:])-1
      y=int(P2[3:])-1
      if(x>=y):
        return dist_only_matrix_df.iloc[x,y]
      else:
        return dist_only_matrix_df.iloc[y,x]
  vac_type = {'Adventure and Outdoors':['Adventure'],'Spiritual':['Religious'],'Relaxing':['Scenic'],'City Life':['Food and Drinks','Shopping','Shows and Concerts'],'Cultural':['Local Experiences','History and Culture','Museum']}
  vac_type
  ## Main Input
  #(Run for changed Input)
  # Type = []

  # print("Choose your vacation type (priority-wise): \nAdventure and Outdoors\nCity Life\nCultural\nRelaxing\nSpiritual\n\nTo Stop, Enter 'N' \n\n ")

  # for i in range(0,5):
  #   j=i+1
  #   k = input('Enter Priority no. %d: '%j)
  #   if (k!='N'):
  #     Type.append(k)
  #   else:
  #     break

  # L=len(Type)

  # try:
  #   Duration = int(input('\n Enter number of days for the trip: '))
  # except:
  #   Duration = int(input('\n Enter a number: '))

  # try:
  #   Budget = int(input('\n Enter a rough budget for the trip: '))
  # except:
  #   Budget = int(input('\n Enter a number: '))

  # TYPE = input('\n Choose one:\nFamily\nFriends\nIndividual\n\n')

  # Ques = input('\n Is covering maximum places a priority (y/n)? ')

  # Algorithms
  ## Info
  def user_info():
    type_print = []
    type_print.append(str('User type choices: '))

    for i in range(0,len(Type)):
      type_print.append(str(str(i+1) +'. '+ Type[i]))

    type_print.append(str('No. of days: '+ str(Duration)))
    type_print.append(str('Budget: '+ str(Budget)))
    type_print.append(str('No. of POIs: '+str(no_of_pois)))
    type_print.append(str('Type: '+TYPE))
    if (Ques == 'y'):
      type_print.append(str('Covering maximum places is a priority.'))
    else:
      type_print.append(str('Covering maximum places is NOT a priority.'))
      #type_print.append(str('Suggested Hotel/Accomodation: '+nearest_hotel))
    type_print.append(str(nearest_hotel))
    
    return type_print

  
  ## User Matrix
  #(Run for changed input)
  vac_hm_df = pd.read_csv('data/vac_hm.csv')
  vac_hm_df.set_index('Unnamed: 0',inplace=True)
  vac_hm_df.head(3)
  Type
  user_matrix = {'Shows and Concerts':0,'Scenic':0,'Local Experiences':0,'Religious':0,'History and Culture':0, 'Museum':0,'Food and Drinks':0,'Adventure':0,'Shopping':0}
  vac_type
  # Creating User 1d array of vacation type according to input choices filled

  for i in range(0,len(Type)):
    pvalue = 5-i
    for j in vac_type[Type[i]]:
      if (j == 'History and Culture'):
        user_matrix[j] = pvalue+(0.075*pvalue)
      elif (j == 'Local Experiences'):
        user_matrix[j] = pvalue+(0.055*pvalue)
      else:
        user_matrix[j] = pvalue
  user_matrix
  val = list(user_matrix.values())
  typ = list(user_matrix.keys()) # to be used in cosine similarity
  #print(val)
  #print(typ)
  TEMP=[typ,val]
  user_df = pd.DataFrame(TEMP,columns=typ)
  user_df.drop(axis=0,index=0,inplace=True)
  user_df
  ## Deciding Places by Priority (Cosine Similarity)
  #(Run for changed Input)
  # J_priority_mapping.csv
  #uploaded = files.upload()
  J_priority_df = pd.read_csv('data/J_priority_mapping.csv')
  J_priority_df.set_index('PID',inplace=True)
  ### Formula
  def cen_cos_h(lis): # takes 1 returns 1
    lol =[]
        
    avg =sum(lis)/9

    for x in lis:
        lol.append(x-avg)
    return lol

  def cencos_formula_h(LIS1,LIS2):

    lis1 = cen_cos_h(LIS1)
    lis2 = cen_cos_h(LIS2)

    i=0

    prod_lis = []
    while (i<len(lis1)):
      if(lis1[i]!=0 and lis2[i]!=0):
        product = lis1[i]*lis2[i]
        prod_lis.append(product)

      i=i+1

    sq_lis1 = [(x)**2 for x in lis1]
    sq_lis2 = [(x)**2 for x in lis2]

    sum_sq_lis1 = sum(sq_lis1)
    sum_sq_lis2 = sum(sq_lis2)

    sqrt_lis1=math.sqrt(sum_sq_lis1)
    sqrt_lis2=math.sqrt(sum_sq_lis2)


    num = sum(prod_lis)
    den = sqrt_lis1*sqrt_lis2

    try:
      cos = num/den
    except:
      cos = 0

    if (den==0):
      cos = 'lalala'




  


    return cos

  print('CHECK1')
  ### Cosine similarity
  #(Run for changed inputs)
  J_priority_df.head()
  cos_sim_list_h = []
  cos_sim_dict_h = {}
  for i in range(0,len(J_priority_df.iloc[:,1:])):

    x = list(J_priority_df.iloc[i,1:]) # one row in the POI priority df
    y = val # user
    
    
    result = cencos_formula_h(x,y)

    cos_sim_list_h.append(result) 
    cos_sim_dict_h[i] = result
  ### Deciding Places
  #(Run this for changed inputs)
  import matplotlib.pyplot as plt
  c=0
  selected={} # vacation cosine similarity is greater than 0
  for k,v in cos_sim_dict_h.items():
    if(v>0):
      c=c+1
      selected[k]=v
  no_of_pois = c
  #print(no_of_pois)
  sorted_selected1 = dict(sorted(selected.items(), key=lambda item: item[1],reverse=True))
  #print(sorted_selected1) #DICTIONARY
  sorted_selected = {}
  for k,v in sorted_selected1.items():
    sorted_selected[k] = v
  x = no_of_pois/Duration

  if (Ques=='y'):
    while (x>6):
      sorted_selected.popitem()
      no_of_pois = len(sorted_selected)
      x=no_of_pois/Duration 

  elif (Ques=='n'):
    while (x>3):
      sorted_selected.popitem()
      no_of_pois = len(sorted_selected)
      x=no_of_pois/Duration 

      
  #print('Final no.: ',no_of_pois)
  # for k,v in sorted_selected.items(): 
  #   p = k+1
  #   pid = 'POI'+str(p)
  #   print(jaipur_poi_df.loc[pid,'POIs'])
  #   print(list(J_priority_df.loc[pid,'Shows and Concerts':])) # range -  " 'Shows and Concerts': "
  #   print(val)
  #   print('\n\n')
  len(sorted_selected)
  # creating selected df
  ll= []
  for k,v in sorted_selected.items():
    l = []
    l.append(k)
    l.append(v)
    ll.append(l)

  sorted_selected_df = pd.DataFrame(ll)
  sorted_selected_df.set_index(0,inplace=True)
  sorted_selected_df.columns = ['sorted priority']


  l1 = []
  l2 = []
  for i in sorted_selected_df.iterrows():
    ind = i[0]
    pid = 'POI'+str(ind+1)
    l1.append(pid)
    l2.append(jaipur_poi_df.loc[pid,'POIs'])

  sorted_selected_df['PID'] = l1
  sorted_selected_df['POIs'] = l2 
  (sorted_selected_df)
  sorted_selected_df.to_csv('data/sorted_selected_df.csv')
  ### 


  ## Get Center Coordinates for initially Selected (based on vacation type input) POIs
  #(run for new inputs)
  #( result )
  #!pip install gmplot
  #uploaded = files.upload()
  lat_lng_df = pd.read_csv('data/lat_lng.csv')
  lat_lng_df.set_index(jaipur_poi_df.index,inplace=True)
  lat_lng_df.drop(columns=['Unnamed: 0'],inplace=True)
  selected_coord = {}
  for i in range(0,no_of_pois):
    selected_coord[list(sorted_selected_df['PID'])[i]] = lat_lng_df.loc[list(sorted_selected_df['PID'])[i],'Lat,Lng']
  selected_coord

  coord_pairs = []
  for k,v in selected_coord.items():
    a = list(map(float,v.split(',')))
    coord_pairs.append(a)
  coord_pairs
  def center(coord_pairs):
    l=len(coord_pairs)
    sum_i=0.0
    sum_j=0.0
    for i,j in coord_pairs:
      sum_i=sum_i+float(i)
      sum_j=sum_j+float(j)

    LAT = sum_i/l
    LONG = sum_j/l

    return [LAT,LONG]
  result = center(coord_pairs)
  result
  # To plot on gmaps

  #coord_pairs_df=pd.DataFrame(coord_pairs)
  #coord_pairs_df.to_csv('data/coord_pairs.csv')


  ## Hotel Assignment

  
  #(run for changed inputs)
  #remove earlier ones CHANGE

  Jaipur_Hotels_df = pd.read_csv('data/Jaipur_Hotels.csv')
  #Jaipur_Hotels_df.set_index('HID',inplace=True)
  h_lat_df = pd.read_csv('data/h_lat_df.csv')
  h_lat_df.set_index('HID',inplace=True)
  def ind_to_id(ind):
    return 'HID'+str(ind+1)

  def id_to_ind(hid):
    return (int(hid[3:])-1)
  def distance(l1,l2): #l1 & l2 - lists with 2 ele each
    R = 6373.0
    lat1 = math.radians(l1[0])
    lon1 = math.radians(l1[1])
    lat2 = math.radians(l2[0])
    lon2 = math.radians(l2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance # km



  def dis_from_centre(centre,lis): # lis has to be a list of lists (2 ele each)
    hotel_centre_lis = []
    for i in range(0,len(lis)):
      dis = distance(centre,lis[i]) # km
      hotel_centre_lis.append(dis)
    return hotel_centre_lis 
  h_lat_lis=[]
  for i in list(h_lat_df['Lat,Lng']):
    j = list(map(float,i.split(',')))
    h_lat_lis.append(j) # lat lng list sperate cells

  hotel_dis_result_lis = []
  hotel_dis_result_lis = dis_from_centre(result,h_lat_lis) # dist from centre to each hotel list

  hotel_dis_result_dict = {}
  for i in range(0,len(hotel_dis_result_lis)):
    hotel_dis_result_dict[ind_to_id(i)]=hotel_dis_result_lis[i]
  def threshold_dis(n,lis_of_distances): # n - threshold in km
    c=0
    lala=[]
    for i in range(0,len(lis_of_distances)):
      if (lis_of_distances[i]<=float(n)):
        c=c+1
        #print(i,': ',lis_of_distances[i],'\t',Jaipur_Hotels_df.iloc[i,0])
        k = dict_index_key(lis_of_distances[i],hotel_dis_result_dict)
        lala.append(k)
    return lala
  dist_pri = [2.5,4,6,8,10,20,35] #[0.5,0.75,1.2,3.5,6.0,10.0,20.0,35.0,50.0] ## 2.5,4
  des_pri = [50,80,130,200,260]
  sorted_by_des = Jaipur_Hotels_df.sort_values(by=['Desirable','Price'],ascending=False,inplace=False)
  # change in hotel assignment notebook
  percent_table = {'10k':[70,60,55],'15k':[65,55,50],'20k':[60,50,45],'25k':[60,40,40],'30k':[60,45,40],'45k':[60,50,50],'60k':[65,55,60],'greater':[70,60,70]}
  percent_table_df = pd.DataFrame(percent_table,index=['Family','Friends','Individual'])
  percent_table_df = percent_table_df*0.01
  percent_table_df
  def percent_check():
    if (Budget<=10000):
      column = '10k'
    elif (Budget > 10000 and Budget <=15000):
      column = '15k'
    elif (Budget > 15000 and Budget <=20000):
      column = '20k'
    elif (Budget > 20000 and Budget <=25000):
      column = '25k'
    elif (Budget > 25000 and Budget <=30000):
      column = '30k'
    elif (Budget > 30000 and Budget <=45000):
      column = '45k'
    elif (Budget > 45000 and Budget <=60000):
      column = '60k'
    elif (Budget > 60000):
      column = 'greater'

    return percent_table_df.loc[TYPE,column]
  def hid_suitable(hid):
    IND = id_to_ind(hid)
    PRICE = Jaipur_Hotels_df.loc[IND,'Price']
    PRODUCT = PRICE*Duration

    # compare the two
    PER = PRODUCT/Budget ## CHANGE LATER
    PER_THRESHOLD = percent_check()

    
    if (PER>PER_THRESHOLD):
      return False  
    elif (PER<=PER_THRESHOLD):
      return True
  flag = 1
  #selected = []
  for i in des_pri: #20%, 30%, ...
    #print('des',i)

    # DESIRABLE
    one_row = []
    for j in range(0,i):  #20%, 30%, ...   
      hid = sorted_by_des.iloc[j,0] # thankgod iloc not loc
      one_row.append(hotel_dis_result_dict[hid])
  # got one_row with some distances 

    # DISTANCE
    dist_selected = [] 
    for j in dist_pri: #[0.5,0.75,1.2,3.5,6.0,10.0,20.0,35.0,50.0]
      #print('dis',j)

      dist_selected = threshold_dis(j,one_row) #Returns a List

      if (dist_selected==[]):
        #print('empty dist list')
        continue
      #else:
        #print('dist selected ',dist_selected)

      # PRICE
      price_dict = {} # NOT SORTED
      for k in dist_selected:   ## TRY EMPTY CHANGE
        price_dict[k]=Jaipur_Hotels_df.loc[id_to_ind(k),'Price']
      #dict of price formed
      #print('price d: ',price_dict)

      p = [v for k,v in price_dict.items()] #List ## CHANGE DUPLICATION
      p.sort(reverse=True)

      PRICE_SORT_DICT = {} # to sort and store by desc order of price (in new dictionary)
      for k in range(0,len(p)):
        key = dict_index_key( p[k] , price_dict )
        PRICE_SORT_DICT[key] = p[k]

      #print('price order: ',PRICE_SORT_DICT)#######
      
      # Main Price Loop
      for k1,k2 in PRICE_SORT_DICT.items():

        if (hid_suitable(k1)==False):
          continue

        elif (hid_suitable(k1)==True): #boolean
          FINAL_HID=k1
          flag = 0
          #print('break')
          break
          
      if (flag==0):
        #print('break: ','j: ',j)
        break
    if (flag==0):
      #print('break: ','i: ',i)
      break

  print('CHECK3')
  INDEX = id_to_ind(FINAL_HID)
  nearest_hotel = Jaipur_Hotels_df.iloc[INDEX,1]
  #user_info()
  nearest_hotel

  ## Time Gantt chart
  time_slots_df = pd.read_csv('data/time_slot_pois.csv')
  time_slots_df.set_index('Section',inplace=True)
  timepois = pd.read_csv('data/time-pois_new.csv')
  timepois.set_index('PID',inplace=True)
  timepoisnew = pd.read_csv('data/time-pois_new.csv')

  for i in range(0,73):
    for j in range(2,8):
      if (timepoisnew.iloc[i,j] is not np.nan):
        timepoisnew.iloc[i,j] = datetime.strptime(timepoisnew.iloc[i,j],'%H:%M')
      else:
        pass
  main = []
  for i in range(0,len(timepoisnew['POIs'])):

    if ((timepoisnew.iloc[i,2] is not np.nan) and (timepoisnew.iloc[i,3] is not np.nan)):
      n = 2
      
      for j in range(0,n):
        temp = []
        temp.append(timepoisnew.iloc[i,0])
        temp.append(timepoisnew.iloc[i,4+j])
        temp.append(timepoisnew.iloc[i,6+j])
        main.append(temp)

    elif ((timepoisnew.iloc[i,2] is not np.nan) and (timepoisnew.iloc[i,3] is np.nan)):
      n = 1
      
      for j in range(0,n):
        temp = []
        temp.append(timepoisnew.iloc[i,0])
        temp.append(timepoisnew.iloc[i,4+j])
        temp.append(timepoisnew.iloc[i,6+j])
        main.append(temp)
  timepoiplotlydf = pd.DataFrame(main)
  timepoiplotlydf.columns = ['PID','Start','Finish']
  timepoiplotlydf
  def get_endtime(pid):
    time1 = str(timepoiplotlydf[timepoiplotlydf['PID']==pid]['Finish'][0])[11:16]

    if ( len(timepoiplotlydf.loc[pid]) > 1 ):
      time2 = str(timepoiplotlydf.loc[pid].iloc[1,2])[11:16]
      return [time1,time2]
    else:
      return [time1]
  arr = []
  for i in range(0,len(timepoiplotlydf)):
    t = (timepoiplotlydf.iloc[i,0],i)
    arr.append(t)

  index = pd.MultiIndex.from_tuples(arr, names=["first", "second"])
  timepoiplotlydf.set_index(index,inplace=True)
  # useless
  #sorted_timepoiplotlydf = timepoiplotlydf.sort_values(by=['Start','Finish'],ascending=True)
  def easy_on_the_len(lis):
    new = []
    for i in range(0,len(lis)):
      if (lis[i] is not np.nan):
        new.append(lis[i])
    return new
  def filter_pois(df):
    s_lis = []
    for i in range(0,len(df)):
      s_lis.append(df.iloc[i,2]) # len is no. of selected pois
    
    a_of_a = []
    for i in range(0,len(time_slots_df)): # row by row; i-section. -- 0 to 12
      b = list(time_slots_df.iloc[i,:]) # list of one section
      a = []
      #for j in range(0,len(easy_on_the_len(b))):
      for k in range(0,len(s_lis)):
        if (s_lis[k] in b):
          a.append(s_lis[k])
      a_of_a.append(a)

    DF = pd.DataFrame(a_of_a)
    return DF 
  selected_time_slots = filter_pois(sorted_selected_df)
  # CHANGE FOR SORTED ORDER ROW WISE

  # making new df of only selected POIs
  main = []
  for i in range(0,len(timepoiplotlydf)):
    if ( timepoiplotlydf.iloc[i,0] in list(sorted_selected_df['PID']) ):
      main.append( list(timepoiplotlydf.iloc[i,:]) )


  main_df = pd.DataFrame(main)
  main_df.columns = ['PID','Start','Finish']
  #user_info()
  fig = px.timeline(main_df, x_start="Start", x_end="Finish", y="PID", color="PID",height=900,width=1300)
  #fig.show()
  ## Routing
  #(run for new inputs)
  #### Preprocessing
  #(run for user inputs)
  #user_info() #change
  nearest_coord = list(map(float,h_lat_df.loc[FINAL_HID,'Lat,Lng'].split(',')))
  nearest_coord # Actual hotel coordinates
  selected_coord_lis = [] # list of lat and long seperately
  for k,v in selected_coord.items():
    j = list(map(float,v.split(',')))
    selected_coord_lis.append(j)

  selected_coord_lis
  selected_coord_dict = {} # list of lat and long seperately
  for k,v in selected_coord.items():
    j = list(map(float,v.split(',')))
    selected_coord_dict[k] = j
  selected_coord_dict
  def dis_from_centre2(centre,dicti): # lis has to be a list of lists (2 ele each)
    centre_dict = {}
    for k,v in dicti.items():
      dis = distance(centre,dicti[k]) # km
      centre_dict[k] = dis # REMEBER NOT OUR POI INDICES
    return centre_dict




  dummy_poi_dis = dis_from_centre2(nearest_coord,selected_coord_dict)
  dummy_poi_dis # distance from Actual hotel to selected pois
  ### Rings
  time_slots_df
  def easy_on_the_len(lis):
    new = []
    for i in range(0,len(lis)):
      if (lis[i] is not np.nan):
        new.append(lis[i])
    return new


  def filter_pois(df):
    s_lis = []
    for i in range(0,len(df)):
      s_lis.append(df.iloc[i,1]) # len is no. of selected pois
    
    a_of_a = []
    for i in range(0,len(time_slots_df)): # row by row; i-section. -- 0 to 12
      b = easy_on_the_len(list(time_slots_df.iloc[i,:])) # list of one section
      a = []
      #for j in range(0,len(easy_on_the_len(b))):
      for k in range(0,len(s_lis)):
        if (s_lis[k] in b):
          a.append(s_lis[k])
      a_of_a.append(a)

    DF = pd.DataFrame(a_of_a)
    return DF  
  selected_time_slots = filter_pois(sorted_selected_df)
  selected_time_slots
  #from IPython.display import Image
  #Image("Unknown.png")
  dummy_sorted = dict(sorted(dummy_poi_dis.items(), key=lambda item: item[1],reverse=False))
  rings = {}

  for i in range(4,len(selected_time_slots)): #each section

    row = [x for x in list(selected_time_slots.iloc[i,:]) if (x != None)] #one row time slots table

    c=0
    grp = []
    for k,v in dummy_sorted.items(): #distance dictionary
      if (v !=None):
        
        if (k in row):
          c=c+1
          grp.append(k)
          dummy_sorted[k]=None

        if (c==Duration):
          break

    rings[i+1]=grp
  rings
  time_rings = { 5:'8:00',6:'9:00',7:'10:00',8:'11:00',9:"12:00",10:'17:00',11:'18:00',12:'20:00',13:'22:00'}
  ### Routing
  # 
  # 
  #  
  print('CHECK4')



  #user_info()
  def pid_finddist(P1,P2): 
      # indices
      x=int(P1[3:])-1
      y=int(P2[3:])-1
      if(x>=y):
        return dist_only_matrix_df.iloc[x,y]
      else:
        return dist_only_matrix_df.iloc[y,x]
  def len_wo_null(dict_of_lis):
    c=0
    for k,v in dict_of_lis.items():
      if (v==[]):
        c=c+1
    return len(dict_of_lis)-c
  main_routes = []

  for day in range(0,Duration):
    day_route=[]
    route_counter = rings[5][day]
    day_route.append(route_counter)

    i=1
    flag = 0
    while (i!=len_wo_null(rings)):#for i in range(1,len_wo_null(rings)): #1,2,3,4,5,6

      store_dist = {} # counter for how many minimmms to skip

      for l in rings[5+i]: ##CHANGE
        dist = pid_finddist(route_counter,l)
        store_dist[l] = dist

      length_of_this_ring = len(rings[5+i])


      dist_sorted = dict(sorted(store_dist.items(), key=lambda item: item[1],reverse=False)) #ascending

      if (flag==length_of_this_ring):
        break
    
      min = list(dist_sorted.keys())[flag] #pid


      if (min in chain(*main_routes)):

        flag = flag+1
        continue
      else:
        route_counter = min
        day_route.append(route_counter)
        i=i+1
        flag=0

    main_routes.append(day_route)
    print('\n')
  new_all_routes = []
  for i in main_routes:
    row = []
    for j in i:
      row.append(jaipur_poi_df.loc[j,'POIs'])
    new_all_routes.append(row)
  all_routes = new_all_routes
  all_routes

  ## Map
  #nearest coord, selected coord list, jaipur poi df, lat_lng_ddf, all_routes


  #user_info()
  def refresh_map():
    m = folium.Map(location=[26.916973348018836,75.82555554188403],tiles='StamenToner',zoom_start=13)

    for i in range(0,len(selected_coord_lis)):
      pid = 'POI'+str(i+1)
      place = get_place(pid)
      folium.Marker(
          location=selected_coord_lis[i], # coordinates for the marker (Earth Lab at CU Boulder)
          popup=place, # pop-up label for the marker
          icon=folium.Icon(color='red')
      ).add_to(m)

    folium.Marker(
          location=nearest_coord, # coordinates for the marker (Earth Lab at CU Boulder)
          popup=place, # pop-up label for the marker
          icon=folium.Icon(color='black')
      ).add_to(m)
    return m
  def get_pid(place):
    return extract(np.array_str(jaipur_poi_df[jaipur_poi_df['POIs']==place].index.values))
  c_arr = ['red','pink','orange','purple','yellow','green','lightblue', 'lightgray', 'lightgreen', 'lightred','beige', 'black','blue']
  def make_route(all): # day is the day 
    
    if (all):
      m = refresh_map()
      for day in range(0,len(all_routes)):

        for j in range(0,len(all_routes[day])-1):

          start = all_routes[day][j]
          end = all_routes[day][j+1]

          loc = [tuple(map(float,lat_lng_df.loc[get_pid(start),'Lat,Lng'].split(','))),
                tuple(map(float,lat_lng_df.loc[get_pid(end),'Lat,Lng'].split(',')))]

          folium.PolyLine(loc,
                          color=c_arr[day],
                          weight=15,
                          opacity=0.8).add_to(m)
    else:
      m = refresh_map()
      day = int(input('Enter day: '))
      for j in range(0,len(all_routes[day])-1):

          start = all_routes[day][j]
          end = all_routes[day][j+1]

          loc = [tuple(map(float,lat_lng_df.loc[get_pid(start),'Lat,Lng'].split(','))),
                tuple(map(float,lat_lng_df.loc[get_pid(end),'Lat,Lng'].split(',')))]

          folium.PolyLine(loc,
                          color=c_arr[day],
                          weight=15,
                          opacity=0.8).add_to(m)
    return m
  # hist={}
  # for i in all_routes:
  #   for j in i:
  #     if (j not in list(hist.keys())):
  #       hist[j]=1
  #     else:
  #       hist[j]=hist[j]+1
  # for key,val in hist.items():
  #   if (val==1):
  #     continue
  #   else:
  #     for k in range(0,val-1):
  #       for i in range(len(all_routes)-1,-1,-1):
  #         for j in range(len(all_routes[i])-1,-1,-1):
  #         # we have one k and its freq (v)
  #           if (all_routes[i][j]==key):
  #             all_routes[i].pop(j)
  # rings
  def get_time(name_place):
    pid = get_pid(name_place)
    
    for i in range(5,14):
      if (rings[i] != []):
        if pid in rings[i]:
          time_slot = dict_index_key(rings[i],rings)
    return time_rings[time_slot]

  big_la = []
  for i in range(0,len(all_routes)):
    la = 'Day %d: '%(i+1)   
    print(la)
    big_la.append(la)

    for j in range(0,len(all_routes[i])):

      time = get_time(all_routes[i][j])
      endtime = get_endtime( get_pid(all_routes[i][j]) )
      no_of_slots = len(endtime)

      lala = []
      if (no_of_slots == 1):

        if (j!=len(all_routes[i])-1):
          la1 = all_routes[i][j]+' (Anytime after '+time+' and before '+endtime[0]+') '
          print(la1)
          big_la.append(str(la1))
        else:
          la1 = all_routes[i][j]+' (Anytime after '+time+' and before '+endtime[0]+') '
          print(la1)
          big_la.append(str(la1))

      elif (no_of_slots == 2):

        if (j!=len(all_routes[i])-1):
          la1 = all_routes[i][j]+' (Anytime after '+time+' and before '+endtime[0]+' and '+endtime[1]+') '
          print(la1)
          big_la.append(str(la1))
        else:
          la1 = all_routes[i][j]+' (Anytime after '+time+' and before '+endtime[0]+' and '+endtime[1]+') '
          print(la1)
          big_la.append(str(la1))
          
    big_la.append('')
    print('')
  big_la

  #user_info()
  our_map = make_route(all=True)
      
  # Deploying
  #pickle_out = open("lol.pkl","wb")
  #pickle.dump(big_la, pickle_out)
  #pickle_out.close()
  print('returning..')
  return [big_la,user_info(),our_map]

#la = FINAL(['Spiritual'],8,4000,'Family','n')
#print(la)

# map
# big _la
# user info