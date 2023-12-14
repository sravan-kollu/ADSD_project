<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/list.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
<h1></h1>
<br>
<h2>store</h2>
<div class="store">
<table >
    <tr>
      <th>S.no</th>
      <th>product Name</th>
      <th>Available stock</th>
    </tr>
    <tr>
    %for item in store:
    <tr>
      <td>{{item['store_id']}}</td>
      <td>{{item['prod_name']}}</td>
      <td>{{item['price']}}</td>
      
      <td><a href="/delete/{{str(item['store_id'])}}">Delete</a></td>
      <td><a href="/update/{{str(item['store_id'])}}"> Update</a></td>
    </tr>
    %end
    </tr>
</table>

<a href="/add">Add new item</a>
</div>
<br>
<h2>customers</h2>
<div class="customers">
  <form class="example" action="/search" method="post">
    <label for="search_query">Search:</label>
        <input type="text" id="search_query" name="search_query" placeholder="Search by item name...">
    <button type="submit"><i class="fa fa-search"></i></button>
  </form>
  <table >
      <tr>
        <th>cust_Id</th>
        <th>Name</th>
        <th>Email</th>
        <th>phone no</th>
        <th>store id</th>
      </tr>
      <tr>
      %for n in customers:
      <tr>
        <td>{{n['cust_id']}}</td>
        <td>{{n['name']}}</td>
        <td>{{n['email']}}</td>
        <td>{{n['ph_no']}}</td>
        <td>{{n['id']}}</td>
        <td><a href="/deletebor/{{str(n['cust_id'])}}">Delete</a></td>
        <td><a href="/updateb/{{str(n['cust_id'])}}"> Update</a></td>

      </tr>
      %end
     
      </tr>  
  </table>
   <a href="/addb">Add new customer</a>
  </div>
<hr/>
</body>
</html>