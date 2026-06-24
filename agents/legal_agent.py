import json

def get_regulation(country, topic="stablecoin"):
    """
    Simula una consulta a una API de regulaciones.
    En una versión real, usarías una API como la de la SEC o BCRP.
    """
    mock_data = {
        "Peru": {
            "stablecoin": "Las stablecoins están reguladas por la SBS. Deben registrarse si son usadas como medio de pago.",
            "incorporation": "Las empresas cripto deben registrarse en SUNAT y SBS."
        },
        "US": {
            "stablecoin": "Las stablecoins son consideradas valores por la SEC. Deben cumplir con las regulaciones de la Ley de Valores.",
            "incorporation": "Los DAOs pueden registrarse como LLC en Wyoming o Delaware."
        }
    }
    return mock_data.get(country, {}).get(topic, "Información no disponible para ese país/tópico.")

if __name__ == "__main__":
    # Ejemplo de uso (para pruebas)
    print(get_regulation("Peru", "stablecoin"))
