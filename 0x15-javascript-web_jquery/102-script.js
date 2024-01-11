$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/' + $.param({ lang: language }),
      function (data) {
        $('DIV#hello').text(data.hello);
      });
  });
});
