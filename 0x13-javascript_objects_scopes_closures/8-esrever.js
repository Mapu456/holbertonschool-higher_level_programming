#!/usr/bin/node
exports.esrever = function (list) {
	var output = [];
    for (var i = list.length - 1; i> -1; i--){
        output.push(list[i]);
    }

    return output;
};
