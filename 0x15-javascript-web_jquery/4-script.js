$(document).ready(() => {
  $('DIV#toggle_header').click(
    () => {
      if ($('header').hasClass('red')) {
        $('header').removeClass('red');
        $('header').addClass('grean');
      } else {
        $('header').removeClass('grean');
        $('header').addClass('red');
      }
    }
  );
}
);
