In this version, the urllib library is used to make the API request and handle the response. Here's how GitHub Copilot assisted in this code:

API Usage: GitHub Copilot provided suggestions for constructing the URL for the API request using urllib.request.urlopen(). It also suggested using json.loads() to parse the JSON response.
Data Parsing: Similar to the previous version, GitHub Copilot suggested accessing the desired weather data fields from the parsed JSON data.
Error Handling: GitHub Copilot provided suggestions for handling potential errors. It recommended using urllib.error.URLError to catch any errors that may occur during the API request.
By incorporating these suggestions, the code demonstrates how to make an API request to OpenWeatherMap, parse the JSON response, and handle errors using the urllib library.
output would be :

![image](https://github.com/hemasreej/weather_snap/assets/92966088/15b73663-91ca-4ba9-b788-7100d6f4c137)
![WhatsApp Image 2023-06-04 at 15 04 39](https://github.com/hemasreej/weather_snap/assets/92966088/61048c1e-58b5-4e80-a7a2-fc578cf76cfb)

