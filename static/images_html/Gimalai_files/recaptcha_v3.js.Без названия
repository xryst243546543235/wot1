(function ($) {

  /**
   * recaptcha v3 js.
   */
  Drupal.behaviors.reCaptchaV3 = {
    attach: function (context, settings) {
      $('input[data-recaptcha-v3-sitekey]', context).once('recaptcha-v3').each(function () {
        var $input = $(this);
        var timer = setInterval(function () {
          if (typeof grecaptcha !== 'undefined') {
            grecaptcha.ready(function () {
              grecaptcha.execute(
                $input.data('recaptcha-v3-sitekey'),
                {
                  action: $input.data('recaptcha-v3-action')
                })
                .then(function (token) {
                  $input.val(token);
                  $input.trigger('change');
                });
            });
            clearInterval(timer);
          }
        }, 500);
      });
    }
  };

})(jQuery);
