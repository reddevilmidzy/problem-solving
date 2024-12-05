use std::cmp::{max, min};
use std::fmt::Debug;
use std::io::{read_to_string, stdin};
use std::ops::Range;

#[derive(Debug, PartialEq, Eq)]
pub enum SegmentTreeError {
    IndexOutOfBounds,
    InvalidRange,
}

pub struct SegmentTree<T, F>
where
    T: Debug + Default + Ord + Copy,
    F: Fn(T, T) -> T,
{
    size: usize,
    nodes: Vec<T>,
    merge_fn: F,
}

impl<T, F> SegmentTree<T, F>
where
    T: Debug + Default + Ord + Copy,
    F: Fn(T, T) -> T,
{
    pub fn from_vec(arr: &[T], merge: F) -> Self {
        let size = arr.len();
        let mut buffer: Vec<T> = vec![T::default(); 2 * size];

        buffer[size..(2 * size)].clone_from_slice(arr);

        for idx in (1..size).rev() {
            buffer[idx] = merge(buffer[2 * idx], buffer[2 * idx + 1]);
        }

        SegmentTree {
            size,
            nodes: buffer,
            merge_fn: merge,
        }
    }

    pub fn query(&self, range: Range<usize>) -> Result<Option<T>, SegmentTreeError> {
        if range.start >= self.size || range.end > self.size {
            return Err(SegmentTreeError::InvalidRange);
        }

        let mut left = range.start + self.size;
        let mut right = range.end + self.size;
        let mut result = None;

        while left < right {
            if left % 2 == 1 {
                result = Some(match result {
                    None => self.nodes[left],
                    Some(old) => (self.merge_fn)(old, self.nodes[left]),
                });
                left += 1;
            }
            if right % 2 == 1 {
                right -= 1;
                result = Some(match result {
                    None => self.nodes[right],
                    Some(old) => (self.merge_fn)(old, self.nodes[right]),
                });
            }
            left /= 2;
            right /= 2;
        }

        Ok(result)
    }

    pub fn update(&mut self, idx: usize, val: T) -> Result<(), SegmentTreeError> {
        if idx >= self.size {
            return Err(SegmentTreeError::IndexOutOfBounds);
        }

        let mut index = idx + self.size;
        if self.nodes[index] == val {
            return Ok(());
        }

        self.nodes[index] = val;
        while index > 1 {
            index /= 2;
            self.nodes[index] = (self.merge_fn)(self.nodes[2 * index], self.nodes[2 * index + 1]);
        }

        Ok(())
    }
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let t: usize = next().parse().unwrap();

    let mut res = String::new();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();

        let arr: Vec<usize> = (0..n).collect();
        let mut min_seg = SegmentTree::from_vec(&arr, min);
        let mut max_seg = SegmentTree::from_vec(&arr, max);

        let q: usize = next().parse().unwrap();

        for _ in 0..q {
            let u: i8 = next().parse().unwrap();

            let a: usize = next().parse().unwrap();
            let b: usize = next().parse().unwrap();
            if u == 0 {
                let pre_a = min_seg.query(a..(a + 1)).unwrap().unwrap();
                let pre_b = min_seg.query(b..(b + 1)).unwrap().unwrap();
                min_seg.update(a, pre_b);
                min_seg.update(b, pre_a);

                max_seg.update(a, pre_b);
                max_seg.update(b, pre_a);
            } else {
                let min_v = min_seg.query(a..(b + 1)).unwrap().unwrap();
                let max_v = max_seg.query(a..(b + 1)).unwrap().unwrap();

                if min_v != a || max_v != b {
                    res.push_str("NO");
                } else {
                    res.push_str("YES");
                }
                res.push_str("\n");
            }
        }
    }
    print!("{res}")
}
