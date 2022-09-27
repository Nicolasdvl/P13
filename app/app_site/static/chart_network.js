function dataForNetwork(conversation) {
    var nodes = [];
    var edges = [];
    var temp = [];
    var data = {
        nodes: nodes,
        edges: edges,
    };
    for (const tweet of conversation["tweets"]) {
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

anychart.onDocumentReady(
    function drawNetwork() {
        const conversations = JSON.parse(JSON.parse(document.getElementById('conversations_json').textContent));
        let i = 0;
        let div_meta_global = document.createElement('div');
        div_meta_global.innerHTML = "<h2>Représentations des réseaux de tweets sur le sujet : " + conversations["meta"]["query"] + "</h2>";
        div_meta_global.innerHTML += "<p> Enchantillon de " + conversations["meta"]["count_tweets"] + " tweets répartis sur " + conversations["meta"]["count_conversations"] + " conversations</p>"
        div_meta_global.innerHTML += "<p>Tweet le plus récent : " + conversations["meta"]["latest_date"] + "</p>";
        div_meta_global.innerHTML += "<p>Tweet le plus ancien : " + conversations["meta"]["earliest_date"] + "</p>";
        document.body.append(div_meta_global);
        for (var key in conversations) {
            if (key != "meta") {
                i++;
                let conversation = conversations[key];
                var data = dataForNetwork(conversation);
                var chart = anychart.graph(data);
                chart.nodes().tooltip().format("Tweet {%id}");
                chart.edges().tooltip().format("{%ref_type}");
                chart.title("Conversation" + key);
                let div = document.createElement('div');
                div.id = "chartNetwork" + i;
                document.body.append(div);
                chart.container("chartNetwork" + i);
                chart.draw();
                let div_meta = document.createElement('div');
                div_meta.innerHTML = "<h3> Représentation du réseau de tweets de la conversation " + key + "</h3>";
                div_meta.innerHTML += "<p>Echantillon : " + conversation["meta"]["count_tweets"] + " tweets</p>";
                div_meta.innerHTML += "<p>Tweet le plus récent : " + conversation["meta"]["latest_date"] + "</p>";
                div_meta.innerHTML += "<p>Tweet le plus ancien : " + conversation["meta"]["earliest_date"] + "</p>";
                document.body.append(div_meta);

            };
        };
    }
);