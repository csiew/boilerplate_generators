import express from 'express';

var app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true, }));

app.get('/', function (req, res) {
  res.send('Hey there, we are trying to learn node js with express.');
});
app.get('/test', function (req, res) {
  res.send('This is test url.');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});