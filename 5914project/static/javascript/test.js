//$('#sumbit').on('click', function(e) {
function submit(){
    let answer = "";
    console.log($("input[name='question1']:checked").val().toString());
    answer = answer + ($("input[name='question1']:checked").val().toString());
    answer = answer + ($("input[name='question2']:checked").val().toString());
    answer = answer + ($("input[name='question3']:checked").val().toString());
    answer = answer + ($("input[name='question4']:checked").val().toString());
    answer = answer + ($("input[name='question5']:checked").val().toString());
    answer = answer + ($("input[name='question6']:checked").val().toString());
    answer = answer + ($("input[name='question7']:checked").val().toString());
    answer = answer + ($("input[name='question8']:checked").val().toString());
    answer = answer + ($("input[name='question9']:checked").val().toString());
    answer = answer + ($("input[name='question10']:checked").val().toString());
    answer = answer + ($("input[name='question11']:checked").val().toString());
    answer = answer + ($("input[name='question12']:checked").val().toString());
    answer = answer + ($("input[name='question13']:checked").val().toString());
    answer = answer + ($("input[name='question14']:checked").val().toString());
    answer = answer + ($("input[name='question15']:checked").val().toString());
    answer = answer + ($("input[name='question16']:checked").val().toString());
    answer = answer + ($("input[name='question17']:checked").val().toString());
    answer = answer + ($("input[name='question18']:checked").val().toString());
    answer = answer + ($("input[name='question19']:checked").val().toString());
    answer = answer + ($("input[name='question20']:checked").val().toString());
    answer = answer + ($("input[name='question21']:checked").val().toString());
    answer = answer + ($("input[name='question22']:checked").val().toString());
    answer = answer + ($("input[name='question23']:checked").val().toString());
    answer = answer + ($("input[name='question24']:checked").val().toString());
    answer = answer + ($("input[name='question25']:checked").val().toString());
    answer = answer + ($("input[name='question26']:checked").val().toString());
    answer = answer + ($("input[name='question27']:checked").val().toString());
    answer = answer + ($("input[name='question28']:checked").val().toString());
    answer = answer + ($("input[name='question29']:checked").val().toString());
    answer = answer + ($("input[name='question30']:checked").val().toString());
    answer = answer + ($("input[name='question31']:checked").val().toString());
    answer = answer + ($("input[name='question32']:checked").val().toString());
    answer = answer + ($("input[name='question33']:checked").val().toString());
    answer = answer + ($("input[name='question34']:checked").val().toString());
    answer = answer + ($("input[name='question35']:checked").val().toString());
    answer = answer + ($("input[name='question36']:checked").val().toString());
    answer = answer + ($("input[name='question37']:checked").val().toString());
    answer = answer + ($("input[name='question38']:checked").val().toString());
    answer = answer + ($("input[name='question39']:checked").val().toString());
    answer = answer + ($("input[name='question40']:checked").val().toString());
    answer = answer + ($("input[name='question41']:checked").val().toString());
    answer = answer + ($("input[name='question42']:checked").val().toString());
    answer = answer + ($("input[name='question43']:checked").val().toString());
    answer = answer + ($("input[name='question44']:checked").val().toString());
    answer = answer + ($("input[name='question45']:checked").val().toString());
    answer = answer + ($("input[name='question46']:checked").val().toString());
    answer = answer + ($("input[name='question47']:checked").val().toString());
    answer = answer + ($("input[name='question48']:checked").val().toString());
    answer = answer + ($("input[name='question49']:checked").val().toString());
    answer = answer + ($("input[name='question50']:checked").val().toString());
    sendResults(answer);
    console.log(answer);
  };

  function sendResults(answer){
    $.ajax({
        url: "/submit/" + answer,
        }).done(function(e) {
        });
    return false;
  }