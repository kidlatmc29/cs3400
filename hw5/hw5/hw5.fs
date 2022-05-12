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
/// params: a list of tuples, matching a variable name to an int; an str representing an equation in postfix notation
/// returns: the result of the postfix equation
let eval vars (expr:string) =  
    let strSeq = Seq.toList expr |> Seq.map(fun x -> string x)
    let strList = Seq.toList strSeq
    
    let rec innerEval vars stack strList = 
        printfn "stack = %A" stack
        match strList with
        | [] -> stack
        | head::tail when head = "+" -> let num1::num2::rest = stack // "pushes" of stack
                                        innerEval vars ((num1+num2)::rest) tail
        | head::tail when head = "-" -> let num1::num2::rest = stack
                                        innerEval vars ((num1-num2)::rest) tail
        | head::tail when head = "*" -> let num1::num2::rest = stack
                                        innerEval vars ((num1*num2)::rest) tail
        | head::tail when head = "/" -> let num1::num2::rest = stack
                                        innerEval vars ((num1/num2)::rest) tail
        | head::tail -> innerEval vars ((findFirstInt head vars)::stack) tail
    innerEval vars [] strList


let eval2 vars (expr:string) = 
    let rec innerEval vars stack (expr:string) = 
       match expr.[0] with
       | '+' -> let num1::num2::rest = stack 
                innerEval vars ((num1+num2)::rest) expr.[1..]
       | '' -> stack
       | _ -> innerEval vars ((findFirstInt expr.[0] vars)::stack) expr.[1..]
    innerEval vars [] expr

    //innerEval vars [] expr
  
///let pop stack =
///    match stack with
///   | head::tail -> let newStack = tail
///                   (head, newStack)

///let countElements list =
///       let rec loop count list =
 ///          match list with
 ///          | [] -> 0
  ///         | head::tail -> loop (1+count) tail
    ///   loop 0 list