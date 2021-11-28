let parent = document.getElementById("pane");
// Callback function to execute when mutations are observed
const callback = function(mutationsList, observer) {
    // Use traditional 'for loops' for IE 11
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList' && window.location.pathname.startsWith("/maps/dir/")) {
            try {
                register_co2button();
            } catch (e) {
                if (e instanceof TypeError) {
                    console.log("registering co2button unsuccsessfull");
                    return;
                }
            }
            try {
                register_options_observer(document.getElementById("pane").children[0].children[0].children[0].children[0].children[1]);
            } catch (e) {
                if (e instanceof TypeError) {
                    console.log("registering options unsuccsessfull");
                    return;
                }
            }
            observer.disconnect();
        }
    }
};

// Create an observer instance linked to the callback function
const observer = new MutationObserver(callback);

// Start observing the target node for configured mutations
observer.observe(parent, { childList: true });

function register_co2button() {
    parent = document.getElementById("pane").children[0].children[0].children[0].children[0].children[1];
    parent.insertAdjacentHTML('beforeEnd', `
        <div class="buttonpadding">
        <button class="greenbutton" id="addco2button">Add CO<sub>2</sub> Values</button>
        </div>
    `);
    addco2button.addEventListener("click", async() => {
        var from = location.pathname.split("/")[3];
        var to = location.pathname.split("/")[4];
        // var from = document.getElementById("directions-searchbox-0").children[0].children[0].children[0].value;
        // var to = document.getElementById("directions-searchbox-1").children[0].children[0].children[0].value;
        var time;

        if (location.href.includes("!8j")) {
            time = location.href.split("!8j")[1].split("!3e")[0];
        } else {
            time = Math.round(new Date().getTime() / 1000);
        }
        httpRequest = new XMLHttpRequest();
        let fueltype;
        chrome.storage.local.get(['fuel-type'], function(result) {
            if (result !== void 0) {
                fueltype = result["fuel-type"];
            }
        });
        url = "http://127.0.0.1:5000/route?origin=" + from +
            "&destination=" + to +
            "&departure_time=" + time +
            "&fuel_type=" + document.querySelector("#fuel-type").value;
        httpRequest.open('GET', url, true);
        httpRequest.onreadystatechange = addCo2;
        httpRequest.send();
        // addCo2();
    });
}

function addCo2() {
    if (httpRequest.readyState !== XMLHttpRequest.DONE) {
        return;
    }
    if (httpRequest.status !== 200) {
        alert('There was a problem with adding the CO2 values.');
    }
    let i = 0;
    let co2value = document.createElement("span");
    co2value.classList.add("co2value");
    co2value.style.marginLeft = "10px";
    co2value.style.color = "#5e5e5e";
    inputData = JSON.parse(httpRequest.responseText);
    while (true) {
        // Ok here we do some kind of hacky matching
        var title = document.getElementById("section-directions-trip-title-" + i);
        if (title == null) {
            break;
        }
        let bestMatch = 0;
        let mode = getMode();
        if (mode !== 'transit') {
            // Read the distance
            let distanceText = title.parentElement.parentElement.children[0].children[1].innerText;
            if (distanceText.includes("\n")) {
                distanceText = distanceText.split("\n")[1];
            }
            let distance;
            if (distanceText.includes("km")) {
                distance = parseFloat(distanceText.replace(" km", "")) * 1000;
            } else if (distanceText.includes("m")) {
                distance = parseInt(distanceText.replace(" m", ""));
            }
            //let diff = [];
            
            let diff = Math.abs(inputData[mode][0]["Total distance"]["0"] - distance);
            let bestDiff = diff;
            for (var j = 1; j < inputData[mode].length; j++) {
                diff = Math.abs(inputData[mode][j]["Total distance"]["0"] - distance);
                console.log(diff);
                if (diff < bestDiff) {
                    console.log(j + "is Best");
                    console.log(bestDiff);
                    bestMatch = j;
                    bestDiff = diff;
                    console.log(bestDiff);
                }
            }
        } else {
            let timeText = title.parentElement.children[0].children[0].innerText;
            let time = 0;
            if (timeText.includes(" hr")) {
                var splitted = timeText.split(" hr");
                time += parseInt(splitted[0] * 60 * 60);
                timeText = splitted[splitted.length - 1];
            } else if (timeText.includes("h")) {
                var splitted = timeText.split(" hr");
                time += parseInt(splitted[0] * 60 * 60);
                timeText = splitted[splitted.length - 1];
            }

            if (timeText.includes("min")) {
                time += parseInt(timeText.split("min")[0]) * 60;
            }


            let diff = Math.abs(inputData[mode][0]["Total duration"]["0"] - time);
            let bestDiff = diff;
            for (var j = 1; j < inputData[mode].length; j++) {
                diff = Math.abs(inputData[mode][j]["Total duration"]["0"] - time);
                console.log(diff);
                if (diff < bestDiff) {
                    console.log(j + "is Best");
                    console.log(bestDiff);
                    bestMatch = j;
                    bestDiff = diff;
                    console.log(bestDiff);
                }
            }
        }

        let text = Math.round(inputData[mode][bestMatch]["Total CO2"]["0"] * 100) / 100 + "g CO<sub>2</sub>";
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

function getMode() {
    switch (parseInt(document.querySelector("button[aria-checked=true]").parentElement.getAttribute("data-travel_mode"))) {
        case 0:
            return "driving";
        case 1:
            return "bicycling";
        case 2:
            return "walking";
        case 3:
            return "transit";
        default:
            return "";
    }
}