document.body.style.backgroundColor = 'orange';


let parent = document.getElementById("section-directions-trip-0").parentElement;
parent.insertAdjacentHTML('afterBegin',
'<button class="greenbutton" id="addco2button" style="\
    border: none;\
    padding: 8px 32px;\
    text-align: center;\
    text-decoration: none;\
    display: inline-block;\
    font-size: 12px;\
    margin: 5px;\
    transition-duration: 0.4s;\
    cursor: pointer;\
    background-color: white;\
    color: black;\
    border: 2px solid #4CAF50;\
">Add CO<sub>2</sub> Values</button>');

addco2button.addEventListener("click", async () => {
    addCo2();
});

function addCo2() {
  let i = 0;
  let co2value = document.createElement("span");
  co2value.classList.add("co2value");
  co2value.style.marginLeft = "10px";
  co2value.style.color = "#5e5e5e";
  while (true) {
    var title = document.getElementById("section-directions-trip-title-" + i);
    if (title == null) {
      break;
    }
    let text = i + "Kg CO<sub>2</sub>";
    if (title.getElementsByClassName("co2value").length > 0) {
      title.getElementsByClassName("co2value")[0].innerHTML = text;
    } else {
      co2value.innerHTML = text;

      // We use this hack to be able to reuse the co2value var
      title.innerHTML += co2value.outerHTML;
    }
    i++;
  }
}