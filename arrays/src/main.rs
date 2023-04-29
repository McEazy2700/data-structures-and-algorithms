use std::mem;

fn main() {
    /* Fundamentally, an arrya is a contiguous memory space (unbreaking)
     * in which contains a certain ammount of bytes*/

    let _arr1: [i32; 5] = [1, 2, 3, 4, 5];
    let arr2: [i32; 6] = [0; 6];
    println!("Length: {}", arr2.len());
    println!("Array ocupies bytes: {}", mem::size_of_val(&arr2));
    /* How Arrays work 
     * So arrays are of a fixed length and of a specific type.
     * this means the with of the array and the size of each element in the array
     * is known before hand. This make accesing and changing data in an array fast
     * It works like this:
     * my_arr = [1, 2 ,3]
     * the mem_address of the first element '1' is the same with the starting point
     * of the block of memory allocated to the array.
     * this means that, when accesing elements in the array, you can multiply the
     * index of that element by the size of the type of that element, and the add
     * that to the memory address of the first value. e.g incase of a 4bytes (32 bits)
     * size integer, accesing element at index 1 '2' will be
     * mem_adrr(my_arr) + (4 * 1) = location of item at index 2 in memory*/

    /* Note: Deleting something at an array index doesn't actually mean that there's
     * no nothing there, it can be set to '0' or something that you've agreed to mean
     * nothing. For example 'null' or 'None' in JavaScript and Python respectively*/
}
