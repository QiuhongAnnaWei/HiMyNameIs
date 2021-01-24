function generate() {
  const postParameters = {
    prefix: document.querySelector("#prefix").value,
    temperature: document.querySelector("#temperature").value/100
  };
  console.log("postParameters", postParameters)
  fetch('/generate', {
    method: "POST",
    body: JSON.stringify(postParameters),
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  .then(response => response.text())
  .then(data => {
    console.log(data)
    document.querySelector("#name").innerHTML = data
  })
  .catch(err => console.log(err))
}
