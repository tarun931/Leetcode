class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int evenDigitCount = 0;
        for (int num : nums) {
            int digitCount = (int) floor(log10(num)) + 1;
            if (digitCount % 2 == 0)
                evenDigitCount++;
        }

        return evenDigitCount;
    }
};