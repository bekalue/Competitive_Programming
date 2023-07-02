/**
 * roman - gets integer value of each roman letters.
 * @c: a roman character passed.
 * Return: an integer value of that roman character.
*/
int roman(char c)
{
    switch(c)
    {
        case 'I':
        return (1);

        case 'V':
        return (5);

        case 'X':
        return (10);

        case 'L':
        return (50);

        case 'C':
        return (100);

        case 'D':
        return (500);

        case 'M':
        return (1000);

        default:
        return (0);
    }
}


int romanToInt(char * s)
{
    int i, n = strlen(s), result = 0, current, next;

    for (i = 0; i < n; i++)
    {
        current = roman(s[i]);
        next = roman(s[i + 1]);
        
        if (current >= next)
        result += current;
        else
        {
            result += (next - current);
            i++;
        }
    }
    return (result);
}