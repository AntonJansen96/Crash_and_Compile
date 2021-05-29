#include <iostream>

// Euclidean algorithm. Returns greatest common denominator of a and b.
int gcd(int a, int b)
{
#ifdef __GNUC__   // This is around 60% faster using specific CPU instructions.
                  // Source https://euler.stephan-brumme.com/toolbox/
    if (a == 0 || b == 0)
        return b;

    // MSVC++: _BitScanForward intrinsic instead
    auto shift = __builtin_ctz(a | b);
    a >>= __builtin_ctz(a);
    do
    {
        b >>= __builtin_ctz(b);
        if (a > b)
            std::swap(a, b);
        
        b -= a;
    } while (b != 0);

    return a << shift;

#else
    // standard GCD
    while (b) 
        b ^= a ^= b ^= a %= b;
    
    return a;

#endif
}

int main()
{
    int n_1  = 1;
    int n    = 2;
    int ones = 2;
    int val  = 0;

    while (true)
    {
        val = gcd(n_1, n);

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
