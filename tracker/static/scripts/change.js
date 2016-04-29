$(function(){
		//==========================Model==========================
		var Model = (function() {
			var URL = "http://localhost:8080/jQuery_MVC/test-change.json";
			return {
				getChanges : function() {
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

		//==========================View==========================
		var View = (function() {
			var template = $("#change-template").html();

			var applyTemplate = function(template, data) {
				return template
					.replace(/\${detail}/g, data.Detail)
					.replace(/\${time}/g, data.Time);
			};

			var renderChanges = function(results) {
				return results.map(function(data) {
					return applyTemplate(template, data);
				}).join("");
			};

			return {
				displayChanges : function(results){
					var rendering = renderChanges(results);
					$(".content").html(rendering);
				}
			};
		}());

		//==========================Controller==========================
		var Controller = (function() {
			return {
				loadAndDisplayChanges : function() {
					var changes = Model.getChanges();//Load
					changes.done(function(results) {
						View.displayChanges(results);   //Display
					});
				}
			};
		}());
	
	//Init controller
	$(document).ready(function () {
		Controller.loadAndDisplayChanges();
    });
});