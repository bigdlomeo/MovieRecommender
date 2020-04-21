

function begin(){
    $.ajax({
        url: "/send_message/begin",
        }).done(function(e) {
            getReply(e);
        });
    return false;
}


function scroll(){
    auto = document.getElementsByClassName("messages");
    auto[0].scrollTop = auto[0].scrollHeight;
}


function sendMessage(){
    let message = $(".message-input input").val();
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));

    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
    $(".messages").animate({ scrollTop: $(document).height() }, "fast");
    $.ajax({
    url: "/send_message/"+message,
    }).done(function(e) {
        getReply(e);
    });

};



function getReply(message){
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="replies"><img src="static/images/robot_chat.png" alt="" width="30px"/><p class="box animated bounceIn">'+message+'</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);

    $(".messages").animate({ scrollTop: $(document).height() }, "fast");

    scroll();

};


$('.submit').click(function () {
    sendMessage();
    getReply();
    return false;
});


$(window).on('keydown', function (e) {
    if (e.which == 13) {
        sendMessage();
        getReply();
        return false;
    }
});


$(".messages").animate({ scrollTop: $(document).height() }, "fast");
