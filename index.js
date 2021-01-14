function getYTVideo() {
    $.ajax({
        type: 'GET',
        url: 'https://www.youtube.com/user/ATienDai',
        success: function (result) {
            console.log(result);
            translate(result);
        }, error: function (result) {
            console.log(result);
        }
    });
}
//console.log(123);
//getYTVideo();