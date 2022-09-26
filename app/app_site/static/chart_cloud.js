

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
        let div = document.createElement('div');
        div.id = "chartCloud";
        document.body.append(div);
        chart.container("chartCloud");
        chart.draw();
    }
);