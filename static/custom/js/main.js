
// Need to separate it to diferent files

/*
General requests
*/

$(document).ready(function() {
	
})


function get_request(user_name) {
	$.get(`/${user_name}/data`, function(data, status) {
		let result = [data, status];
		return result;
	});
}

/*
Profile (index.hmtl) form requests
*/

function create_profile() {
	let user_name = $("[name=username]").val();
	$.post(`/${user_name}/data`, function (data, status) {
		console.log(status)
		// Data are sent as str
		if (data == user_name) {
			$("#message").html("Profile " + `${data}` + " already exist");
			$("#create_profile_overlay").slideDown(1000);
		// Data are sent as arr
		}else if (data[0].status == status) {
			window.location.replace(`/${data[1].profile}`);
		}else {
			$("#message").html("Sorry.\n There seems to be a problem ...");
			$("#create_profile_overlay").slideDown(1000);
		}
	})
	return false
} 


/*
Create (riddle.hmtl) 
*/

function create_riddle_game() {
	let user_name = $("[name=username]").val();
	$.post(`/${user_name}/data`, function (data, status) {
		console.log(status)
		// Data are sent as str
		if (data == user_name) {
			$("#message").html("Profile " + `${data}` + " already exist");
			$("#create_profile_overlay").slideDown(1000);
			// Data are sent as arr
		} else if (data[0].status == status) {
			window.location.replace(`/${data[1].profile}`);
		} else {
			$("#message").html("Sorry.\n There seems to be a problem ...");
			$("#create_profile_overlay").slideDown(1000);
		}
	})
	return false
}
/*
Misc
*/

