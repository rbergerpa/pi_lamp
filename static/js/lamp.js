function initLamp() {
  console.log("initLamp");

  $('#btn-on').on('mousedown', function() {
    send('/lamp_on');
  });

  $('#btn-off').on('mousedown', function() {
    send('/lamp_off');
  });
}

function send(url) {
console.log("url: " + url);

  $.ajax({
    url: url,
    type: 'PUT',
    contentType: 'application/json',
  });
}

$(document).ready(function() {
  initLamp();
});

