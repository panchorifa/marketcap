const {readdirSync} = require('fs');
const DEFAULT_DATA_DIR = __dirname + '/../../data/';

const dataDir = (dir) => {
  let d = dir || DEFAULT_DATA_DIR;
  if(!d.endsWith('/')) {
    d += '/';
  }
  return d;
};

const dataFilenames = (dir) => {
  const files = readdirSync(dir);
  return files.reverse();
};

const latestMarket = (dir) => {
  const dataDirectory = dataDir(dir);
  const filename = dataFilenames(dataDirectory)[0];
  const data = require(dataDirectory + filename);
  data.time = filename.substring(7, filename.length-5);
  return data;
};

module.exports = {
  latestMarket
};
