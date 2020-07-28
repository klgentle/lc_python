package main

import (
    "fmt"
    "time"
)

func main() {

    t := time.Now()
    switch {
    case t.Hour() < 12:
        fmt.Println("It's before noon")
    default:
        fmt.Println("It's after noon")
    }
    
    whatAmI := func(i interface{}) {
        switch t := i.(type) {
        case bool:
            fmt.Println("I'm a bool")
        default:
            fmt.Println("Don't know type %T\n", t)
        }
    }
    whatAmI(true)
    whatAmI("hey")
}