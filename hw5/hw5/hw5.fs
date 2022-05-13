/// Isabel Ovalles
/// hw5.fs
/// CPSC 3400
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

/// findFirstInt
/// params: list of tuples representing var bindings and expression as a str
/// returns: the integer bound to the var 
let rec findFirstInt varName = function
    | [] -> 0
    | head::tail when fst(head) = varName -> snd(head)
    | head::tail -> findFirstInt varName tail

/// eval
/// params: a list of tuples (string * int), an str representing an equation in postfix notation
/// returns: a int list with only one element as the result
let eval vars (expr:string) =  
    let strSeq = Seq.toList expr |> Seq.map(fun x -> string x)  // takes string and turn it into a seq of strings
    let strList = Seq.toList strSeq                             // turns seq of str into a list of strings
    
    let rec innerEval vars stack strList = 
        match strList with
        | [] -> stack
        | head::tail when head = "+" -> let num1::num2::rest = stack            // "pop" off stack
                                        innerEval vars ((num1+num2)::rest) tail //"pushing" on stack
        | head::tail when head = "-" -> let num1::num2::rest = stack
                                        innerEval vars ((num2-num1)::rest) tail
        | head::tail when head = "*" -> let num1::num2::rest = stack
                                        innerEval vars ((num1*num2)::rest) tail
        | head::tail when head = "/" -> let num1::num2::rest = stack
                                        innerEval vars ((num2/num1)::rest) tail
        | head::tail when head = "$" -> let num1::num2::rest = stack
                                        innerEval vars (num2::num1::rest) tail
        | head::tail when head = "@" -> let char1::char2::restOfChars = strList
                                        let newInt::rest = stack
                                        innerEval ((char2, newInt)::vars) rest restOfChars
        | head::tail when head = " " -> innerEval vars stack tail
        | head::tail -> innerEval vars ((findFirstInt head vars)::stack) tail
    innerEval vars [] strList