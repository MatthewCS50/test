document.addEventListener('DOMContentLoaded', () => {
	// if on the login page
	if(!localStorage.getItem("orders")) {
		var orders = []
		localStorage.setItem("orders", JSON.stringify(orders))
	}

	if (document.querySelector("#form")) {
		// when login form is submitted save username
		document.querySelector("#form").onsubmit = () => {
			let user = document.querySelector("#name").value;
			localStorage.setItem("current", user)
		}
	}

	// if user logs out remove username
	document.querySelector("#logout").addEventListener("click", () => {
		localStorage.removeItem("current");
	})

	// if user is logged in
	if (localStorage.getItem("current")) {
		var user = localStorage.getItem("current")

		// create items and price variables on first time
		if(!localStorage.getItem(user + "items")) {
			var items = [];
			localStorage.setItem(user + "items", JSON.stringify(items))
			localStorage.setItem(user + "price", "0")
		}

		// if user is on menu page
		if (document.querySelector("#menu")) {
			
			// select the form for each type of food 
			document.querySelectorAll(".order").forEach(function(form) {
				button = form.querySelector(".add-food")
				// when user adds food to shopping cart
				button.onclick = () => {
					// get existing shopping cart and total price
					var food = JSON.parse(localStorage.getItem(user + "items"))
					var cost = localStorage.getItem(user + "price")

					// find information about chosen option
					var e = form.querySelector(".select")
					var choice = e.options[e.selectedIndex].text;
					price = form.querySelector(".select").value
					
					// add chosen food to shopping cart list
					food.push(choice);

					// calculate total cost
					var bill = parseFloat(cost) + parseFloat(price)
					var total = bill.toFixed(2)

					// update user variables for shopping cart and total price
					localStorage.setItem(user + "items", JSON.stringify(food))
					localStorage.setItem(user + "price", total)
				}
			});
		}

		if (window.location.pathname == "/cart") {
			items = JSON.parse(localStorage.getItem(user + "items"))
			price = localStorage.getItem(user + "price")

			var i;
			for (i=0; i < items.length; i++) {
				item = items[i]
				var li = document.createElement('li');
				li.innerHTML = `${item}`
				//alert(li.innerHTML)

				document.querySelector('#items').append(li);
			}
			document.querySelector('#price').append(price)
		}

		if (window.location.pathname == "/orders") {
			orders = JSON.parse(localStorage.getItem("orders"))
			var i;
			for (i=0; i < orders.length; i++) {
				order = orders[i]
				items = JSON.parse(order.items)
				var li = document.createElement("li")
				li.innerHTML = `User: ${order.user}, Items: ${items}, Price: ${order.price}`

				document.querySelector("#placed").append(li)
			}
		}


		// works
		if (document.querySelector("#ordered")) {
			document.querySelector("#ordered").onclick = () => {
				orders = JSON.parse(localStorage.getItem("orders"))
				//place order
				order = {}
				order.user = user
				order.items = localStorage.getItem(user + "items")
				order.price = localStorage.getItem(user + "price")

				orders.push(order)

				localStorage.setItem("orders", JSON.stringify(orders))
				localStorage.removeItem(user + "items")
				localStorage.removeItem(user + "price")
			}
		}
	}
});