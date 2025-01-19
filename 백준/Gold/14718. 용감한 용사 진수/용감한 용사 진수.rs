use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut nums = Vec::with_capacity(n * 3);
    for _ in 0..n {
        let (a, b, c): (u32, u32, u32) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );
        nums.push(vec![a, b, c]);
    }
    nums.sort_by(|a, b| a[2].cmp(&b[2]));

    let mut res = u32::MAX;
    for u in 0..n {
        for v in 0..n {
            let mut cnt = 0;
            for w in 0..n {
                if nums[u][0] >= nums[w][0] && nums[v][1] >= nums[w][1] {
                    cnt += 1;
                }
                if cnt >= m {
                    res = res.min(nums[u][0] + nums[v][1] + nums[w][2]);
                }
            }
        }
    }

    print!("{res}");
}
