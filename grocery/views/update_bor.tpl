<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/add.css">
</head>
<body>
<h2>Update customers</h2>
<hr/>
<div class="center">
<form action="/updateb" method="post">
  <input type="hidden" name="id" value="{{cust_id}}"/>
  <p>Name: <input name="name" value="{{name}}"/></p>
  <p>email: <input name="email" value="{{email}}"/></p>
  <p>cust_id: <input name="id" value="{{id}}"/></p>
  <p><button type="submit">Submit</button></p>
</form>
</div>
<hr/>
</body>
</html>