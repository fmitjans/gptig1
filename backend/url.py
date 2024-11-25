
def encode_url(string):
    values_table = {
        "": "",
        "Metropolitana": 378,
        "Arica y Parinacota": 388,
        "Tarapacá": 376,
        "Antofagasta": 387,
        "Atacama": 386,
        "Coquimbo": 383,
        "Valparaíso": 375,
        "O'Higgins": 377,
        "Maule": 379,
        "Ñuble": 391,
        "Bío Bío": 384,
        "La Araucanía": 382,
        "Los Ríos": 389,
        "Los Lagos": 381,
        "Aysén": 385,
        "Magallanes y Antártica Chilena": 380
    }
    
    return values_table.get(string, None)