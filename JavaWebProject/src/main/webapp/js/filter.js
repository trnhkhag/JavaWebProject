function validateFilter() {
    // Get the min and max price values
    const minPriceValue = document.querySelector('input[name="minPrice"]').value.trim();
    const maxPriceValue = document.querySelector('input[name="maxPrice"]').value.trim();

    // Check if min price or max price is null or empty
    if (minPriceValue === "" || maxPriceValue === "") {
        Swal.fire({
            icon: 'error',
            title: 'Missing Input',
            text: 'Both Min Price and Max Price are required.',
        });
        return false; // prevent form submission
    }

    // Parse the price values to numbers
    const minPrice = parseFloat(minPriceValue);
    const maxPrice = parseFloat(maxPriceValue);

    // Check if min price or max price is not a number
    if (isNaN(minPrice) || isNaN(maxPrice)) {
        Swal.fire({
            icon: 'error',
            title: 'Invalid Input',
            text: 'Both Min Price and Max Price must be valid numbers.',
        });
        return false; // prevent form submission
    }

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
