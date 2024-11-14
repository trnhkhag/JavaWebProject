function validateFilter() {
    // Get the min and max price values
    const minPrice = parseFloat(document.querySelector('input[name="minPrice"]').value);
    const maxPrice = parseFloat(document.querySelector('input[name="maxPrice"]').value);

    // Check if min price or max price is negative
    if (minPrice < 0 || maxPrice < 0) {
        Swal.fire({
            icon: 'error',
            title: 'Invalid Price',
            text: 'Price values cannot be negative.',
        });
        return false; // prevent form submission
    }

    // Check if min price is greater than max price
    if (minPrice > maxPrice) {
        Swal.fire({
            icon: 'error',
            title: 'Invalid Price Range',
            text: 'Min price cannot be greater than Max price.',
        });
        return false; // prevent form submission
    }

    // If validation passed, allow form submission
    return true;
}
