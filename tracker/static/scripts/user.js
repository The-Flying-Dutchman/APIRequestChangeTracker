$(function(){
<<<<<<< HEAD
	//Model
	var Model = (function() {
		var URL = "http://localhost:8080/jQuery_MVC/test.json";
		return {
			getRequests : function() {
				return $.ajax({
					type : "GET",
					url : URL,
					dataType : "json",
					contentType : "application/json",
					success : function(text) {
						
					},
					error: function(textStatus, errorThrown){
						alert("Loading data error!");
					}
				});
			}
		};
	}());

	//View
	var View = (function() {
		var template = $("#request-template").html();

		var applyTemplate = function(template, data) {
			return template
				.replace(/\${requestURL}/g, data.URL)
				.replace(/\${timeInterval}/g, data.Time);
		};

		var renderRequests = function(results) {
			return results.map(function(data) {
				return applyTemplate(template, data);
			}).join("");
		};

		return {
			displayRequests : function(results){
				var rendering = renderRequests(results);
				$(".current-request-section-list").html(rendering);
			}
		};
	}());

	//Controller
	var Controller = (function() {
		return {
			loadAndDisplayRequests : function() {
				var requests = Model.getRequests();//Load
				requests.done(function(results) {
					View.displayRequests(results);   //Display
				});
			}
		};
	}());
	
	
	
	//Add Click Events (Still works for dynamically created HTML elements)
	$(document).on("click", ".edit-icon", function(){
=======
﻿	$.ajax{
		var user_id = document.cookie;
		url: "/list",
		data: {"user_id": 1},
		success: function(data){
			var array = data;
			for(var i=0; i<=array.length; i++){
				var content = '<div class="current-request-section">';
				content += '<p>Request URL:<span>'+array[i]["request_url"]+'</span></p>';
				content+='<p>Time interval:<span>'+array[i]["request_interval"]+'</span></p>';
				content+='<a class="edit-icon"><img src="images/edit.png" /></a>';
				content+='<a class="delete-icon"><img src="images/delete.png" /></a></div>';
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
>>>>>>> 37165790d21db6de83ba78aa40fe0a635d47fb40
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
	$(document).on("click", ".cancel-icon",function(){
		var parent = $(this).parent();
		parent.addClass("flipOut");
		setTimeout(function(){
			parent.removeClass("flipOut");
			parent.hide();
			parent.siblings(".display").show();
			parent.siblings(".display").addClass("flipIn");
		},500);
	});
<<<<<<< HEAD
	
	//Animation
	setTimeout(function(){
		$('.logo').addClass("zoom");
	},4000);
	setTimeout(function(){
		$('.current-request-section').addClass("bounceInFromBottom");
		$('.current-request-section').show();
	},2500);
	
	//Init controller
	$(document).ready(function () {
		Controller.loadAndDisplayRequests();
    });
});
=======
});
>>>>>>> 37165790d21db6de83ba78aa40fe0a635d47fb40
