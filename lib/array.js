// 一个关于数组的方法。
const a = (array,num) => {
  if (array[0] !== 'undefined' || array !== 'undefind' || array[num] !== 'undefind'){
    if (num < 0){
        return array[array.length + num]
    }
   return array[num]
  }
  return `❌❌❌`
}
