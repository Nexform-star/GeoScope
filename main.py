import requests
import folium

menu = """
================================
          GeoScope V1
   Open-Source Geospatial Analysis
================================

1. Analyze a location
2. Exit
"""
print(menu)
select = int(input("Select an option: "))
if select == 1:
    menu1 = """
================================
          GeoScope V1
   Open-Source Geospatial Analysis
================================

1. Analyze a location by Lat and Lon
2. Analyze a location by Address
"""
    print(menu1)
    select1 = int(input("Select an option (1 or 2): "))
    if select1 == 1:
        lat = (input("Enter latitude: "))
        lon = (input("Enter longitude: "))
        url = requests.get(f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json", headers={"User-Agent" : "GeoScope/1.0"})
        url_json = url.json()
        display_name = url_json["display_name"]
        adresse = url_json["address"]["road"]
        county = url_json["address"].get("county")
        state = url_json["address"]["state"]
        postcode = url_json["address"]["postcode"]
        country = url_json["address"]["country"]
        city = url_json["address"].get("city")
        lat = url_json["lat"]
        lon = url_json["lon"]
        addresstype = url_json["addresstype"]
        print(f"County : {county}")
        print(f"Address : {adresse}")
        print(f"Postal code : {postcode}")
        print(f"Country : {country}")
        print(f"City : {city}")
        print(f"Longitude : {lon}, Latitude : {lat}")
        print(f"Address type : {addresstype}")
        print(f"Display name : {display_name}")
        m = folium.Map(location=(lat, lon))
        folium.Marker(
            location=[lat, lon],
            tooltip="Click me!",
            popup=display_name,
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)
        m
        m.save("output/index.html")
        print("Location save in index.html in output")

    if select1 == 2:
        adresse = input("Enter an address: ")
        url = requests.get(f"https://nominatim.openstreetmap.org/search?q={adresse}&format=json", headers={"User-Agent" : "GeoScope/1.0"})
        url_json = url.json()
        if len(url_json) >= 1:
            name = url_json[0]["name"]
            display_name = url_json[0]["display_name"]
            type1 = url_json[0]["type"]
            lat = url_json[0]["lat"]
            lon = url_json[0]["lon"]
            boundingbox = url_json[0]["boundingbox"]
            print(f"Display name: {display_name}")
            print(f"Place type: {type1}")
            print(f"Latitude : {lat}")
            print(f"Longitude : {lon}")
            print(f"Bounding box: {boundingbox}")
            m = folium.Map(location=(lat, lon))
            folium.Marker(
                location=[lat, lon],
                tooltip="Click me!",
                popup=display_name,
                icon=folium.Icon(icon="cloud"),
            ).add_to(m)
            m
            m.save("output/index.html")
            print("Location save in index.html in output")
            if name == "":
                print(f"Name: {adresse}")
            else:
                print(f"Name: {name}")
        else:
            print("No results found for this address.")
if select == 2:
    exit