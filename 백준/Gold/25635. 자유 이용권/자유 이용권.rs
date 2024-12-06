use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut tot: u64 = 0;
    let mut max_val : u64 = 0;
    for num in &nums {
        tot += *num;
        max_val = max_val.max(*num);
    }

    if (tot + 1) / 2 < max_val {
        tot -= max_val;
        tot *= 2;
        tot += 1;
    }
    print!("{tot}");
}
// 10 2가 반례였음