use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();
    let t: usize = next().parse().unwrap();
    let mut res = String::new();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        let nums: Vec<usize> = (0..n).map(|_| next().parse::<usize>().unwrap() - 1).collect();

        let mut visited = vec![false; n];
        let mut cnt = 0;
        for cur in 0..n {
            if !visited[cur] {
                cnt += 1;
                let mut nxt = cur;

                while !visited[nxt] {
                    visited[nxt] = true;
                    nxt = nums[nxt];
                }
            }
        }
        res.push_str(cnt.to_string().as_str());
        res.push('\n');
    }
    print!("{res}")
}
