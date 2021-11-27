let parent = document.getElementById("section-directions-trip-0").parentElement;


parent.insertAdjacentHTML('afterBegin', `
<div class="buttonpadding">
<button class="greenbutton" id="addco2button">Add CO<sub>2</sub> Values</button>
</div>
`);

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
