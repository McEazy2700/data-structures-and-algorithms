use std::iter::Iterator;
pub fn linear_search<T: PartialEq, I: Iterator<Item = T>>(iter: I, value: T) -> Option<usize> {
    for (_i, v) in iter.enumerate() {
        if v == value {
            return Some(1)
        }
    }
    return None
}
