const WEATHER_API_KEY = "42c3a22ceb654f3d8a8192521253007";
const WEATHER_API_CALL_URL = `http://api.weatherapi.com/v1/current.json?key=${WEATHER_API_KEY}&q=Nador&aqi=no`;

const timeDiv = document.querySelector("header .time");
const weatherDiv = document.querySelector("header .weather");

setInterval(() => {
  const now = new Date();
  const hours = now.getHours();
  const minutes = now.getMinutes();

  timeDiv.textContent = `${hours}:${minutes}`;
});

// fetch(WEATHER_API_CALL_URL)
//   .then(async (response) => {
//     const json = await response.json();
//     weatherDiv.textContent = `${json.current.condition.text}, ${json.current.temp_c} °C`;
//   })
//   .catch((error) => console.log(`ERROR GETTING WEATHER: ${error}`));
