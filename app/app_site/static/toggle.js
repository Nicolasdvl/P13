function toggle() {
    let bar = document.getElementById("side-bar");
    let children = bar.children;
    if (bar.style.display == "none") {
        for (let child of children) {
            child.removeAttribute("style");
        }
        bar.removeAttribute("style");
    }
    else {
        for (let child of children) {
            child.style.display = "none";
        }
        bar.style.display = "none";
    };
}

