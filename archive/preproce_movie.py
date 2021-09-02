import pandas as pd

moviesmd=pd.read_csv("movies_metadata.csv", low_memory=False)
moviesmd=pd.DataFrame(moviesmd)

n=len(moviesmd)
nulos='NULL'

movie=pd.DataFrame() #peliculas
genre=pd.DataFrame() #generos
gen_mov=pd.DataFrame() #relacion pelicula-genero
votes=pd.DataFrame() #votos

#movies
data_idmov=[]
data_ti=[]
#genero
data_idgen=[]
data_namegen=[]
#gen_mov
data_idm=[]
data_idg=[]
#votos
data_idmv=[]
data_avg=[]
data_cnt=[]

eliminar="'"


for i in range(0,n):
	#movie
	mov=moviesmd.iloc[i]['id']
	title=moviesmd.iloc[i]['title']
	title=str(title)
	for x in range(len(eliminar)):
		title=title.replace(eliminar[x],"")
	title=""+title+""
	data_idmov.append(mov)
	data_ti.append(title)
	#generos
	gen=moviesmd.iloc[i]['genres']
	gen=eval(gen)   
	if len(gen)>0:
		for j in range(0,len(gen)):
			dato=(gen[j])
			idgen=dato['id']
			ngen=dato['name']
			data_idgen.append(idgen)#genre
			data_namegen.append(ngen)#genre
			data_idm.append(mov)#gen_mov
			data_idg.append(idgen)#gen_mov
	#votos       
	avg=moviesmd.iloc[i]['vote_average']
	cnt=moviesmd.iloc[i]['vote_count']
	data_idmv.append(mov)
	data_avg.append(avg)
	data_cnt.append(cnt)

#movies
movie.insert(0,'id',data_idmov,True)#id de pelicual
movie.insert(1,'title',data_ti,True)#titulo
movie.drop_duplicates(subset=['id'], keep="first", inplace=True)
#genres
genre.insert(0,'id',data_idgen,True)
genre.insert(1,'name',data_namegen,True)
gen_mov.insert(0,'genre',data_idg,True)
gen_mov.insert(1,'movie',data_idm,True)
genre.drop_duplicates(subset=['id'], keep="first", inplace=True)
#votos
votes.insert(0,'movie',data_idmv,True)
votes.insert(1,'promedio',data_avg,True)
votes.insert(2,'total',data_cnt,True)

#a csv
movie.to_csv("movies.csv", index= False)#pelicula
genre.to_csv("genres.csv", index= False)#genero
gen_mov.to_csv("gen_mov.csv", index= False)#gen_mov
votes.to_csv("votes.csv", index= False)#votos
