#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const toDoData = JSON.parse(body);
    const completedtask = {};
    toDoData.forEach((todo) => {
      if (todo.completed) {
        const id = todo.userId;
        completedtask[id] = (completedtask[id] || 0) + 1;
      }
    });
    console.log(completedtask);
  }
});
