let car_options = `
    <div class="custom-options">
        <label for="fuel-type">Fuel type: </label>
        <select id="fuel-type" class="custom-select">
            <option value="benzin">Benzin E10</option>
            <option value="diesel">Diesel</option>
            <option value="natural gas">Erdgas</option>
            <option value="electric">Electric</option>
        </select>
    </div>

    <div class="custom-options">
        <label for="fuel-consumption">Fuel consumption per 100km:</label>
        <input id="fuel-consumption" class="custom-numberinput" type="number" value="5.0" step="1" min="0">
        <select id="fuel-consumption-type" class="custom-select">
            <option value="l">L</option>
            <option value="kg">Kg</option>
            <option value="kWh">kWh</option>
        </select>
    </div>
`;

let pedestrain_options = `
    <div class="custom-options">
        <label for="walking-distance">Maximum walking: </label>
        <input id="walking-distance" class="custom-numberinput" type="number" value="3.0" step="1" min="0">
        <select id="walking-distance-type" class="custom-select">
            <option value="km">km</option>
            <option value="min">min</option>
        </select>
    </div>
`;

let cycling_options = `
    <div class="custom-options">
        <label for="cycling-distance">Maximum cycling:  </label>
        <input id="cycling-distance" class="custom-numberinput" type="number" value="10.0" step="1" min="0">
        <select id="cycling-distance-type" class="custom-select">
            <option value="km">km</option>
            <option value="min">min</option>
        </select>
    </div>
`;


function register_options_observer(parent) {
    // Callback function to execute when mutations are observed
    var callback2 = function(mutationsList, observer) {
        for (const mutation of mutationsList) {
            if (mutation.type === 'childList') {
                register_options();
                observer.disconnect();
            }
        }
    };

    parent = parent.children[5];
    // Create an observer instance linked to the callback function
    const observer2 = new MutationObserver(callback2);

    // Start observing the target node for configured mutations
    observer2.observe(parent, { childList: true });
}

function register_options() {
    document.getElementsByClassName("directions-options-drive")[0].insertAdjacentHTML('beforeEnd', car_options);
    document.getElementsByClassName("directions-options-walk-bike")[0].insertAdjacentHTML('beforeEnd', pedestrain_options);
    document.getElementsByClassName("directions-options-walk-bike")[0].insertAdjacentHTML('beforeEnd', cycling_options);
    document.getElementsByClassName("directions-options-transit")[0].insertAdjacentHTML('beforeEnd', pedestrain_options);
    document.getElementsByClassName("directions-options-transit")[0].insertAdjacentHTML('beforeEnd', cycling_options);

    let fuel_type = document.getElementById("fuel-type");
    let fuel_consumption = document.getElementById("fuel-consumption");
    let fuel_consumption_type = document.getElementById("fuel-consumption-type");
    let walking_distance = document.getElementById("walking-distance");
    let walking_distance_type = document.getElementById("walking-distance-type");
    let cycling_distance = document.getElementById("cycling-distance");
    let cycling_distance_type = document.getElementById("cycling-distance-type");

    chrome.storage.local.get(['fuel-type'], function(result) {
        if (result !== void 0) {
            fuel_type.value = result["fuel-type"];
        }
    });

    chrome.storage.local.get(['fuel-consumption'], function(result) {
        if (typeof result !== void 0) {
            fuel_consumption.value = result["fuel-consumption"];
        }
    });

    chrome.storage.local.get(['fuel-consumption-type'], function(result) {
        if (result !== void 0) {
            fuel_consumption_type.value = result['fuel-consumption-type'];
        }
    });

    chrome.storage.local.get(['walking-distance'], function(result) {
        if (result !== void 0) {
            walking_distance.value = result['walking-distance'];
        }
    });

    chrome.storage.local.get(['walking-distance-type'], function(result) {
        if (result !== void 0) {
            walking_distance_type.value = result['walking-distance-type'];
        }
    });

    chrome.storage.local.get(['cycling-distance'], function(result) {
        if (result !== void 0) {
            cycling_distance.value = result['cycling-distance'];
        }
    });

    chrome.storage.local.get(['cycling-distance-type'], function(result) {
        if (result !== void 0) {
            cycling_distance_type.value = result['cycling-distance-type'];
        }
    });



    fuel_type.onchange = function() {
        chrome.storage.local.set({ "fuel-type": fuel_type.value }, {});
    };

    fuel_consumption.onchange = function() {
        chrome.storage.local.set({ "fuel-consumption": fuel_consumption.value }, {});
    };

    fuel_consumption_type.onchange = function() {
        chrome.storage.local.set({ "fuel-consumption-type": fuel_consumption_type.value }, {});
    };

    walking_distance.onchange = function() {
        chrome.storage.local.set({ "walking-distance": walking_distance.value }, {});
    };

    walking_distance_type.onchange = function() {
        chrome.storage.local.set({ "walking-distance-type": walking_distance_type.value }, {});
    };

    cycling_distance.onchange = function() {
        chrome.storage.local.set({ "cycling-distance": cycling_distance.value }, {});
    };

    cycling_distance_type.onchange = function() {
        chrome.storage.local.set({ "cycling-distance-type": cycling_distance_type.value }, {});
    };
}