(function ($) {
    "use strict";
        var Ecommerce = {
            initialised: false,
            version: 1.0,
            mobile: false,
            init: function () {
                if (!this.initialised) {
                    this.initialised = true;
                } else {
                    return;
                }             
                this.preloader();
			},
            preloader: function () {
                $(window).on('load', function () {
                    $(".preloader-wrapper").removeClass('preloader-active');
                });
                $(window).on('load', function () {
                    setTimeout(function () {
                        $('.preloader-open').addClass('loaded');
                    }, 100);
                });
            },
	};

		Ecommerce.init();
	})(jQuery);
