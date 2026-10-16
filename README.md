# GeoScope V1

**An open-source geospatial analysis tool built with Python.**

GeoScope is a command-line tool that uses the OpenStreetMap Nominatim API to retrieve geographical information about locations using GPS coordinates or an address.

This project is built for learning purposes and aims to explore Python, API requests, and open-source geospatial data.

## Features

- **Reverse Geocoding:** Retrieve location information from latitude and longitude.
- **Address Search:** Search for a location using an address or place name.
- **Location Information:** Retrieve details such as coordinates, place types, and display names.
- **Bounding Box:** Retrieve the geographical bounding box of a search result.
- **No Results Handling:** Display a message when no matching address is found.

## Technologies

- Python
- Requests
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

3. Install the required dependency:

   ```bash
   pip install requests
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

## Data Source

GeoScope uses the [OpenStreetMap Nominatim API](https://nominatim.openstreetmap.org/) for geocoding and reverse geocoding.

Geographical data is provided by [OpenStreetMap contributors](https://www.openstreetmap.org/copyright).

Please respect the [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/), including its request rate limits and attribution requirements.

## Limitations

- Results depend on the data available in OpenStreetMap.
- Some geographical fields may be missing for certain locations.
- This version is a basic command-line application and does not include a graphical interface.
- Error handling and input validation may be improved in future versions.

## Future Improvements

- Improve error handling and input validation.
- Add more detailed geographical information.
- Improve the command-line interface.
- Add additional geospatial analysis features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

GeoScope V1 is a learning project exploring Python and open-source geospatial data.
