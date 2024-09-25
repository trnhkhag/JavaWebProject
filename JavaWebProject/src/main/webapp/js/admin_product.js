let productForm = document.forms["manage-product-form"];
let confirmDeleteForm = document.forms["delete-confirm-form"];
let productDltConfirm = document.querySelector('.product-delete');
let productFormContainer = document.querySelector(".product-form");
let cancelBtn = document.querySelector('.cancel');
let productIdDelete = document.forms['delete-confirm-form'].pid;
let productId = document.forms['manage-product-form'].pid;
let productName = document.forms['manage-product-form'].pname;
let productPrice = document.forms['manage-product-form'].pprice;
let productStock = document.forms['manage-product-form'].pstock;
let productStatus = document.forms['manage-product-form'].pstatus;
let productBrand = document.forms['manage-product-form'].pbrand;
let productCategory = document.forms['manage-product-form'].pcategory;
let productDesc = document.forms['manage-product-form'].pdesc;
console.log(productName);

function addProduct() {
	productForm.action = "AddProduct";
	productFormContainer.style.display = "flex";
	productId.value = '';
	productName.value = '';
	productPrice.value = '';
	productStock.value = '';
	productStatus.value = '';
	productBrand.value = '';
	productCategory.value = '';
	productDesc.value = '';
}

cancelBtn.addEventListener('click', () => {
	productFormContainer.style.display = 'none';
})

function productEdit(id) {
	productForm.action = "EditProduct";
	productFormContainer.style.display = 'flex';
	$.ajax({
		type: "POST",
		url: "GetProductInfo",
		data: {
			productId: id,
		},
		success: function(response) {
			console.log(response);
			productId.value = id;
			productName.value = response["name"];
			productPrice.value = response["price"];
			productStock.value = response["stock"];
			productStatus.value = response["status"];
			productBrand.value = response["brand"];
			productCategory.value = response["cateId"];
			productDesc.value = response["desc"];
		}
	});
}

function productDelete(id) {
	productDltConfirm.style.display = 'flex';
	confirmDeleteForm.action = 'StopSelling';
	productIdDelete.value = id;
}

//product detail
let productDetail = document.querySelector('.product-detail');
let detailBtn = document.getElementsByClassName('bxs-detail');
let closeBtn = document.querySelector('.close');
for (let i = 0; i < detailBtn.length; i++) {
	detailBtn[i].addEventListener('click', () => {
		productDetail.style.display = 'flex';
	});
}
closeBtn.addEventListener('click', () => {
	productDetail.style.display = 'none';
});

//product delete

let deleteBtn = document.getElementsByClassName('bxs-trash');
let confirmDeletion = document.querySelector('.confirm');
let cancelDeletion = document.querySelector('.cancel-deletion');
confirmDeletion.addEventListener('click', () => {
	productDltConfirm.style.display = 'none';
});
cancelDeletion.addEventListener('click', () => {
	productDltConfirm.style.display = 'none';
});

window.onclick = function(event) {
	if (event.target == productFormContainer) {
		productFormContainer.style.display = 'none';
	}
	if (event.target == productDetail) {
		productDetail.style.display = 'none';
	}
	if (event.target == productDltConfirm) {
		productDltConfirm.style.display = 'none';
	}
}