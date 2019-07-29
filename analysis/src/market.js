const {readdirSync} = require('fs');
const DEFAULT_DATA_DIR = __dirname + '/../../data/';

const dataDir = (dir) => {
  const dataDir = dir || DEFAULT_DATA_DIR
  if(!dataDir.endsWith('/')) {
    dataDir += '/';
  }
  return dataDir;
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
