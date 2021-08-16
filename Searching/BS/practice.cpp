#include <algorithm>
#include <iostream>

int main() {
    int N, C;
    std::cin >> N >> C;
    int nums[N];
    for (int i = 0; i < N; ++i) std::cin >> nums[i];
    std::sort(nums, nums + N);
    int min = 1, max = nums[N - 1] - nums[0], best = 1;
    while (max >= min) {
        int cur = nums[0], count = 1;
        int mid = (max + min) / 2;
        for (int i = 1; i < N; ++i) {
            if (cur + mid <= nums[i]) {
                cur = nums[i];
                ++count;
            }
        }
        if (count >= C) {
            min = mid + 1;
            best = mid;
        } else {
            max = mid - 1;
        }
    }
    std::cout << best << std::endl;
}
