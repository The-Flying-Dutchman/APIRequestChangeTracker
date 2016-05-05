$(function(){
		//==========================Model==========================
		var Model = (function() {
			var URL = "/get_request_details";
			//var URL = "http://localhost:8080/jQuery_MVC/test-change.json";
			var currentPageURL=$(location).attr('href');
			var requestId = currentPageURL.substring(currentPageURL.lastIndexOf('/detail/') + 8);
			return {
				getChanges : function() {
					return $.ajax({
						type : "GET",
						url : URL,
						data: {"request_id": requestId},
						dataType : "json",
						contentType : "application/json",
					});
				}
			};
		}());

		//==========================View==========================
		var View = (function() {
			var template = $("#change-template").html();

			var applyTemplate = function(template, data) {
				console.log(data)
				return template
					.replace(/\${data_request_id}/g, data.data_request_id)
					.replace(/\${detail}/g, data.data_content)
					.replace(/\${time}/g, data.data_timestamp);
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
					changes.success(function(results) {
						View.displayChanges(results);   //Display
					});
					changes.error(function(textStatus, errorThrown) {
						alert("Loading data error!");
					});
				}
			};
		}());
	
	//Init controller
	$(document).ready(function () {
		Controller.loadAndDisplayChanges();
    });
});