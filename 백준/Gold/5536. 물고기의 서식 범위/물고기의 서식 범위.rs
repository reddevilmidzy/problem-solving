use std::collections::{HashMap, HashSet};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: i32 = next().parse().unwrap();

    let mut nums = Vec::with_capacity(n);
    let mut x_set: HashSet<usize> = HashSet::new();
    let mut y_set: HashSet<usize> = HashSet::new();
    let mut z_set: HashSet<usize> = HashSet::new();

    for _ in 0..n {
        let st_x: usize = next().parse().unwrap();
        let st_y: usize = next().parse().unwrap();
        let st_z: usize = next().parse().unwrap();
        let ed_x: usize = next().parse().unwrap();
        let ed_y: usize = next().parse().unwrap();
        let ed_z: usize = next().parse().unwrap();

        x_set.insert(st_x);
        x_set.insert(ed_x);
        y_set.insert(st_y);
        y_set.insert(ed_y);
        z_set.insert(st_z);
        z_set.insert(ed_z);

        nums.push((st_x, st_y, st_z, ed_x, ed_y, ed_z));
    }

    let mut x_list: Vec<usize> = x_set.iter().map(|x| *x).collect();
    let mut y_list: Vec<usize> = y_set.iter().map(|x| *x).collect();
    let mut z_list: Vec<usize> = z_set.iter().map(|x| *x).collect();

    x_list.sort();
    y_list.sort();
    z_list.sort();

    // println!("{:?}", x_list);
    // println!("{:?}", y_list);
    // println!("{:?}", z_list);
    let x_len = x_list.len();
    let y_len = y_list.len();
    let z_len = z_list.len();

    let x_map: HashMap<usize, usize> = x_list.iter().cloned().zip(0..x_len).collect();
    let y_map: HashMap<usize, usize> = y_list.iter().cloned().zip(0..y_len).collect();
    let z_map: HashMap<usize, usize> = z_list.iter().cloned().zip(0..z_len).collect();
    // println!("x_map={:?}", x_map);
    // println!("y_map={:?}", y_map);
    // println!("z_map={:?}", z_map);

    let mut pre = vec![vec![vec![0; z_len]; y_len]; x_len];

    for (st_x, st_y, st_z, ed_x, ed_y, ed_z) in nums {
        let st_x = *x_map.get(&st_x).unwrap();
        let st_y = *y_map.get(&st_y).unwrap();
        let st_z = *z_map.get(&st_z).unwrap();

        let ed_x = *x_map.get(&ed_x).unwrap();
        let ed_y = *y_map.get(&ed_y).unwrap();
        let ed_z = *z_map.get(&ed_z).unwrap();

        pre[st_x][st_y][st_z] += 1;
        pre[ed_x][st_y][st_z] -= 1;

        pre[st_x][ed_y][st_z] -= 1;
        pre[st_x][st_y][ed_z] -= 1;

        pre[ed_x][ed_y][st_z] += 1;
        pre[ed_x][st_y][ed_z] += 1;
        pre[st_x][ed_y][ed_z] += 1;
        pre[ed_x][ed_y][ed_z] -= 1;
    }

    for x in 1..x_len {
        for y in 0..y_len {
            for z in 0..z_len {
                pre[x][y][z] += pre[x - 1][y][z];
            }
        }
    }

    for x in 0..x_len {
        for y in 1..y_len {
            for z in 0..z_len {
                pre[x][y][z] += pre[x][y - 1][z];
            }
        }
    }

    for x in 0..x_len {
        for y in 0..y_len {
            for z in 1..z_len {
                pre[x][y][z] += pre[x][y][z - 1];
            }
        }
    }

    let mut res: usize = 0;
    for x in 0..x_len - 1 {
        for y in 0..y_len - 1 {
            for z in 0..z_len - 1 {
                if pre[x][y][z] >= m {
                    let dx = x_list[x + 1] - x_list[x];
                    let dy = y_list[y + 1] - y_list[y];
                    let dz = z_list[z + 1] - z_list[z];

                    res += dx * dy * dz;
                }
            }
        }
    }
    print!("{res}")
}
