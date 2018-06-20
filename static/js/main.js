function setAll() {
	t = document.forms.q.elements;
	t.technology.checked = !1;
	t.web.checked = !1;
	t.software.checked = !1;
	t.hacking.checked = !1;
	t.programming.checked = !1;
	t.other.checked = !1
}

function rmAll() {
	document.forms.q.elements.all.checked = !1
}
