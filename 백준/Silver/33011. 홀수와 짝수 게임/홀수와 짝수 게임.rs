use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let t: usize = next().parse().unwrap();
    let mut res = String::new();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        let nums: Vec<u8> = (0..n).map(|_| next().parse().unwrap()).collect();

        // 채완부터 시작함
        // 경우의수 홀 > 짝
        // 채완이는 홀수개 있는 걸 가져가야함
        // 만약 홀수개 있는게 없다면, 희원이 승리.
        // 홀수개 있는게 있다면,
        // 채완이는 그거 선택하고, 다른게 그거보다 크다면 희원이 승리

        let mut odd: u8 = 0;
        let mut even: u8 = 0;

        for num in nums {
            if num % 2 == 0 {
                even += 1;
            } else {
                odd += 1;
            }
        }

        if odd % 2 == 0 && even % 2 == 0 {
            writeln!(res, "heeda0528").unwrap();
        } else if odd != even && ((odd % 2 != 0 && odd >= even) || (even % 2 != 0 && even >= odd)) {
            writeln!(res, "amsminn").unwrap();
        } else {
            writeln!(res, "heeda0528").unwrap();
        }
    }
    print!("{res}");
}
