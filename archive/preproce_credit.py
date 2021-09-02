import pandas as pd

credits=pd.read_csv("credits.csv")
credits=pd.DataFrame(credits)

n=len(credits)
nulos='NULL'

credits_cast=pd.DataFrame() #actores
credits_credi=pd.DataFrame() #crew
credits_crew=pd.DataFrame() #personas

#cast
data_idcast=[]
dataidcast=[]
datamoviecast=[]
#personas
data_idcrew=[]
data_name=[]
#crew
dataidcred=[]
dataidcrew=[]
datajob=[]
datamovie=[]
eliminar="'"
for i in range(0,n):
    #casting
    cast=credits.iloc[i]['cast']
    cast=eval(cast)   
    if len(cast)>0:
        for j in range(0,len(cast)):
            dato=(cast[j])
            idcredit=dato['credit_id']
            id=dato['id']
            name=dato['name']
            name=str(name)
            for x in range(len(eliminar)):
            	name=name.replace(eliminar[x],"\"")
            name=""+name+""
            data_idcast.append(idcredit)
            dataidcast.append(id)
            data_idcrew.append(id)#persona
            data_name.append(name)#persona
            datamoviecast.append(credits.iloc[i]['id'])
     #credit crew       
    cred=credits.iloc[i]['crew']
    cred=eval(cred)   
    if len(cred)>0:
        for j in range(0,len(cred)):
            dato=(cred[j])
            idcredit=dato['credit_id']
            id=dato['id']
            job = dato['job']
            name=dato['name']
            dataidcred.append(idcredit)
            dataidcrew.append(id)
            data_idcrew.append(id)#persona
            data_name.append(name)#persona
            datajob.append(job)
            datamovie.append(credits.iloc[i]['id'])

#casting
credits_cast.insert(0,'id',data_idcast,True)#id de trabajo
credits_cast.insert(1,'actor',dataidcast,True)#id personal
credits_cast.insert(2,'movie',datamoviecast,True)#id pelicula
credits_cast.drop_duplicates(subset=['id'], keep="first", inplace=True)
#dir/pro/writ... etc
credits_credi.insert(0,'id',dataidcred,True)
credits_credi.insert(1,'crew',dataidcrew,True)
credits_credi.insert(2,'job',datajob,True)
credits_credi.insert(3,'movie',datamovie,True)
credits_credi.drop_duplicates(subset=['id'], keep="first", inplace=True)
#personas
credits_crew.insert(0,'id',data_idcrew,True)
credits_crew.insert(1,'name',data_name,True)
credits_crew.drop_duplicates(subset=['id'], keep="first", inplace=True)
#a csv
credits_cast.to_csv("casting.csv", index= False)#cast
credits_credi.to_csv("credito.csv", index= False)
credits_crew.to_csv("crew.csv", index= False)
