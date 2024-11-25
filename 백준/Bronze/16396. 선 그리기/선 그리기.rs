use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut nums: Vec<Vec<i32>> = (0..n).map(|_| vec![next().parse().unwrap(), next().parse().unwrap()]).collect();
    nums.sort();
    let mut res = 0;

    let mut st = 0;
    let mut ed = 0;


    for i in 0..n {
        let u = nums[i][0];
        let v = nums[i][1];

        if ed < u {
            res += ed - st;
            st = u;
            ed = v;
        } else if u <= ed {
            ed = ed.max(v);
        }
    }
    res += ed - st;
    print!("{res}")
}
