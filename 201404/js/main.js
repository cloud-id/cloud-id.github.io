$(document).ready(function(){
	//Contact us section
	$(".contact").click(function(){
		if($(".contact-content").css("display")=="none"){
			// $(this).css("background","url(img/slideUp_icon.png)");
			$(this).html("隐藏");
			$(".contact-content").slideDown();
		}else{
			// $(this).css("background","url(img/contactUs_icon.png)");
			$(this).html("联系我们");
			$(".contact-content").slideUp();
		}
	});
}