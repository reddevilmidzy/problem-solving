use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();

    let mut tot: u64 = 0;
    let mut max_val: u64 = 0;
    for _ in 0..n {
        let num: u64 = next().parse().unwrap();
        tot += num;
        max_val = max_val.max(num);
    }

    if (tot + 1) / 2 < max_val {
        tot = (tot - max_val) * 2 + 1;
    }
    print!("{tot}");
}
