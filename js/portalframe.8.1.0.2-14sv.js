
var agt=navigator.userAgent.toLowerCase();var is_ie=((agt.indexOf("msie")!=-1)&&(agt.indexOf("opera")==-1));var winpops1=0;var winpops2=0;var winpops3=0;var winpops4=0;var winpops5=0;var winpops6=0;var winpops=0;var heights=410;function no_error(){return true;}
function resizer(){window.onerror=no_error;if(parent.scrollTo)parent.scrollTo(0,0);parent.resizeme(0);heights=document.body.scrollHeight;if(100>heights){setTimeout("resizerwait()",1000);}
if(heights==null){setTimeout("resizerwait()",1000);}
parent.resizeme(heights);}
function resizerwait(){heights=document.body.scrollHeight;if(100>heights){heights=460;}
if(heights==null){heights=460;}
parent.resizeme(heights);}
var strftptitle='FTP&nbsp;Session';var strftprename='Rename&nbsp;FTP&nbsp;Files';var strftpupload='Upload&nbsp;FTP&nbsp;Files';var strmycert='Current&nbsp;Certificates';var strviewcert='General&nbsp;&#187;&nbsp;View&nbsp;Certificates';var strnetworktools='Network&nbsp;Tools';var strbookmarks='Bookmarks';var strsettings='Settings';var strnetplaces='My&nbsp;Network&nbsp;Places';var strrestart='General&nbsp;&#187;&nbsp;Restart';var strtcptunneling='Access&nbsp;&#187;&nbsp;TCP&nbsp;Tunneling';var strstatus='General&nbsp;&#187;&nbsp;Status';var straddbookmarks='Add&nbsp;Bookmarks';var straddbookmark='Add&nbsp;Bookmark';var streditbookmark='Edit&nbsp;Bookmark';var strmydesktop='My&nbsp;Desktop';var strapplications='Applications';var strssslvpnclient='NetExtender';var blogin='Login';var bdeletemarked='Delete&nbsp;Marked';var titlestring=0;var bsubmit='Submit';var baddbookmark='Add&nbsp;Bookmark';var bcancel='Cancel';var benter='Enter';var brename='Rename';var agent=navigator.userAgent.toLowerCase();var browser=navigator.appName;var version=navigator.appVersion;function title(titlestring){document.write('<font  class="headingstylenomargin">&nbsp;'+titlestring+'&nbsp;</font>');}
function button(buttonstring){document.write('<font class=buttons>&nbsp;&nbsp;'+buttonstring+'&nbsp;&nbsp;</font>');}
function bbutton(buttonstring){document.write('<font class=bbuttons>&nbsp;'+buttonstring+'&nbsp;</font>');}
function bbutton2(buttonstring,titlename){if(agent.indexOf("msie")!=-1){document.write('<font class=bbuttons>&nbsp;'+buttonstring+'&nbsp;</font>');}
else{document.write('<a href="JavaScript:void();" title="'+titlename+'"><font class=bbuttons>&nbsp;'+buttonstring+'&nbsp;</font></a>');}}
function closechildren(){if(winpops!=0){if(!winpops.closed)winpops.close();}
if(winpops1!=0){if(!winpops1.closed)winpops1.close();}
if(winpops2!=0){if(!winpops2.closed)winpops2.close();}
if(winpops3!=0){if(!winpops3.closed)winpops3.close();}
if(winpops4!=0){if(!winpops4.closed)winpops4.close();}
if(winpops5!=0){if(!winpops5.closed)winpops5.close();}
if(winpops6!=0){if(!winpops6.closed)winpops6.close();}}
docObj=(document.all)?"document.all.":"document.";var thisRow;var thisRow1;function chgColor(rowNum){thisRow1=eval('"row" + rowNum + "Class"');document.getElementById(thisRow1).className='OnRowStyle2';}
function chgColorOut(rowNum){thisRow1=eval('"row" + rowNum + "Class"');document.getElementById(thisRow1).className='OddRowStyle2';}
function chgeven(rowNum){thisRow1=eval('"row" + rowNum + "Class"');document.getElementById(thisRow1).className='OnRowStyle2';}
function chgevenOut(rowNum){thisRow1=eval('"row" + rowNum + "Class"');document.getElementById(thisRow1).className='EvenRowStyle2';}
function chgmenu(rowNum){thisRow=eval(docObj+"row"+rowNum+"Class");thisRow.bgColor="#afafaf";}
function chgmenuOut(rowNum){thisRow=eval(docObj+"row"+rowNum+"Class");thisRow.bgColor="#eeebe9";}
function parseLoginHref(href)
{var loginUrl="";for(var i=0;i<href.length;i++)
{if(href.charAt(i)=='?')
return loginUrl;else
loginUrl+=href.charAt(i);}
return loginUrl;}
function nothing(){;}