use std::{
    collections::HashMap,
    fmt::Write,
    io::{read_to_string, stdin},
};

#[derive(Debug)]
struct Key {
    alphabet: char,
    number: usize,
    is_sharp: bool,
}

impl Into<Key> for String {
    fn into(self) -> Key {
        let res = self.chars().collect::<Vec<_>>();
        Key {
            alphabet: res[0],
            number: res[1].to_string().parse().unwrap(),
            is_sharp: res.len() == 3,
        }
    }
}

impl Key {
    fn into_position(&self) -> usize {
        let map = HashMap::from([
            ('C', 0),
            ('D', 2),
            ('E', 4),
            ('F', 5),
            ('G', 7),
            ('A', 9),
            ('B', 11),
        ]);
        self.number * 12 + map.get(&self.alphabet).unwrap() + if self.is_sharp { 1 } else { 0 }
    }
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let l = Into::<Key>::into(next().parse::<String>().unwrap()).into_position();
    let r = Into::<Key>::into(next().parse::<String>().unwrap()).into_position();
    let n = next().parse::<usize>().unwrap();
    let nums = (0..n)
        .map(|_| Into::<Key>::into(next().parse::<String>().unwrap()).into_position())
        .collect::<Vec<_>>();

    print!("{}", solve(l, r, n, &nums));
}

fn find(
    n: usize,
    i: usize,
    l: usize,
    r: usize,
    dp: &mut Vec<Vec<Vec<i32>>>,
    nums: &Vec<usize>,
) -> i32 {
    if i >= n {
        return 0;
    }
    if dp[i][l][r] != -1 {
        return dp[i][l][r];
    }

    let target = nums[i];
    let l_dist = l.abs_diff(target) as i32;
    let r_dist = r.abs_diff(target) as i32;
    let l_cost = l_dist + find(n, i + 1, target, r, dp, nums);
    let r_cost = r_dist + find(n, i + 1, l, target, dp, nums);
    dp[i][l][r] = l_cost.min(r_cost);
    dp[i][l][r]
}

fn trace(
    n: usize,
    i: usize,
    l: usize,
    r: usize,
    dp: &mut Vec<Vec<Vec<i32>>>,
    nums: &Vec<usize>,
    res: &mut String,
) {
    if i >= n {
        return;
    }

    let target = nums[i];
    let l_dist = l.abs_diff(target) as i32;
    let r_dist = r.abs_diff(target) as i32;
    let l_cost = l_dist + find(n, i + 1, target, r, dp, nums);
    let r_cost = r_dist + find(n, i + 1, l, target, dp, nums);

    if l_cost <= r_cost {
        write!(res, "1 ").unwrap();
        trace(n, i + 1, target, r, dp, nums, res);
    } else {
        write!(res, "2 ").unwrap();
        trace(n, i + 1, l, target, dp, nums, res);
    }
}

fn solve(l: usize, r: usize, n: usize, nums: &Vec<usize>) -> String {
    let mut res = String::with_capacity(n);
    const M: usize = 140;
    let mut dp = vec![vec![vec![-1; M]; M]; n + 1];

    writeln!(res, "{}", find(n, 0, l, r, &mut dp, &nums)).unwrap();
    trace(n, 0, l, r, &mut dp, nums, &mut res);

    res
}
