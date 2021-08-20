// Halvor, 18.07.2021, js injection on google search results
// pre something of chrome extension, idk cba making a better one, used with 'Custom JavaScript for websites'

let results = [...document.getElementsByClassName("g")]
let h3Results = []

// Remove some unwanted 'g's
for (let i = 0; i < results.length; i++) {
  if (results[i].className !== "g") {
    results.splice(i, 1)
  }
}

// Max length 9
if (results.length > 9) {
  results = results.slice(0,9)
}

// Create list of page titles
for (let el of results) {
  let firstNumber = 0
  let secondNumber = 0
  if (el.children.length > 1) {
    firstNumber = 1
  }
  if (el.children[firstNumber].children.length > 1) {
    secondNumber = 1
  }

  h3Results.push(el.children[firstNumber].children[secondNumber].children[0].children[0].children[1])
}

// Put number in front of page titles
for (let i = 0; i < h3Results.length; i++) {
  if (h3Results[i]) {
    h3Results[i].innerHTML = `<span style="color: red;">${i + 1}. </span>` + h3Results[i].innerHTML
  }
}

document.body.addEventListener("keypress", (e) => {
  // Check if is typing
  if (e.path[0].tagName.toLowerCase() === "input" || e.path[0].tagName.toLowerCase() === "textarea") {
    return
  }

  const num = e.code.substr(e.code.length - 1, 1)

  // Click link if key pressed is number (1-9)
  if (!isNaN(num) && +num !== 0) {
    h3Results[+num - 1].click()
  }
})