

function begin(){
    $.ajax({
        url: "/send_message/begin",
        }).done(function(e) {
            getReply(e);
        });
    return false;
}


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
    temp= message.substring(59);
    newMessage= temp.substring(0, temp.indexOf('"'));
    $('<li class="replies"><p>' + newMessage + '</p></li>').appendTo($('.messages ul'));
    $('.message-input input').val(null);
    $('.contact.active .preview').html('<span>You: </span>' + newMessage);

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