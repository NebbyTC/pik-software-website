
// Robi z znacznika link
function redirect(url) {
	console.log("worked")
	window.location.href = url;
}

// dla poszczegłonych kategorii
function redirect_1() {
	redirect("/pcc")
}

function redirect_2() {
	redirect("/oprogramowanie")
}

function redirect_3() {
	redirect("/peryferia")
}


function redirect_4() {
	redirect("/oprogramowanie/sabaka")
}

function redirect_5() {
	redirect("/oprogramowanie/pik-kalkulator")
}

function redirect_6() {
	redirect("/oprogramowanie/sheetworks")
}

function redirect_7() {
	redirect("/oprogramowanie/snakestudio")
}

function redirect_zakup_software() {
	redirect("/zakup")
}

function redirect_job() {
	redirect("/aplikuj")
}

function submit_form(){
	console.log("Przesłano")
	var form = document.getElementById("pygame-dev-form");
	form.submit();
}
