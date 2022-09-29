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
};

function display_chart(div_id) {
    let chart = document.getElementById(div_id);
    let meta = document.getElementById(div_id + '_meta');
    let btn = document.getElementById(div_id + '_btn');
    if (chart.style.display == "none") {
        chart.removeAttribute("style");
        meta.removeAttribute("style");
        btn.setAttribute("class", "font-medium text-xs dark:text-blue-600");
    }
    else {
        chart.style.display = "none";
        meta.style.display = "none";
        btn.setAttribute("class", "font-medium text-xs text-gray-600 dark:text-white");
    };
}

