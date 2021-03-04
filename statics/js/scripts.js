$(window).scroll(function () {
    const scroll = $(window).scrollTop();
    $('.banner-section').css({
        backgroundSize: 'calc(100vw + 50px + ' + scroll * 2 + 'px)'
    })
});

$("#submitButton").on("click", function () {
    const name = $("#name").val();
    const email = $("#email").val();
    const phone = $("#phone").val();
    const website = $("#website").val();
    const username = "";
    const password = ""
    if (name === '' || email === '' || phone === '') {
        alert("Please Fill Required Fields");
    } else {
        $.ajax({
            type: "POST",
            url: "https://api.mailjet.com/v3.1/send",
            dataType: "json",
            headers: {
                "Authorization": "Basic " + btoa(username + ":" + password),
                "Content-Type": "application/json"
            },
            data: {
                "Messages": [
                    {
                        "From": {
                            "Email": "visitor@jmdigitalmarketingservices.com",
                            "Name": "Website Visitor"
                        },
                        "To": [
                            {
                                "Email": "support@jmdigitalmarketingservices.com",
                                "Name": "Support"
                            }
                        ],
                        "Subject": "Visitor",
                        "TextPart": "Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website,
                        "HTMLPart": "Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website
                    }
                ]
            },
            success: function () {
                $("#form")[0].reset();
                alert('Thanks for your response!');
            }
        });
    }
});

