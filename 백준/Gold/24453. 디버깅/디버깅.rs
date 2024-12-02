use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let mut error: Vec<usize> = vec![0; n + 1];

    for _ in 0..m {
        let num: usize = next().parse().unwrap();
        error[num] += 1;
    }

    for i in 1..=n {
        error[i] += error[i - 1];
    }

    let x: usize = next().parse().unwrap();
    let y: usize = next().parse().unwrap();

    let mut deb: usize = x;
    for i in x..=n {
        deb = deb.min(error[i] - error[i - x]);
        if deb <= y {
            break;
        }
    }
    print!("{}", m - y.max(deb));
}
