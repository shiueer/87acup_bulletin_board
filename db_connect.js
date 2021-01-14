var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "shiueer",
  password: "123456789",
  database: "87acup_board"
});

con.connect(function(err) {
  if (err) throw err;
  con.query("SELECT `Video` FROM video", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
});