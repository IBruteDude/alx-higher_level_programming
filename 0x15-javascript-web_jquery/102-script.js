$(document).ready(
  () => {
    $('INPUT#btn_translate').click(
      () => {
        const lang = $('INPUT#language_code').val();
        $.get({
          url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
          dataType: 'json'
        }).done(
          (data) => {
            $('DIV#hello').text(data.hello);
          }
        );
      }
    );
  }
);
