var email_regex = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/); //regex from : https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript
var name_regex = new RegExp(/^[A-za-z0-9-\s]+/);
var phone_regex = new RegExp(/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im);
//var csrftoken = $("[name=csrfmiddlewaretoken]").val();
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*$("#profile_form").on('submit', function(e) {
    e.preventDefault();
    var formData = new FormData(this);    
    var url = "";
    $.post(url, formData, function(data) {
        alert(data);
    });
});*/

/*submitProfileForm = function(e){
		$.ajax({
           		type: "POST",
           		url: url,
           		data: $("#profile_form").serialize(),
           		success: function(data)
           		{
               			$("#container-div").html(data);
           		}
         	});
		//e.preventDefault();	
}*/
/**
 *Custom methods for Tectum
 * */
loadprofile = function(userid){/*User id will be passed as null for static page*/
    $("#container-div").load('profile.html');
}
load_profile_data = function(user_id){
	console.log(user_id)
	$.ajax({
    		url: '/profile/data/'+user_id,
    		type: 'GET',
    		data: {
    		},
    		headers: {
    			//"X-CSRFToken": csrftoken,
    		},
    		//dataType: 'json',
    		success: function (data) {
                var template = $("#user_profile_template").html();
                data = JSON.parse(data)
                template = template.replace(/##first_name##/g,data[0].fields.first_name)
                .replace(/##last_name##/g,data[0].fields.last_name).replace(/##dept##/g,data[0].fields.branch)
                .replace(/##univ##/g,data[0].fields.university)
                if(data[0].fields.is_veg ==='N' ){
                    template = template.replace(/##meal_title##/g,'Non-Vegetarian').replace(/%23%23meal_image%23%23/g,'nv');
                } else {
                    template = template.replace(/##meal_title##/g,'Vegetarian').replace(/%23%23meal_image%23%23/g,'veg');
                }
                if(data[0].fields.is_smoke ==='N' ){
                    template = template.replace(/##smk_title##/g,'Non-Smoker').replace(/%23%23smk_image%23%23/g,'ns');
                } else {
                    template = template.replace(/##smk_title##/g,'Smoker').replace(/%23%23smk_image%23%23/g,'smoke');
                }
                if(data[0].fields.is_alcohol ==='N' ){
                    template = template.replace(/##alc_title##/g,'Non-Alcoholic').replace(/%23%23alc_image%23%23/g,'na');
                } else {
                    template = template.replace(/##alc_title##/g,'Alcoholic').replace(/%23%23alc_image%23%23/g,'drink');
                }
                gender = 'Prefer Not to Mention';
                if(data[0].fields.gender === 'F'){
                    gender = 'Female';
                } else if(data[0].fields.gender === 'O'){
                    gender = 'Others';
                } else if(data[0].fields.gender ==='M'){
                    gender = 'Male';
                }
                template = template.replace(/##gen##/g,gender).replace(/##email##/g,data[0].fields.email).replace(/##phone##/g,data[0].fields.phone);
                $("#container-div").html(template);
    		}
	});
}
loadapartment = function(userid){
    $("#container-div").load('apartment.html');
}
loadfeedback = function(userid){
    $("#container-div").load('feedback.html');
}
loadhome =function(userid){
    $("#container-div").load('home.html');
}
load_profile_edit =function(userid){
    if(userid==undefined || userid == null){
        userid = '';
    }
	$.ajax({
    		url: '/profile/'+userid+'/edit/',
    		type: 'post',
    		data: {
    		},
    		headers: {
    			"X-CSRFToken": csrftoken,
    		},
    		//dataType: 'json',
    		success: function (data) {
        		$("#container-div").html(data);
    		}
	});
	//var param = {}
	//param['X-CSRFToken'] = csrftoken;
	//param.csrfmiddlewaretoken= csrftoken;
	//$.post('/profile/',param,function(msg){
	//	$("#container-div").html(msg);
	//});
  //  $("#container-div").load('profile-edit.html');     
}
load_sign_up = function(){
    window.location.href='signup1.html';
}
load_apartment_list = function(){
    $("#container-div").load('apartment_list.html');
}
toggleMealSelection = function(){
    var src = $("#meal");
    if(src.attr("src").indexOf("nv.svg") >=0){
            src.attr("src","/static/images/svg/veg.svg");
            $("#is_veg_hidden").val("V");
    } else {
        src.attr("src","/static/images/svg/nv.svg");
        $("#is_veg_hidden").val("N");
    }
}
toggleSmokeSelection = function(){
    var src = $("#smoke");
    if(src.attr("src").indexOf("ns.svg") >=0){
            src.attr("src","/static/images/svg/smoke.svg");
            $("#is_smoke_hidden").val("S");
    } else {
        src.attr("src","/static/images/svg/ns.svg");
        $("#is_smoke_hidden").val("N");
    }
}
toggleAlcoholSelection = function(){
    var src = $("#alcohol");
    if(src.attr("src").indexOf("na.svg") >=0){
            src.attr("src","/static/images/svg/drink.svg");    
            $("#is_alcohol_hidden").val("A");      
    } else {
        src.attr("src","/static/images/svg/na.svg");
        $("#is_alcohol_hidden").val("N");
    }
}
/*$('#feedbackform').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            Name: {
                validators: {
                    notEmpty: {
                        message: 'The Name is required and cannot be empty'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required'
                    },
                    emailAddress: {
                        message: 'The email address is not valid'
                    }
                }
            },
            Message: {
                validators: {
                    notEmpty: {
                        message: 'The Message is required and cannot be empty'
                    }
                }
            }
        }
    });
*/
changeRating = function(value){
    $("#rating").attr("value",value);
}