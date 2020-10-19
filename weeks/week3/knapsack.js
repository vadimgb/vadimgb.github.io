function buildItems()
{
	const names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
	const values = [175, 90, 20, 50, 10, 200]
	//const weights = [5, 4, 2, 0.3, 10]
	const weights = [10, 9, 4, 2, 1, 20]
	const items = []
	for (let i = 0; i < values.length; i++)
	{
		items.push({
			name:names[i], 
			value: values[i], 
			weight: weights[i]
		})
	} 
	return items
}


function greedy(items, maxWeight, keyFunction)
{
	const copy = items.slice()
	copy.sort(keyFunction)
	let totalWeight = 0
	let totalValue = 0
	const result = []
	for (let i = 0; i < copy.length; i++)
	{
		if( totalWeight + copy[i].weight <= maxWeight)
		{
			result.push(copy[i].name)
			totalWeight += copy[i].weight
			totalValue += copy[i].value
		}
	}
	return {totalValue: totalValue, result: result}
}

function value(itemA, itemB)
{
	return itemB.value - itemA.value
}

function weightInverse(itemA, itemB)
{
	return 1/itemB.weight - 1/itemA.weight
}

function density(itemA, itemB)
{
	return itemB.value/itemB.weight - itemA.value /itemA.weight
}

const items = buildItems()
/*
let copy = items.slice()
copy.sort(value)
console.log(copy)
let res = []
for(let i = 0; i < copy.length; i++)
{
	res.push(copy[i].name)
}
console.log(res)

copy = items.slice()
copy.sort(density)
console.log(copy)
res = []
for(let i = 0; i < copy.length; i++)
{
	res.push(copy[i].name)
}
console.log(res)
*/
let res = greedy(items, 20, value)
console.log(res.totalValue)
console.log(res.result)

res = greedy(items, 20, weightInverse)
console.log(res.totalValue)
console.log(res.result)

res = greedy(items, 20, density)
console.log(res.totalValue)
console.log(res.result)
