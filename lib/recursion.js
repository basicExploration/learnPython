// 测试recursion
function file(n) {
  if (n === 1) {
    return 1
  }
  return file(n - 1) * n
}

console.log(file(100))

// 9.33262154439441e+157
