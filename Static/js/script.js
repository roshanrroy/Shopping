function increment() {
    let qtyInput = document.getElementById('quantity');
    let currentQty = parseInt(qtyInput.value);
    qtyInput.value = currentQty + 1;

    // Update the hidden field for form submission
    document.getElementById('cart-qty').value = qtyInput.value;
}

function decrement() {
    let qtyInput = document.getElementById('quantity');
    let currentQty = parseInt(qtyInput.value);
    if (currentQty > 1) {
        qtyInput.value = currentQty - 1;
    }

    // Update the hidden field for form submission
    document.getElementById('cart-qty').value = qtyInput.value;
}

