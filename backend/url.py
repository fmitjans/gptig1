from datetime import datetime, timedelta

def format_date(date):
    # Convert date string to datetime if it's not already a datetime object
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')
    
    # Format to DD/MM/YYYY and replace / with %2F
    formatted_date = date.strftime('%d/%m/%Y').replace('/', '%2F')
    return formatted_date

def encode_url(string):
    # Get today's date
    today = datetime.now().date()
    values_table = {
        "": "",
        "Metropolitana de Santiago": 378,
        "Arica y Parinacota": 388,
        "Tarapacá": 376,
        "Antofagasta": 387,
        "Atacama": 386,
        "Coquimbo": 383,
        "Valparaíso": 375,
        "Libertador General Bernardo O'Higgins": 377,
        "Maule": 379,
        "Ñuble": 391,
        "Bío Bío": 384,
        "Araucanía": 382,
        "Los Ríos": 389,
        "Los Lagos": 381,
        "Aysén del General Carlos Ibáñez del Campo": 385,
        "Magallanes y Antártica Chilena": 380,

        "Sin Educación formal": "1",
        "Educación básica incompleta": "2",
        "Educación básica completa": "3",
        "Educación media incompleta": "4",
        "Educación media completa": "5",
        "Educación superior Incompleta": "6",
        "Educación superior Completa": "7",
        "Magíster": "8",
        "Educación especial": "9",
        "Doctorado": "10",

        "Full time": "9",
        "Part time": "10",

        "Hoy": format_date(today),
        "Ayer": format_date(today - timedelta(days=1)),
        "Menor a 3 días": format_date(today - timedelta(days=3)),
        "Menor a 1 semana": format_date(today - timedelta(weeks=1)),
        "Menor a 15 días": format_date(today - timedelta(days=15)),
        "Menor a 1 mes": format_date(today - timedelta(days=30)),
        "Menor a 2 meses": format_date(today - timedelta(days=60))
    }
    
    return values_table.get(string, "")



