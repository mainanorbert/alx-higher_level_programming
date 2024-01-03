#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const toDoData = JSON.parse(body);
    const completedData = toDoData.reduce((acc, todo) => {
      if (todo.completed) {
        acc[todo.userId] = (acc[todo.userId] || 0) + 1;
      }
      return acc;
    }, {});
  }
});
