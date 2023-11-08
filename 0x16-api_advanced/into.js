#!/usr/bin/node
const request = require("request");
const id = process.argv.slice(2);
const url = `https://www.reddit.com/r/${id[0]}/about.json`;
const headers = { "User-Agent": "custom" };

request({ url, headers }, (err, response, body) => {
    if (err) {
        return;
    }

    if (response.statusCode === 200) {
        const subreddit = JSON.parse(body).data;
        console.log(subreddit.subscribers);
    } else {
        console.log(NaN);
    }
});
