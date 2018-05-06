#include <iostream>
char *beautiful(char *str)
{
    char *p, *q;
    if (str == NULL)
    {
        return NULL;
    }

    for (p = str, q = str; *p != '\0'; p++)
    {
        if (*p >= '0' && *p <= '9' || *p >= 'A' && *p <= 'Z')
        {
            *q++ = *p;
        }
    }
    *q = *p;
    return str;
}

int main()
{
    char str[100] = "hdjhka dhasSADHLKDSAH LDKSAK 53684369871 hjhd *^*@* hdilhsaJHFDA";
    std::cout << beautiful(str) << std::endl;
    return 0;
}