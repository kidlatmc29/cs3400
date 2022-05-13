/// Isabel Ovalles
/// CPSC 3400
/// hw4.fs
/// All of the code you turn in must have been written by you without immediate 
/// reference to another solution to the problem you are solving.  That means that you can look at 
/// other programs to see how someone solved a similar problem, but you shouldn't have any code 
/// written by someone else visible when you write yours (and you shouldn't have looked at a 
/// solution just a few seconds before you type!).  You should compose the code you write based on 
/// your understanding of how the features of the language you are using can be used to implement 
/// the algorithm you have chosen to solve the problem you are addressing.  Doing it this way is 
/// "real programming" - in contrast to just trying to get something to work by cutting and pasting 
/// stuff you don't actually understand.  It is the only way to achieve the learning objectives of the 
/// course. 

/// getVolume
/// param: tuple containing three floats
/// return: product of the three floats 
let getVolume dim =
    let (x:float), (y:float) , (z:float) = dim
    x * y * z

/// volumeList
/// param: a list containing tuples that have three floats
/// return: a list containing tuples that has one float representing the volume
let rec volumeList list = 
    if list = []
        then []
    else
        let head::tail = list
        getVolume head :: volumeList tail

/// getMax
/// param: list of floats
/// return: the largest float in the list
let getMax list = 
    let rec loop max list = 
        match list with
        | [] -> max
        | head::tail -> loop (if head > max then head else max) tail
    loop 0.0 list

/// maxCubeVolume
/// params: list of tuples containing three floats
/// return: a float of the greatest volume
let rec maxCubeVolume list =
    if list = []
        then 0.0
    else 
        getMax (volumeList list)

/// findMatches
/// params: string and a list of tuples. tuple consist of a string and int
/// return: a list of integers based on the matched string with the first 
///         argument of the tuple
let rec findMatches value = function
    | [] -> []
    | head::tail -> if value = fst(head)
                        then List.sort (snd(head)::findMatches value tail)
                    else findMatches value tail

let elimDuplicates list = 
   


// Tree definition for problem 3
type BST =
    | Empty
    | TreeNode of int * BST * BST

/// insert
/// param: a integer value to add into the bst, current bst
/// return: bst tree with added bst
let rec insert newVal tree = 
    match tree with
    |Empty -> TreeNode(newVal, Empty, Empty)
    |TreeNode(value, left, right) -> 
        if newVal = value
            then tree
        else if newVal > value
            then TreeNode(value, left, (insert newVal right))
        else 
            TreeNode(value, (insert newVal left), right)

/// contains
/// params: target integer and a bst tree to search
/// returns: a bool, true if target is in tree, false if otherwise
let rec contains target tree =
    match tree with
    | Empty -> false
    | TreeNode(value, left, right) -> 
        if target = value
            then true
        else if target > value 
            then contains target right
        else 
            contains target left

/// count
/// params: func which is a Boolean function with a single param, and a bst tree
/// returns: int representing the number of nodes that evaluted to true based on func
let count func tree = 
    let rec loop total = function
        | Empty -> 0
        | TreeNode(value, left, right) ->
            if func value
                then 1 + (loop total left) + (loop total right)
                else loop total left + loop total right
    loop 0 tree

/// evenCount
/// param: a bst tree
/// return: int, which represents the total even numbers in the tree
let evenCount tree =
    count(fun x -> x % 2 = 0) tree