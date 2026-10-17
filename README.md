# GeoScope V1

**An open-source geospatial analysis tool built with Python.**

GeoScope is a command-line tool that uses the OpenStreetMap Nominatim API to retrieve geographical information about locations using GPS coordinates or an address. It also generates interactive maps to visualize the selected locations.

This project is built for learning purposes and aims to explore Python, API requests, open-source geospatial data, and interactive map generation.

## Features

- **Reverse Geocoding:** Retrieve location information from latitude and longitude.
- **Address Search:** Search for a location using an address or place name.
- **Location Information:** Retrieve details such as coordinates, place types, and display names.
- **Bounding Box:** Retrieve the geographical bounding box of a search result.
- **Interactive Maps:** Generate interactive maps using Folium.
- **Location Markers:** Display a marker at the selected location.
- **Interactive Popups:** View the location's full display name by clicking its marker.
- **HTML Export:** Save the generated map to `output/index.html`.
- **No Results Handling:** Display a message when no matching address is found.

## Technologies

- Python
- Requests
- Folium
- OpenStreetMap
- Nominatim API

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nexform-star/GeoScope.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GeoScope
   ```

3. Install the required dependencies:

   ```bash
   python -m pip install requests folium
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

Launch GeoScope and choose an option from the command-line menu.

You can:

1. Analyze a location using latitude and longitude.
2. Search for a location using an address.
3. View the geographical information returned by Nominatim.
4. Generate an interactive map of the selected location.
5. View the location's marker and popup on the map.

The generated map is saved as `output/index.html`. Open this file in a web browser to explore the map.

**Note:** The `output` directory must exist before GeoScope saves the map.

## Data Sources

GeoScope uses the [OpenStreetMap Nominatim API](https://nominatim.openstreetmap.org/) for geocoding and reverse geocoding.

Geographical data is provided by [OpenStreetMap contributors](https://www.openstreetmap.org/copyright).

Folium is used to generate interactive maps, with map tiles loaded from the selected tile provider.

Please respect the [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/) and the [OpenStreetMap Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/), including their usage limits and attribution requirements.

## Limitations

- Results depend on the data available in OpenStreetMap.
- Some geographical fields may be missing for certain locations.
- The application currently uses a command-line interface.
- Error handling and input validation may be improved in future versions.
- Generated maps require an internet connection to load online map tiles.

## Future Improvements

- Improve error handling and input validation.
- Add more detailed geographical information.
- Improve the command-line interface.
- Add multiple location markers to a single map.
- Add additional geospatial analysis features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

GeoScope V1 is a learning project exploring Python, open-source geospatial data, and interactive mapping.
