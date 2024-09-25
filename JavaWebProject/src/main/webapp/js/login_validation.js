function validate() {
  let user = document.forms["login"]["username"].value;
  let pass = document.forms["login"]["password"].value;
  console.log(user);
  if (user == "" || pass == "") {
    alert("username and password can not be empty!");
    return false;
  }
  return true;
}