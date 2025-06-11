// document.addEventListener("DOMContentLoaded", function () {
//     const unitPrice = parseFloat(document.getElementById("price").dataset.unitPrice);

  
//     function changeQuantity(change) {
//         const quantityInput = document.getElementById("quantity");
//         let currentValue = parseInt(quantityInput.value);
//         let newValue = currentValue + change;
//         if (newValue >= 1) {
//           quantityInput.value = newValue;
//           document.getElementById("quantity-form").submit(); // Auto-submit on change
//         }
//       }

//     function updatePrice() {
//         const qty = parseInt(document.getElementById("quantity").value) || 1;
//         const total = (unitPrice * qty).toFixed(2);
//         document.getElementById("price").innerText = `${total} rs`;
//     }
//     function changeQuantity(change) {
//         const quantityInput = document.getElementById("quantity");
//         let currentValue = parseInt(quantityInput.value);
//         let newValue = currentValue + change;
    
//         if (newValue >= 1) {
//           quantityInput.value = newValue;
//           document.getElementById("quantity-form").submit();  // auto-submit
//         }
//       }
    

//     // Attach functions to global scope so HTML buttons can access them
//     window.changeQuantity = changeQuantity;
//     window.updatePrice = updatePrice;

// });


document.addEventListener("DOMContentLoaded", function () {
  window.changeQuantity = function (button, change) {
    const form = button.closest(".quantity-form");
    const quantityInput = form.querySelector(".quantity-input");
    const priceElement = form.querySelector(".price");
    let currentValue = parseInt(quantityInput.value);
    let newValue = currentValue + change;

    if (newValue >= 1) {
      quantityInput.value = newValue;

      // Update price display only
      const unitPrice = parseFloat(priceElement.dataset.unitPrice);
      const total = (unitPrice * newValue).toFixed(2);
      priceElement.innerText = `${total} rs`;

      // ❌ Don't submit the form here
      // form.submit();  <-- remove or comment this line
    }
  };
});





// function syncQuantity(orderForm) {
//   const cartItem = orderForm.closest(".cart-item");
//   const quantityInput = cartItem.querySelector(".quantity-input");
//   const hiddenQuantity = orderForm.querySelector(".sync-quantity");
  
//   hiddenQuantity.value = quantityInput.value;
// }

// document.addEventListener("DOMContentLoaded", function () {
//   window.changeQuantity = function (button, change) {
//     const form = button.closest(".quantity-form");
//     const quantityInput = form.querySelector(".quantity-input");
//     const priceElement = form.querySelector(".price");
//     let currentValue = parseInt(quantityInput.value);
//     let newValue = currentValue + change;

//     if (newValue >= 1) {
//       quantityInput.value = newValue;

//       // Update price
//       const unitPrice = parseFloat(priceElement.dataset.unitPrice);
//       const total = (unitPrice * newValue).toFixed(2);
//       priceElement.innerText = `${total} rs`;

//       // Submit quantity update form
      
//     }
//   };
// });











// new

// document.addEventListener("DOMContentLoaded", function () {
//   window.changeQuantity = function (button, change) {
//     const form = button.closest("form");
//     const quantityInput = form.querySelector(".quantity-input");
//     let currentValue = parseInt(quantityInput.value);
//     let newValue = currentValue + change;

//     if (newValue >= 1) {
//       quantityInput.value = newValue;

//       // ✅ Update price
//       const priceElement = form.querySelector(".price");
//       if (priceElement) {
//         const unitPrice = parseFloat(priceElement.dataset.unitPrice);
//         if (!isNaN(unitPrice)) {
//           const total = (unitPrice * newValue).toFixed(2);
//           priceElement.innerText = `${total} rs`;
//         }
//       }

//       // form.submit(); // Or remove this if you're debugging
//     }
//   };
// });







// document.addEventListener("DOMContentLoaded", function () {
//   window.changeQuantity = function(button, change) {
//       const form = button.closest("form"); // Get the closest form
//       const quantityInput = form.querySelector(".quantity-input");
//       let currentValue = parseInt(quantityInput.value);
//       let newValue = currentValue + change;

//       if (newValue >= 1) {
//           quantityInput.value = newValue;

//           // Update the price if there's a price element inside this form
//         const priceElement = form.querySelector(".price");
//         if (priceElement) {
//           const unitPrice = parseFloat(priceElement.dataset.unitPrice);
//             if (!isNaN(unitPrice)) {
//               const total = (unitPrice * newValue).toFixed(2);
//               priceElement.innerText = `${total} rs`;
//         }
//       }

//           form.submit();  // Submit only this form
//       }
//   };
// });









































  // document.addEventListener("DOMContentLoaded", function () {
  //   const quantityInput = document.getElementById("quantity");
  //   const priceElement = document.getElementById("price");
  //   const unitPrice = parseFloat(priceElement.dataset.unitPrice);

  //   window.changeQuantity = function(change) {
  //     let currentValue = parseInt(quantityInput.value);
  //     let newValue = currentValue + change;

  //     if (newValue >= 1) {
  //       quantityInput.value = newValue;
  //       updatePrice();
  //       document.getElementById("quantity-form").submit(); // Auto-submit
  //     }
  //   }

  //   function updatePrice() {
  //     const qty = parseInt(quantityInput.value) || 1;
  //     const total = (unitPrice * qty).toFixed(2);
  //     priceElement.innerText = `${total} rs`;
  //   }
  // });












































  // function changeQuantity(change) {
    //     const input = document.getElementById("quantity");
    //     let value = parseInt(input.value) || 1;
    //     value = Math.max(1, value + change);
    //     input.value = value;
    //     updatePrice();
    // }