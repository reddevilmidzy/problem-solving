import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        final StringBuilder res = new StringBuilder(); 
        final int n = numbers.length;
        final List<String> nums = new ArrayList<>();
        
        for (final int num : numbers) {
            nums.add(String.valueOf(num));
        }
        
        Collections.sort(nums, (o1, o2) -> (o2.concat(o1).compareTo(o1.concat(o2))));
        if (nums.get(0).equals("0")) {
            return "0";
        }
        for (final String num : nums) {
            res.append(num);
        }
        return res.toString();
    }
}