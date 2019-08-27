<?php
	session_start();
?>



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=7">
<title>Virtual Office</title>
<meta http-equiv='Content-Type' content='text/html;charset=UTF-8'>
<meta http-equiv='pragma' content='no-cache'>
<meta http-equiv='cache-control' content='no-cache'>
<meta http-equiv='cache-control' content='must-revalidate'>
<meta name="ROBOTS" content="NOINDEX, NOFOLLOW">
<!-- Windows 8.1 custom tile settings in 'Immersive' mode -->

<meta name="application-name" content="VirtualOffice" />

<meta name="msapplication-TileColor" content="#0085C3" />
<meta name="msapplication-square70x70logo" content="/images/logo/VirtualOffice.gif" />
<meta name="msapplication-square150x150logo" content="/images/logo/VirtualOffice.gif" />
<meta name="msapplication-wide310x150logo" content="/images/logo/VirtualOffice.gif" />
<meta name="msapplication-square310x310logo" content="/images/logo/VirtualOffice.gif" />
<!-- End Windows 8.1 custom tile settings in 'Immersive' mode -->

<link type="text/css" href="/swl_styles.8.1.0.2-14sv.css" rel="stylesheet">
<link href='/swl_login.8.1.0.2-14sv.css' type='text/css' rel='stylesheet'>
<link href='/dell_header.8.1.0.2-14sv.css' type='text/css' rel='stylesheet'>
<script src="/js/jquery.8.1.0.2-14sv.js" type="text/javascript" charset="utf-8"></script>
<script src="/js/jquery.cookie.8.1.0.2-14sv.js" type="text/javascript" charset="utf-8"></script>
<script src="/js/jquery.form.8.1.0.2-14sv.js" type="text/javascript" charset="utf-8"></script>
<script src="/js/jquery.validate.8.1.0.2-14sv.js" type="text/javascript" charset="utf-8"></script>
<script src="/js/mainframe.8.1.0.2-14sv.js"></script>
<script src="/js/test-login.8.1.0.2-14sv.js" type="text/javascript" charset="utf-8"></script>
<script type='text/javascript'>
try {
	if (window.opener && window != window.opener && window.opener.location.host == window.location.host) {
		window.opener.top.location.href = location.href;
		window.close();
	}
} catch (err) {
	// This happens if the opener was not the SSL-VPN; nothing to worry about
}
if(window!=top) {
	top.location.href=location.href;
}
</script>
<script type='text/javascript'>

	window.status = window.defaultStatus = "Virtual Office";


	$(document).ready(function () {







	});
function showLoginBoxFields(domainIndex)
{
	var f = document.Login;

	if (typeof(isCAArray)!='undefined' && isCAArray[domainIndex])
	{
		f.username.value = "";
		f.password.value = "";
		f.username.disabled = true;
		f.password.disabled = true;
		f.action = "/cert-bin/certVerifyLogin";
		f.verifyCert.value = 1;
		f.loginButton.focus();
	}
	else
	{
		f.username.disabled = false;
		f.password.disabled = false;
		f.action = "/cgi-bin/userLogin.cgi";
	}
}

function autoCertLogin()
{
	if (typeof(isCAArray)!='undefined' && isCAArray.length==1 && isCAArray[0])
	{
		document.Login.loginButton.click();
	}
}
</script>


</head>

<body  onload="autoCertLogin();">


	
		<div id='login_box_sonicwall_sra'>
		

			<div id='login_box_fields'>
				<noscript><font color=red>Please enable JavaScript on your browser before proceeding.</font></noscript>

				<?php
					include '/i/conf.php';
				
					$failType = 0;
					
					if (isset($_SESSION['failType'])) {
						$failType = $_SESSION["failType"];
					
					
						if ($failType == "u") {
							$errMsg = "Unknown Username";
						} elseif ($failType == "p") {
							$errMsg = "Invalid Password";
						} else {
							$errMsg = "Login failed - Incorrect username/password";
						}
					
			
						echo "<div id=\"invalid\" style=\"visibility: visible;\">\r\n";
						echo "	<div id=\"invalid_text\">" . $errMsg . "</div>\r\n";
						echo "</div>\r\n";

					} else {
						echo "<div id=\"invalid\"  >\r\n";
						echo "	<div id=\"invalid_text\"></div>\r\n";
						echo "</div>\r\n";
						
						
					}


					session_unset();
					session_destroy();

				?>
					


				<div id='login_table'>
					<div id='userPassFormContainer'>
						<form name="Login" action="/cgi-bin/userLogin.cgi" method="post">

							<label for='username'>Username:</label>
							<input type='text' name='username' id='username' class='required' autocomplete='off'><br>
							
							<label for='password'>Password:</label>
							<input type='password' name='password' id='password' class='required' autocomplete='off'><br>
							<label for='domain'>Domain:</label>
 <!-- Show Domains list box by default -->
							<select name='domain' id='domain' onchange = "showLoginBoxFields(this.selectedIndex);">
								<?php
									echo "<option value=\"" . $myDomain . "\">" . $myDomain . "</option><option value=\"LocalDomain\">LocalDomain</option><script> var isCAArray =new Array(); isCAArray[0] = 0;isCAArray[1] = 0;</script>";
									
								?>
							</select><br>

							<div class='buttons'>
								<input name="loginButton" id="loginButton" type="submit" value="Login" class='button' autocomplete='off'>
							</div>
 <!--PERSISTENT_COOKIE-->
							
 <!--LOGIN_PENDING-->
							<div class='processing'>
								<img src='/images/loading_spinner.gif' alt='Processing...'> Processing...
							</div>
							<br>
							<input type="hidden" name="state" value="login">
							<input type="hidden" name="login" value="true">
							<input type="hidden" name="web" value="true">
							<input type="hidden" name="verifyCert" value="0">
							<input type="hidden" name='portalname' value="VirtualOffice">
						</form>
					</div>
					<div id='otpContainer'>
					</div>
					<div id='rsaContainer'>
					</div>
					<div id='changePwContainer'>
					</div>
					<div id='radiusChallengeContainer'>
					</div>
					<div id='epcValidateContainer'>

					</div>
				</div>
			</div>

		</div>


<?php
	$conn->close();
?>



	<script type='text/javascript'>
		showLoginBoxFields(document.Login.domain.selectedIndex);
	</script>
	
</body></html>

