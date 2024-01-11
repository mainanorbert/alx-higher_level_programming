(document).ready(function () {
  function fetchData () {
    language = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?${$.param({ lang: language })}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(fetchData);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchData();
    }
  });
});
