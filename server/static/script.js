function generate() {
  fetch("/generate", {
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
