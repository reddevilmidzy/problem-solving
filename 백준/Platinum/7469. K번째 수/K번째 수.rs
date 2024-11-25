use std::io::{read_to_string, stdin};

fn upper_bound(nums: &Vec<i32>, target: i32) -> i32 {
    let mut left: i32 = 0;
    let mut right: i32 = (nums.len() - 1) as i32;

    while left <= right {
        let mid = (left + right) / 2;
        if nums[mid as usize] > target {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    left
}

fn update(tree: &mut Vec<Vec<i32>>, node: usize, st: usize, ed: usize, idx: usize, val: i32) {
    if idx < st || idx > ed {
        return;
    }

    tree[node].push(val);
    if st != ed {
        update(tree, node * 2, st, (st + ed) / 2, idx, val);
        update(tree, node * 2 + 1, (st + ed) / 2 + 1, ed, idx, val);
    }
}

fn query(tree: &Vec<Vec<i32>>, node: usize, st: usize, ed: usize, left: usize, right: usize, val: i32) -> i32 {
    if left > ed || right < st {
        return 0;
    }
    if left <= st && ed <= right {
        return upper_bound(&tree[node], val);
    }

    query(tree, node * 2, st, (st + ed) / 2, left, right, val) + query(tree, node * 2 + 1, (st + ed) / 2 + 1, ed, left, right, val)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let h = (n as f64).log2().ceil() as usize;
    let tree_size: usize = 1 << (h + 1);
    let mut tree = vec![Vec::new(); tree_size];

    let mut res = String::with_capacity(m);

    for i in 1..=n {
        update(&mut tree, 1, 1, n, i, nums[i - 1]);
    }

    for i in 1..tree_size {
        tree[i].sort();
    }

    for _ in 0..m {
        let i: usize = next().parse().unwrap();
        let j: usize = next().parse().unwrap();
        let k: i32 = next().parse().unwrap();

        let mut low = -1_000_000_000;
        let mut high = 1_000_000_000;

        while low <= high {
            let mid = (low + high) / 2;
            if query(&tree, 1, 1, n, i, j, mid) < k {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        res.push_str(low.to_string().as_str());
        res.push('\n');
    }
    print!("{res}")
}
