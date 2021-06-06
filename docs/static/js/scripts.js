window.addEventListener('load', function () {
    var contactFormFooter = document.getElementById('ContactFormFooter');
    var contactForm = document.getElementById('ContactForm');

    contactFormFooter.addEventListener("submit", handleContactFormFooter, false);
    contactForm.addEventListener("submit", handleContactForm, false);

    function handleContactFormFooter(event) {
        event.preventDefault();
        sendEmail('nameFooter', 'emailFooter', 'phoneFooter', 'websiteFooter')
    }

    function handleContactForm(event) {
        event.preventDefault();
        sendEmail('name', 'email', 'phone', 'website')
    }

    function sendEmail(nameID, emailID, phoneID, websiteID) {
        const name = document.getElementById(nameID).value;
        const email = document.getElementById(emailID).value;
        const phone = document.getElementById(phoneID).value;
        const website = document.getElementById(websiteID).value;
        const username = "e039e3ebb13a45f7b0c5964d23ccab1d";
        const password = "c12da6bcdc4ca15442eeec53513215e5"
        if (name === '' || email === '' || phone === '') {
            alert("Please Fill Required Fields");
        } else {
            fetch("https://jmdigitalmarketingservices.herokuapp.com/api/email/send/", {
                method: "POST",
                headers: {
                    "Authorization": "Basic " + btoa(username + ":" + password),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "from_email": "visitor@jmdigitalmarketingservices.com",
                    "from_name": "Website Visitor",
                    "to_email": "jackmel@hotmail.com",
                    "to_name": "Melwyn D'Silva",
                    "subject": "New Site Visitor",
                    "text_body": "Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website,
                    "html_body": "<p>Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website + "</p>",
                })
            })
                .then(function (res) {
                    contactFormFooter.reset();
                    console.log(res.statusText);
                    alert('Thanks for your response!');
                });
        }
    }

});