 function judge() {
        var email = document.getElementById("id_email").value;
        var username = document.getElementById("id_username").value;
        var password = document.getElementById("id_password").value;
        var password_confirmation = document.getElementById("id_password_confirmation").value;
        var re =/^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        var reg=/^[a-zA-Z]+$/ ;
        if(!re.test(email)) {
            document.getElementById('error').innerText = "enter a valid email address.";
            return false;
        }
        else if (!reg.test(username)) {
            document.getElementById('error').innerText = "username has illegal characters.";
            return false;
        }
        else if (password.length < 6 || password_confirmation.length < 6) {
            document.getElementById('error').innerText = "password too short.";
             return false;
        }
        else if (password.length != password_confirmation.length ) {
            document.getElementById('error').innerText = "password mismatch.";
            return false;
        }

 }

 // function ljudge(){
 //        var email = document.getElementById("lemail").value;
 //        var re =/^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
 //        if(!re.test(email)) {
 //            document.getElementById('error').innerText = "Invalid email!";
 //            return false;
 //        }
 // }

 function p_judge(){
        var password = document.getElementById("id_password").value;
        var password_confirmation = document.getElementById("id_password_confirmation").value;
        if (password.length < 6 || password_confirmation.length < 6) {
            document.getElementById('error').innerText = "password too short.";
             return false;
        }
        else if (password.length != password_confirmation.length ) {
            document.getElementById('error').innerText = "password mismatch.";
            return false;
        }

 }