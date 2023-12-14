<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/add.css">
</head>
<body>
<h2>Add a new item</h2>
<hr/>
<div class="center">
<form action="/add" method="post">
  <p>storeid: <input name="store_id"/></p>
  <p>prod_name: <input name="prod_name"/></p>
  <p>No of available items: <input name="price"/></p>
  <p><button type="submit">Submit</button></p>
</form>
</div>
<hr/>
</body>
</html>