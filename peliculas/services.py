import requests

def consumir_api(url: str):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()

    return None
    
def ver_peliculas(params: dict[str, int]):
    response = consumir_api(
    'https://api.themoviedb.org/3/movie/popular?api_key=ecbcdcf9044928d12b179d9153f5a269&language=es-VE&with_genres={genres}&page={page}'.format(**params)    
    )
    
    if response: 
        return response.get('results')
    
    return None