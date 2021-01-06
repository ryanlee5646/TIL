// Array Helper Methods

// case 1.
// ESS
// var colors = ['red', 'blue', 'green']

// for (var i = 0; i < colors.length; i++){
//     console.log(colors[i]);
// }
// ES6+ - forEach
let colors = ['red', 'blue', 'green']

colors.forEach(function(color){ // function() 익명함수(callback function)
    console.log(color)
})

// case 2.
// ES5
// var numbers = [1,2,3]
// var doubleNumbers = []
// for (var i = 0; i < numbers.length; i++){
//     doubleNumbers.push(numbers[i] * 2)
// }

// console.log(doubleNumbers)

// ES6+ - map
const numbers = [1,2,3]

const doubleNumbers = numbers.map(function(number){
    return number * 2
})

console.log(doubleNumbers) // map object가 아닌 배열을 출력함

// case 3.
// ES6+ - filter
const products = [
    {name: 'cucumber', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'apple', type: 'fruit'},
]

const fruitProducts = products.filter(function(product){
    return product.type === 'fruit'
    // 해당 조건이 true일 경우, item을 가져와 배열에 넣음
})
console.log(fruitProducts)

// case 4.
// ES6+ - find

const users = [
    {name: 'gyujin'},
    {name: 'hye'},
    {name: 'zzuli'},
]

const foundUser = users.find(function(user){
    return user.name === 'gyujin'
})

console.log(foundUser)

// case 5.
// ES6+ - every & some
const computers = [
    {name: 'macbook', ram:16},
    {name: 'gram', ram:8},
    {name: 'series9', ram:32},
]

const everyComputersAvailable = computers.every(function(computer){
    return computer.ram > 16 // every는 모두 조건을 만족해야함
})

const someComputersAvailable = computers.some(function(computer){
    return computer.ram > 16 // some은 하나만 조건을 만족해도됨
})

console.log(everyComputersAvailable)
console.log(someComputersAvailable)