#include <iostream>
char *beautiful(char *str)
{
    int i, j;
    if (str == NULL)
    {
        return NULL;
    }

    for (i = j = 0; str[i] != '\0'; i++)
    {
        if (str[i] >= '0' && str[i] <= '9' || str[i] >= 'A' && str[i] <= 'Z')
        {
            str[j] = str[i];
            j++;
        }
    }
    str[j] = '\0';
    return str;
}

int main()
{
    char str[100] = "hdjhka dhasSADHLKDSAH LDKSAK 53684369871 hjhd *^*@* hdilhsaJHFDA";
    std::cout << beautiful(str) << std::endl;
    return 0;
}