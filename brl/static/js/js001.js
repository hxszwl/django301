function chaCloor(field) {

	var name = field.parentNode;
	if(name.style.color == 'red') {
		name.style.color = 'black';
	} else {
		name.style.color = 'red';

	}
}

function show_hide(el) {
	var name_wd = []
	var name_dl = []
	var name_dy = []
	var name_qt = []
	if(el.value == '温度') {
		name_wd = ['环境温度1', '环境温度2', '环境温度3', '环境温度4', '环境温度5', '环境温度6', '环境温度7', '环境温度8', '环境温度9', '环境温度10', '环境温度11', '环境温度12']
	} else if(el.value == '电压') {
		name_dy = ['A相电压', 'B相电压', 'C相电压']
	} else if(el.value == '电流') {
		name_dl = ['A相电流', 'B相电流', 'C相电流']
	} else {
		name_qt = ['总有功电度', '总无功电度', '当月有功电度', '当月无功电度', '环境温度11', '环境温度12']
	}

	//				if($("input[value='"+el.value+"']").is(':checked')) {

	if(el.checked == true) {

		//					var name1 = $("input[name='A相电流']").parent().parent()　　
		//					list_show(name_wd)　　　
		if(name_wd.length > 1) {
			list_show(name_wd)

		}
		if(name_dy.length > 1) {
			list_show(name_dy)
		}
		if(name_dl.length > 1) {
			list_show(name_dl)
		}
		if(name_qt.length > 1) {
			list_show(name_qt)
		}

		//					name1.hide()
	} else {
		//					var name2 = $("input[name='A相电流']").parent().parent()
		//					name2.show()　
		//						　list_hide(name_wd)
		if(name_wd.length > 1) {
			list_hide(name_wd)　
		}
		if(name_dy.length > 1) {
			list_hide(name_dy)
		}
		if(name_dl.length > 1) {
			list_hide(name_dl)
		}
		if(name_qt.length > 1) {
			list_hide(name_qt)
		}

		　
	}　
}

function list_show(element1) {
	for(i = 0; i < element1.length; i++) {
		//					$("input[name='"+element1[i]+"']").parent().parent().hide()
		$("input[name='" + element1[i] + "']").parent().parent().css('display', 'inline-block')

	}
}

function list_hide(element1) {
	for(i = 0; i < element1.length; i++) {
		//					$("input[name='"+element1[i]+"']").parent().parent().show()
		$("input[name='" + element1[i] + "']").parent().parent().css('display', 'none')
	}

}

// function asb(v1) {
// 	var x = "<input type='checkbox' name='userName1' value='" + val[i] + "'><span>" + val[i] + "</span><br/>"
// 	// console.log(x)
// 	return x
// }