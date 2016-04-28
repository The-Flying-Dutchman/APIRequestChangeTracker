$(function(){
	setTimeout(function(){
		$('.logo').addClass("zoom");
	},3000);
	$(".register-section .login-tag").click(function(){
		$(".register-section").addClass("rotateOut");
		setTimeout(function(){
			$(".register-section").removeClass("rotateOut");
			$(".register-section").hide();
			$(".login-section").show();
			$(".login-section").addClass("rotateIn");
		},400);
	});
	$(".login-section .register-tag").click(function(){
		$(".login-section").addClass("rotateOut");
		setTimeout(function(){
			$(".login-section").removeClass("rotateOut");
			$(".login-section").hide();
			$(".register-section").show();
			$(".register-section").addClass("rotateIn");
		},400);
	});
	
});