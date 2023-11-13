#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
	console.log('Size Missing');
} else {
	for (let x = 0; x < size; x++) {
		let row = '';
		for (c = 0; c < size; c++) {
			row += 'X';
		}
		console.log(row);
	}
}
