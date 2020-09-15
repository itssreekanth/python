function trim(strVar){if(strVar.length>0)
{while(strVar.charAt(0)==" ")
strVar=strVar.substring(1,strVar.length);while(strVar.charAt(strVar.length-1)==" ")
strVar=strVar.substring(0,strVar.length-1);}
return strVar;}
function checkEmail(email)
{if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
{return(true);}
return false;}
var pop='';function openwin(nm,width,height){var name=nm;if(pop&&!pop.closed){pop.close();}
pop=eval("window.open('"+name+"', 'NewWIN', 'chrome[4], toolbar=no, left=5, top=5, width="+width+", height="+height+", directories=no, menubar=no, SCROLLBARS=yes, left=2, right=2')");if(!pop.opener)popUpWin.opener=self;}
function closewin()
{window.close();}
function textLimitCheck(thisArea,maxLength,msg)
{if(thisArea.value.length>maxLength)
{alert(maxLength+' characters limit. \rExcessive data will be truncated.');thisArea.value=thisArea.value.substring(0,maxLength);thisArea.focus();}
document.getElementById(msg).innerText=thisArea.value.length;}
function checkAnnounce(theForm)
{var email_to=theForm['email_to[0]'];var email_from=trim(theForm.email_from.value);var name_from=trim(theForm.name_from.value);email_to=trim(email_to.value);var email1=theForm['email_to[1]'];var email2=theForm['email_to[2]'];var email3=theForm['email_to[3]'];var email4=theForm['email_to[4]'];email1=trim(email1.value);email2=trim(email2.value);email3=trim(email3.value);email4=trim(email4.value);if(email_to.length==0)
{alert("Please enter your friend's e-mail!");document.catForm['email_to[0]'].focus();return false;}
if(checkEmail(email_to)==false)
{alert("Invalid e-mail address! Please re-enter.");document.catForm['email_to[0]'].select();return false;}
if(email1.length>0)
{if(checkEmail(email1)==false)
{alert("Invalid e-mail address! Please re-enter.");document.catForm['email_to[1]'].select();return false;}}
if(email2.length>0)
{if(checkEmail(email2)==false)
{alert("Invalid e-mail address! Please re-enter.");document.catForm['email_to[2]'].select();return false;}}
if(email3.length>0)
{if(checkEmail(email3)==false)
{alert("Invalid e-mail address! Please re-enter.");document.catForm['email_to[3]'].select();return false;}}
if(email4.length>0)
{if(checkEmail(email4)==false)
{alert("Invalid e-mail address! Please re-enter.");document.catForm['email_to[4]'].select();return false;}}
if(email_from.length==0)
{alert("Please enter your e-mail!");theForm.email_from.focus();return false;}
if(checkEmail(email_from)==false)
{alert("Invalid your e-mail! Please re-enter.");theForm.email_from.select();return false;}
if(name_from.length==0)
{alert("Please enter your name!");theForm.name_from.focus();return false;}
return true;}
function checkBabyName(theForm)
{var babyName=trim(theForm.babyName.value);var gender=theForm.gender;var sender_name=trim(theForm.sender_name.value);var sender_email=trim(theForm.sender_email.value);var req_imageCode=trim(theForm.req_imageCode.value);if(babyName.length==0)
{alert("Please enter name!");theForm.babyName.focus();return false;}
if(gender[0].checked==false&&gender[1].checked==false)
{alert("Please select gender!");theForm.gender[0].focus();return false;}
if(sender_name.length==0)
{alert("Please enter sender name!");theForm.sender_name.focus();return false;}
if(sender_email.length==0)
{alert("Please enter sender email!");theForm.sender_email.focus();return false;}
if(checkEmail(sender_email)==false)
{alert("Invalid your e-mail! Please re-enter.");theForm.sender_email.select();return false;}
if(req_imageCode.length==0)
{alert("Please enter image code!");theForm.req_imageCode.focus();return false;}
return true;}