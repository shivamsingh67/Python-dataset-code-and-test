const matchData = require('./readCsv');
// console.log(matchData);
function matchesPlayedPerYear(matchData) {

    let totalMatchPlayedPerYear = {};

    for (let index of matchData) {
        if (totalMatchPlayedPerYear[index["season"]]) {
            totalMatchPlayedPerYear[index["season"]] += 1;

        } 
        else {
            totalMatchPlayedPerYear[index["season"]] = 1;
        }
    }
    return totalMatchPlayedPerYear;
}

let answer = matchesPlayedPerYear(matchData.matches);

console.log(answer);
