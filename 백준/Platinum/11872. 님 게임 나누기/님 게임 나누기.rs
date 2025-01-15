use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();

    // 0,
    // 1,2,4,3,
    // 5,6,8,7

    let mut res: u32 = 0;
    for num in nums {
        if num % 4 == 0 {
            res ^= num - 1;
        } else if num % 4 == 3 {
            res ^= num + 1;
        } else {
            res ^= num;
        }
    }

    if res != 0 {
        print!("koosaga");
    } else {
        print!("cubelover");
    }
}
