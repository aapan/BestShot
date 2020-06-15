/*** autocomplete search word ***/

function moreSlideDown() {

    // 下滑列表
    $("#more ul").hide();
    $("#more").hover( function () {
        $(">ul:not(:animated)", this).slideDown("fast");
    }, function(){
        $(">ul", this).slideUp("fast");
    });

}

function searchComplete(classList, authList){

    // 自動完成
    $("#keyword").keyup(function (e) {

        // 上、下、Enter 不執行
        if(e.keyCode == 38 || e.keyCode == 40 || e.keyCode == 13) {
            if (e.keyCode == 13 && $("#keyword").val() != "") {
                $()
            }
            return;
        }

        autocomplete($("#keyword")[0], classList);

        var event = new Event('input');
        $("#keyword")[0].dispatchEvent(event);

    });
}

function remindWindow(){

    var remindHtml = '<div id="popup1" class="overlay">' +
        '<div class="popup">' +
        '<h2>Alert</h2>\n' +
        '<a class="close" href="#" onclick="closePopup();">&times;</a>\n' +
        '<div class="content">\n' + 'You need to login first' +
        '</div>' +
        '</div>' +
        '</div>';

    $("body").before(remindHtml);
    $(".overlay").css("visibility", "visible");
    $(".overlay").css("opacity", 1);

}

function closePopup(){
    $(".overlay").css("visibility", "hidden");
    $(".overlay").css("opacity", 0);
}
