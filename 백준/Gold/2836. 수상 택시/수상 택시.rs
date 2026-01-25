use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    // 결국 문제는 빠꾸하는 놈들.
    // 이것만 모아서 한줄로 병합시키면 될듯.
    let mut nums = Vec::with_capacity(n);

    for _ in 0..n {
        let (st, ed): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        if st > ed {
            nums.push((ed, st));
        }
    }
    nums.sort_unstable();

    let mut res = m;
    if nums.is_empty() {
        print!("{res}");
        return;
    }
    let mut pre_st = nums[0].0;
    let mut pre_ed = nums[0].1;
    for i in 1..nums.len() {
        let (st, ed) = nums[i];
        if st > pre_ed {
            res += (pre_ed - pre_st) * 2;
            pre_st = st;
        }
        pre_ed = pre_ed.max(ed);
    }

    res += (pre_ed - pre_st) * 2;
    print!("{res}");
}
