/**
 * Note: The returned array must be malloced, assume caller calls free().
 * twoSum - a function taht returns indices of the two numbers such that they add up to target.
 * @nums: given array of integers.
 * @target: an integer that equals to the possible sum of array of integers
 * @numsSize: array size.
 * @returnSize: size of return array.
 *
 * Return: indices(indexs)
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    int i, j;
    int *indice = malloc(sizeof(int) * 2);
    if (!indice)
    return (NULL);
    for (i = 0; i < numsSize; i++)
    {
        for (j = i + 1; j < numsSize; j++)
        {
            if (nums[j] == target - nums[i])
            {
                *returnSize = 2;
                indice[0] = i;
                indice[1] = j;
                return (indice);
            }
        }
    }
    *returnSize = 0;
    return (NULL);
}