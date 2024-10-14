document.addEventListener("DOMContentLoaded", (event) => {
	
	// Contact Form 
	document.querySelector('#contactt').onsubmit = (event) => {
		event.preventDefault(); 
		let name = document.querySelector('#name').value;
		let email = document.querySelector('#email').value;
		let subject = document.querySelector('#subject').value;
		let message = document.querySelector('#message').value;
		let csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
		let h3 = '<h3>We appreciate your message! Expect a response from us soon.</h3>'
		
		fetch('/', {
			method: "POST",
			headers: {"X-CSRFToken": csrf},
			name: "name",
			body: JSON.stringify({
				name: "name",
				email: "email",
				subject: "subject",
				message: "message",
				
				})
		});
		
		document.querySelector('#contact').replaceWith(h3)
		// document.querySelector('#contact').style.display = 'none';
		
	};
  
});
