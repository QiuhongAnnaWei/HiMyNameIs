const URL = "/generate"
const NAMES = ["Stacy", "Leonardo", "Kyle", "Cookie"]

function generate() {
  fetch(URL, { method: 'GET' })
    .then(data => {
      document.querySelector("#name").innerHTML = data
    })
}

function generateDummy() {
  document.querySelector("#name").innerHTML = NAMES[Math.floor(Math.random() * NAMES.length)]
}
