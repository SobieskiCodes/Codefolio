try {
    let fileName = require('../../.codespaces/shared/.env');
    console.log("file found");
  } catch (e) {
    console.log("sorry, file not found");
  }

  console.log('Current directory: ' + process.cwd());