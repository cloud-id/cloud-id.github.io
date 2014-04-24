$(document).ready(function(){
	//Contact us section
	$(".contactUs-icon").click(function(){
		if($(".contact-content").css("display")=="none"){
			// $(this).css("background","url(img/slideUp_icon.png)");
			$(this).html("Hidden");
			$(".contact-content").slideDown();
		}else{
			// $(this).css("background","url(img/contactUs_icon.png)");
			$(this).html("Contact us");
			$(".contact-content").slideUp();
		}
	});

	$(".case-section .thumbnail img").click(function(){
		$(this).parent().find('.overview').removeClass("hide").addClass("active");
	});
    $(".overview .close").click(function(){
      $(".overview").removeClass("active").addClass("hide");
    });
    $(".case-content li h5").click(function(){
		$(this).parent().find('.overview').removeClass("hide").addClass("active");
	});
	$(".case-content li p img").click(function(){
		$(this).parent().parent().find('.overview').removeClass("hide").addClass("active");
	});

	carouselResize();
	carouselSwitch();
	$(window).resize(function(){
		carouselResize();
	});

	function carouselResize(){
		var carouselControlW = $(".carousel-control").width();
		$(".carousel-control").css("height", carouselControlW);
	}

	//Carousel
	function carouselSwitch(){
		for(i=1; i<6; i++){
			var img_src = "img/banner_"+i+".jpg";		
			var wap_img_src = "img/wap_banner_"+i+".jpg";
			var windowW = $(window).width();

			if(windowW > 600){
				if(i==1){
					var item_active = "<div class='item active'><img src='"+img_src+"'></div>";
					$(".carousel-inner").append(item_active);
				}else{
					var item = "<div class='item'><img src='"+img_src+"'></div>";
					$(".carousel-inner").append(item);
				}
			}else{
				if(i==1){
					var item_active = "<div class='item active'><img src='"+wap_img_src+"'></div>";
					$(".carousel-inner").append(item_active);
				}else{
					var item = "<div class='item'><img src='"+wap_img_src+"'></div>";
					$(".carousel-inner").append(item);
				}

				$(".carousel-control span").css("top","250%");
			}					
		}
	}

})