$(function(){
﻿	$.ajax{
		var user_id = '<%= Session["user_id"] %>';
		url: "/list",
		data: {"user_id": 1},
		success: function(data){
			var array = data;
			for(var i=0; i<=array.length; i++){
				var content = '<div class="current-request-section">
				<p>Request URL:<span>'+array[i]["request_url"]+'</span></p>
				<p>Time interval:<span>'+aray[i]["request_interval"]+'</span></p>
				<a class="edit-icon"><img src="images/edit.png" /></a>
				<a class="delete-icon"><img src="images/delete.png" /></a>
				</div>';
				$(".current-request-section-list").append(content);
			}
		}, error: function(error) {
			console.log("error");
		}
	}
	setTimeout(function(){
		$('.logo').addClass("zoom");
	},4000);
	setTimeout(function(){
		$('.current-request-section').addClass("bounceInFromBottom");
		$('.current-request-section').show();
	},2500);
	$(".edit-icon").click(function(){
		var parent = $(this).parent();
		var original_url = parent.children("p:nth-of-type(1)").children("span").text();
		var original_time_interval = parent.children("p:nth-of-type(2)").children("span").text();
		parent.siblings(".edit").children("form").children("input:nth-of-type(1)").val(original_url);
		parent.siblings(".edit").children("form").children("input:nth-of-type(2)").val(original_time_interval);
		parent.addClass("flipOut");
		setTimeout(function(){
			parent.removeClass("flipOut");
			parent.hide();
			parent.siblings(".edit").show();
			parent.siblings(".edit").addClass("flipIn");
		},500);
	});
	$(".cancel-icon").click(function(){
		var parent = $(this).parent();
		parent.addClass("flipOut");
		setTimeout(function(){
			parent.removeClass("flipOut");
			parent.hide();
			parent.siblings(".display").show();
			parent.siblings(".display").addClass("flipIn");
		},500);
	});
});
