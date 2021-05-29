// It's no secret that the prime locations on a monolopy board are very desirable, 
// as you can charge the highest rents on them. However aiming for the prime locations
// might not always be the best strategy. While a prime location can be a good source
// of income, it might not be very robust. Odds are that the orange and red streets
// are a more robust source of income, and can be turned into prime revenue streams
// with the appropriate amount of hotels. Talking about robust primes. A prime number
// is considered left-truncatable if you can obtain a sequence of prime numbers by
// consecutive removal of the leftmost digit (e.g. 373,73,3). A prime number is
// considered right-truncatable if you can obtain a sequence of prime numbers by
// consecutive removal of the rightmost digit (e.g. 373,37,3). A prime number is
// considered truncatable if you can obtain a sequence of prime numbers by consecutive
// removal of the either the rightmost or the leftmost digit (e.g. 373,(37,73),((3,7),(7,3))).
// Robust primes are prime numbers that allow the consecutive removal of *any* digit
// and still produce a sequence of prime numbers (So 373 is not robust, since taking
// away the middle digit 7, will give you 33 which is not prime.). What is the
// product of all robust prime numbers smaller than 1,000,000?

#include "euler/euler.h"
#include "easy/easy.h"
#include <algorithm>

std::vector<int> num2vec(int num)
{
    std::vector<int> numbers;
    
    while (num)
    {
        numbers.push_back(num % 10);
        num /= 10;
    }

    std::reverse(numbers.begin(), numbers.end());

    return numbers;
}

std::vector<int> genCombs(int prime)
{
    std::vector<int> numberlist = num2vec(prime);
    
    std::vector<int> combinationList;
    for (int k = 1; k != euler::math::intlog10(prime) + 1; ++k)
    {
        euler::Combinations combinations(numberlist, k);

        while (not combinations.done())
            combinationList.push_back(combinations.yieldnumber());
    }

    combinationList.push_back(prime);

    return combinationList;
}

int main()
{
    euler::Primetools primetools;
    
    auto const primes = primetools.sieve(1'000'000);
    bool robust;

    size_t product = 1;
    for (int prime : primes)
    {
        std::vector<int> combinationList = genCombs(prime);

        robust = true;
        for (int comb : genCombs(prime))
            if (not primetools.isPrime(comb))
                robust = false;

        if (robust)
        {
            product *= prime;
            std::cout << "prime " << prime << " is robust\n";
            easy::print(combinationList);
        }
    }

    std::cout << "solution: " << product << '\n';
}

// 691428990
// instant
