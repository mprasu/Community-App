	function firstnamevalidation()
		{
			var firstname=document.getElementById("fname").value;
			if(firstname!=='')
			{
				if(firstname.match(/^[A-Z][a-z]+$/))
				{
					if(firstname.length >= 3 && firstname.length <= 10)
					{
						document.getElementById('firstnamemessage').innerHTML=" ";
						return true;
					}
					else
					{
						document.getElementById('firstnamemessage').innerHTML="**firstname length should be 3 to 10 characters only";
					    return false;
					}


				}
				else
				{
					document.getElementById('firstnamemessage').innerHTML="**firstname should start with uppercase letter and remaining lowercase letters only but no numbers...";
					return false;
				}
			}
		    else
		    {
		    	document.getElementById('firstnamemessage').innerHTML="**please fill this field";
		    	return false;
		    }
		}

function lastnamevalidation()
		{
			var lastname=document.getElementById("lname").value;
			if(lastname!=='')
			{
				if(lastname.match(/^[a-z]+$/))
				{
					if(lastname.length >= 5 && lastname.length <= 15)
					{
						document.getElementById('lastnamemessage').innerHTML=" ";
						return true;
					}
					else
					{
						document.getElementById('lastnamemessage').innerHTML="**lastname length should be 5 to 15 characters only";
					    return false;
					}


				}
				else
				{
					document.getElementById('lastnamemessage').innerHTML="**lastname should have only lowercase letters but no numbers...";
					return false;
				}
			}
		    else
		    {
		    	document.getElementById('lastnamemessage').innerHTML="**please fill this field";
		    	return false;
		    }
		}


function usernamevalidation()
		{
			var username=document.getElementById("uname").value;
			if(username!=='')
			{
				if(username.match(/^[a-zA-Z]+\d+$/))
				{
					if(username.length >= 6 && username.length <= 15)
					{
						document.getElementById('usernamemessage').innerHTML=" ";
						return true;
					}
					else
					{
						document.getElementById('usernamemessage').innerHTML="**username length must be 6 to 15 characters only";
					    return false;
					}


				}
				else
				{
					document.getElementById('usernamemessage').innerHTML="**username should start with letter but no numbers and it should have atleast 1 number at the end of username...";
					return false;
				}
			}
		    else
		    {
		    	document.getElementById('usernamemessage').innerHTML="**please fill this field";
		    	return false;
		    }
		}


function phonevalidation()
		{
			var phonenumbermessage=document.getElementById("mobile").value;
			if(phonenumbermessage!=='')
			{
				if(phonenumbermessage.match(/^[1-9]+\d+$/))
				{
					if(phonenumbermessage.length == 8 || phonenumbermessage.length == 10)
					{
						document.getElementById('phonemessage').innerHTML=" ";
					    return true;
					}
					else
					{
						document.getElementById('phonemessage').innerHTML="**phonenumber length must be 8 or 10 digits only";
					    return false;
					}


				}
				else
				{
					document.getElementById('phonemessage').innerHTML="**phonenumber should not start with 0 and it should have digits only but not characters";
					return false;
				}
			}
		    else
		    {
		    	document.getElementById('phonemessage').innerHTML="**please fill this field";
		    	return false;
		    }
		}


function mailvalidation()
		{
			var mailvalue=document.getElementById("mail").value;
			var regularexpression=/^[a-zA-Z]+[\W]?[a-zA-Z]*[\w]+@[a-zA-Z]+.[a-zA-Z]{2,3}$/
			//^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$//
			if(mailvalue=='')
			{
				document.getElementById('emailmessage').innerHTML="**please fill this field";
		    	return false;
			}
			else if(mailvalue.search(/[0-9]/)==-1)
            	{
            		document.getElementById("emailmessage").innerHTML="**password should have atleast 1 digit";
                    return false;
                }
            else if(mailvalue.search(/[a-z]/)==-1)
            	{
            		document.getElementById("emailmessage").innerHTML="**password should have atleast 1 lowercase";
                    return false;
                }
            else if(mailvalue.search(/[!@\#\$]/)==-1)
            	{
            		document.getElementById("emailmessage").innerHTML="**password should have atleast 1 spl character";
                    return false;
                }
            else if(mailvalue.length <= 10 && mailvalue.length >=25)
            	{
            		document.getElementById("emailmessage").innerHTML="**mailid length should be between 10 to 25 characters only..";
                    return false;
                }
            if (!mailvalue.match(regularexpression))
                {
                	document.getElementById("emailmessage").innerHTML="**invalid mail";
                    return false;
                }
            else
            {
            	document.getElementById("emailmessage").innerHTML="";
                    return true;

            }
            }

 function passwordvalidation(){
			var password=document.getElementById("pass").value;
			var cpassword=document.getElementById("cpass").value;
			if(password=="")
				{
					document.getElementById("passwordmessage").innerHTML="**please fill this field";
			        return false;
			    }

            else if(password.search(/[0-9]/)==-1)
            	{
            		document.getElementById("passwordmessage").innerHTML="**password should have atleast 1 digit";
                    return false;
                }
            else if(password.search(/[A-Z]/)==-1)
            	{
            		document.getElementById("passwordmessage").innerHTML="**password should have atleast 1 uppercase";
                    return false;
                }
            else if(password.search(/[a-z]/)==-1)
            	{
            		document.getElementById("passwordmessage").innerHTML="**password should have atleast 1 lowercase";
                    return false;
                }
            else if(password.search(/[!@\#\$]/)==-1)
            	{
            		document.getElementById("passwordmessage").innerHTML="**password should have atleast 1 spl character";
                    return false;
                }
            else if(password.length <=10 && password.length >= 25)
            	{
            		document.getElementById("passwordmessage").innerHTML="**password length should be between 10 to 25 characters only..";
                    return false;
                }
            else
            {
            	document.getElementById("passwordmessage").innerHTML=" ";
                    return false;

            }

        }


 function confirmpasswordvalidation(){
 	var password=document.getElementById("pass").value;
	var cpassword=document.getElementById("cpass").value;
 	if(password!=cpassword)
            	{
            		document.getElementById("cpasswordmessage").innerHTML="**password are not same";
                    return false;
                }
            else
            	{
            		document.getElementById('cpasswordmessage').innerHTML=" ";
            		return true;
				}
 }

function gendervalidation()
		{
			alert("select any option in gender field...");
		return false;
		}





function castevalidation()
{
 alert("select any caste...");
		return false;
}

 function addressvalidation()
		{


			var add=document.getElementById("address").value;
			if(add!=="")
			    {
			    	if(add.match(/^[a-zA-Z0-9,-]+$/))
			    	{
			    		if(add.length>=5 && add.length<=100)
			    		{
			    			document.getElementById('addressmessage').innerHTML=" ";
			    		    return true;

			    		}
			    		else
			    		{
			    			document.getElementById('addressmessage').innerHTML="**address length should be in the range of 5-100 charcters only";
					        return false;
					    }

			    	}
			    	else
			    	{
			    		document.getElementById('addressmessage').innerHTML=" ";
			    		    return true;

			    	}

			    }
			else
				{
					document.getElementById("addressmessage").innerHTML="please fill this field";
			        return false;
			    }

        }


function districtvalidation(){
			alert("select any option in district field...");
		return false;}

function statevalidation(){
			alert("select any option in gender,district,state field...");
		return false;}


