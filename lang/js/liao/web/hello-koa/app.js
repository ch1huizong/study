'use strict';

const Koa = require('koa2');
const app = new Koa();

app.use(async (ctx, next) => {
  await next();
  ctx.response.type = 'text/html';
  ctx.response.body = '<h1>Hello, Koa2!</h1>';
});

app.listen(3000);
console.log('app started at port 3000...');
