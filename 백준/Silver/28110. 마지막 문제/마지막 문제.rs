use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();
    nums.sort();

    if nums[0] + n - 1 == nums[n - 1] {
        print!("-1");
    } else {
        let mut res = 0;
        let mut diff = 0;

        for i in 0..n - 1 {
            let tmp = nums[i + 1] - nums[i];

            if diff < tmp / 2 {
                diff = tmp / 2;
                res = nums[i] + tmp / 2;
            }
        }

        print!("{res}")
    }
}
