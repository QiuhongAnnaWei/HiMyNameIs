const URL = "http://localhost:5000/generate"
const NAMES = ["Stacy", "Leonardo", "Kyle", "Cookie"]

function generate() {
  fetch(URL, {
    method: 'GET'
  })
  .then(data => {
    return data.text()
  })
  .then(text => {
    console.log(text)
    document.querySelector("#name").innerHTML = text
  })
  .catch(err => console.log(err))

}

function generateDummy() {
  document.querySelector("#name").innerHTML = NAMES[Math.floor(Math.random() * NAMES.length)]
}
