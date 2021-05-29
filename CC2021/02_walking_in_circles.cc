//  Sometimes while playing monopoly it seems you're walking the same triangle over
//  and over again, jail, free-parking and go to jail. This is a fairly simple
//  triangle, having a right angle and 2 equal sides. This triangle isn't Pythagorean
//  however. Not all triangles are Pythagorean. Not all triangles have a right angle.
//  What is the sum of the perimeters of all perimareal triangles with all sides under
//  10000, where the sides are integers? Perimareal triangles are triangles that have
//  equal area and perimeter (disregarding units).

// Use Heron's formula for brute force:
// P = a + b + c
// A = sqrt(s(s - a)(s - b)(s - c))  with  s = 1/2(a + b + c)
// P = A
// a + b + c = sqrt(s(s - a)(s - b)(s - c))
// 2s = sqrt(s(s - a)(s - b)(s - c))
// 4s^2 = s(s - a)(s - b)(s - c)
// 4s = (s - a)(s - b)(s - c)
// 2(a + b + c) = (s - a)(s - b)(s - c)
// 2(a + b + c) = (1/2(a + b + c) - a)(1/2(a + b + c) - b)(1/2(a + b + c) - c)
// 2(a + b + c) = 1/8(b + c - a)(a + c - b)(a + b - c)
// 16(a + b + c) = (b + c - a)(a + c - b)(a + b - c)

#include <iostream>
#include <omp.h>
#include <atomic>

int main()
{
    int const lim = 10000;
    std::atomic<int> total = {0};

    #pragma omp parallel for
    for (size_t a = 1; a < lim; ++a)
        for (size_t b = a; b < lim; ++b)
            for (size_t c = b; c < lim; ++c)
                if (16 * (a + b + c) == (b + c - a) * (a + c - b) * (a + b - c))
                    total += a + b + c;
    
    std::cout << total << '\n';
}

// 192
// ~18s
