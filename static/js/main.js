(function ($) {
	"use strict";

	new WOW().init();

	/*---background image---*/
	function dataBackgroundImage() {
		$('[data-bgimg]').each(function () {
			var bgImgUrl = $(this).data('bgimg');
			$(this).css({
				'background-image': 'url(' + bgImgUrl + ')', // + meaning concat
			});
		});
	}

	$(window).on('load', function () {
		dataBackgroundImage();
	});

	/*---stickey menu---*/
	$(".sticky-header").not(".sticky_header_four").after('<div class="sticky-header-placeholder"></div>');
	$(".sticky-header-placeholder").hide();
	
	$(window).on('scroll load resize', function () {
		var scroll = $(window).scrollTop();
		
		if (scroll < 100) {
			$(".sticky-header").removeClass("sticky");
			$(".sticky-header-placeholder").hide();
		}
		else {
			$(".sticky-header").addClass("sticky");
			$(".sticky-header-placeholder").show();
		}

		$(".sticky-header-placeholder").height($(".sticky-header").height() + 54);
	});

	/*---slider activation---*/
	$('.slider3_carousel').owlCarousel({
		animateOut: 'fadeOut',
		rtl: true,
		loop: true,
		nav: false,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 1,
		dots: true,
	});

	/*---Initialize Swiper---*/

	var galleryThumbs = new Swiper('.gallery-thumbs', {
		spaceBetween: 1,
		slidesPerView: 4,
		freeMode: true,
		watchSlidesVisibility: true,
		watchSlidesProgress: true,
		breakpoints: {
			1200: {
				slidesPerView: 3,
			},
			767: {
				slidesPerView: 2,
			},
			300: {
				slidesPerView: 1,
			}
		},
	});
	var galleryTop = new Swiper('.gallery-top', {
		dynamicBullets: true,
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
		},
		thumbs: {
			swiper: galleryThumbs
		}
	});

	/*---product column5 activation---*/
	$('.product_column5').on('changed.owl.carousel initialized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 5,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 3,
			},
			992: {
				items: 4,
			},
			1200: {
				items: 5,
			},

		}
	});

	function checkClasses() {
		var total = $('.product_column5 .owl-stage .owl-item.active').length;

		$(".product_column5").each(function () {
			$(this).find('.owl-item').removeClass('firstActiveItem');
			$(this).find('.owl-item').removeClass('lastActiveItem');
			$(this).find('.owl-item.active').each(function (index) {
				if (index === 0) {
					$(this).addClass('firstActiveItem');
				}
				if (index === total - 1 && total > 1) {
					$(this).addClass('lastActiveItem');
				}
			});
		});

	}
	checkClasses();

	/*---product column4 activation---*/
	$('.product_column4').on('changed.owl.carousel initialized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 4,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 3,
			},
			992: {
				items: 3,
			},
			1200: {
				items: 4,
			},

		}
	});

	function checkClasses() {
		var total = $('.product_column4 .owl-stage .owl-item.active').length;

		$(".product_column4").each(function () {
			$(this).find('.owl-item').removeClass('firstActiveItem');
			$(this).find('.owl-item').removeClass('lastActiveItem');
			$(this).find('.owl-item.active').each(function (index) {
				if (index === 0) {
					$(this).addClass('firstActiveItem');
				}
				if (index === total - 1 && total > 1) {
					$(this).addClass('lastActiveItem');
				}
			});
		});

	}
	checkClasses();

	/*---product column3 activation---*/
	$('.product_column3').on('changed.owl.carousel initialized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 3,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 3,
			},
			992: {
				items: 2,
			},
			1200: {
				items: 3,
			},

		}
	});

	/*---small product column2 activation---*/
	$('.small_product_column2').on('changed.owl.carousel initialized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 2,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 2,
			},
			992: {
				items: 2,
			},

		}
	});

	/*---small product column3 activation---*/
	$('.small_product_column3').on('changed.owl.carousel initialized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 3,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 2,
			},
			992: {
				items: 2,
			},
			1200: {
				items: 3,
			},

		}
	});

	/*---product column2 activation---*/
	$('.product_column2').on('changed.owl.carousel initialized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 2,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 1,
			},
			992: {
				items: 2,
			},

		}
	});

	/*---product column1 activation---*/
	$('.product_column1').on('changed.owl.carousel initialized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 1,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 2,
			},
			992: {
				items: 1,
			},

		}
	});

	/*---product sidebar active activation---*/
	$('.product_sidebar_slider').on('changed.owl.carousel initialized.owl.carousel resized.owl.carousel', function (event) {
		$(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')
	}).owlCarousel({
		rtl: true,
		loop: true,
		nav: false,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 1,
		dots: false,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 2,
			},
			992: {
				items: 1,
			},

		}

	});

	/*---Category sidebar active activation---*/
	$('.categories_sidebar_slider').owlCarousel({
		rtl: true,
		loop: true,
		nav: false,
		autoplay: true,
		autoplayTimeout: 8000,
		items: 1,
		dots: false,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 2,
			},
			992: {
				items: 1,
			},

		}
	});

	/*---testimonial active activation---*/
	$('.testimonial-two').owlCarousel({
		rtl: true,
		loop: true,
		nav: false,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 1,
		dots: true,

	})

	/*---blog column3 activation---*/
	$('.blog_column4').owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 4,
		dots: false,
		navText: ['<i class="ion-ios-arrow-forward"></i>', '<i class="ion-ios-arrow-back"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			768: {
				items: 2,
			},
			992: {
				items: 3,
			},
			1200: {
				items: 4,
			},

		}
	});

	/*---blog thumb activation---*/
	$('.blog_thumb_active').owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 1,
		navText: ['<i class="ion-ios-arrow-right"></i>', '<i class="ion-ios-arrow-left"></i>'],
	});

	/*---single product activation---*/
	$('.single-product-active').owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 4,
		margin: 15,
		dots: false,
		navText: ['<i class="fa fa-angle-right"></i>', '<i class="fa fa-angle-left"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			320: {
				items: 2,
				margin: 10,
			},
			992: {
				items: 3,
			},
			1200: {
				items: 4,
			},
		}
	});

	/*---product navactive activation---*/
	$('.product_navactive').owlCarousel({
		rtl: true,
		loop: true,
		nav: true,
		autoplay: false,
		autoplayTimeout: 8000,
		items: 4,
		dots: false,
		navText: ['<i class="fa fa-angle-right"></i>', '<i class="fa fa-angle-left"></i>'],
		responsiveClass: true,
		responsive: {
			0: {
				items: 1,
			},
			250: {
				items: 2,
			},
			480: {
				items: 3,
			},
			768: {
				items: 4,
			},
		}
	});

	$('.modal').on('shown.bs.modal', function (e) {
		$('.product_navactive').resize();
	});

	$('.product_navactive a').on('click', function (e) {
		e.preventDefault();

		var $href = $(this).attr('href');

		$('.product_navactive a').removeClass('active');
		$(this).addClass('active');

		$('.product-details-large .tab-pane').removeClass('active show');
		$('.product-details-large ' + $href).addClass('active show');

	});

	/*--- Tooltip Active---*/
	$('.action_links ul li a,.add_to_cart a,.footer_social_link ul li a').tooltip({
		animated: 'fade',
		placement: 'top',
		container: 'body'
	});

	/*--- niceSelect---*/
	$('.select_option, .niceselect_option').niceSelect();

	/*---  ScrollUp Active ---*/
	$.scrollUp({
		scrollText: '<i class="fa fa-angle-double-up"></i>',
		easingType: 'linear',
		scrollSpeed: 900,
		animation: 'fade'
	});

	/*---countdown activation---*/

	$('[data-countdown]').each(function () {
		var $this = $(this),
			finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function (event) {
			$this.html(event.strftime('<div class="countdown_area"><div class="single_countdown"><div class="countdown_number">%D</div><div class="countdown_title">روز</div></div><div class="single_countdown"><div class="countdown_number">%H</div><div class="countdown_title">ساعت</div></div><div class="single_countdown"><div class="countdown_number">%M</div><div class="countdown_title">دقیقه</div></div><div class="single_countdown"><div class="countdown_number">%S</div><div class="countdown_title">ثانیه</div></div></div>'));

		});
	});

	/*---slider-range here---*/
	$("#slider-range").slider({
		range: true,
		min: 0,
		max: 5000000,
		step: 10000,
		values: [700000, 4000000],
		slide: function (event, ui) {
			var $value0 = ui.values[0].toLocaleString();
			var $value1 = ui.values[1].toLocaleString();
			$("#amount").val($value1 + " تومان - " + $value0 + " تومان");
			$("#price-min").val(ui.values[0]);
			$("#price-max").val(ui.values[1]);
		}
	});
	var $value0 = $("#slider-range").slider("values", 0).toLocaleString();
	var $value1 = $("#slider-range").slider("values", 1).toLocaleString();
	$("#amount").val($value1 + " تومان - " + $value0 + " تومان");
	$("#price-min").val($("#slider-range").slider("values", 0));
	$("#price-max").val($("#slider-range").slider("values", 1));

	/*---elevateZoom---*/
	$("#zoom1").elevateZoom({
		gallery: 'gallery_01',
		responsive: true,
		cursor: 'crosshair',
		zoomType: 'inner'
	});

	$(window).on('resize', function () {
		$('.zoomContainer').remove();
		$("#zoom1").elevateZoom({
			gallery: 'gallery_01',
			responsive: true,
			cursor: 'crosshair',
			zoomType: 'inner'
		});
		setTimeout(function () {
			$('.zoomGalleryActive').click();
		}, 10);
	});

	/*---widget sub categories---*/
	$(".widget_sub_categories > a").on("click", function () {
		$(this).toggleClass('active');
		$(this).siblings('.widget_dropdown_categories').stop().slideToggle('medium');
	});

	/*---categories slideToggle---*/
	$(".categories_title").on("click", function () {
		$(this).toggleClass('active');
		$('.categories_menu_toggle').slideToggle('medium');
	});

	/*---addClass/removeClass categories---*/
	$("#cat_toggle.has-sub > a").on("click", function () {
		$(this).removeAttr('href');
		$(this).toggleClass('open').next('.categorie_sub').toggleClass('open');
		$(this).parents().siblings().find('#cat_toggle.has-sub > a').removeClass('open');
	});

	/*---MailChimp---*/
	$('#mc-form').ajaxChimp({
		language: 'en',
		callback: mailChimpResponse,
		// ADD YOUR MAILCHIMP URL BELOW HERE!
		url: 'http://devitems.us11.list-manage.com/subscribe/post?u=6bbb9b6f5827bd842d9640c82&amp;id=05d85f18ef'

	});

	function mailChimpResponse(resp) {

		if (resp.result === 'success') {
			$('.mailchimp-success').addClass('active')
			$('.mailchimp-success').html('' + resp.msg).fadeIn(900);
			$('.mailchimp-error').fadeOut(400);

		} else if (resp.result === 'error') {
			$('.mailchimp-error').html('' + resp.msg).fadeIn(900);
		}
	}

	/*---Category menu---*/
	function categorySubMenuToggle() {
		$('.categories_menu_toggle li.menu_item_children > a').on('click', function () {
			if ($(window).width() < 992) {
				$(this).removeAttr('href');
				var element = $(this).parent('li');
				if (element.hasClass('open')) {
					element.removeClass('open');
					element.find('li').removeClass('open');
					element.find('ul').slideUp();
				} else {
					element.addClass('open');
					element.children('ul').slideDown();
					element.siblings('li').not('.has-sub').children('ul').slideUp();
					element.siblings('li').removeClass('open');
					element.siblings('li').find('li').removeClass('open');
					element.siblings('li').not('.has-sub').find('ul').slideUp();
				}
			}
		});
		$('.categories_menu_toggle li.menu_item_children > a').append('<span class="expand"></span>');
	}
	
	categorySubMenuToggle();

	/*---shop grid activation---*/
	$('.shop_toolbar_btn > button').on('click', function (e) {

		e.preventDefault();

		$('.shop_toolbar_btn > button').removeClass('active');
		$(this).addClass('active');

		var parentsDiv = $('.shop_wrapper');
		var viewMode = $(this).data('role');


		parentsDiv.removeClass('grid_4 grid_list').addClass(viewMode);

		if (viewMode == 'grid_4') {
			parentsDiv.children().addClass('col-lg-3 col-md-4 col-sm-6').removeClass('col-lg-4 col-cust-5 col-12');
		}

		if (viewMode == 'grid_list') {
			parentsDiv.children().addClass('col-12').removeClass('col-lg-3 col-lg-4 col-md-4 col-sm-6 col-cust-5');
		}

	});

	/*---Newsletter Popup activation---*/

	/*
	setTimeout(function () {
		if ($.cookie('shownewsletter') == 1) $('.newletter-popup').hide();
		$('#subscribe_pemail').keypress(function (e) {
			if (e.which == 13) {
				e.preventDefault();
				email_subscribepopup();
			}
			var name = $(this).val();
			$('#subscribe_pname').val(name);
		});
		$('#subscribe_pemail').change(function () {
			var name = $(this).val();
			$('#subscribe_pname').val(name);
		});
		//transition effect
		if ($.cookie("shownewsletter") != 1) {
			$('.newletter-popup').bPopup();
		}
		$('#newsletter_popup_dont_show_again').on('change', function () {
			if ($.cookie("shownewsletter") != 1) {
				$.cookie("shownewsletter", '1')
			} else {
				$.cookie("shownewsletter", '0')
			}
		});
	}, 2500);
	*/

	/*---search box slideToggle---*/
	$(".search_box > a").on("click", function () {
		$(this).toggleClass('active');
		$('.search_widget').slideToggle('medium');
	});

	/*---slide toggle activation---*/
	$('.mini_cart_wrapper > a').on('click', function (event) {
		if ($(window).width() < 991) {
			$('.mini_cart').slideToggle('medium');
		}
	});

	/*---canvas menu activation---*/
	$('.canvas_open').on('click', function () {
		$('.Offcanvas_menu_wrapper,.off_canvars_overlay').addClass('active')
	});

	$('.canvas_close,.off_canvars_overlay').on('click', function () {
		$('.Offcanvas_menu_wrapper,.off_canvars_overlay').removeClass('active')
	});

	/*---Off Canvas Menu---*/
	var $offcanvasNav = $('.offcanvas_main_menu'),
		$offcanvasNavSubMenu = $offcanvasNav.find('.sub-menu');
	$offcanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i class="fa fa-angle-down"></i></span>');

	$offcanvasNavSubMenu.slideUp();

	$offcanvasNav.on('click', 'li a, li .menu-expand', function (e) {
		var $this = $(this);
		if (($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand'))) {
			e.preventDefault();
			if ($this.siblings('ul:visible').length) {
				$this.siblings('ul').slideUp('slow');
			} else {
				$this.closest('li').siblings('li').find('ul:visible').slideUp('slow');
				$this.siblings('ul').slideDown('slow');
			}
		}
		$this.closest('.offcanvas_main_menu').find('.menu-open').not($this).not($this.parents()).removeClass('menu-open');
		if ($this.is('a') || $this.is('span') || $this.attr('clas').match(/\b(menu-expand)\b/)) {
			$this.parent().toggleClass('menu-open');
			$this.parent().find('ul li .sub-menu').slideUp('slow');
		} else if ($this.is('li') && $this.attr('class').match(/\b('menu-item-has-children')\b/)) {
			$this.toggleClass('menu-open');
			$this.find('ul li .sub-menu').slideUp('slow');
		}
	});

	/*---js ripples activation---*/
	$('.js-ripples').ripples({
		resolution: 512,
		dropRadius: 20,
		perturbance: 0.04
	});

	/*---ajax-mail.js---*/
	$(function () {

		// Get the form.
		var form = $('#contact-form');

		// Get the messages div.
		var formMessages = $('.form-messege');

		// Set up an event listener for the contact form.
		$(form).submit(function (e) {
			
			// Stop the browser from submitting the form.
			e.preventDefault();

			// Serialize the form data.
			var formData = $(form).serialize();

			// Show sending message
			$(formMessages).text('در حال ارسال ...');

			// Submit the form using AJAX.
			$.ajax({
				type: 'POST',
				url: $(form).attr('action'),
				data: formData
			})
			.done(function (response) {

				// Make sure that the formMessages div has the 'success' class.
				$(formMessages).removeClass('error');
				$(formMessages).addClass('success');

				// Set the message text.
				$(formMessages).text(response);

				// Clear the form.
				$('#contact-form input,#contact-form textarea').val('');
			})
			.fail(function (data) {

				// Make sure that the formMessages div has the 'error' class.
				$(formMessages).removeClass('success');
				$(formMessages).addClass('error');

				// Set the message text.
				if (data.responseText !== '') {
					$(formMessages).text(data.responseText);
				} else {
					$(formMessages).text('خطایی در ارسال پیام رخ داده است.');
				}
			});
		});

	});

	/*---Custom Contact Form Validation Messages---*/
	$('#contact-form [name="name"]').on('invalid', function () {
		this.setCustomValidity('لطفا نام خود را وارد نمایید');
	});

	$('#contact-form [name="email"]').on('invalid', function () {
		if (this.validity.valueMissing) {
			this.setCustomValidity("لطفا ایمیل خود را وارد نمایید");
		}
		else if (this.validity.typeMismatch) {
			this.setCustomValidity("لطفا یک ایمیل معتبر وارد نمایید");
		}
	});

	$('#contact-form [name="message"]').on('invalid', function () {
		this.setCustomValidity('لطفا پیام خود را وارد نمایید');
	});

	$('#contact-form').find('input, textarea').on('input', function () {
		this.setCustomValidity('');
	});

})(jQuery);
