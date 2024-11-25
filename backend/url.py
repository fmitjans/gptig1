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
        "Menor a 2 meses": format_date(today - timedelta(days=60)),

        "Alhué": "1117",
        "Buin": "1124",
        "Calera de Tango": "1125",
        "Cerrillos": "1131",
        "Cerro Navia": "1132",
        "Colina": "1128",
        "Conchalí": "1133",
        "Curacaví": "1116",
        "El Bosque": "1134",
        "El Monte": "1120",
        "Estación Central": "1135",
        "Huechuraba": "1136",
        "Independencia": "1137",
        "Isla de Maipo": "1121",
        "La Cisterna": "1138",
        "La Florida": "1139",
        "La Granja": "1140",
        "La Pintana": "1141",
        "La Reina": "1142",
        "Lampa": "1129",
        "Las Condes": "1143",
        "Lo Barnechea": "1144",
        "Lo Espejo": "1145",
        "Lo Prado": "1146",
        "Macúl": "1147",
        "Maipú": "1148",
        "María Pinto": "1115",
        "Melipilla": "1114",
        "Ñuñoa": "1149",
        "Padre Hurtado": "1122",
        "Paine": "1126",
        "Pedro Aguirre Cerda": "1150",
        "Peñaflor": "1123",
        "Peñalolén": "1151",
        "Pirque": "1112",
        "Providencia": "1152",
        "Pudahuel": "1153",
        "Puente Alto": "1111",
        "Quilicura": "1154",
        "Quinta Normal": "1155",
        "Recoleta": "1156",
        "Renca": "1157",
        "San Bernardo": "1127",
        "San Joaquín": "1158",
        "San José de Maipo": "1113",
        "San Miguel": "1159",
        "San Pedro": "1118",
        "San Ramón": "1160",
        "Santiago": "1161",
        "Talagante": "1119",
        "Tiltil": "1130",
        "Vitacura": "1162"
    }
    
    return values_table.get(string, "")
