


function sendMessage(){

    let message = $(".message-input input").val();
    if ($.trim(message) == '') {
        return false;
    }
    $('<li class="sent"><p>' + message + '</p></li>').appendTo($('.messages ul'));

    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);
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
    $('<li class="replies"><p>' + message + '</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + message);

};

$('.submit').click(function () {
    sendMessage();
    getReply();
});


$(window).on('keydown', function (e) {
    if (e.which == 13) {
        sendMessage();
        getReply();
        return false;
    }
});