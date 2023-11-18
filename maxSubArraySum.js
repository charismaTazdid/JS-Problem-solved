function maxSubarraySum(arr) {
  let currentMaxSum = 0;
  let maxSoFar = arr[0];

  for (const num of arr) {
    currentMaxSum = Math.max(currentMaxSum + num, num);
    maxSoFar = Math.max(maxSoFar, currentMaxSum);
  }

  return maxSoFar;
}