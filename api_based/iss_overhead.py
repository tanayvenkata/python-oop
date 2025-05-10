import requests
import plotly.express as px
import pandas as pd
import time

def plot_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lon = float(data["iss_position"]["longitude"])

    zoom = 10 # 0-18 where higher means more zoomed in. 
    language = "en-US"

    iss_location_json = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={iss_lat}&lon={iss_lon}&zoom={zoom}&accept-language={language}"
    response = requests.get(iss_location_json, 
                            headers={"User-Agent": "ISSLocator (tanayvenkata@gmail.com)"})

    json_data = response.json()
    location_name = json_data.get("display_name", "N/A")


    df = pd.DataFrame({
        "Latitude": [iss_lat],
        "Longitude": [iss_lon],
        "Label": ["ISS Current Location"],
        "Location": [location_name]
    })


    fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", 
                hover_name="Label",
                hover_data=["Location"],
                projection="orthographic",
                )

    fig.update_traces(marker=dict(color="blue", size=10), 
                    )


    fig.show()

plot_iss()


