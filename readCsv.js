let csvToJson = require('covert-csv-to-json');

matches = csvToJson.fieldDelimiter(',').getJsonFromCsv('src/server/data/matches.csv');
deliveries = csvToJson.fieldDelimiter(',').getJsonFromCsv('src/server/data/deliveries.csv');


module.export = {
    deliveries : deliveries,
    matches : matches
};