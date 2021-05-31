#include "euler/euler.h"
#include <iostream>

int main()
{
    int n_1  = 1;
    int n    = 2;
    int ones = 2;
    int val  = 0;

    while (true)
    {
        val = euler::gcd(n_1, n);

        if (val == 1)
            n_1 = n_1 + n + 1;
        else
            n_1 = n_1 / val;
        
        if (n_1 == 1)
            ++ones;
        
        if (ones == 19841012)
        {
            std::cout << n << '\n';
            break;
        }
            
        ++n;
    }
}

// 79364654
// ~1.6s
