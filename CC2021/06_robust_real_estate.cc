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
