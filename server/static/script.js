function generate() {
  const postParameters = {
    prefix: document.querySelector("#prefix").value,
    temperature: document.querySelector("#temperature").value/100
  };
  console.log("postParameters", postParameters)
  fetch("/generate", {
    method: 'POST',
    headers:{'Content-Type': 'application/json'},
    body: JSON.stringify(postParameters)
  })
  .then(data => {
    console.log("data", data)
    console.log("data.json()", data.json())
    document.querySelector("#name").innerHTML = data.text()
  })
  .catch(err => console.log(err))
}
