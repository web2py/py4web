var app = Q.app();
var params = new URLSearchParams(window.location.search);
app.data.app = params.get('app');
app.data.dbname = params.get('dbname');
app.data.tablename = params.get('tablename');
app.start();
