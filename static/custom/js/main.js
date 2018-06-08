function check_login_details(input) {
	const user_name = input.username.value;
	$.post(`/${user_name}/data`, user_name, function(result) {
		console.log(result)
	})
}

