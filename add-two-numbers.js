// https://leetcode.com/problems/add-two-numbers/submissions/
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
	let carry = 0;
	let currentNode = new ListNode();
	let headNode = currentNode;
	let nextVal = 0;

	while (l1 || l2) {
		if (l1 === null) {
			nextVal = 0 + l2.val;
		} else if (l2 === null) {
			nextVal = l1.val + 0;
		} else {
			nextVal = l1.val + l2.val;
		}
		if (carry === 1) {
			nextVal = nextVal + 1;
		}
		if (nextVal >= 10) {
			carry = 1;
			let nextNode = new ListNode(nextVal - 10);
			currentNode.next = nextNode;
			currentNode = nextNode;
		} else {
			let nextNode = new ListNode(nextVal);
			currentNode.next = nextNode;
			currentNode = nextNode;
			carry = 0;
		}

		if (l1 && l1.next) {
			l1 = l1.next;
		} else {
			l1 = null;
		}
		if (l2 && l2.next) {
			l2 = l2.next;
		} else {
			l2 = null;
		}
	}
	if (carry === 1) {
		let nextNode = new ListNode(1);
		currentNode.next = nextNode;
		currentNode = nextNode;
	}
	return headNode.next;
};
