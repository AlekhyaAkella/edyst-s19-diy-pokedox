import requests
urll="https://pokeapi.co/api/v2/pokemon/"
poke_full_data={}

for i in range(1,152):

    poke_data=requests.get(url=urll+str(i))
    poke_data=poke_data.json()

    poke_full_data[i]=[poke_data['id'],poke_data['name'],poke_data['sprites']['front_default']]
file=open("data.txt",'w')
file.write(str(poke_full_data))
