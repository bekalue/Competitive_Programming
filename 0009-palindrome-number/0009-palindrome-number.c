/**
 * isPalindrome - checks if the integer is a palindrome.
 * @x: a given integer.
 * Return: true or false.
 */
bool isPalindrome(int x)
{
    size_t revNum = 0, last_digit, temp = x;

    while (temp > 0)
    {
        last_digit = temp % 10;
        revNum = (revNum * 10) + last_digit;
        temp /= 10;
    }
    if (x == revNum)
    return (true);
    else
    return (false);
}