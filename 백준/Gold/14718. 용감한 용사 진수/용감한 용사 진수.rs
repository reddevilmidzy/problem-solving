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

    let mut res = u32::MAX;
    for u in 0..n {
        for v in 0..n {
            for w in 0..n {
                let mut cnt = 0;
                let a = nums[u][0];
                let b = nums[v][1];
                let c = nums[w][2];

                for x in 0..n {
                    if a >= nums[x][0] && b >= nums[x][1] && c >= nums[x][2] {
                        cnt += 1;
                    }
                }
                if cnt >= m {
                    res = res.min(a + b + c);
                }
            }
        }
    }

    print!("{res}");
}
