<?php

	// Set this page to your apache 404 destination.  Page will track web scanning attempts to the scan table.

	include '/i/conf.php';
	
	$srcIP = $_SERVER['REMOTE_ADDR'];

	$URI = $_SERVER['REQUEST_URI'];
	
	$URI = $conn->real_escape_string($URI);
	
	$qString = "Insert Into scan (source,uri) VALUES ('" .  $srcIP . "', '" . $URI . "')";
	if ($conn->query($qString) === TRUE) {
		//echo "Added source to DB";
		
	} else {
		
		echo "Error inserting new src: " . $conn->error;
	}

?>

<html xmlns:v="urn:schemas-microsoft-com:vml">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>Page Not Found</title>
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="cache-control" content="must-revalidate">
<script src="/js/portalframe.8.1.0.2-14sv.js"></script>
<link href="/themes/styleblueblackgrey.8.1.0.2-14sv.css" rel="stylesheet" type="text/css">
</head>
<body class=loginbody leftmargin=0 topmargin=0 marginwidth=0 marginheight=0>
<center>
<img src="/images/shim.gif" height=100 width=8><BR>
<table width=430 border=0 margin=0 cellpadding=0 cellspacing=0>
<tr>
<td width=430>
<font class=loginError><B>Error:</b></font>
<font class=toolbar> The page you are trying to access is not available.</font>
<a href="JavaScript:history.back();" onMouseOver="window.status='Back'; return true" onMouseOut="window.status='';"><font class=toolbar style="color:#0106ee; onMouseOver="JavaScript:window.status='Back';"><u> Click here</u></font></a> <font class=toolbar>to go back.</font>
</td>
</tr>
</table>
</center>

