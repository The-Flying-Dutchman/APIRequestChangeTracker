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

function pwdVerify(){
	var pwd1 = $("#pass").val();
	var pwd2 = $("#ver").val();
	if($('#registerForm')[0].checkValidity()){
		if( pwd1 != pwd2){
			$("#indicator").show();
			$("#indicator").addClass("showFromTop");
			setTimeout(function(){
				$("#indicator").removeClass("showFromTop");
				$("#indicator").fadeOut();
			},2000);
			return false;
		}else{
			return true;
		}
	}else
		return true;
}