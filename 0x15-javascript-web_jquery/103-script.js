const translateCallback = function () {
  const lang = $('INPUT#language_code').val();
  $.get({
    url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
    dataType: 'json'
  }).done(
    (data) => {
      $('DIV#hello').text(data.hello);
    }
  );
};

$(document).ready(
  () => {
    $('INPUT#btn_translate').click(translateCallback);
    $('INPUT#language_code').on('keydown', (eventData) => {
      if (eventData.originalEvent.key === 'Enter') translateCallback();
    });
  }
);
