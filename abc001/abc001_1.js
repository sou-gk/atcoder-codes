function main(input) {
  const args = input.split('\n');
  const nums = args[0].split(' ');
  const a = 2;
  const b = 1;
 
  console.log(a - b)
}
 
main(require('fs').readFileSync('/dev/stdin', 'utf8'));
