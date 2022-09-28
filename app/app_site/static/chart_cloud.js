

anychart.onDocumentReady(
    function drawCloud() {
        const tags = JSON.parse(JSON.parse(document.getElementById('cloud_json').textContent));
        var data = [];
        for (var key in tags) {
            data.push({ x: key, value: tags[key] });
        };
        var chart = anychart.tagCloud(data);
        chart.fromAngle(0);
        chart.toAngle(0);
        chart.listen("pointClick", function (e) {
            let search = document.getElementById("search_input");
            let submit = document.getElementById("search_submit");
            search.value = e.point.get("x");
            submit.click();
        });
        let container = document.createElement('div');
        container.className = "col-start-2 col-span-4 row-span-2"
        let div = document.createElement('div');
        div.id = "chartCloud";
        container.append(div);
        document.getElementById("grid-head").append(container);
        chart.container("chartCloud");
        chart.draw();
    }
);