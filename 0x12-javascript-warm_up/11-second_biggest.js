#!/usr/bin/node
if (!process.argv[3]) console.log("0");
else {
	nums = process.argv.slice(2);
	for (let i = 0; i < nums.length; i++) {
		nums[i] = parseInt(nums[i]);
	}
	nums.sort((a, b) => a - b);
	console.log(nums[nums.length - 1]);
}
