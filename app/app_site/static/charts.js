function dataForNetwork(conversation) {
    var nodes = [];
    var edges = [];
    var data = {
        nodes: nodes,
        edges: edges,
    };
    for (const tweet of conversation) {
        // TO DO : check if node already exist before push it.
        data.nodes.push({ id: tweet.id });
        data.nodes.push({ id: tweet.referenced_tweets });
        data.edges.push({ from: tweet.id, to: tweet.referenced_tweets });
    };

    return data;
};

anychart.onDocumentReady(function () {
    const conversations = JSON.parse(JSON.parse(document.getElementById('conversations_json').textContent));
    let i = 0;
    for (var key in conversations) {
        i++;
        let conversation = conversations[key];
        var data = dataForNetwork(conversation);
        var chart = anychart.graph(data);
        let div = document.createElement('div');
        div.id = "chart" + i;
        document.body.append(div);
        chart.container("chart" + i);
        chart.draw();
    };
});