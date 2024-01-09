#!/usr/bin/node
// Finds the second biggest integer in the list of arguments

const findSecondBiggest = (nums) => {
  if (nums.length <= 1) {
    return 0; // If there's only one or no number, return 0
  }

  const maxNum = Math.max(...nums); // Find the biggest number
  nums = nums.filter(num => num !== maxNum); // Remove the biggest number

  const secondMaxNum = Math.min(...nums); // Find the smallest number among the remaining
  return secondMaxNum; // Return the second biggest number
};

const args = process.argv.slice(2).map(Number);
console.log(findSecondBiggest(args));
