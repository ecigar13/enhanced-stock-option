// user OAuth module

var oauth = require('oauth');

console.log("Imported all modules.");

var credentials = {
    /* Replace your own keys here */
    oauth_version: "1.0",
    api_url: "https://api.tradeking.com/v1",
    api_stream: "https://stream.tradeking.com/v1/",
    consumer_key: "keyHere",
    consumer_secret: "keyHere",
    access_token: "keyHere",
    access_secret: "keyHere"
};

/* Make a request to the API endpoint
 Manually update the access token/secret as parameters.  Typically this would be done through an OAuth callback when 
 authenticating other users.
 */
var tradeking_consumer = new oauth.OAuth(
    "https://developers.tradeking.com/oauth/request_token",
    "https://developers.tradeking.com/oauth/access_token",
    credentials.consumer_key,
    credentials.consumer_secret,
    credentials.oauth_version,
    "http://mywebsite.com/tradeking/callback",
    "HMAC-SHA1");


var querystring = require('querystring');

var urlQuery = new URLSearchParams([
    ['symbol', 'NXPI'],
    ['query', 'xdate-gte:20180501']
]);

url = credentials.api_url + '/market/options/search.json?' + urlQuery.toString();
var optionResult;
tradeking_consumer.get(url, credentials.access_token, credentials.access_secret,
    function (error, data, response) {
        if (!error && response.statusCode < 400) {
            // Parse the JSON data
            optionResult = JSON.parse(data);
            // Display the response
        } else {
            console.log("Got nothing.");
            console.log(error);
            console.log(response.toString());
        }
        //console.log(JSON.stringify(optionResult, null, 2));
    }
);




console.log("End program.");

console.log(url)
