
'''
    You can run the part 1 firstly to see what will be created in folder 'm_data'
    And then run the part2 to see what will be modifed for each json file.
    Usually, I might run the both part at the same time. 

    @Attentions: Since there are still some issues with my code. After you have modified json files, you need to 
    go the folder and delete the last several json files manually  which (start with "RESULT") or (empty json files.)
    The eligible json file should start with 'rating'. 


    @ just simply run "python3 data.py"
'''


# *******************e.g the first 90 json objects will be created from plot.txt*************************
# you can change this value to have different number of json file.
num =20




#PART 1:  convert plot.txt file to separate json files. 
# These json files will be stoed in " m_data" folder

f = open("plot.txt", "r")
count =0
for x in f:
    output = open("m_data/course"+str(count)+'.json','w')
    output.write(x)
    count+=1
    output.close()
    if count == num:
        break

f.close()



# ======================================================================================================================================

#PART 2:  modify each json file so that it can be fed by IBM Discovery. 

import json
error = 0
M_id =0
for i in range(num):
    flag =True
    with open('m_data/course'+str(i)+'.json','r') as f:
        data = json.load(f)['RESULT']    
        if data['imdbinfo'] == "notfound":
            flag =False
            error+=1
        else:
            # You can use  【 print(data) 】 to see what is stored in the data
            nfinfo = data['nfinfo']
            imdbinfo = data['imdbinfo']
            mgname = data['mgname']

            # merge several information together.
            imdbinfo.update(nfinfo)
            imdbinfo.update({'mgname' : mgname})
            imdbinfo.update({'M_id' : M_id})
            M_id+=1

    f.close()

    # you might have questions why do I use (i-error) below, but you can just ignore this part. 
    # some json objects dont have completed information. So I try to delete those. 
    with open('m_data/course'+str(i-error)+'.json','w') as F:
        if flag is True:
            data= json.dump(imdbinfo, F)
        else:
            data= json.dump('', F)
            error+=1
            

    
    F.close()
  
    
