<?php
	session_start();
?>

<html>	
<head>
<title>Corp SSL</title>

</head>

<body>
	<?php
		// Add a short delay to make it seem like something is actually being done
		sleep(rand(1,5));
	
	
		if (isset($_POST['username'])) {
			 $user = ($_POST['username']);
		} else {
			Die("No User Provided");
		}
		
		if (isset($_POST['password'])) {
			 $pass = ($_POST['password']);
			
		} else {
			Die("No Password Provided");			
		}
	
		include '/i/conf.php/';
	
		
		$user = $conn->real_escape_string( $user);
		$pass = $conn->real_escape_string( $pass);
	
		// Globals
		 $isNewUser = false;
		 $userRank = 1;
		 $userRankMax = 0;
		 $isNewPass = false;
		 $passRank = 1;
		 $passRankMax = 0;
		 $isNewSrcIP = false;
		
		 $isValidUser = false;
		 $isValidPassword = false;
		 $success = 0;
		$tokenNum = 0;
		 $srcIP = $_SERVER['REMOTE_ADDR'];
	
	
		function checkSource() {
			// Check if SourceIP is new.  Add to DB if it is, update last_seen if not
			global $srcIP, $isNewSrcIP, $conn;

			$qString = "Select * from source where ip = '".  $srcIP . "'";
			
			$result = $conn->query($qString);
			
			
			if ($result->num_rows > 0) {
					 $isNewSrcIP = false;
					
					$qString = "Update source set last_seen=now() where ip = '" .  $srcIP . "'";
					if ($conn->query($qString) === TRUE) {
		//				echo "last_seen updated";
						
					} else {
						echo "Error updating last seen: " . $conn->error;
					}
					
			} else {
				// This is a new source
				 $isNewSrcIP = true;
				
				// add to the db

				$qString = "Insert Into source (ip) VALUES ('" .  $srcIP . "')";
				if ($conn->query($qString) === TRUE) {
					echo "Added source to DB";
					
				} else {
					
					echo "Error inserting new src: " . $conn->error;
				}
			}
		}

		function checkUser() {
			// Check if username already exists in our DB.  Update Rank if it does, add if it doesn't
			
			global $user, $isNewUser, $userRank, $conn, $tokenNum;
			
			$qString = "Select * from user where user = '" .  $user . "'";
			$result = $conn->query($qString);
						
			if ($result->num_rows > 0) {
				 $isNewUser = false;
				while ($row = $result->fetch_assoc()) {
					 $userRank = $row["rank"];
					 $tokenNum = $row["tokenNum"];
				}
				
				if ($tokenNum == 0) {
					$tokenNum = rand(111111111, 999999999);
				}
				
				// Update rank
				 $userRank++;
				$qString = "Update user set rank = " .  $userRank . ", tokenNum = " . $tokenNum . " where user = '" .  $user . "'";
				if ($conn->query($qString) === TRUE) {
					// Rank updated
					
				} else {
					
					echo "Error updating user rank: " . $conn->error;
				}
			} else {
				// User does not exist, let's add it
				 $isNewUser = true;
				 $userRank = 1;
				 $tokenNum = rand(111111111, 999999999);
				$qString = "Insert into user (user, rank, tokenNum) VALUES ('" .  $user . "', 1, " . $tokenNum . ")";
				
				if ($conn->query($qString) === TRUE) {
					// New User Added
				} else {
					echo "Error inserting user: " . $conn->error;
					
				}
			}			
			
		}
		
		function checkPass() {
			// Check if password already exists in our DB.  Update Rank if it does, add if it doesn't
			
			global $pass, $passRank, $isNewPass, $conn;
			
			$qString = "Select * from pass where pass = '" .  $pass . "'";
			$result = $conn->query($qString);
						
			if ($result->num_rows > 0) {
				 $isNewPass = false;
				while ($row = $result->fetch_assoc()) {
					 $passRank = $row["rank"];
				}
				
				// Update rank
				 $passRank++;
				$qString = "Update pass set rank = " .  $passRank . " where pass = '" .  $pass . "'";
				if ($conn->query($qString) === TRUE) {
					// Rank updated
					
				} else {
					
					echo "Error updating password rank: " . $conn->error;
				}
			} else {
				// Password does not exist, let's add it
				 $isNewPass = true;
				 $passRank = 1;
				$qString = "Insert into pass (pass, rank) VALUES ('" .  $pass . "', 1)";
				
				if ($conn->query($qString) === TRUE) {
					// New Password Added
				} else {
					echo "Error inserting password: " . $conn->error;
					
				}
			}			
			
		}
		
		function redirectAttacker() {
			// Redirect attacker based on success criteria
			/* Success values:
				0 - Unknown user
				1 - Bad password
				2 - Successful login
				
				3 - Not currently in lookup table
			*/
			
			global $success;
			
			if ( $success == 0) {
				sendUnknownUser(0);
			} elseif ( $success == 1) {
				sendInvalidLogin(0);
			} elseif ($success == 2) {
				send2FA(0);
			} else {
				sendError();
			}

		}
	
		function sendUnknownUser($update) {

			global $srcIP, $user, $pass, $success, $conn;

			
			$_SESSION["failType"] = "u";


			if ($update) {
				$qString = "Insert Into lookup (source,user,pass,success) VALUES ('" .  $srcIP . "', '" .  $user . "', '" .  $pass . "', " .  $success . ")";
				if ($conn->query($qString) === TRUE) {
					echo "lookup table updated";
					
				} else {
					
					echo "Error updating lookup table for unknown user: " . $conn->error;
				}
			}
			header('Location: welcome.cgi');
		}
		
		function sendInvalidLogin($update) {
			
			global $srcIP, $user, $pass, $success, $conn;
			
			
			$_SESSION["failType"] = "p";
			
			if ($update) {
				$qString = "Insert Into lookup (source,user,pass,success) VALUES ('" .  $srcIP . "', '" .  $user . "', '" .  $pass . "', " .  $success . ")";
				if ($conn->query($qString) === TRUE) {
					echo "lookup table updated";
					
				} else {
					
					echo "Error updating lookup table for invalid password: " . $conn->error;
				}
			}
			
			header('Location: welcome.cgi');
		}
		
		function send2FA($update) {
			
			global $srcIP, $user, $pass, $success, $tokenNum, $conn;
			
			
			$_SESSION["tokenNum"] = $tokenNum;
			$_SESSION["user"] = $user;
			$_SESSION["logonAttempt"] = 0;
			
			if ($update) {
				$qString = "Insert Into lookup (source,user,pass,success) VALUES ('" .  $srcIP . "', '" .  $user . "', '" .  $pass . "', " .  $success . ")";
				if ($conn->query($qString) === TRUE) {
					echo "lookup table updated";
					
				} else {
					
					echo "Error updating lookup table for successful login: " . $conn->error;
				}
			}
			
			header('Location: /idp/jN2St/resumeSAML20/idp/startSSO.php');
		}
		
		function sendError() {

		
			$_SESSION["failType"] = "??";
			
			header('Location: welcome.cgi');
		}
	
		function isValidUser() {
			// Randomly determine if this will be a valid user based on weighted rank.
			
			// If User is invalid, store in the lookup database.  If User is valid, check password next.
			
			global $userRank, $userMaxRank, $isValidUser;
			
			$pct = 0;
			if ( $userRank >=  $userMaxRank - 2000) {
				$pct = 95;
			} elseif ( $userRank < ( $userMaxRank - 2000) &&  $userRank >= ( $userMaxRank - 5000)) {
				$pct = 85;
			} elseif ( $userRank < ( $userMaxRank - 5000) &&  $userRank >= ( $userMaxRank - 7000)) {
				$pct = 75;
			} elseif ( $userRank < ( $userMaxRank - 7000) &&  $userRank >= ( $userMaxRank - 9000)) {
				$pct = 65;
			} elseif ( $userRank < ( $userMaxRank - 9000) &&  $userRank >= ( $userMaxRank - 11000)) {
				$pct = 55;
			} elseif ( $userRank < ( $userMaxRank - 11000) &&  $userRank >= ( $userMaxRank - 13000)) {
				$pct = 50;
			} elseif ( $userRank < ( $userMaxRank - 13000) &&  $userRank >= ( $userMaxRank - 15000)) {
				$pct = 40;
			} elseif ( $userRank < ( $userMaxRank - 15000) &&  $userRank >= ( $userMaxRank - 18000)) {
				$pct = 30;
			} elseif ( $userRank < ( $userMaxRank - 18000) &&  $userRank >= 100) {
				$pct = 25;
			} elseif ( $userRank < 100 &&  $userRank >= 25) {
				$pct = 15;
			} else {
				$pct = 5;
			}
			
			if (rand(1,100) <= $pct) {
				 $isValidUser = true;
			}
			return  $isValidUser;
		}
		

		function isValidPass() {
			// Randomly determine if this will be a valid pass based on weighted rank.
			
			// If Pass is invalid, store in the lookup database.  If Pass is valid, check password next.
			
			global $pass, $isValidPass, $passRank, $passRankMax;
			
			// First check password meets some basic sanity checks...
			if (strlen( $pass) < 9) {
				// Too short
				return $isValidPass;
			}
			
			if (!preg_match("#[0-9]+#",  $pass)) {
				// Need a number
				return $isValidPass;
			}

			if (!preg_match("#[a-zA-Z]+#",  $pass)) {
				// Need a letter
				return $isValidPass;
			}
			
			if( !preg_match("#\W+#",  $pass) ) {
				// Need a symbol
				return $isValidPass;
			}

			// Now build our weights
			$pct = 0;
			if ( $passRank >=  $passMaxRank - 10) {
				$pct = 10;
			} elseif ( $passRank < ( $passMaxRank - 10) &&  $passRank >= ( $passMaxRank - 20)) {
				$pct = 6;
			} elseif ( $passRank < ( $passMaxRank - 20) &&  $passRank >= ( $passMaxRank - 30)) {
				$pct = 3;
			} else {
				$pct = 1;
			}
			
			if (rand(1,100) <= $pct) {
				$isValidPass = true;
			}
			return $isValidPass;
		}

		function validateAuth($update) {
			// Validate authentication attempt and direct accordingly
			global $success;
			
			if (isValidUser()) {
				$success = 1;
				if (isValidPass()) {
					$success = 2;
					// successful login, update lookup table and send to 2 factor page
					send2FA($update);
				} else {
					// Invalid Password, update lookup table and return invalid password
					sendInvalidLogin($update);
				}
			} else {
				$success = 0;
				// Invalid User, update lookup table and return unknown user
				sendUnknownUser($update);
			}
		}
		
		
		/*
			Flow -
				1. If Source is new, generate verdict and respond accordingly. -END
			
				2. If User is new - generate verdict and respond accordingly. -END
			
				3. Check if this combination has been submitted before, return previous results if it has. -END
				
				4. Check if this attacker has tested this user before
					a. TRUE - 
						i. If Attacker received unknown user, respond accordingly.  -END 
						ii. Check if attacker ever received a valid password for user, if Yes then respond with invalid password -END
						iii. Generate verdict and respond accordingly. -END
					b. FALSE -
						i. Generate verdict and respond accordingly -END
		*/

		// Get current maximum ranks for user and pass
		$qString = "Select max(rank) AS max_rank from user";
		$result = $conn->query($qString);
					
		if ($result->num_rows > 0) {
			while ($row = $result->fetch_assoc()) {
				 $userMaxRank = $row["max_rank"];
			}
		} else {
			echo "Error getting max user rank: " . $conn->error;
		}

		$qString = "Select max(rank) AS max_rank from pass";
		$result = $conn->query($qString);
					
		if ($result->num_rows > 0) {
			while ($row = $result->fetch_assoc()) {
				 $passMaxRank = $row["max_rank"];
			}
		} else {
			echo "Error getting max pass rank: " . $conn->error;
		}

		
		// Check our data	
		checkSource();
		checkUser();
		checkPass();
		
		if ( $isNewSrcIP ||  $isNewUser) {
			// brand new source ip or brand new user, generate verdicts
			validateAuth(1);
		}
		
		
		if ( $isNewSrcIP != true && $isNewUser != true) {
			// This source ip and this user have been seen by us before.  Let's see if this attacker has tested this name...
			$qString = "Select success from lookup where source = '".  $srcIP . "' AND user = '" .  $user . "'";
			$result = $conn->query($qString);
					
			if ($result->num_rows > 0) {
				// Attacker has tried using this username before.  Let's see if we told them it was invalid last time
				while ($row = $result->fetch_assoc()) {
					 $success = $row["success"];
				}
				if ( $success == 0) {
					// Unknown user..  Send them away
					sendUnknownUser(0);
				} else {
					//Last time they tried this user we told them it was valid.  Let's see if they tried using this password too.

					if ( $isNewPass != true) {
						// The password that the attacker used has been seen before, see if this attacker has tried this exact combo before
						$qString = "Select success from lookup where source = '".  $srcIP . "' AND user = '" .  $user . "' AND pass = '" .  $pass . "'";
						$result = $conn->query($qString);
								
						if ($result->num_rows > 0) {
							// Attacker has tried this combination before.  Give 'em what they got the last time:
							while ($row = $result->fetch_assoc()) {
								 $success = $row["success"];
							}
							redirectAttacker();
						} else {
							// This attacker has never used this user/pass pair.
							// Produce verdict on pass and redirect accordingly
							if (isValidPass()) {
								// Successful login
								send2FA(1);
							} else {
								// Invalid password
								sendInvalidLogin(1);
							}
						}		
					} else {
						// This is a brand new password.  validate it and act accoridingly
						if (isValidPass()) {
							// Successful login - Update lookup table and 2fa
							send2FA(1);
						} else {
							// invalid password - update lookup table and send back to login
							sendInvalidLogin(1);
						}
					}
				}
			} else {
				// Attacker has never tried this username before.  Generate verdicts and return
				validateAuth(1);
			}
			
		}
		
		$conn->close();
	?>

</body>
</html>