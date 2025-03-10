use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(n, nums));
}

fn solve(_n: usize, nums: Vec<u32>) -> String {
    let mut res =0 ;
    let nim = get_grundy();

    for num in nums {
        res ^= nim[num as usize];
    }
    if res != 0 {
        "koosaga".to_string()
    } else {
        "cubelover".to_string()
    }
}

fn get_grundy() -> Vec<u8> {
    let n = 3_000_000;
    let mut grundy = vec![0u8; n + 1];
    grundy[1] = 1;
    let fibo = vec![
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
        17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578];

    for i in 2..=n {
        let mut bit = 0i32;
        for j in &fibo {
            if i >= *j {
                bit |= 1 << grundy[i - *j];
            } else {
                break;
            }
        }
        grundy[i] = bit.trailing_ones() as u8;
    }

    grundy
}
