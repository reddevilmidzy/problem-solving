use std::io::{read_to_string, stdin};

fn xor_upto(k: u128) -> u128 {
    if k % 4 == 0 {
        return k;
    }
    if k % 4 == 1 {
        return 1;
    }
    if k % 4 == 2 {
        return k + 1;
    }
    0
}

fn range_xor(x: u128, m: u128) -> u128 {
    xor_upto(x + m - 1) ^ xor_upto(x - 1)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut res: u128 = 0;

    for _ in 0..n {
        let x: u128 = next().parse().unwrap();
        let m: u128 = next().parse().unwrap();

        res ^= range_xor(x, m);
    }

    if res != 0 {
        print!("koosaga");
    } else {
        print!("cubelover");
    }
}
