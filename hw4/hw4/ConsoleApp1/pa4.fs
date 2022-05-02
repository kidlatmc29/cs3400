/// hw4.fs
/// Isabel Ovalles
/// CPSC 3400

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