function dataForNetwork(conversation) {
    var nodes = [];
    var edges = [];
    var temp = [];
    var data = {
        nodes: nodes,
        edges: edges,
    };
    for (const tweet of conversation) {
        // TO DO : check if node already exist before push it.
        if (!(temp.includes(tweet.id))) {
            data.nodes.push({ id: tweet.id, group: tweet.author_id });
            temp.push(tweet.id);
        };

        if (tweet.hasOwnProperty("referenced_tweets_id")) {
            if (!(temp.includes(tweet.referenced_tweets_id))) {
                data.nodes.push({ id: tweet.referenced_tweets_id });
                temp.push(tweet.referenced_tweets_id);
            };
            data.edges.push({ from: tweet.id, to: tweet.referenced_tweets_id, ref_type: tweet.referenced_tweets_type });
        };

    };

    return data;
};


function drawNetwork() {
    const conversations = JSON.parse(JSON.parse(document.getElementById('conversations_json').textContent));
    let i = 0;
    for (var key in conversations) {
        i++;
        let conversation = conversations[key];
        var data = dataForNetwork(conversation);
        var chart = anychart.graph(data);
        chart.nodes().tooltip().format("Tweet {%id} by {%group}");
        chart.edges().tooltip().format("{%ref_type}");
        let div = document.createElement('div');
        div.id = "chartNetwork" + i;
        document.body.append(div);
        chart.container("chartNetwork" + i);
        chart.draw();
    };
};

anychart.onDocumentReady(function () {
    const tags = JSON.parse(JSON.parse(document.getElementById('cloud_json').textContent));
    var data = [];
    for (var key in tags) {
        data.push({ x: key, value: tags[key] });
    };
    var chart = anychart.tagCloud(data);
    let div = document.createElement('div');
    chart.fromAngle(0);
    chart.toAngle(0);
    chart.listen("pointClick", function (e) {
        let search = document.getElementById("search_input");
        let submit = document.getElementById("search_submit");
        search.value = e.point.get("x");
        submit.click();
    });
    div.id = "chartCloud";
    document.body.append(div);

    chart.container("chartCloud");

    chart.draw();

});