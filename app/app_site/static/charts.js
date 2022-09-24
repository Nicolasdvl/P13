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
            data.nodes.push({ id: tweet.id });
            temp.push(tweet.id);
        };

        if (tweet.hasOwnProperty("referenced_tweets_id")) {
            if (!(temp.includes(tweet.referenced_tweets_id))) {
                data.nodes.push({ id: tweet.referenced_tweets_id });
                temp.push(tweet.referenced_tweets_id);
            };
            data.edges.push({ from: tweet.id, to: tweet.referenced_tweets_id });
        };

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