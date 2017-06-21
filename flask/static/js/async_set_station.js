$(function(){

  function displayStationBlock() {
    var block = $('#block-station');
    block.hide();
    block.show();
  }

  $('.set_station_id').on('click', function() {
    var station_id = $(this).data('station_id');

    var postData = {}
    postData["station_id"] = station_id;

    var request = window.superagent;
    request
      .post('/station')
      .type('form')
      .set('Content-Type', 'application/json; charset=utf-8')
      .send(postData)
      .end(function(err, res){
        console.log("station_id:"+station_id);
        if (res.ok) {
          if (station_id == res.body['station_id']) {
            console.log("success");
            displayStationBlock();

            var target = $('#block-station');
            var position = target.offset().top;
            var speed = 500; // ミリ秒で記述
            $('body,html').animate({scrollTop:position}, speed, 'swing');
            return false;
          }
        } else {
          console.log('error occured');
        }
      });
  });
});
