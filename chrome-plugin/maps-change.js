// Register buttons and stuff after url change

let lastUrl = location.href;
let url_obeserver = new MutationObserver(() => {
    const url = location.href;
    if (url !== lastUrl && location.pathname.startsWith("/maps/dir/")) {
        lastUrl = url;
        onDirUrl();
        // url_obeserver.disconnect();
    }
})

url_obeserver.observe(document, { subtree: true, childList: true });

function onDirUrl() {
    if (document.getElementById("addco2button") === null) {
        try {
            register_co2button();
        } catch (e) {
            if (e instanceof TypeError) {
                console.log("registering co2button unsuccsessfull");
                return;
            }
        }
    }
    if (document.querySelector("#fuel-type") === null) {
        try {
            register_options();
        } catch (e) {
            if (e instanceof TypeError) {
                console.log("registering options unsuccsessfull");
                return;
            }
        }

    }
}