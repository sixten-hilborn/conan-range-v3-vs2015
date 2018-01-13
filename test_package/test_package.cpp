#include <vector>
#include <range/v3/all.hpp>

int main()
{
    std::vector<int> vi{1,2,3,4,5,6,7,8,9,10};
    using namespace ranges;
    auto rng = vi | view::remove_if([](int i){return i % 2 == 1;})
                | view::transform([](int i){return std::to_string(i);});
    // rng == {"2","4","6","8","10"};
    return 0;
}
