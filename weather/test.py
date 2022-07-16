testdict = {
"type":
"weather_result",
"temperature":
"77",
"unit":
"Fahrenheit",
"precipitation":
"0%",
"humidity":
"41%",
"wind":
"4 mph",
"location":
"London, UK",
"date":
"Saturday 1:00 PM",
"weather":
"Sunny",
"thumbnail":
"https://ssl.gstatic.com/onebox/weather/64/sunny.png",
"forecast":
[
{
"day":
"Saturday",
"weather":
"Partly cloudy",
"temperature":
{
"high":
"84",
"low":
"61"
},
"thumbnail":
"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"
},]}

print(testdict["forecast"][0]["thumbnail"])