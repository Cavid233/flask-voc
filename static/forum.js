$(document).ready(function() {
    $(".commet").click(function() {
        $(".commet").eq(1).hide();
        $(".text_area").eq(1).show();
    });
    $(".cancel").click(function() {
        $("#FormControlTextarea1").val('')
        $(".text_area").eq(1).hide();
        $(".commet").eq(1).show();
    });
    $("#show_comment").click(function() {
        $("#show_comment").hide();
        $(".seeComment").show();
    });
    $("#hide_comment").click(function() {
        $("#show_comment").show();
        $(".seeComment").hide();
    });

    ////// Like and Unlike //////
    $("#unlike").click(function() {
        $("#like").show();
        $("#unlike").hide();
    });
    $("#like").click(function() {
        $("#unlike").show();
        $("#like").hide();
    });
    ///////////////////////////

});