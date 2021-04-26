
$(window).scroll(function () {
    const scroll = $(window).scrollTop();
    $('.banner-section').css({
        backgroundSize: 'calc(100vw + 50px + ' + scroll * 2 + 'px)'
    })
});

$("#ContactForm").on("submit", function (event) {
    event.preventDefault();
    const name = $("#name").val();
    const email = $("#email").val();
    const phone = $("#phone").val();
    const website = $("#website").val();
    const username = "e039e3ebb13a45f7b0c5964d23ccab1d";
    const password = "c12da6bcdc4ca15442eeec53513215e5"
    if (name === '' || email === '' || phone === '') {
        alert("Please Fill Required Fields");
    } else {
        $.ajax({
            type: "POST",
            url: "http://jmdigitalmarketingservices.herokuapp.com/api/email/send/",
            dataType: "json",
            headers: {
                "Authorization": "Basic " + btoa(username + ":" + password),
                "Content-Type": "application/json"
            },
            data: JSON.stringify({
                "from_email": "visitor@jmdigitalmarketingservices.com",
                "from_name": "Website Visitor",
                "to_email": "jackmel@hotmail.com",
                "to_name": "Melwyn D'Silva",
                "subject": "New Site Visitor",
                "text_body": "Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website,
                "html_body": "<p>Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website + "</p>",
            }),
            success: function () {
                $("#ContactForm")[0].reset();
                alert('Thanks for your response!');
            }
        });
    }
});

$("#ContactFormFooter").on("submit", function (event) {
    event.preventDefault();
    const name = $("#nameFooter").val();
    const email = $("#emailFooter").val();
    const phone = $("#phoneFooter").val();
    const website = $("#websiteFooter").val();
    const username = "e039e3ebb13a45f7b0c5964d23ccab1d";
    const password = "c12da6bcdc4ca15442eeec53513215e5"
    if (name === '' || email === '' || phone === '') {
        alert("Please Fill Required Fields");
    } else {
        $.ajax({
            type: "POST",
            url: "http://jmdigitalmarketingservices.herokuapp.com/api/email/send/",
            dataType: "json",
            headers: {
                "Authorization": "Basic " + btoa(username + ":" + password),
                "Content-Type": "application/json"
            },
            data: JSON.stringify({
                "from_email": "visitor@jmdigitalmarketingservices.com",
                "from_name": "Website Visitor",
                "to_email": "jackmel@hotmail.com",
                "to_name": "Melwyn D'Silva",
                "subject": "New Site Visitor",
                "text_body": "Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website,
                "html_body": "<p>Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website + "</p>",
            }),
            success: function () {
                $("#ContactFormFooter")[0].reset();
                alert('Thanks for your response!');
            }
        });
    }
});

