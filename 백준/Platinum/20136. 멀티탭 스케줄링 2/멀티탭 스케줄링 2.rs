use std::collections::{BinaryHeap, HashMap, VecDeque};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..k).map(|_| next().parse().unwrap()).collect();

    // 최대 힙에 다음에 올 인덱스를 넣기.
    print!("{}", solve(n, k, nums));
}

fn solve(n: usize, k: usize, nums: Vec<u32>) -> i32 {
    let mut res = 0;
    let mut idx = HashMap::new();
    let mut used = vec![false; k + 1];

    for i in 0..k {
        if !idx.contains_key(&nums[i]) {
            idx.insert(nums[i], VecDeque::new());
        }
        idx.get_mut(&nums[i]).unwrap().push_back(i);
    }

    let mut hq = BinaryHeap::with_capacity(n);
    let mut cnt = 0;

    for i in 0..k {
        idx.get_mut(&nums[i]).unwrap().pop_front();
        let val = *idx.get(&nums[i]).unwrap().front().unwrap_or(&k);
        if cnt >= n && !used[nums[i] as usize] {
            res += 1;

            loop {
                let (_p_idx, p_val) = hq.pop().unwrap();
                if used[p_val as usize]{
                    used[p_val as usize] = false;
                    cnt -= 1;
                    break;
                }
            }
        }
        hq.push((val, nums[i]));
        if !used[nums[i] as usize] {
            cnt += 1;
        }
        used[nums[i] as usize] = true;
    }

    res
}

#[test]
fn tmp() {
    assert_eq!(2, solve(2, 7, vec![2, 3, 2, 3, 1, 2, 7]));
    assert_eq!(5, solve(3, 8, vec![1, 2, 3, 4, 5, 6, 7, 8]));
    assert_eq!(2, solve(1, 3, vec![2, 1, 2]));
    assert_eq!(4, solve(2, 8, vec![1, 2, 3, 4, 1, 3, 4, 2]));
    assert_eq!(4, solve(2, 9, vec![1,2,3,1,2,3,1,2,3]));
    assert_eq!(0, solve(2, 10, vec![1, 1, 2, 1, 1, 2, 1, 1, 2, 1]));
}
