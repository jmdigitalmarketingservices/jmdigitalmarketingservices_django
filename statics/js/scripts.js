$(window).scroll(function () {
    const scroll = $(window).scrollTop();
    $('.banner-section').css({
        backgroundSize: 'calc(100vw + 50px + '+ scroll * 2 +'px)'
    })
});
