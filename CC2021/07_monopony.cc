// On your trip through Groningen, you've accidentally ended up in the Diephuisstraat
// and started playing a game called Monopony. This game uses 'streepjes' as currency,
// and for some reason you've been appointed the task of keeping track of the 'streepjes'.
// After a while 2 of your opponents start a fierce argument and to pass the time you
// start writing as many Roman numerals as you can. Your permanent marker can write
// exactly 4000 lines before it runs out of ink. We use 'modern' roman numbers 44 == XLIV,
// C is one line, X 2, L 2, M 4, etc. How many numbers starting at I can you write 
// before you run out of ink? Don't count the last partial roman number.

#include "euler/euler.h"
#include <iostream>

int main()
{
    int const lim = 1000;
    
    std::vector<std::string> romans;
    
    for (int num = 1; num != lim; ++num)
        romans.push_back(euler::dec2roman(num));
    
    int numbers = 0;
    int ink = 4000;
    for (auto const &roman : romans)
    {
        for (auto const &letter : roman)
        {
            if (letter == 'I')
                ink -= 1;
            if (letter == 'V')
                ink -= 2;
            if (letter == 'X')
                ink -= 2;
            if (letter == 'L')
                ink -= 2;
            if (letter == 'C')
                ink -= 1;
            if (letter == 'D')
                ink -= 2;
            if (letter == 'M')
                ink -= 4;
        }

        if (ink >= 0)
            ++numbers;
        
        if (ink < 0)
        {
            std::cout << numbers << '\n';
            break;
        }
    }
}

// 484
// instant
