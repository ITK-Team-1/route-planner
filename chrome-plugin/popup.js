// When the button is clicked, inject setPageBackgroundColor into current page
addco2button.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: addCo2,
  });
});

window.onload = async function() {
  console.log("Hello");
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab.url.includes("google.com/maps")) {
    info.innerText = "This extension only works in Google Maps";
  }
}

// The body of this function will be executed as a content script inside the
// current page
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
