$(document).ready(() => {
  $('DIV#toggle_header').click(
    () => {
      if ($('header').hasClass('red')) {
        $('header').removeClass();
        $('header').addClass('green');
      } else if ($('header').hasClass('green')) {
        $('header').removeClass();
        $('header').addClass('red');
      }
    }
  );
}
);
