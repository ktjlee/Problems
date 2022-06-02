/* https://leetcode.com/problems/maximum-subarray/submissions/ */

var maxSubArray = function (nums) {
	let maxSum = nums[0];
	let possSum = 0;
	count = 0;
	if (nums.length === 1) {
		return maxSum;
	}
	for (let i = 0; i < nums.length; i++) {
		count += 1;
		if (possSum < 0) {
			possSum = 0;
		}
		possSum += nums[i];
		if (possSum > maxSum) {
			maxSum = possSum;
		}
	}
	return maxSum;
};
