document.addEventListener('DOMContentLoaded', function () {
    const productList = document.getElementById('productList');
    const modal = document.getElementById('productDetailsModal');
    const modalProductName = document.getElementById('modalProductName');
    const modalProductDescription = document.getElementById('modalProductDescription');
    const modalProductPrice = document.getElementById('modalProductPrice');
    const closeModal = document.getElementsByClassName('close')[0];

    productList.addEventListener('click', function (event) {
        if (event.target.classList.contains('showDetails')) {
            const productItem = event.target.closest('li');
            const productName = productItem.querySelector('h2').textContent;
            const productDescription = productItem.querySelector('p:nth-child(3)').textContent;
            const productPrice = productItem.querySelector('p:nth-child(4)').textContent;

            modalProductName.textContent = productName;
            modalProductDescription.textContent = productDescription;
            modalProductPrice.textContent = productPrice;

            modal.style.display = 'block';
        }
    });

    closeModal.onclick = function () {
        modal.style.display = 'none';
    };

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
});
