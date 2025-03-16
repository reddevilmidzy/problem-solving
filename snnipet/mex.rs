fn mex(mut nums: Vec<i32>) -> i32 {
    nums.sort_unstable();
    for i in 0..nums.len() {
        if nums[i] != i as i32 {
            return i as i32;
        }
    }
    nums.len() as i32
}
