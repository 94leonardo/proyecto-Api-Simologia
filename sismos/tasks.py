import requests
from datetime import datetime
from .models import Feature
from django.utils.dateparse import parse_datetime

# convertidor Unix -> datetime


def convert_unix_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000.0)


# validaciones de campos numericos


def is_valid_feature(feature):
    props = feature["properties"]
    coords = feature["geometry"]["coordinates"]

    if not all(
        [
            props.get("title"),
            props.get("url"),
            props.get("place"),
            props.get("magType"),
            coords,
        ]
    ):
        return False

    magnitude = props.get("mag")
    longitude = coords[0]
    latitude = coords[1]
    return (
        magnitude is not None
        and -1.0 <= magnitude <= 10.0
        and -180.0 <= longitude <= 180.0
        and -90.0 <= latitude <= 90.0
    )


def load_features_from_usgs():
    print("Solicitando datos del USGS...")
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error al obtener datos del feed USGS.")
        return

    print("Respuesta resibida.")
    data = response.json()
    total = 0
    inserted = 0
    print(f"Total de Features: {len(['features'])}")

    for idx, feature in enumerate(data["features"]):
        if idx % 50 == 0:
            print(f"Procesando feature #{idx}")

        if not is_valid_feature(feature):
            continue

    for feature in data["features"][:50]:  # ← solo 50 eventos por ahora
        total += 1
        if not is_valid_feature(feature):
            continue

        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]
        external_id = feature["id"]

        # varificar sis ya existe

        if Feature.objects.filter(external_id=external_id).exists():
            continue

        # crear y guardar nuevo feature
        Feature.objects.create(
            external_id=external_id,
            magnitude=props.get("mag"),
            place=props.get("place"),
            time=convert_unix_timestamp(props.get("time")),
            tsunami=bool(props.get("tsunami")),
            mag_type=props.get("magType"),
            title=props.get("title"),
            longitude=coords[0],
            latitude=coords[1],
            url=props.get("url"),
        )
        inserted += 1
    print(f"Se procesaron {total} eventos. Insertados:{inserted}")
