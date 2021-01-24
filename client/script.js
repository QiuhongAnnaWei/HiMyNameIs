const URL = "0.0.0.0:5000/generate"
const NAMES = ["Stacy", "Leonardo", "Kyle", "Cookie"]

function generate() {
  fetch(URL, {
    method: 'GET',
    headers: {
      "Content-Type": "application/json",
      'Access-Control-Allow-Origin': '*',
      },
    mode: "cors",
    // credentials: "same-origin",
  })
    .then(data => {
      document.querySelector("#name").innerHTML = data
    }).catch(err => console.log(err))

}

function generateDummy() {
  document.querySelector("#name").innerHTML = NAMES[Math.floor(Math.random() * NAMES.length)]
}
