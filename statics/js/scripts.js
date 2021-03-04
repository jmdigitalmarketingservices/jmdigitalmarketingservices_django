$(window).scroll(function () {
    const scroll = $(window).scrollTop();
    $('.banner-section').css({
        backgroundSize: 'calc(100vw + 50px + ' + scroll * 2 + 'px)'
    })
});

// $("#submitButton").on("click", function () {
//     const name = $("#name").val();
//     const email = $("#email").val();
//     const phone = $("#phone").val();
//     const website = $("#website").val();
//     const username = "57c0ef882a9d275b73efd242f60b2458";
//     const password = "6b452c1d00684460267e8c4e0e0c16a5"
//     if (name === '' || email === '' || phone === '') {
//         alert("Please Fill Required Fields");
//     } else {
//         $.ajax({
//             type: "POST",
//             url: "https://api.mailjet.com/v3.1/send",
//             dataType: "json",
//             headers: {
//                 "Authorization": "Basic " + btoa(username + ":" + password),
//                 "Content-Type": "application/json"
//             },
//             data: JSON.stringify({
//                 "Messages": [
//                     {
//                         "From": {
//                             "Email": "visitor@jmdigitalmarketingservices.com",
//                             "Name": "Website Visitor"
//                         },
//                         "To": [
//                             {
//                                 "Email": "support@jmdigitalmarketingservices.com",
//                                 "Name": "Support"
//                             }
//                         ],
//                         "Subject": "Visitor",
//                         "TextPart": "Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website,
//                         "HTMLPart": "Email: " + email + ", Name: " + name + ", Phone: " + phone + ", website: " + website
//                     }
//                 ],
//                 "SandboxMode": true
//             }),
//             success: function () {
//                 $("#form")[0].reset();
//                 alert('Thanks for your response!');
//             }
//         });
//     }
// });

