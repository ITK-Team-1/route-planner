let registered = false;

// Register buttons and stuff after url change

let lastUrl = location.href; 
let url_obeserver = new MutationObserver(() => {
  const url = location.href;
  if (url !== lastUrl && location.pathname.startsWith("/maps/dir/")) {
    lastUrl = url;
    onDirUrl();
    url_obeserver.disconnect();
  }
})

url_obeserver.observe(document, {subtree: true, childList: true});

function onDirUrl() {
    if (!registered  
    && document.getElementById("addco2button") === null  
    && document.getElementById("fuel-type") === null ) {
        register_co2button();
        register_options();
        registered = true;
    }
}