let userFormContainer = document.querySelector('.user-form');
let userForm = document.forms['manage-user-form'];
let cancelBtn = document.querySelector('.cancel');
let userId = userForm.uid;
let userName = userForm.uname;
let userPass = userForm.upass;
let userEmail = userForm.uemail;
let userPhone = userForm.uphone;
let userRole = userForm.urole;

function addUser() {
	userFormContainer.style.display = 'flex';
	userForm.action = 'AddUser'; 
	userId.value = '';
	userName.value = '';
	userPass.value = '';
	userEmail.value = '';
	userPhone.value = '';
	userRole.value = '';
}

cancelBtn.addEventListener('click', () => {
	userFormContainer.style.display = 'none';
})

window.onclick = function(event) {
	if (event.target == userFormContainer) {
		userFormContainer.style.display = 'none';
	}
}

function editUser(id) {
	userFormContainer.style.display = 'flex';
	userForm.action = 'EditUser';
	$.ajax({
		type: "POST",
		url: "GetUserInfo",
		data: {
			userId: id,
		},
		success: function(response) {
			console.log(response);
			userId.value = id;
			userName.value = response['username'];
			userPass.value = response['password'];
			userEmail.value = response['email'];
			userPhone.value = response['phone'];
			userRole.value = response['role'];
		}
	});
}