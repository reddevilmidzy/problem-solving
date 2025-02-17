use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let mut res = String::new();

    let t = next().parse().unwrap();
    for i in 1..=t {
        let n: usize = next().parse().unwrap();
        let m: usize = next().parse().unwrap();

        let nums: Vec<Vec<u32>> = (0..n)
            .map(|_| (0..m).map(|_| next().parse::<u32>().unwrap()).collect())
            .collect();

        writeln!(res, "Case #{i}: {}", solve(n, m, nums)).unwrap();
    }
    print!("{res}");
}

fn get_factor(num: u32) -> Vec<u32> {
    let mut res = Vec::new();
    // res.push(1);
    res.push(num);

    for i in 2..=(num as f32).sqrt() as u32 {
        if num % i == 0 {
            res.push(i);
            if num / i != i {
                res.push(num / i);
            }
        }
    }
    res.sort();

    res
}

fn solve(n: usize, m: usize, nums: Vec<Vec<u32>>) -> String {
    let grundy = get_grundy();
    // 내가 동시에 취할 수 있는 행동은 xor 시키고.
    // 한 턴에서 할 수 있는 그런디 수를 확인하기 위해 현재 상태에서 갈 수 있는 상태 값들의 mex를 구한다.

    let mut res = 0;
    let mut flag = false;

    for i in 0..n {
        // 이번 턴에서 할 수 있느 것
        let mut add = 0;

        for j in 0..m {
            // nums[i][j] 의 팩터를 구한 다음
            // nums[i] 의 모든 수의 팩터를 구한 다음 각 조합을 xor 시킨 후 mex를 취한 것이 그런디 수
            add += grundy[nums[i][j] as usize];
            // print!("{} ", grundy[nums[i][j] as usize]);
        }

        flag |= add != 1;
        res ^= add;

    }

    if (res == 0) ^ flag {
        "YES".to_string()
    } else {
        "NO".to_string()
    }
}

fn mex(num: u16) -> u16 {
    for i in 0..=15 {
        if num & (1 << i) == 0 {
            return i as u16;
        }
    }
    16
}

fn get_grundy() -> Vec<u16> {
    let m = 10000;
    let mut grundy = vec![0; m + 1];

    for i in 2..=m {
        let factors = get_factor(i as u32);
        let mut bit = 0;

        for factor in factors {
            bit |= 1 << grundy[factor as usize];
        }

        grundy[i] = mex(bit);
    }

    grundy
}

#[test]
fn tmp() {

    // let val = get_grundy();
    // println!("{:?}", val);
    // println!("{}", solve(2,2,vec![vec![2,3], vec![2,3]]));


    let val = solve(2,3,vec![vec![4,5,6],vec![7,8,9]]);

    print!("{}", val);
}

// [0, 0, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 3, 1, 2, 2, 4, 1, 3, 1, 3, 2, 2, 1, 4, 2, 2, 3, 3, 1, 3, 1, 5, 2, 2, 2, 4, 1, 2, 2, 4, 1, 3, 1, 3, 3, 2, 1, 5, 2, 3]
