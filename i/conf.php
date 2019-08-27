<?php
		// Domain for logon page
		$myDomain = 'industrybestpractice.com';

		// Database Connection Information
	
		$servername = "localhost";
		$username = "<username>";
		$password = "<password>";
		$dbname = "<db name>";
	
		$conn = new mysqli($servername,  $username,  $password, $dbname);
		
		if ($conn->connect_error) {
				die("Connection Failed: ". $conn->connect_error);
		
		}


?>